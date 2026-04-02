# 네트워크 장비 점검 스크립트

## 1. 계정 관리
```
! 계정 관리
show running-config | include username
show running-config | include enable secret
```

## 2. 접근 관리
```
! 접근 관리
show running-config | include line vty
show running-config | include access-class
```

## 3. SNMP
```
! SNMP
show running-config | include snmp-server
```

## 4. 불필요 서비스
```
! 불필요 서비스
show running-config | include no service
show ip http server
```
