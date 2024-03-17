# NOTEGATHER

![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/5810374a-ef56-450f-b080-9f535357b9c6)

[프론트엔드 레포지토리](https://github.com/Ewhathon-youhahak/Ewhathon-Youhahak-Front)  
[백엔드 레포지토리](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back)


## **서비스 소개**

NOTEGATHER - 교육 정보 격차 해소를 위한 필기 공유 플랫폼
 
[학생들의 협력으로 만들어가는 학습 공유 커뮤니티, NOTEGATHER]
NOTEGATHER는 대학생들 사이의 교육 정보 격차를 해소하고자 탄생한 플랫폼입니다. 이는 학생들이 강의 중에 작성한 노트를 서로 공유하고, 생성형 AI를 이용해 이 필기를 바탕으로 맞춤형 퀴즈를 생성함으로써, 모든 학생이 효과적으로 자가 학습할 수 있도록 돕습니다. '함께 모이다(GATHER)'와 '노트(NOTE)'의 결합으로 명명된 NOTEGATHER는 교육 자료의 상호 공유를 통해 성장하는 커뮤니티를 목표로 합니다. 특히, 장애 학생 등 수업 참여에 어려움을 겪는 학생들이 학습 자료에 쉽게 접근할 수 있도록 하는 것을 핵심 목표로 하며, 이들을 위한 맞춤형 교육 자원 제공에 기여하고자 합니다. 이렇게 NOTEGATHER는 학생들의 자발적인 참여를 바탕으로 모든 대학생이 필요한 학습 자료를 손쉽게 공유하고 접할 수 있는 환경을 조성함으로써 교육의 격차를 줄이는 데 중점을 둡니다.
[주요 기능]
1.   필기 공유하기: 학생들이 강의 중 작성한 필기를 플랫폼에 업로드하고 공유합니다.
2.   생성형 AI 활용하여 퀴즈 생성하기: 업로드된 필기를 바탕으로 AI가 맞춤형 퀴즈를 자동 생성해줍니다. 이 기능을 활용하여 학생들의 자가 학습 효율을 극대화할 수 있습니다.
3.   노트 필기 검색하기: 강의명, 교수명 등의 키워드로 필요한 필기 노트를 쉽게 찾아볼 수 있습니다.
4.   내가 올린 노트 필기 모아보기: 자신이 업로드한 필기 노트를 한눈에 확인하고 관리할 수 있습니다.
NOTEGATHER는 교육의 격차를 줄이고, 모든 학생이 평등하게 학습 자원을 공유하고 접근할 수 있는 환경을 목표로 합니다. 이화여대에 재학 중인 모든 학생들이, 학년과 국적을 불문하고, 이 플랫폼을 통해 학습의 질을 높이고, 학습 커뮤니티 내에서 서로를 지원하며 성장할 수 있기를 기대합니다.

## 팀원 소개

---

| 정수완 | 박서연 | 오서영 | 박현아 | 황채원 |
| --- | --- | --- | --- | --- |
| 국제학과/융합콘텐츠학과 | 융합콘텐츠학과/컴퓨터공학 | 사이버보안학과 | 컴퓨터공학 | 컴퓨터공학 |
| ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/b93931f7-021e-4d2f-ac1b-2f31ced90be9) | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/fac5983b-7df5-4615-bf8b-7bc16b6fea05) | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/ec8c5fa2-2ec8-43cc-bf33-856e8f32b9d2) | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/d1937470-9e99-4580-a7b1-671b2b47ba1e) | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/01a35cce-0ad5-4bad-a2e1-6d2a14ca1b8a) |
| Design/Service Design | Frontend Developer | Frontend Developer | Backend Developer | AI, Backend Developer |

## 기술 스택

### Frontend

- React
- Vercel

### Backend

- Springboot 3.2.3
- MySQL 8.0
- Github Actions
- Docker/Google Artifact Registry
- Google Cloud Storage/Cloud Run
- OpenAI API

## 기능 설명
### AuthController: 회원가입 및 로그인 관련 API
| HTTP Method | API Path | Description |
| --- | --- | --- |
| POST | /signup | 회원가입 |
| POST | /login | 로그인 |

### StudentController: 학생 관련 API
| HTTP Method | API Path | Description |
| --- | --- | --- |
| GET | /student | 학생 하나 가져오기 |
| PATCH | /student | 학생 수정하기 |

### NoteController: 노트필기 관련 API
| HTTP Method | API Path | Description |
| --- | --- | --- |
| POST | /notes | 필기 업로드 |
| GET | /notes | 필기 목록 가져오기 및 필기 검색 |
| GET | /notes/{note_id} | 필기 하나 가져오기 |
| GET | /notes/student | 특정 학생이 작성한 필기 목록 가져오기 |
| PATCH | /notes/{note_id} | 필기 수정하기 |
| DELETE | /notes/{note_id} | 필기 삭제하기 |

### QuizController: 퀴즈 관련 API
| HTTP Method | API Path | Description |
| --- | --- | --- |
| POST | /api/quizzes/generate?noteId={note_id} | 퀴즈 생성하기 |

