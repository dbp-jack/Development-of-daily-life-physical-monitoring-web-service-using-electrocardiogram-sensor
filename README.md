# Development-of-daily-life-physical-monitoring-web-service-using-electrocardiogram-sensor
캡스톤디자인 (아두이노) 심전도 센서를 활용한 일상 생활 신체 모니터링 웹 서비스 개발 프로젝트

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
#E34F26
- CSS3  
- Bootstrap  

### 🔹 Backend
- Python  
- Django  

### 🔹 Hardware & Sensor
- Arduino R4 WiFi  
- ECG Sensor (AD8232)  

### 🔹 Database
- MySQL  

### 🔹 Server
- Raspberry Pi 4B  
- Raspbian OS  

---

## 📌 프로젝트 목적 요약

> **"실시간 부정맥 감지와 개인 건강 관리를 지원하는 통합 웹 서비스 구축"**

---

