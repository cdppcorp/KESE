# 제38장. 디지털헬스케어 서비스 인프라 보안

디지털헬스케어(Digital Healthcare, DHC) 서비스는 모바일 앱, 웹 서비스, 서버, 웹 서버, 데이터베이스 관리 시스템(Database Management System, DBMS)으로 구성됩니다. 각 계층은 개인의료정보(Protected Health Information, PHI)를 처리하거나 중계합니다. 이 장에서는 KESE KIT 기술적 취약점 점검(3~12장)의 기반 위에서, 의료 환경 특수성을 반영한 인프라 계층별 보안 요구사항을 다룹니다.

> **TIP**
> 이 장의 내용은 KESE KIT Part II(기술적 취약점 점검)와 상당 부분 중복됩니다. 기존 점검 항목을 그대로 적용하되, 의료 환경 특수 요구사항(PHI 보호, 24/7 가용성, 식품의약품안전처 인증 등)을 추가로 확인하세요.

---

## 38-1. 모바일 앱 보안

디지털헬스케어 모바일 앱은 환자 데이터를 직접 수집하고 표시합니다. 기기 분실·도난 시 PHI 유출 위험이 큽니다. 네 가지 영역으로 보안 요구사항을 구분합니다.

### (1) 인증 (Authentication)

**사용자 인증** 항목은 다음을 포함합니다.

- 초기 자격증명(Credential) 설정 및 변경을 앱 최초 실행 시 요구합니다.
- 관리 기능 또는 중요정보 접근 전에 반드시 인증 절차를 거칩니다.
- 반복 인증 실패 시 계정을 잠금(Lockout) 처리합니다.
- 계정 및 권한(Role) 생성·변경·삭제를 관리자만 수행하도록 통제합니다.
- 비밀번호(Password) 길이·복잡도·변경 주기 정책을 강제합니다.

**인증 정보 안전 사용** 항목은 다음을 포함합니다.

- 비밀번호·토큰(Token)을 소스코드에 하드코딩하거나 평문으로 저장하는 것을 금지합니다.
- 비밀번호 입력 화면에서 마스킹(Masking)을 적용합니다.
- 인증 실패 시 실패 사유(아이디 불일치/비밀번호 불일치 구분)를 외부에 노출하지 않습니다.

**제품 인증** 항목은 다음을 포함합니다.

- 의료기기(Medical Device)·웨어러블(Wearable) 등 제품 간 중요 정보를 전송하거나 제어 명령을 실행하기 전에 상호 인증(Mutual Authentication)을 수행합니다.

> **TIP**
> Android에서는 키스토어(Android KeyStore)를 사용하여 인증 키를 안전하게 저장하세요. iOS에서는 키체인(Keychain)을 활용합니다. 두 플랫폼 모두 생체인증(Biometric Authentication) API를 제공하므로, 중요 기능 진입 시 지문·안면 인증을 추가 적용하는 것을 권장합니다.

### (2) 암호 (Cryptography)

- 전송 및 저장되는 중요정보는 안전한 암호 알고리즘(Algorithm)으로 보호합니다.
- 국내 기준: 「암호이용활성화」 고시에 따라 AES-128 이상, SHA-256 이상을 사용합니다.
- 키(Key) 관리는 플랫폼 제공 보안 저장소(KeyStore/Keychain)를 활용합니다.
- 사용이 금지된 알고리즘(DES, MD5, SHA-1)은 즉시 교체합니다.

### (3) 데이터 보호 (Data Protection)

**전송데이터** 항목은 다음을 포함합니다.

- 제품 간 전송하는 중요정보는 암호화합니다.
- TLS(Transport Layer Security) 등 알려진 보안 프로토콜 사용 시 보안 모드(TLS 1.2 이상)를 적용합니다.
- 인증서 고정(Certificate Pinning)으로 중간자 공격(MITM, Man-In-The-Middle Attack)을 방어합니다.

**저장데이터** 항목은 다음을 포함합니다.

- 기기 내부에 저장하는 중요정보는 암호화합니다.
- 외부 저장소(SD 카드 등)에 PHI를 저장하는 것을 지양합니다.

**정보흐름 통제** 항목은 다음을 포함합니다.

- 비인가 네트워크 트래픽을 차단합니다.
- 앱이 선언한 네트워크 도메인 외부로의 데이터 전송을 방지합니다.

**세션 관리** 항목은 다음을 포함합니다.

