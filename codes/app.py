from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import logging
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

app = Flask(__name__)
app.secret_key = 'testKey'  # 플래시 메시지 및 세션에 사용할 시크릿 키 설정

# 데이터베이스 연결 함수
def connect_db():
    conn = sqlite3.connect('survey_database.db')
    conn.row_factory = sqlite3.Row
    return conn

# 데이터베이스 테이블 만드는 함수
def create_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS surveys
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL)''')
    conn.commit()
    conn.close()

    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS questions
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                survey_id INTEGER,
                question TEXT NOT NULL,
                FOREIGN KEY (survey_id) REFERENCES surveys(id))''')
    conn.commit()
    conn.close()

    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS answers
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                survey_id INTEGER,
                question_id INTEGER,
                respondent_id INTEGER,
                answer TEXT,
                FOREIGN KEY (survey_id) REFERENCES surveys(id),
                FOREIGN KEY (question_id) REFERENCES questions(id))''')
    conn.commit()
    conn.close()

# SQLite 데이터베이스 연결 및 테이블 생성
create_table()

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('survey_database.db')
    conn.row_factory = sqlite3.Row
    return conn

# 초기 페이지
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')

# 암호화를 위한 키 생성
key = get_random_bytes(16)  # 128-bit key for AES

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    global encrypted_data
    if request.method == 'POST':
        data = request.form['data'].encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        encrypted_data = {'iv': iv, 'ct': ct}
        return render_template('encrypted.html', iv=iv, ct=ct)
    return render_template('encrypted.html')  # GET 요청에 대한 렌더링

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        iv = base64.b64decode(request.form['iv'])
        ct = base64.b64decode(request.form['ct'])
        
        if 'decrypt_checkbox' in request.form:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
            return render_template('decrypted.html', pt=pt)
        else:
            return render_template('encrypted.html', iv=request.form['iv'], ct=request.form['ct'])
    except Exception as e:
        # Handle decryption errors gracefully
        error_message = f"Error occurred during decryption: {str(e)}"
        return render_template('error.html', error_message=error_message)


##########설문작성기능###########
# 설문 추가 페이지 
@app.route('/add_survey', methods=['GET', 'POST'])
def add_survey():
    if request.method == 'POST':
        # 사용자가 제출한 설문 제목 가져오기
        title = request.form['title']
        # 설문 제목을 데이터베이스에 추가
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO surveys (title) VALUES (?)", (title,))
        # 새로운 설문의 ID를 가져옴
        survey_id = cur.lastrowid
        conn.commit()
        conn.close()
        # 설문 완료 페이지로 리디렉션
        return redirect(url_for('add_question', survey_id=survey_id))  # 'add_question' 함수로 리디렉션하며, survey_id 값을 함께 전달
    return render_template('add_survey.html')

# 질문 추가 페이지
@app.route('/add_question/<int:survey_id>', methods=['GET', 'POST'])
def add_question(survey_id):
    if request.method == 'POST':
        # 사용자가 제출한 질문 내용 가져오기
        question = request.form['question']
        # 데이터베이스에 질문 추가
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO questions (survey_id, question) VALUES (?, ?)", (survey_id, question))
        conn.commit()
        conn.close()
        # 현재 설문에 대한 질문 추가 페이지로 리디렉션
        return redirect(url_for('add_question', survey_id=survey_id))
    
    if request.method == 'GET' and 'submit_complete' in request.args:
        return redirect(url_for('survey_complete'))  # "설문 작성 완료" 버튼을 클릭하면 survey_complete 페이지로 이동
    
    return render_template('add_question.html', survey_id=survey_id)


# 설문 작성 완료 페이지
@app.route('/survey_complete', methods=['GET'])
def survey_complete():
    return render_template('survey_complete.html')

###########################


# 설문 목록을 가져오는 함수
def get_surveys():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM surveys')
    surveys = cur.fetchall()
    conn.close()
    return surveys

# 설문 목록 페이지
@app.route('/survey_list')
def survey_list():
    surveys = get_surveys()
    return render_template('survey_list.html', surveys=surveys)

# 특정 설문 내용을 가져오는 함수
def get_survey_content(survey_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM surveys WHERE id = ?', (survey_id,))
    survey = cur.fetchone()
    conn.close()
    return survey

##########설문조회및답변기능############

# 특정 설문의 질문들을 가져오는 함수
def get_survey_questions(survey_id):
    questions = []
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM questions WHERE survey_id = ?', (survey_id,))
        questions = cur.fetchall()
    return questions

# survey_detail 함수 내부의 POST 요청 부분 수정
@app.route('/survey_detail/<int:survey_id>', methods=['GET', 'POST'])
def survey_detail(survey_id):
    survey = get_survey_content(survey_id)  # 조건문 밖에서 survey 변수 정의
    if request.method == 'POST':
        encrypted_answers = []  # 암호화된 답변을 저장할 리스트
        questions = get_survey_questions(survey_id)
        for question in questions:
            answer = request.form.get(f'answer_{question["id"]}')
            # 사용자가 입력한 답변을 AES로 암호화하여 리스트에 추가
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(answer.encode('utf-8'), AES.block_size))
            iv = base64.b64encode(cipher.iv).decode('utf-8')
            ct = base64.b64encode(ct_bytes).decode('utf-8')
            encrypted_answers.append({'question_id': question["id"], 'iv': iv, 'ct': ct})

        # 암호화된 답변을 템플릿으로 전달하여 보여줌
        return render_template('survey_detail.html', survey=survey, questions=questions, encrypted_answers=encrypted_answers)
    
    else:
        questions = get_survey_questions(survey_id)
        return render_template('survey_detail.html', survey=survey, questions=questions)




# 설문 검색 기능
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query', '')  # 사용자가 입력한 검색어 가져오기
        conn = connect_db()  # 데이터베이스 연결
        cur = conn.cursor()
        cur.execute("SELECT * FROM surveys WHERE title LIKE ?", ('%' + query + '%',))  # 제목에 검색어가 포함된 설문 검색
        surveys = cur.fetchall()  # 검색 결과 가져오기
        conn.close()  # 데이터베이스 연결 닫기
        return render_template('search.html', surveys=surveys, query=query)
    else:
        return render_template('search.html')


# 특정 설문 내용을 보여주는 페이지
@app.route('/survey/<int:survey_id>')
def show_survey(survey_id):
    return redirect(url_for('survey_detail', survey_id=survey_id))

##############################

###########회원정보관련기능##########
# 마이페이지
@app.route('/my_page')
def my_page():
    # You can implement this route to render the user's page
    return render_template('my_page.html')


# 회원가입 페이지
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 데이터베이스에 사용자 정보 추가
        conn = get_db_connection()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return render_template('register.html', message = 'successfully registered.')
    return render_template('register.html')

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''  # 기본적으로 메시지를 빈 문자열로 설정
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 데이터베이스에서 사용자 정보 조회
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session['username'] = username  # 로그인 성공 시 세션에 사용자명 저장
            flash('로그인 성공!')
            return redirect(url_for('index'))
        else:
            message = 'Invalid username or password.'  # 로그인 실패시 메시지 설정

    return render_template('login.html', message=message)


# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)  # 세션에서 사용자명 제거
    
    return render_template('index.html', message = 'Logout succeeded')
################

if __name__ == '__main__':
    app.run(debug=True)
