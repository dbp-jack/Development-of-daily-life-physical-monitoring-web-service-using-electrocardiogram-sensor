# 캡스톤디자인 (아두이노) 심전도 센서를 활용한 일상 생활 신체 모니터링 웹 서비스 개발 프로젝트
Development-of-daily-life-physical-monitoring-web-service-using-electrocardiogram-sensor

대전대-호치민시베트남국립대학교, 글로벌 캡스톤디자인 성과 교류

https://www.dailycc.net/news/articleView.html?idxno=751998#google_vignette

2023 한국실천공학교육학회 추계종합학술대회 - 학술 논문 발표

https://slime-face-7c4.notion.site/2023-1f0eeaa2f0af802ebe9ece38cc503e4d?pvs=4



# 🫀 실시간 부정맥 감지 및 건강 관리 웹 서비스

## 📝 프로젝트 소개

코로나19 팬데믹 이후 20~30대의 생활 습관 악화 및 피로 누적으로 인해 **심장질환** 환자가 증가하고 있으며, 이에 따른 **협심증, 심근경색, 부정맥, 심혈관질환** 등의 치사율도 높아지고 있습니다.

본 캡스톤 디자인 프로젝트는 **부정맥을 일상 생활 속에서도 실시간으로 확인할 수 있도록 돕는 웹 기반 건강 관리 서비스**를 개발하는 데 목적이 있습니다. 사용자는 웹 페이지를 통해 본인의 **심전도(ECG)** 데이터를 실시간으로 확인할 수 있으며, 부정맥 여부를 파악하고, 건강 진단 체크리스트 및 건강 정보 가이드를 통해 자신의 건강 상태를 관리할 수 있습니다.

---

## ⚙️ 주요 기능

- **실시간 부정맥 측정 및 시각화**  
  아두이노 및 ECG 센서를 통해 측정한 심전도 데이터를 실시간으로 웹에서 확인

- **건강 진단 체크리스트 제공**  
  사용자가 자가 건강 상태를 점검할 수 있는 문진 기반 체크리스트 제공

- **건강 정보 가이드**  
  심장 건강 관리에 도움이 되는 생활 정보 및 질병 관련 가이드 제공

- **사용자 인증 및 보안 기능**  
  비밀번호 암호화, 세션 기반 로그인, SSL 인증 등 개인정보 보호 기능 탑재

---
### 🔧 트러블슈팅: 실시간 심전도 데이터 처리

### 🔍 문제 배경

프로젝트 핵심 기능인 **실시간 부정맥 감지**를 구현하기 위해, ECG 센서로부터 받은 데이터를 사용자 웹 페이지에 실시간으로 표시해야 했습니다.  
하지만 초기에는 일반적인 **AJAX 주기 요청 방식(`setInterval`)**을 사용했으며, 이 방식에서는 다음과 같은 문제가 발생했습니다:

- **데이터 지연**: 서버 응답이 누적되며 타이밍이 밀려 실시간성이 떨어짐  
- **서버 부하 증가**: 매초 반복 요청으로 인해 서버에 무의미한 트래픽이 발생  
- **데이터 누락**: 클라이언트가 요청을 보내기 전 수집된 데이터가 저장되지 않는 경우 발생  

---

### ⚙️ 해결 방법: AJAX 롱 폴링 (Long Polling)

이 문제를 해결하기 위해 **AJAX 롱 폴링** 방식을 도입했습니다.  
이 방식은 일반 폴링과는 달리, **서버가 새로운 데이터를 감지할 때까지 응답을 지연시킨 후 전송**하는 구조입니다.

- 클라이언트는 AJAX 요청을 보낸 후, 서버의 응답이 오기를 기다림  
- 서버는 새로운 ECG 데이터가 생성되면 응답을 반환  
- 클라이언트는 응답 수신 후 즉시 다음 요청을 보내, 연속적인 실시간 흐름을 유지  

---

### 🎯 결과

- 기존 방식 대비 **데이터 수신 지연이 70% 이상 감소**
- **0.1초 이내의 실시간 반응성** 확보로 사용자에게 자연스러운 ECG 시각화 제공
- 서버는 **불필요한 요청에 응답하지 않아 리소스 절약**, 시스템 전체 안정성 증가


---

## 🖥️ 시스템 구성

### 1. 하드웨어 구성
- **Raspberry Pi 4B** (Raspbian OS)
- **Arduino R4 WiFi**
- **ECG Sensor (AD8232)**

### 2. 데이터 처리
- 아두이노로부터 ECG 신호 수집
- Raspberry Pi에 설치된 MySQL DB에 실시간 저장

### 3. 웹 애플리케이션
- Django(Python) 기반 웹 서버 구축
- Bootstrap을 활용한 사용자 친화적 UI 구현
- Arduino ↔ Web ↔ DB 간의 연동을 통한 실시간 데이터 처리

---

## 🛠️ 기술 스택

### 🔹 Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### 🔹 Backend
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

### 🔹 Hardware & Sensor
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
- ECG Sensor (AD8232)  

### 🔹 Database
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

### 🔹 Server
![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi) 
- Raspbian OS  

---

## 📌 프로젝트 목적 요약

> **"실시간 부정맥 감지와 개인 건강 관리를 지원하는 통합 웹 서비스 구축"**

---