- 유휴 시간 초과(Session Timeout) 발생 시 세션을 잠금 또는 종료합니다.
- 백그라운드 전환 시에도 민감 화면을 숨깁니다.

**개인정보** 항목은 다음을 포함합니다.

- 앱이 처리하는 개인정보(Personal Information)를 화면 표시·로그·전송 시 비식별화(De-identification)합니다.
- 주민등록번호, 진단명, 처방 내역 등은 마스킹 또는 가명처리(Pseudonymization) 후 사용합니다.

### (4) 플랫폼 보호 (Platform Protection)

**SW 보안** 항목은 다음을 포함합니다.

- 시큐어코딩(Secure Coding) 가이드라인을 적용합니다. (KESE KIT 29~31장 참조)
- 알려진 취약점(CVE, Common Vulnerabilities and Exposures)을 정기적으로 검증하고 제거합니다.

**SW 보안(추가)** 항목은 다음을 포함합니다.

- 역공학 방지를 위해 코드 난독화(Obfuscation)를 적용합니다.
- 주요 설정 파일 및 실행 코드의 무결성(Integrity)을 검증합니다.
- 루팅(Rooting) 및 탈옥(Jailbreak) 환경을 탐지하고 실행을 제한합니다.

**업데이트** 항목은 다음을 포함합니다.

- 앱 업데이트 전 인가된 사용자 또는 서버임을 확인합니다.
- 업데이트 패키지의 무결성 검사(Hash 검증)를 수행합니다.

**보안 관리** 항목은 다음을 포함합니다.

- 앱에서 불필요한 서비스·퍼미션(Permission)을 제거합니다.
- 원격 관리는 신뢰 환경(VPN, 전용망)에서만 허용합니다.
- 서드파티(Third-party) 라이브러리는 최신 보안 패치를 유지합니다.

**감사기록** 항목은 다음을 포함합니다.

- 로그인·로그아웃, 인증 실패, 중요 데이터 접근 등 보안 관련 이벤트의 감사 로그(Audit Log)를 생성합니다.
- 감사 로그를 변조·삭제하지 못하도록 보호합니다.

> **WARNING**
> 루팅·탈옥 환경에서는 KeyStore/Keychain 보호가 우회될 수 있습니다. 루팅·탈옥 탐지 라이브러리(예: Android의 RootBeer, iOS의 DTTJailbreakDetection)를 적용하고, 탐지 시 앱 실행을 차단하거나 사용자에게 경고를 표시하세요.

---

## 38-2. 웹 서비스 보안

디지털헬스케어 웹 서비스는 의사·환자·관리자가 브라우저로 접근합니다. 웹 취약점은 PHI 대량 유출로 직결될 수 있습니다. KESE KIT 6장(웹 애플리케이션 점검)과 29장(입력데이터 검증)을 기반으로 합니다.

### (1) 입력값 검증

- SQL 삽입(SQL Injection, CWE-89): 모든 DB 쿼리(Query)에 매개변수화된 쿼리(Parameterized Query)를 사용합니다.
- 크로스사이트 스크립팅(Cross-Site Scripting, XSS, CWE-79): 출력 시 HTML 이스케이프(Escape)를 적용합니다.
- 크로스사이트 요청 위조(Cross-Site Request Forgery, CSRF, CWE-352): CSRF 토큰(Token)을 모든 상태 변경 요청에 검증합니다.
- 파일 업로드 공격: 허용 확장자를 화이트리스트(Whitelist)로 제한하고, 업로드 파일을 웹 루트 외부에 저장합니다.

```python
# Django: 매개변수화된 쿼리 예시
from django.db import connection

def get_patient(patient_id):
    # 안전: 매개변수화된 쿼리 사용
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM patients WHERE id = %s",
            [patient_id]
        )
        return cursor.fetchone()
```

> **TIP**
> 헬스케어 웹 서비스의 검색 기능(환자명, 진단코드 등)은 SQL Injection 공격의 주요 대상입니다. ORM(Object-Relational Mapping)을 사용하더라도 raw 쿼리 사용 시에는 반드시 매개변수 바인딩(Binding)을 확인하세요.

### (2) 인증 관리

