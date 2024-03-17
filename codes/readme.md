코드 URL

https://github.com/ewhamoa



파일 구조

EwhaMoa_FE repo (프론트엔드)

public: 로컬 사진 자료
src: App.jsx를 포함한 전체 메인 코드 폴더
components: 각 페이지 포함하고 있는 폴더
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
sort: 필터링 분류 요소


EwhaMoa_BE repo (백엔드)

/EwhaMoa_BE/src/main/java/com/example/EwhaMoa_BE: 백엔드 자바 코드
초반에는 기능별로 분류하여 작업했으나 기능별로 분류할 시 bean을 찾지 못하는 에러가 생겨 파일 수준 구분 없이 한 디렉터리에 넣어두었습니다
User~: User 기능 (로그인/회원가입/내 프로필/내 북마크/내 작성글)
Post~: Post 기능 (동아리/학회 구분 없는 게시글 업로드)
Club~: 동아리 관련 기능 (동아리 홍보글 수정, 삭제/전체 동아리 홍보글 조회/특정 동아리 홍보글 상세정보 조회/북마크 추가, 삭제)
Conference~: 학회 관련 기능 (학회 홍보글 수정, 삭제/전체 학회 홍보글 조회/특정 학회 홍보글 상세정보 조회/북마크 추가, 삭제)
Bookmark~: 북마크 관련 기능 (북마크 추가/내 북마크 조회)
Moa~, Inquire~: 챗봇 기능 (동아리 추천/문의사항)
Department~, College~: 필터링 기능 중 과/단대 분류를 위한 기능
S3Config: S3 버킷 연결을 위한 Configuration
/EwhaMoa_BE/src/main/python: 백엔드에 임베딩한 AI 코드*
