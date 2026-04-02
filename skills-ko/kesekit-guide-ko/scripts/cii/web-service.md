# 웹 서비스 점검 스크립트

## 1. 디렉터리 리스팅 (WEB-04)
```bash
# Apache
grep -i "Options" /etc/httpd/conf/httpd.conf | grep -i "Indexes"
# Nginx
grep -i "autoindex" /etc/nginx/nginx.conf
```

## 2. 프로세스 권한 (WEB-09)
```bash
ps -ef | grep httpd | grep -v root
```

## 3. 헤더 정보 노출 (WEB-16)
```bash
# Apache: grep "ServerTokens" httpd.conf → Prod 설정
# Nginx: grep "server_tokens" nginx.conf → off 설정
```

## 4. WebDAV (WEB-18)
```bash
grep -i "LoadModule.*dav" /etc/httpd/conf/httpd.conf
```

## 5. SSL/TLS (WEB-20)
```bash
grep -i "SSLProtocol\|ssl_protocols" /etc/httpd/conf.d/ssl.conf /etc/nginx/nginx.conf
```
