# Unix 서버 점검 스크립트

## 1. 계정 관리
```bash
# U-01: root 원격 접속 제한
grep -i "PermitRootLogin" /etc/ssh/sshd_config
cat /etc/default/login | grep CONSOLE  # Solaris
cat /etc/securetty  # Linux

# U-02: 비밀번호 정책
cat /etc/login.defs | grep -E "PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_MIN_LEN|PASS_WARN_AGE"
cat /etc/security/pwquality.conf  # Linux

# U-03: 계정 잠금
cat /etc/pam.d/system-auth | grep pam_tally
cat /etc/security/user | grep loginretries  # AIX

# U-04: shadow 파일 보호
ls -la /etc/shadow

# U-05: UID 0 점검
awk -F: '$3==0 {print $1}' /etc/passwd

# U-06: su 제한
cat /etc/pam.d/su | grep pam_wheel
ls -la /usr/bin/su

# U-12: 세션 타임아웃
echo $TMOUT
```

## 2. 파일 및 디렉터리 관리
```bash
# U-14: root PATH
echo $PATH | grep "::"
echo $PATH | grep ":$"

# U-16~U-22: 주요 파일 권한
ls -la /etc/passwd /etc/shadow /etc/hosts /etc/services
ls -la /etc/inetd.conf /etc/xinetd.conf /etc/syslog.conf /etc/rsyslog.conf

# U-23: SUID/SGID
find / -perm -4000 -o -perm -2000 2>/dev/null

# U-25: world writable
find / -type f -perm -002 2>/dev/null

# U-26: /dev 점검
find /dev -type f 2>/dev/null

# U-27: rhosts
find / -name ".rhosts" -o -name "hosts.equiv" 2>/dev/null

# U-28: 접속 제한
cat /etc/hosts.allow
cat /etc/hosts.deny
iptables -L

# U-30: umask
umask
grep umask /etc/profile /etc/bashrc
```

## 3. 서비스 관리
```bash
# U-34~U-44: 불필요 서비스 점검
systemctl list-unit-files --state=enabled
chkconfig --list  # CentOS 6
inetadm  # Solaris

# U-39~U-40: NFS
showmount -e
cat /etc/exports
cat /etc/dfs/dfstab  # Solaris

# U-45~U-48: 메일 서비스
sendmail -d0.1 -bt < /dev/null 2>&1 | grep Version
postconf mail_version
cat /etc/mail/sendmail.cf | grep "O PrivacyOptions"

# U-49~U-51: DNS
named -v
cat /etc/named.conf | grep "allow-transfer"

# U-58~U-61: SNMP
cat /etc/snmp/snmpd.conf | grep -i community
ps -ef | grep snmp
```

## 4. 패치 관리
```bash
# 패치 현황
uname -a
rpm -qa --last | head -20  # Linux
showrev -p  # Solaris
instfix -i | grep ML  # AIX
```

## 5. 로그 관리
```bash
# U-65: NTP
ntpq -p
cat /etc/ntp.conf
chronyc sources  # CentOS 8+

# U-66: 로깅 설정
cat /etc/rsyslog.conf
cat /etc/syslog.conf

# U-67: 로그 권한
ls -la /var/log/
```