- 불충분한 인증(Insufficient Authentication) 및 인가(Authorization) 취약점을 방지합니다.
- 관리 메뉴 및 개인 의료정보 메뉴 접근 전에 인증을 반드시 수행합니다.
- 수평적 권한 상승(Horizontal Privilege Escalation): 타 환자 데이터 접근을 URL 파라미터 조작으로 시도하는 공격을 차단합니다.
- 세션(Session) 관리:
  - 예측 불가능한 세션 ID(Session ID)를 사용합니다.
  - 세션 타임아웃(Session Timeout)을 30분 이하로 설정합니다.
  - 로그아웃 시 서버 측 세션을 즉시 무효화합니다.

### (3) 암호 관리

- 전송 시: HTTPS(TLS 1.2 이상)를 강제합니다. HTTP는 리다이렉트(Redirect) 처리합니다.
- 저장 시: 비밀번호는 bcrypt, Argon2 등 단방향 해시(Hash) 함수로 저장합니다.
- 비밀번호 정책:
  - 최소 길이 8자 이상, 영문·숫자·특수문자 조합
  - 90일 이하 주기 변경 권고
  - 최근 사용 비밀번호 재사용 금지 (최근 5개)

### (4) 보안 관리

- 에러 메시지(Error Message) 정보 노출을 방지합니다. 스택 트레이스(Stack Trace)를 외부에 노출하지 않습니다.
- 디렉터리 인덱싱(Directory Indexing)을 비활성화합니다.
- 관리자 페이지는 내부망 IP 대역 또는 VPN으로 접근을 제한합니다.
- 응답 헤더(Response Header)에서 서버 기술 정보(X-Powered-By, Server 등)를 제거합니다.
- 콘텐츠 보안 정책(Content Security Policy, CSP) 헤더를 설정합니다.

KESE KIT 5장(웹 서비스 점검) 및 6장(웹 애플리케이션 점검)에서 세부 점검 항목을 확인하세요.

---

## 38-3. 서버 보안

헬스케어 인프라 서버는 전자의무기록(Electronic Medical Record, EMR), 처방전달시스템(Order Communication System, OCS), 영상저장전송시스템(Picture Archiving and Communication System, PACS) 등 핵심 시스템을 운용합니다. KESE KIT 3장(Unix/Linux 점검)과 4장(Windows 점검)을 기반으로 합니다.

### (1) 계정 관리

- 반복 로그인 실패 시 계정 잠금 정책을 설정합니다.
- 유효기간이 만료된 계정의 서비스 접근을 즉시 제한합니다.
- 게스트(Guest)·테스트(Test)·공유 계정의 사용을 통제합니다.
- 운영 서버에 개발자 계정을 남겨두는 것을 금지합니다.

```bash
# 계정 잠금 정책 설정 (Linux - PAM 방식)
# /etc/pam.d/system-auth 또는 /etc/pam.d/common-auth 편집
# 5회 실패 시 잠금, 600초 후 자동 해제
auth required pam_tally2.so deny=5 unlock_time=600

# 비밀번호 만료 설정 (90일 만료, 7일 전 경고)
chage -M 90 -W 7 username

# 현재 계정 만료 정보 확인
chage -l username
```

```bash
# 불필요 계정 확인 및 잠금
# 비활성 계정 목록 조회 (90일 이상 미사용)
lastlog | awk '$4 == "Never" || ...'

# 계정 잠금 (삭제 전 백업 용도)
usermod -L username

# 테스트 계정 확인
grep -E '^(test|demo|guest|tmp)' /etc/passwd
```

### (2) 파일 및 디렉터리 관리

주요 시스템 파일의 소유자 및 권한을 다음과 같이 설정합니다.

| 파일 경로 | 권장 소유자 | 권장 권한 |
|-----------|------------|-----------|
| /etc/passwd | root | 644 |
| /etc/shadow | root | 000 또는 400 |
| /etc/hosts | root | 644 |
| /etc/syslog.conf | root | 640 |
| /etc/crontab | root | 600 |

[표 38-1] 주요 시스템 파일 권한 설정 기준

- 사용자 홈 디렉터리 및 환경 설정 파일(`.bashrc`, `.profile`)의 권한을 700 이하로 설정합니다.
- 접속 허용 IP(IP Address) 및 포트(Port)를 `/etc/hosts.allow`, `/etc/hosts.deny`로 제한합니다.

```bash
# 주요 파일 권한 일괄 점검
stat -c "%n %U %a" /etc/passwd /etc/shadow /etc/hosts /etc/syslog.conf

# shadow 파일 권한 설정
chmod 400 /etc/shadow
chown root:root /etc/shadow
```

