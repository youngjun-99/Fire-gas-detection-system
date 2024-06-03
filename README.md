### 프로젝트 이름: 불 및 가스 센서기반 화재 감지 및 소화기 위치 알림 시스템

이 프로젝트는 ESP8266 모듈을 사용하여 화재 및 가스 센서를 통해 데이터를 수집하고, 이 데이터를 REST API를 통해 제공하는 시스템입니다. 파이썬 클라이언트는 주기적으로 API를 호출하여 데이터를 받아, 특정 조건이 만족되면 알람을 울리고 네오픽셀 LED 스트립을 점등합니다.

---

### 목차

1. [개요](#개요)
2. [하드웨어](#하드웨어)
3. [설치 및 설정](#설치-및-설정)
4. [작동 방식](#작동-방식)

---

### 개요

이 프로젝트는 다음과 같은 기능을 제공합니다:

- 화재 및 가스 센서로부터 데이터를 수집합니다.
- ESP8266 모듈을 통해 수집된 데이터를 REST API로 제공합니다.
- 파이썬 클라이언트가 주기적으로 API를 호출하여 데이터를 수집합니다.
- 특정 조건이 만족되면 버저로 알람을 울리고, 네오픽셀 LED 스트립을 점등합니다.

### 하드웨어

- ESP8266 모듈
- MQ-2 가스 센서 (또는 유사한 가스 센서)
- 화재 감지 센서
- 네오픽셀 LED 스트립
- 버저
- 라즈베리 파이 (파이썬 클라이언트 실행용)

### 설치 및 설정

1. **ESP8266 설정**:

   - Arduino IDE를 설치하고 ESP8266 보드 매니저 URL을 추가합니다.
   - ESP8266 보드를 선택하고 필요한 라이브러리를 설치합니다 (`ESP8266WiFi`, `ESP8266WebServer`).

2. **파이썬 클라이언트 설정**:

   - 라즈베리 파이에 필요한 파이썬 라이브러리를 설치합니다.
     ```bash
     pip install -r requirements.txt
     ```

### 작동 방식

1. **ESP8266 모듈**:
   - 화재 및 가스 센서로부터 데이터를 읽습니다.
   - 데이터를 REST API로 제공합니다 (`/api/data`).

2. **파이썬 클라이언트**:
   - 주기적으로 ESP8266의 API를 호출하여 센서 데이터를 가져옵니다.
   - 특정 조건 (예: 화재가 없고 가스 수치가 300 이상일 때)이 만족되면 버저로 알람을 울리고 네오픽셀 LED 스트립을 빨간색으로 점등합니다.

이 프로젝트는 IoT 기반의 화재 및 가스 감지 시스템으로, 실시간 모니터링과 경고 기능을 제공합니다.