## 프로젝트 구조
### 프론트엔드
```
📦src
 ┣ 📂home
 ┃ ┣ 📜home.style.js
 ┃ ┗ 📜index.js
 ┣ 📂login
 ┃ ┣ 📜index.js
 ┃ ┗ 📜signUp.jsx
 ┣ 📂mypage
 ┃ ┣ 📜documentList.jsx
 ┃ ┗ 📜index.js
 ┣ 📂navbar
 ┃ ┣ 📜Navbar.jsx
 ┃ ┣ 📜index.js
 ┃ ┗ 📜navbar.style.js
 ┣ 📂note
 ┃ ┣ 📜Note.jsx
 ┃ ┣ 📜index.js
 ┃ ┗ 📜note.style.js
 ┣ 📂quiz
 ┃ ┣ 📂quizBox
 ┃ ┃ ┣ 📜QuizBox.jsx
 ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┗ 📜quizBox.style.js
 ┃ ┣ 📜Quiz.jsx
 ┃ ┣ 📜index.js
 ┃ ┗ 📜quiz.style.js
 ┣ 📂upload
 ┃ ┣ 📜Upload.jsx
 ┃ ┣ 📜index.js
 ┃ ┗ 📜upload.style.js
 ┣ 📜App.css
 ┣ 📜App.jsx
 ┣ 📜App.test.js
 ┣ 📜index.css
 ┣ 📜index.js
 ┣ 📜logo.svg
 ┣ 📜reportWebVitals.js
 ┗ 📜setupTests.js
```
### 백엔드
```
└─src
    ├─main
    │  ├─java.com.ewhathon.notegather
    │  │              │  NotegatherApplication.java
    │  │              │
    │  │              ├─auth
    │  │              │  │  AuthController.java
    │  │              │  │  AuthDetails.java
    │  │              │  │  AuthDetailService.java
    │  │              │  │  AuthService.java
    │  │              │  │
    │  │              │  ├─dto
    │  │              │  │      LoginRequestDto.java
    │  │              │  │      RegisterRequestDto.java
    │  │              │  │
    │  │              │  ├─jwt
    │  │              │  │      JwtAuthenticationFilter.java
    │  │              │  │      JwtAuthorizationFilter.java
    │  │              │  │      JwtToken.java
    │  │              │  │      JwtTokenProvider.java
    │  │              │  │
    │  │              │  └─security
    │  │              │          SecurityConfig.java
    │  │              │
    │  │              ├─config
    │  │              │      CommonResponse.java
    │  │              │
    │  │              ├─domain
    │  │              │  ├─entity
    │  │              │  │      Lecture.java
    │  │              │  │      Note.java
    │  │              │  │      Student.java
    │  │              │  │      UserRole.java
    │  │              │  │
    │  │              │  └─repository
    │  │              │          LectureRepository.java
    │  │              │          NoteRepository.java
    │  │              │          StudentRepository.java
    │  │              │
    │  │              ├─service
    │  │              │      GptService.java
    │  │              │      LectureService.java
    │  │              │      NoteService.java
    │  │              │      StudentService.java
    │  │              │
    │  │              └─web
    │  │                  │  NoteController.java
    │  │                  │  QuizController.java
    │  │                  │  StudentController.java
    │  │                  │
    │  │                  └─dto
    │  │                          NoteListRequestDto.java
    │  │                          NoteListResponseDto.java
    │  │                          NoteRequestDto.java
    │  │                          NoteResponseDto.java
    │  │                          QuizItem.java
    │  │                          QuizRequestDto.java
    │  │                          QuizResponseDto.java
    │  │                          StudentRequestDto.java
    │  │                          StudentResponseDto.java
    │  │
    │  └─resources\
    └─test\
```

## 아키텍처

![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/a1687c5f-7883-4123-abf1-dbf1d68f5780)

## 실행 화면
### 회원 관련 페이지
| 페이지명 | 페이지화면 |
| --- | --- |
| 회원가입 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/18b54133-9e16-40af-ae27-fd8f5f5549d9) |
| 로그인 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/581508d4-1489-4e24-bafa-8049292a6b88) |
| 마이페이지 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/dc4ab821-0417-4dfc-9458-5de5d683ed4c) |

### 필기 관련 페이지
| 페이지명 | 페이지화면 |
| --- | --- |
| 필기 업로드 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/4dcc2601-df4c-438b-b4bc-4594c055b98b) |
| 필기 과목명 검색 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/42bbbc44-f14d-4e99-8245-7a0ff0c82beb) |
| 필기 교수명 검색 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/3a6cde56-9095-4cb2-ab99-91ca44b4607a) |
| 필기 조회 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/69884187-6fc9-4a16-9340-051f953b4502) |

## 퀴즈 페이지
| 페이지명 | 페이지화면 |
| --- | --- |
| 퀴즈 생성 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/9de7c202-9988-4f13-b237-b1d6d18b0681) |
| 퀴즈 채점 | ![image](https://github.com/Ewhathon-youhahak/Ewhathon-youhahak-back/assets/67725652/195d596f-7a8a-43fe-a085-019e63fd7e18) |


## 데모 영상 링크

https://www.youtube.com/watch?v=O9Y7png3yps&feature=youtu.be
