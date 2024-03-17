# 🍚 밥이화(BabEwha) 🍚
### OCR 기반 배달 어플리케이션 **🍚** **밥이화(BabEwha) 🍚** Client 레포지토리입니다.
#### 1️⃣ Backend 레포지토리 링크: https://github.com/BabEwha/BabEwha-Backend
#### 2️⃣ AI 레포지토리 링크: https://github.com/BabEwha/BabEwha-AI

<br/>

## 🍙 프로젝트 소개

개발 기간: 2023.03.15(금) ~ 2023.03.17(일) <br/>
예상 사용자 설문조사: 3.15(금) 21:00 ~ 3.17(일) 14:00<br/>
설문 링크 (현재 폐쇄): https://docs.google.com/forms/d/e/1FAIpQLSfulZbuCy8cGD-FTW601AuBbd7FedH7zUMOYdtjfu-iqWXjSw/viewform?usp=sf_link

<br/><br/>

## 🍙 프로젝트 구조

<img width="1000" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/adda6865-b0f4-4f80-9cad-79eb534990bb"/>

- Client: Swift(iOS)
- Server: Django, MySQL, AWS EC2, AWS S3
- AI: Google Vision, Flask, AWS EC2

<br/><br/>

## 🍙 팀원 소개

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/1a77ca56-1b72-48cc-81e1-09d2d2ee1688"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/0c997a4a-b942-457a-8c20-fb8bdd0a7277"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/f1414b85-9269-4aae-a121-af8e01090579"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/6b676f0c-d5e1-44e9-ab1d-1d00d7c48046"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/4be5a2b8-fd32-4ccc-b89c-00d4269c77ce"/> |
| --- | --- | --- | --- | --- |
| **엄채은** | **양연우** | **허혜민** | **김원정** | **이남영** |
| 기획 | 디자이너 | 프론트엔드 | 백엔드 | IT기술(AI) |

<br/><br/>

-----

## 🍙 Client 정보

### 1️⃣ 버전
- iOS 17.0 +
- 다크 모드, 세로모드 미지원 
- iPhone 15 Pro에서 최적화되어 있습니다. 

### 2️⃣ 프레임워크
- View 
    - SwiftUI

