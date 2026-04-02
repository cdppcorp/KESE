# DBMS 점검 스크립트

## 1. 계정 관리
```sql
-- Oracle: 계정 확인
SELECT USERNAME, ACCOUNT_STATUS, PROFILE FROM DBA_USERS;
-- Oracle: 비밀번호 변경
ALTER USER <계정> IDENTIFIED BY <신규비밀번호>;

-- MSSQL: sa 비밀번호 변경
ALTER LOGIN sa WITH PASSWORD = '신규비밀번호';

-- MySQL: root 비밀번호 변경
ALTER USER 'root'@'localhost' IDENTIFIED BY '신규비밀번호';

-- PostgreSQL: 역할 확인
SELECT rolname, rolsuper FROM pg_roles;
```