### (3) 서비스 관리

불필요하거나 취약한 서비스는 비활성화합니다.

- Anonymous FTP(File Transfer Protocol)를 비활성화합니다.
- DoS(Denial of Service) 취약 서비스를 비활성화합니다.
  - echo(7), discard(9), daytime(13), chargen(19)
  - NTP(123), DNS(53), SNMP(161-162), SMTP(25)

```bash
# inetd 기반 서비스 비활성화
# /etc/inetd.conf 에서 불필요 서비스 주석 처리
# echo    stream  tcp  nowait  root  internal  →  # echo  stream ...

# systemd 기반 서비스 비활성화
systemctl disable telnet.socket
systemctl stop telnet.socket

# 현재 활성 포트 확인
ss -tlnp | grep -E ':(7|9|13|19|23|25|53|123|161)'
```

- DNS(Domain Name System) Zone Transfer를 허가된 슬레이브(Slave) 서버로만 제한합니다.
- 디렉터리 리스팅(Directory Listing)을 제거합니다.
- 불필요한 샘플·기본 파일을 제거합니다.
- 파일 업로드·다운로드 경로를 허용 목록으로 제한합니다.

### (4) 패치 관리

- 운영체제 및 설치된 패키지의 최신 보안 패치를 정기적으로 적용합니다.
- 백신(Antivirus) 프로그램 및 악성코드(Malware) 탐지 솔루션을 최신 버전으로 업데이트합니다.

```bash
# 보안 업데이트 확인 및 적용 (Ubuntu/Debian)
apt-get update && apt-get upgrade --only-upgrade

# 보안 업데이트만 선별 적용
unattended-upgrades --dry-run  # 사전 확인
unattended-upgrades             # 실제 적용

# 설치된 패키지 취약점 확인
apt-get install debsecan
debsecan --suite $(lsb_release -cs) --format detail
```

> **WARNING**
> 의료 서버는 24/7 가용성(Availability)이 요구됩니다. 패치 적용 시 반드시 테스트 환경에서 검증 후 운영 서버에 적용하세요. 환자 생명과 직결된 시스템의 다운타임(Downtime)은 최소화해야 합니다. 패치 적용 전 스냅샷(Snapshot) 또는 백업(Backup)을 반드시 생성하세요.

### (5) 로그 관리

- 보안 이벤트 로그(Log)를 정기적으로 검토하고 보고합니다.
- 로그 보존 정책에 따라 시스템 로깅(Logging)을 설정합니다. (의료법상 최소 5년 권장)
- 원격 중앙 로그 서버(Syslog Server)로 로그를 전송하여 로컬 변조를 방지합니다.

```bash
# rsyslog를 사용한 원격 로그 서버 전송 설정
# /etc/rsyslog.conf 에 추가
*.* @10.0.0.100:514       # UDP 전송
*.* @@10.0.0.100:514      # TCP 전송 (신뢰성 높음)

# 로그 감사 (auditd) 설정
systemctl enable auditd
auditctl -w /etc/passwd -p wa -k passwd_changes
auditctl -w /var/log/auth.log -p r -k auth_access
```

---

## 38-4. 웹 서버 보안

디지털헬스케어 서비스의 웹 서버(Apache, Nginx 등)는 외부에서 직접 접근 가능한 계층입니다. KESE KIT 5장(웹 서비스 점검)을 기반으로 합니다.

### (1) 접근제어

- 웹 서버 프로세스(Process)를 전용 계정(예: `www-data`, `nginx`)으로 실행하고 최소 권한(Least Privilege)을 부여합니다.
- 웹 루트(Web Root) 디렉터리에 쓰기(Write) 권한을 부여하지 않습니다.
- 웹 서버 계정이 시스템 파일(/etc, /bin 등)에 접근하지 못하도록 제한합니다.

```bash
# Apache 프로세스 실행 계정 확인
ps aux | grep apache2

# 웹 루트 쓰기 권한 점검
find /var/www/html -perm -o+w -type f
find /var/www/html -perm -o+w -type d

# 소유권 및 권한 설정
chown -R root:www-data /var/www/html
find /var/www/html -type d -exec chmod 755 {} \;
find /var/www/html -type f -exec chmod 644 {} \;
```

### (2) 보안 설정

불필요한 파일을 제거하고 서버 정보를 숨깁니다.

