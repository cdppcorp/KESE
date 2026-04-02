# Web Application 점검 스크립트

## 1. SQL Injection
```
- 문자열 연결 쿼리: "SELECT * FROM users WHERE id = '" + input
- 안전: PreparedStatement, 매개변수화 쿼리, ORM
```

## 2. XSS
```
- innerHTML, document.write(input), v-html
- 안전: textContent, DOMPurify, 자동 이스케이프
```

## 3. Command Injection
```
- Runtime.exec(input), subprocess(shell=True)
- 안전: 화이트리스트 검증, execFile
```

## 4. CSRF
```
- POST 요청에 CSRF 토큰 누락
- 안전: 프레임워크 CSRF 미들웨어
```

## 5. File Upload
```
- 확장자 미검증, 웹 루트 내 저장
- 안전: 화이트리스트, 웹 루트 외부 저장, 랜덤 파일명
```
