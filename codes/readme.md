코드 URL</br>

https://github.com/ewhamoa



파일 구조 </br>

EwhaMoa_FE repo (프론트엔드) </br>

public: 로컬 사진 자료 </br>
src: App.jsx를 포함한 전체 메인 코드 폴더 </br>
components: 각 페이지 포함하고 있는 폴더</br>
auth: 로그인, 회원가입 페이지 폴더
- Login.jsx: 로그인
- Register.jsx: 회원가입

chatbot: 챗봇 페이지 폴더
- Chatbot.jsx: 챗봇 기본 틀, 첫 접속 시 인사
- SelectChat.jsx: 채팅 선택지 제공, 각 선택지마다 컴포넌트 연결
- Instruction.jsx: 사이트 사용법 시나리오
- Recommend.jsx: 동아리 추천 시나리오
- Ask.jsx: 문의하기 시나리오
- AnythingElse.jsx: 선택지에 대한 챗봇 답변 제공 후 재질문하는 시나리오

main: 홈 화면
- Logo.jsx: 로고
- Header.jsx: 웹사이트 헤더
- ClubMain.jsx: 동아리 메인화면
- ConfMain.jsx: 학회 메인화면
- SearchBar.jsx: 검색창 컴포넌트

mypage: 마이페이지
- Bookmarks.jsx: 북마크한 게시글 보기 페이지
- MyPosts.jsx: 내가 작성한 글 보기 페이지
- Profile.jsx: 프로필 정보 및 위 요소들의 네비게이터 창

posts: 게시글 개체 관련 요소
- PostItem.jsx: 메인화면 게시글 요소 틀
- PostDetail.jsx: 게시글 상세조회 창 및 게시글 삭제 기능
- PostEdit.jsx: 동아리 게시글 수정
- ConfEdit.jsx: 학회 게시글 수정

sort: 필터링 분류 요소

</br>
</br>

EwhaMoa_BE repo (백엔드) </br>

/EwhaMoa_BE/src/main/java/com/example/EwhaMoa_BE: 백엔드 자바 코드 </br>
초반에는 기능별로 분류하여 작업했으나 기능별로 분류할 시 bean을 찾지 못하는 에러가 생겨 파일 수준 구분 없이 한 디렉터리에 넣어두었습니다 </br>
User~: User 기능 (로그인/회원가입/내 프로필/내 북마크/내 작성글) </br>
Post~: Post 기능 (동아리/학회 구분 없는 게시글 업로드) </br>
Club~: 동아리 관련 기능 (동아리 홍보글 수정, 삭제/전체 동아리 홍보글 조회/특정 동아리 홍보글 상세정보 조회/북마크 추가, 삭제) </br>
Conference~: 학회 관련 기능 (학회 홍보글 수정, 삭제/전체 학회 홍보글 조회/특정 학회 홍보글 상세정보 조회/북마크 추가, 삭제) </br>
Bookmark~: 북마크 관련 기능 (북마크 추가/내 북마크 조회) </br>
Moa~, Inquire~: 챗봇 기능 (동아리 추천/문의사항) </br>
Department~, College~: 필터링 기능 중 과/단대 분류를 위한 기능 </br>
S3Config: S3 버킷 연결을 위한 Configuration </br>

</br>
</br>

/EwhaMoa_BE/src/main/python: 백엔드에 임베딩한 AI 코드* </br>

- 동아리 이름을 입력받아 동아리를 추천하는 모델:
데이터를 불러와 TF-IDF 벡터화를 진행합니다. 생성된 TF-IDF 행렬로 단어의 중요도를 판단하고 코사인 유사도를 계산할 수 있습니다. 코사인 유사도를 계산할 때엔 하나의 동아리에 대한 전체 동아리와의 유사도를 모두 계산했습니다. 이후 유사도가 높은 세 개의 동아리를 리턴하는 함수를 만들었습니다.

- 찾는 동아리의 상세설명을 입력 받아 동아리를 추천해주는 모델: 
먼저 입력 문장을 koBERT 모델(한국어에 특화된 BERT모델)을 사용하여 임베딩 합니다. BERT는 입력 문장을 토큰화한 후 임베딩 벡터로 변환하는 모델입니다. 사용자의 입력으로 만들어진 벡터와 기존 동아리와의 코사인 유사도를 비교하여 사용자가 원하는 동아리를 추천합니다.