```apache
# Apache - 서버 정보 숨김 설정
# /etc/apache2/conf-available/security.conf 편집
ServerTokens Prod
ServerSignature Off

# HTTP 메서드 제한 (GET, POST만 허용)
<Directory /var/www/html>
    <LimitExcept GET POST>
        Require all denied
    </LimitExcept>
</Directory>

# MultiViews 비활성화 (콘텐츠 협상 공격 방지)
<Directory /var/www/html>
    Options -MultiViews -Indexes
</Directory>

# 디렉터리 인덱싱 비활성화
Options -Indexes
```

```nginx
# Nginx - 서버 정보 숨김 설정
# /etc/nginx/nginx.conf 편집
server_tokens off;

# HTTP 메서드 제한
server {
    if ($request_method !~ ^(GET|POST)$) {
        return 405;
    }
}

# 디렉터리 인덱싱 비활성화
autoindex off;
```

추가 보안 설정 항목입니다.

- 응답 메시지 헤더(Response Header)에서 서버 버전 정보를 숨깁니다.
- 파일 업로드·다운로드 경로 및 크기를 제한합니다.
- 접근 로그(Access Log) 및 오류 로그(Error Log)를 설정하고 주기적으로 검토합니다.
- 불필요한 기본 설정 파일(welcome.conf, autoindex.conf 등)을 제거합니다.

> **TIP**
> HSTS(HTTP Strict Transport Security) 헤더를 설정하면 브라우저가 HTTP 접속을 자동으로 HTTPS로 전환합니다. `Strict-Transport-Security: max-age=31536000; includeSubDomains` 헤더를 응답에 추가하세요. 의료 서비스에서는 필수 설정으로 권장합니다.

### (3) 보안 패치

- 웹 서버 소프트웨어(Apache, Nginx, IIS 등)의 최신 보안 패치를 정기적으로 적용합니다.
- 웹 서버 버전을 공개된 취약점 데이터베이스(NVD, CVE)와 대조하여 점검합니다.

```bash
# Apache 버전 확인
apache2 -v

# 알려진 취약점 버전 확인 (예시)
# Apache 2.4.49 이하: CVE-2021-41773 경로 순회 취약점
# 설치된 버전 확인 후 최신 패치 적용 여부 판단

# Nginx 버전 확인
nginx -v
```

---

## 38-5. DBMS 보안

의료 데이터베이스에는 PHI가 직접 저장됩니다. 데이터베이스 관리 시스템(DBMS) 보안은 KESE KIT 7장(DBMS 점검)을 기반으로 합니다.

### (1) 계정 관리

- 기본 계정(root, sa, admin, sys 등)의 비밀번호를 초기 설치 즉시 변경합니다.
- 비밀번호 만료 및 복잡도 정책을 DBMS 자체적으로 설정합니다.
- DBA(Database Administrator) 권한은 최소 필요 계정·그룹에만 부여합니다.

```sql
-- MySQL: 기본 계정 보안 강화
ALTER USER 'root'@'localhost' IDENTIFIED BY 'StrongP@ss!2026';

-- 익명 계정 제거
DROP USER IF EXISTS ''@'localhost';
DROP USER IF EXISTS ''@'%';

-- 테스트 데이터베이스 제거
DROP DATABASE IF EXISTS test;

-- 계정 목록 확인
SELECT user, host, authentication_string
FROM mysql.user
ORDER BY user;
```

```sql
-- PostgreSQL: 비밀번호 정책 설정
-- postgresql.conf 또는 ALTER SYSTEM 사용
ALTER SYSTEM SET password_encryption = 'scram-sha-256';

-- 계정 비밀번호 만료 설정
ALTER USER app_user VALID UNTIL '2026-12-31';

-- 슈퍼유저 목록 확인
SELECT usename, usesuper, usecreatedb
FROM pg_user
WHERE usesuper = true;
```

### (2) 접근 관리

- DB 서버에 대한 원격 접근을 최소한의 허용 IP로 제한합니다.
- 비DBA 사용자의 시스템 테이블(Information Schema, pg_catalog 등) 접근을 제한합니다.
- 반복 로그인 실패 시 계정을 잠금 처리합니다.

```sql
-- MySQL: 원격 접근 제한 (특정 IP 대역만 허용)
-- 기존 전체 허용 권한 제거
REVOKE ALL PRIVILEGES ON *.* FROM 'app_user'@'%';

-- 특정 IP 대역에서만 접근 허용
GRANT SELECT, INSERT, UPDATE ON healthcare_db.*
  TO 'app_user'@'10.0.0.%'
  IDENTIFIED BY 'AppP@ss!2026';

-- 권한 즉시 반영
FLUSH PRIVILEGES;
```