### 3️⃣ 아키텍쳐
- MVVM 패턴 (Model - View - ViewModel) 
![image](https://github.com/team-rocketdan/MAKS-iOS/assets/97100404/7ea2be2c-f69a-490f-919a-2714a0566fb1)

(출처: https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8D%B8-%EB%B7%B0-%EB%B7%B0%EB%AA%A8%EB%8D%B8)

<br/><br/>

## 🍙 실행 화면 (스마트폰 화면 직접 녹화)

### 1️⃣ 진입
| <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/89905ce9-09b6-4638-b4af-a0f4e118b0ba"/> |
| :---: |
| **진입** |  

### 2️⃣ 로그인
| <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/9e55b9a4-3b57-4738-a9a6-b3ba57339c69"/>  |
| :---: |
| **로그인** |  

### 3️⃣ 회원가입
 | <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/1172027f-4921-4369-aa12-aa811259b77c"/> | <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/62ba7fa6-4577-4c05-8a05-2791644149b2"/> |<img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/b9df24f5-29f3-4675-adb0-ada10a03310a"/> | <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/945f69b2-27d2-4ac9-b2e5-8dadd0b7e52f"/> |
| :---: | :---: | :---: | :---: |
| **이메일** | **이름** | **비밀번호** | **권한** | 


### 4️⃣ 리더벗(방장)
| <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/abd3e428-4a3e-4fcd-b091-11ac8d69c4c9"/> 
| :---: |
| **주문과정** |  
### 5️⃣ 참여벗(참여자)
| <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/8183baf3-8b0d-4cf2-8732-bf3ce3f9ea8d"/> | <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/22d0186c-ab09-4b5e-902c-92aac4beeaef"/> | <img height = "400" width="200" src="https://github.com/BabEwha/BabEwha-Client/assets/97100404/abd3e428-4a3e-4fcd-b091-11ac8d69c4c9"/> |
| :---: | :---: | :---: |
| **앱에서 메뉴보기** | **주문 보내기** | **주문과정** | 

<br/><br/>

## 🍙 폴더 구조 
```sh
BabEwha
├── Assets.xcassets
├── BabEwhaApp.swift
├── Extension
│   ├── Color+.swift
│   ├── Date+.swift
│   ├── Font+.swift
│   ├── Image+.swift
│   └── View+.swift
├── Info.plist
├── Model
│   ├── Party.swift
│   └── User.swift
├── Preview Content
│   └── Preview Assets.xcassets
│       └── Contents.json
├── View
│   ├── Add
│   ├── Archive
│   │   └── ArchiveView.swift
│   ├── Component
│   │   ├── BEButton.swift
│   │   ├── BECheckBox.swift
│   │   ├── BENavigationBar.swift
│   │   ├── BEProcessView.swift
│   │   ├── BEProgressView.swift
│   │   ├── BETextField.swift
│   │   ├── HandoutPlace.swift
│   │   ├── ImageBanner.swift
│   │   ├── Information.swift
│   │   ├── LargeDivider.swift
│   │   ├── RestPeopleChip.swift
│   │   ├── SelectPlace.swift
│   │   └── TimeChip.swift
│   ├── Font
│   │   └── PretendardVariable.ttf
│   ├── History
│   │   ├── DepositView.swift
│   │   ├── HistoryView.swift
│   │   └── Leader
│   │       ├── ETASheet.swift
│   │       └── LeaderHistoryView.swift
│   ├── Home
│   │   ├── HomeView.swift
│   │   ├── PartyDetailView.swift
│   │   ├── PhotoPickerView.swift
│   │   ├── SelectImageSheet.swift
│   │   └── SendMenuSheet.swift
│   ├── Login
│   │   ├── LogoView.swift
│   │   ├── ReLoginRouteView.swift
│   │   ├── SignInView.swift
│   │   └── SignUp
│   │       ├── AuthorityView.swift
│   │       ├── SignUpView.swift
│   │       ├── TypeEmailView.swift
│   │       ├── TypeNameView.swift
│   │       └── TypePasswordView.swift
│   ├── Profile
│   │   └── ProfileView.swift
│   └── TabBarRouteView.swift
└── ViewModel
    ├── ToastViewModel.swift
    └── UserViewModel.swift

```

<br/><br/>

-----

<br/><br/>

## 🍙 백엔드 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/e6e67c4b-a277-41ec-b0a4-e7056b3af2b9"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/b77a0873-1c1f-4e9a-b5f2-2bb8a94dc1c7"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/af74bdba-9617-477d-ad85-83b286cf14ea"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/d4c2512a-0dce-4f2e-b2b9-043047349607"/> |
| --- | --- | --- | --- |
| **서버** | **DB 관리** | **데이터 관리** | **배포** |
| Django | MySQL | AWS S3 | AWS EC2 |

<br/><br/>

## 🍙 ERD
<img width="800" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/7342b758-3dce-4911-9d31-a736582aec5e"/>

<br/><br/>

## 🍙 MySQL 쿼리문
| <img width="200" src=""/> | <img width="200" src=""/> | <img width="200" src=""/> |
| --- | --- | --- |
| **** | **** | **** |
|  |  |  |

<br/><br/>

## 🍙 백엔드 응답 확인 (주기능 3가지)

| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/092ea509-35d5-491b-aced-47ed477f1239"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/ab21662a-8203-4395-9842-20cec571714c"/> | <img width="400" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/9f17aabf-5bf6-4eca-a329-9e3efa4b374e"/> |
| --- | --- | --- |
| **1️⃣ 배달 모임 생성(리더벗)** | **2️⃣ 주문 넣기(참여벗)** | **3️⃣ 배달 모임 리스트 나열** |
| 리더벗이 '장소, 최대 인원,시간 제한 등'을 기입하여 모임 생성 | 참여벗이 장바구니 캡쳐본으로 주문을 넣을시 주문 생성 | 현재 공구 중인 배달 게시물을 피드의 형태로 나열 |

<br/><br/>

-----
<br/><br/>

## 🍙 AI 사용 기술

| <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/075295ea-6122-458d-991e-a4a95ab8221d"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/941f9767-efb6-4950-8647-01a987f7708c"/> | <img width="150" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/7fc0098a-47e4-4af4-a167-8defc53d5920"/> |
| --- | --- | --- |
| **OCR** | **서버** | **배포** |
| Google Vision | Flask | AWS EC2 |

<br/><br/>

## 🍙 코드 설명
### 1️⃣ cart.py
- 장바구니 캡쳐본의 text를 추출하여 'menu: 주문 음식 메뉴'와 'price: 메뉴 가격'을 json으로 반환
### 2️⃣ receipt_combined.py
- 주문내역 캡쳐본의 text를 추출하여 'fee: 배달팁과 정액 할인 금액을 합산한 금액', 'discount: % 할인 값'을 json으로 반환
### 3️⃣ receipt_separate.py
- 주문내역 캡쳐본의 text를 추출하여 'delivery: 배달팁', 'coupon: 정액 할인 금액', 'discount: % 할인 값'을 json으로 반환
<br/>

<img width="600" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/b36edf38-7659-44fe-a5f0-f8c5d9ea1512"/>

### *receipt.py(2,3번)의 경우 서버 배포 후 github 파일명만 편의를 위해 수정
##### ✔ 밥이화(BabEwha) 서비스에서는 receipt_separate.py 사용
##### ✔ 과금 문제로 서버를 닫게 될 경우를 대비해 캡쳐 증명

<br/><br/>

## 🍙 장바구니, 주문내역 이미지 분석

### OCR을 통한 text 추출 후 필요 요소 추출을 위한 탐색 과정

### 1. 장바구니
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/41f517cc-b0da-4fe5-8a0c-5ed57ae6959e"/> |
| --- |
| 장바구니의 2가지 구성 <br/> 🟥 메뉴 (menu) <br/> 🟦 가격 (price) |

<br/>

### 2. 주문내역
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/92de8380-1b91-454e-a40c-6bb78ba2bfd5"/> |
| --- |
| 주문내역의 3가지 구성 <br/> 🟩 배달팁 (delivery) <br/> 🟥 % 할인 쿠폰 (discount) <br/> 🟦 정액 할인 쿠폰 (coupon) |

<br/>

### 3. 할인 (4가지 요소)
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/56052773-1171-4688-8924-634fb28e2f46"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/0bbc4676-d64e-4db4-abb7-cfdc70eb19dc"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/374fa377-0d0a-4dac-bfac-e888f97ca9ea"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/a07c564a-34d5-454e-a250-6107ee88407b"/> |
| --- | --- | --- | --- |
| 🟥 % 할인 (discount) | 🟦 정액 할인 (coupon) | 🟥🟦 %할인 + 정액할인 | ✖ 할인 없음 |

<br/><br/>

## 🍙 장바구니(메뉴, 가격) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/4831d60f-4719-496f-a43f-39a17e95835d"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/018cdeeb-8cc5-4deb-bcd0-2882799c1499"/> |
| --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/bb22b3b9-f7f8-4364-8faa-6c3a6fec4554"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/d2f78841-cbdf-4a60-a5b0-cf45373c7add"/> |
| **1️⃣ 메뉴 1개** | **2️⃣ 메뉴 2개** |

<br/>

### 🍘 장바구니에 담긴 모든 음식 메뉴와 메뉴별 개별 가격 분석
### 1. 스크롤 캡쳐/풀페이지 캡쳐 등 모든 형태의 캡쳐본 취급
### 2. 메뉴의 개수와 옵션 제한 없이 분석 가능

✔ 웹 서비스 주소(배포 완료): http://18.118.254.47:5000/cart

<br/><br/>

## 🍙 주문내역(배달팁, % 할인, 정액 할인) 분석

| <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/2d306c90-cf27-453a-abd5-1d0ac78a7a2b"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/8b01f011-026c-4bbd-a88b-9f62470b4e46"/> | <img width="200" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/45f51eb5-551b-44cc-a9be-70d41b24f8ff"/> |
| --- | --- | --- |
| <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/893d9ee4-bea4-4ecd-b8ab-939eaa327d3c"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/819132f5-37d2-4770-9a37-15a7aa001477"/> | <img width="300" src="https://github.com/BabEwha/BabEwha-ai-private/assets/91009436/c873a8c2-a32b-4b93-8ce0-f8ca2a87bad5"/> |
| **1️⃣ % 할인** | **2️⃣ 정액 중복 할인** | **3️⃣ % 할인 + 정액 할인** |


<br/>

### 🍘 배달팁과 할인 쿠폰 종류 2가지(% 할인, 정액 할인) 분석
### 1. %할인시 각 사용자의 결제 금액에 따라 차등 할인 적용
### 2. 중복 할인도 모두 적용해서 배달팁과 정액 할인 금액 1/n



<br/><br/><br/><br/>
