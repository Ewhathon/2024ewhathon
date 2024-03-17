# 백엔드
## 코드
https://github.com/EarlyUs/back

## 🎲 백엔드 관여 주요 기능
### 장애 학생 수업 매칭 기능
- 도우미 희망자가 활동 가능하다고 선택한 시간에 장애 학생의 수업 시간이 모두 포함되는 경우, 활동 가능한 수업으로 매칭
- 장애학생지원센터에서 제공한 장애 학생 수업 데이터를 이용해 DisabledCourse에 해당 데이터를 입력, 각 수업 별 수업 시간표를 ClassTime과의 ManyToMany 연관관계로 처리
- Java Stream API로 모든 수업 데이터에 대해 도우미 신청자의 시간에 포함되는지 확인
- 이 때 containsAll()은 reference가 아닌 value로 equality를 판단하며 이를 이용하기 위해 아래와 같이 비교할 클래스의 equals() 메서드를 오버라이드해야 함
```java
package com.earlyus.ewhanarae.domain.disabledCourse.domain;
...
@Override  
public boolean equals(Object o) {  
    if (this == o) return true;  
    if (o == null || getClass() != o.getClass()) return false;  
    ClassTime classTime = (ClassTime) o;  
    return Objects.equals(time, classTime.time);  
}  
  
@Override  
public int hashCode() {  
    return Objects.hash(time);  
}
```


  
### 날개 매칭 기능 
- 기획팀이 제작한 날개 유형 데이터를 저장해 전공 일치 여부와 도우미가 제공하고자 하는 도움 유형에 따라 도우미의 날개 유형을 판단
- DisabledCourse에 도우미와 일치하는 전공의 수업이 존재하는지 여부에 따라 majorMatched에 0 또는 1을 저장
- 날개 유형 중 `전공 일치 여부`, `도움 유형` 이 일치하는 날개 하나를 찾아서 반환

  

## 🛠 서비스 구조 및 흐름
![](https://blog.kakaocdn.net/dn/nn1NH/btsFt3BRvzR/xMSfFzHPA4gkRdwd2wEMaK/img.png)
### 배포 흐름
![](https://blog.kakaocdn.net/dn/bxqMy1/btsFoDYDmXc/fmLuRG7ttTu8hrW0qkaC01/img.png)
1. 깃허브 디폴트 브랜치에 변경 내용 커밋
2. Github workflow가 java 프로젝트를 빌드
3. Codedeploy, S3 접근이 가능한  IAM 키를 알고 있는 Github workflow가 S3에 빌드 파일을 업로드하고, Codedeploy로 배포 요청
4. Codedeploy가 appspec.yml에 따라 지정한 hook 시점에 scripts/deploy.sh 스크립트를 실행
5. deploy.sh는 현재 실행 중인 blue 컨테이너가 있다면 green 컨테이너를 실행시키고, 없다면 blue 컨테이너를 실행 -> 배포 중에도 서비스가 중단되지 않도록 함

### HTTPS 요청 처리 흐름
1. 도메인으로 들어온 요청은 EC2의 로드 밸런서로 라우팅 됨
2. AWS ALB는 요청이 HTTP라면 HTTPS로 리다이렉트하고, HTTPS라면 등록된 인증서로 SSL/TLS 처리
3. AWS ALB는 모든 요청을 대상 그룹에 등록된 EC2의 80포트로 보냄
4. NginX의 리버스 프록시 기능을 이용해 블루 컨테이너가 사용 중인 8081포트와 그린 컨테이너가 사용 중인 8082포트 중 연결 가능한 곳으로 연결함

### 사용한 기술 및 툴
- Spring Boot
- AWS(EC2, ALB, S3, RDS/MySQL, Codedeploy, Route53, ACM)
- NginX
- Docker
- Github Actions

  

## 🦺 테스트 코드
- 주요 기능을 제공하는 match 도메인에 대한 테스트 코드 작성
- Jacoco를 이용해 테스트 커버리지 측정
![image](https://github.com/Mt-EB-Rainbow/back/assets/69039161/eaf76b28-30a7-49e4-be2d-de25c462e926)