```bash
# MySQL 방화벽 수준 접근 제한 (iptables)
# 외부에서 MySQL 포트(3306) 직접 접근 차단
iptables -A INPUT -p tcp --dport 3306 -s 10.0.0.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j DROP
```

### (3) 옵션 관리

- 애플리케이션 계정 및 DBA 계정의 역할(Role)이 `PUBLIC`으로 설정되지 않도록 합니다.
- `PUBLIC` 역할에 부여된 불필요한 권한을 제거합니다.
- 저장 프로시저(Stored Procedure) 실행 권한을 최소화합니다.

```sql
-- PostgreSQL: PUBLIC 권한 점검 및 제거
-- PUBLIC에 부여된 권한 목록 조회
SELECT grantee, table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'PUBLIC';

-- PUBLIC 권한 제거 예시
REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC;
```

### (4) 패치 관리

- DBMS 소프트웨어(MySQL, PostgreSQL, Oracle, MSSQL 등)의 최신 보안 패치를 적용합니다.
- DB 접근·변경·삭제 이벤트에 대한 감사 로깅(Audit Logging)을 활성화합니다.

```sql
-- PostgreSQL: 감사 로깅 활성화
ALTER SYSTEM SET log_statement = 'all';
ALTER SYSTEM SET log_connections = on;
ALTER SYSTEM SET log_disconnections = on;
ALTER SYSTEM SET log_duration = on;
ALTER SYSTEM SET log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h ';

-- 설정 반영
SELECT pg_reload_conf();
```

```sql
-- MySQL: 감사 플러그인 활성화 (MySQL Enterprise 또는 MariaDB Audit)
INSTALL PLUGIN audit_log SONAME 'audit_log.so';
SET GLOBAL audit_log_policy = 'ALL';
SET GLOBAL audit_log_format = 'JSON';
```

### (5) 로그 관리

- 감사 테이블(Audit Table)이 DBA 계정 소유임을 보장합니다.
- 일반 애플리케이션 계정이 감사 로그에 쓰기·삭제 권한을 갖지 않도록 설정합니다.
- 감사 로그를 별도 저장소 또는 중앙 로그 관리 시스템(SIEM)으로 전송합니다.

```sql
-- PostgreSQL: 감사 테이블 소유권 보장
CREATE TABLE audit_log (
    id          BIGSERIAL PRIMARY KEY,
    event_time  TIMESTAMPTZ NOT NULL DEFAULT now(),
    user_name   VARCHAR(100),
    action      VARCHAR(50),
    table_name  VARCHAR(100),
    row_data    JSONB
);

-- 소유권을 DBA 계정으로 설정
ALTER TABLE audit_log OWNER TO dba_user;

-- 애플리케이션 계정은 INSERT만 허용
GRANT INSERT ON audit_log TO app_user;
REVOKE UPDATE, DELETE, TRUNCATE ON audit_log FROM app_user;
```

> **WARNING**
> 의료 데이터베이스에는 PHI(개인의료정보)가 저장됩니다. 컬럼 레벨 암호화(Column-Level Encryption, CLE)를 적용하여 DB 관리자도 평문 PHI에 접근할 수 없도록 해야 합니다. MySQL의 경우 AES_ENCRYPT/AES_DECRYPT 함수, PostgreSQL의 경우 pgcrypto 확장을 활용하세요.

---

## 38-6. 인프라 보안 종합 체크리스트

이 장에서 다룬 인프라 계층별 보안 항목을 요약합니다. 각 항목 옆에 관련 KESE KIT 장을 병기합니다.

[표 38-2] 디지털헬스케어 인프라 보안 체크리스트

