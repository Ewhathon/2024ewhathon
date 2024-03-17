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



<br/><br/><br/><br/>
