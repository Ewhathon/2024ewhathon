import io
import sys
import json
import pyrebase

from flask import Flask,  render_template, jsonify, request, Blueprint, redirect, url_for
from .db_handler import DBModule
from .verify_card import verify

bp = Blueprint('main',__name__,url_prefix='/')
DB = DBModule()




#로그인 화면
@bp.route("/login")
def view_login():
    return render_template("login.html")


@bp.route("/user/signin", methods=['POST'])
def signin():
    # POST 요청으로부터 사용자 정보 받아오기
    user_id = request.form['email']
    pwd = request.form['pwd']

    # DB_Module의 signin 메서드 호출하여 사용자 인증 처리
    authenticated = DBModule.signin(email, pwd)

    if authenticated:
        return "Login successful", 200  # 로그인 성공 시 응답
    else:
        return "Invalid username or password", 401 # 로그인 실패 시 응답
    
#회원가입 화면

@bp.route("/create-account")
def create_account():
    return render_template("create-account.html")

    
@bp.route("/user/signup/submit", methods=["POST"])
def reg_user_submit():
    # user_id = request.form['user_id']
    data=request.form

    # 회원가입 성공 여부에 따른 응답 반환
    
    if DB.insert_user(data):
        return redirect("/")
    else:
        return jsonify({"message": "회원가입 실패"}), 500
    

@bp.route("/user/card-veri", methods=["POST"])
def card_veri():
    data=request.form
    image=data['image']
    name = verify(image)
    # if (name == data['name']): return render_template("")

@bp.route("/user/name-veri", methods=["POST"])
def name_veri():
    pass

# @bp.route("/user/signup/post", methods=["POST"])
# def reg_user_post():
#     data = request.form
#     if DB.signup(data['user_id'], data):
#         return render_template("signup_result.html", data=data)
#     else:
#         return render_template("signup_error.html")


#홈 화면

@bp.route("/")
def view_index():
    return render_template("index.html")

@bp.route("/index/ongoing", methods=["GET"])
def ongoing():
    return json(DB.get_ongoing()), 200

@bp.route("/index/open-design", methods=["GET"])
def open_design():
    return json(DB.get_open_design()), 200


##제품 상세 화면

@bp.route("/product-detail/<int:post_id>", methods=["GET"])
def view_post(post_id):
    return render_template("post.html", post=DB.post_detail(post_id))

@bp.route("/product-detail/notice", methods=["POST"])
def insert_notice():
    data = request.form
    if DB.insert_notice(data['post_id'], data):
        return 200
    else:
        return 500

@bp.route("/product-detail/review", methods=["POST"])
def insert_review():
    data = request.form
    if DB.insert_review(data['post_id'], data):
        return 200
    else:
        return 500

@bp.route("/product-detail/qna", methods=["POST"])
def insert_question():
    data = request.form
    if DB.insert_qna(data['post_id'], data):
        return 200
    else:
        return 500
    
@bp.route("/product-datil/answer", methods=["POST"])
def insert_answer():
    data = request.form
    if DB.insert_answer(data['post_id'], data):
        return 200
    else:
        return 500

@bp.route("/product-detail/order", methods=["POST"])
def insert_order():
    data = request.form
    if DB.insert_order(data['post_id'], data):
        return 200
    else:
        return 500


###제품 등록 화면
    
@bp.route("/product-register")
def view_register():
    print("product-register")
    return render_template("product-register.html")

@bp.route("/product-register/submit", methods=["POST"])
def insert_post():
    data = request.form
    if DB.insert_post(data):
        return redirect("/")
    else:
        return jsonify({"message": "제품등록 실패"}), 500

@bp.route("/product-register/edit/<int:post_id>", methods=["GET", "POST"])
def update_post(post_id):
    post = DB.post_detail(post_id=post_id)
    data = request.form
    if DB.update_post(post_id, data):
        return 200
    else:
        return 500

    



####제품 관리 화면

@bp.route("/product-manage")
def view_manage():
    return render_template("product-manage.html")


#####마이 페이지

@bp.route("/mypage")
def view_mypage():
    return render_template("mypage.html")

######오픈 디자인 등록

@bp.route("/design")
def view_design():
    return render_template("design-register.html")