| 영역 | 보안 항목 | 확인 | 관련 장 |
|------|-----------|------|---------|
| **모바일 앱** | 초기 자격증명 설정 요구 | ☐ | 38-1 |
| | 반복 인증 실패 잠금 | ☐ | 38-1 |
| | 비밀번호 하드코딩 금지 | ☐ | 38-1, 29장 |
| | 제품 간 상호 인증 | ☐ | 38-1 |
| | AES-128 이상 암호화 적용 | ☐ | 38-1 |
| | TLS 1.2 이상 전송 보안 | ☐ | 38-1 |
| | 인증서 고정(Certificate Pinning) | ☐ | 38-1 |
| | 저장 데이터 암호화 | ☐ | 38-1 |
| | 세션 타임아웃 설정 | ☐ | 38-1 |
| | PHI 비식별화 | ☐ | 38-1, 37장 |
| | 시큐어코딩 적용 | ☐ | 38-1, 29장 |
| | 코드 난독화 | ☐ | 38-1 |
| | 루팅·탈옥 탐지 | ☐ | 38-1 |
| | 서드파티 라이브러리 패치 | ☐ | 38-1 |
| | 감사 로그 생성 및 보호 | ☐ | 38-1 |
| **웹 서비스** | SQL Injection 방어 | ☐ | 38-2, 6장, 29장 |
| | XSS 방어 | ☐ | 38-2, 6장 |
| | CSRF 방어 | ☐ | 38-2, 6장 |
| | 파일 업로드 제한 | ☐ | 38-2 |
| | 불충분한 인증·인가 방지 | ☐ | 38-2, 6장 |
| | 세션 ID 예측 불가 | ☐ | 38-2 |
| | 세션 타임아웃 30분 이하 | ☐ | 38-2 |
| | HTTPS 강제 적용 | ☐ | 38-2 |
| | 비밀번호 단방향 해시 저장 | ☐ | 38-2 |
| | 에러 메시지 정보 노출 방지 | ☐ | 38-2, 5장 |
| | 디렉터리 인덱싱 비활성화 | ☐ | 38-2, 5장 |
| | 관리자 페이지 접근 제한 | ☐ | 38-2, 5장 |
| **서버** | 계정 잠금 정책 (5회) | ☐ | 38-3, 3장, 4장 |
| | 만료 계정 접근 제한 | ☐ | 38-3, 3장 |
| | 게스트·테스트 계정 통제 | ☐ | 38-3, 3장 |
| | /etc/shadow 권한 400 | ☐ | 38-3, 3장 |
| | 불필요 서비스 비활성화 | ☐ | 38-3, 3장 |
| | Anonymous FTP 비활성화 | ☐ | 38-3, 3장 |
| | DNS Zone Transfer 제한 | ☐ | 38-3, 3장 |
| | 최신 보안 패치 적용 | ☐ | 38-3 |
| | 중앙 로그 서버 전송 | ☐ | 38-3 |
| **웹 서버** | 전용 계정으로 프로세스 실행 | ☐ | 38-4, 5장 |
| | 웹 루트 쓰기 권한 제한 | ☐ | 38-4 |
| | ServerTokens Prod 설정 | ☐ | 38-4, 5장 |
| | HTTP 메서드 제한 (GET/POST) | ☐ | 38-4 |
| | MultiViews 비활성화 | ☐ | 38-4 |
| | 디렉터리 인덱싱 비활성화 | ☐ | 38-4, 5장 |
| | HSTS 헤더 설정 | ☐ | 38-4 |
| | 웹 서버 최신 패치 적용 | ☐ | 38-4 |
| **DBMS** | 기본 계정 비밀번호 변경 | ☐ | 38-5, 7장 |
| | 익명 계정 제거 | ☐ | 38-5, 7장 |
| | DBA 권한 최소화 | ☐ | 38-5, 7장 |
| | DB 원격 접근 IP 제한 | ☐ | 38-5, 7장 |
| | PUBLIC 권한 제거 | ☐ | 38-5, 7장 |
| | 감사 로깅 활성화 | ☐ | 38-5 |
| | 감사 테이블 DBA 소유 | ☐ | 38-5 |
| | 컬럼 레벨 암호화(PHI) | ☐ | 38-5 |
| | 최신 패치 적용 | ☐ | 38-5 |

> **TIP**
> 디지털헬스케어 서비스 인프라 보안은 KESE KIT의 기존 기술적 취약점 점검(Part II)과 많은 부분이 겹칩니다. 기존 점검 항목을 그대로 적용하되, 이 장에서 다루는 의료 환경 특수 요구사항(PHI 보호, 24/7 가용성, 식품의약품안전처 인증 등)을 추가로 확인하세요.

---

*관련 장: 3장(Unix/Linux 점검), 4장(Windows 점검), 5장(웹 서비스 점검), 6장(웹 애플리케이션 점검), 7장(DBMS 점검), 29장(입력데이터 검증), 37장(DHC 서비스 보안요구사항)*
