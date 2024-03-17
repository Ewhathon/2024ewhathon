# 2024ewhathon

# 🌱 벗돋움

## 💚 팀원
| 이름   | 학번    | 소속학과       | 역할           |
|------|-------|------------|--------------|
| 최윤서 | 2244027 | 융합콘텐츠학과    | 팀장, 기획 및 디자인 |
| 김리나 | 2176046 | 컴퓨터공학과     | 백엔드         |
| 정유정 | 2276288 | 컴퓨터공학과     | 백엔드         |
| 복지희 | 2244010 | 컴퓨터공학과     | 프론트엔드      |
| 예서연 | 2277018 | 인공지능학과     | 첨단기술(AI)    |



## ❓ 문제 정의
- 이화여대 내 동아리 및 소모임을 통해 진행되는 행사들의 홍보처가 마땅치 않음
- 에브리타임의 홍보 게시판의 특성상 글이 다른 학생들에게 제대로 노출되지 않음

## 🛠 서비스 정의
이화여대 내 이벤트 및 행사를 집중 타겟팅하여, 해시태그 추천 시스템을 이용해 정보를 쉽고 빠르게 얻을 수 있는 웹 서비스를 기획함

## 📋 기능 설명

### 💻 keword_2.py 
행사글 등록 과정에서 사용할 해시태그를 추천해주는 모델.
행사글의 내용(content)을 참고하여 추천함.


### 📚 domain package
- **User**: 사용자의 정보와 관련된 엔티티. 속성: `username`, `email`, `password`.
- **Category**: 행사의 다양한 분야(공연, 학술, 전시 등)를 정의하는 열거형.
- **Event**: 행사 정보와 관련된 엔티티. 속성: `category`, `title`, `location`, `host`, `post_date`, `start_date`, `end_date`, `free`, `filepath`, `heart_count`, `rsvp_count`, `selected_keywords`.
- **Hashtag**: 행사의 분위기나 특성을 나타내는 해시태그를 정의하는 열거형.
- **Heart**: 등록된 행사글에 대한 좋아요를 관리하는 엔티티. 연결: `user_id`, `event_id`.
- **Rsvp**: 등록된 행사글에 대한 참석 여부를 관리하는 엔티티. 연결: `user_id`, `event_id`.
- **Suggestion**: 추천 해시태그와 관련된 엔티티. 연결: `event_id`, 저장: `suggestedKeywords`.

### 🗃️ Repository
- EventRepository
- HeartRepository
- RsvpRepository
- SuggestionRepository
- UserRepository

### 🔐 Authentication Package
- **UserController**
- **UserDTO**
- **UserService**
  - `saveUser`: 유저 등록 (이화여자대학교 이메일 도메인만 허용).
  - `loginUser`: 로그인 기능.
  - `isEmailAvailable`: 이메일 중복 검사.

### 🎉 Event Package
- **EventController**
- **EventRequestDto**
- **EventResponseDto**
- **EventService**
  - `createEvent`: 행사글 등록 (`selectedKeywords`는 null로 저장).
  - `showEventDetail`: 행사글 상세보기.

### ❤️ Heart Package
- **HeartController**
- **HeartRequestDto**
- **HeartService**
  - `insert`: 좋아요 표시.
  - `delete`: 좋아요 취소.

### 📝 RSVP Package
- **RsvpController**
- **RsvpRequestDto**
- **RsvpService**
  - `insert`: 참여 표시.
  - `delete`: 참여 취소.

### 🏠 Home Package
- **HomeController**
- **HomeResponseDto**
- **HomeService**
  - `getHomeInfo`: 좋아요가 많은 행사글, 최신 등록글 정보 불러오기.

### 🙍‍♂️ MyPage Package
- **MypageController**
- **MypageResponseDto**
- **MypageService**
  - `getMypageInfo`: 유저 정보, 유저가 좋아한/참여 이벤트, 유저가 주최한 이벤트 정보 불러오기.

### 🔍 Search Package
- **SearchController**
- **SearchService**
  - `searchEvents`: 제목, 분야, 시작/종료 날짜, 무료 여부, 키워드로 이벤트 검색.
- **SearchSpecifications**
  - 검색 쿼리의 사양 포함.

### 🏷️ Suggestion Package
- **SuggestionController**
- **SuggestService**
  - `fetchSuggestedKeywords`: flask 서버와 연결하여 `keword_2.py`에서 생성된 '추천 해시태그' 리스트 가져오기.
  - `saveKeywords`: 추천 해시태그 리스트를 단일 해시태그로 끊어 `suggestedKeywords`에 저장.
  - `saveSelectedKeywords`: 사용자가 선택한 해시태그를 `selectedKeywords`에 저장.

### 🔒 Security Config
- 사용자 보안 관련 설정, 비밀번호 해싱 등 관리.

