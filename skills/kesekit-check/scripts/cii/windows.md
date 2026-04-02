# Windows 서버 점검 스크립트

## 1. 계정 관리
```powershell
# W-01: Administrator 계정명
Get-LocalUser | Where-Object {$_.SID -like "*-500"} | Select Name

# W-02: Guest 비활성화
Get-LocalUser -Name "Guest" | Select Enabled

# W-04: 계정 잠금
net accounts

# W-06: 관리자 그룹
net localgroup Administrators

# W-09: 패스워드 정책
net accounts
```

## 2. 서비스 관리
```powershell
# W-17: 기본 공유
net share
Get-SmbShare

# W-18: 서비스 목록
Get-Service | Where-Object {$_.Status -eq "Running"}

# W-19: IIS
Get-Service W3SVC

# W-29~31: SNMP
Get-Service SNMP
reg query "HKLM\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities"
```

## 3. 패치 관리
```powershell
# W-38: 패치 현황
Get-HotFix | Sort-Object InstalledOn -Descending | Select -First 10
systeminfo | findstr "KB"

# W-39: 백신
Get-MpComputerStatus  # Windows Defender
```

## 4. 로그 관리
```powershell
# W-40: 감사 정책
auditpol /get /category:*

# W-41: NTP
w32tm /query /status

# W-42: 이벤트 로그 설정
Get-EventLog -List
```

## 5. 보안 관리
```powershell
# W-44: 원격 레지스트리
Get-Service RemoteRegistry | Select Status

# W-46: SAM 파일
icacls C:\Windows\System32\config\SAM

# W-47: 화면보호기
reg query "HKCU\Control Panel\Desktop" /v ScreenSaveTimeOut
reg query "HKCU\Control Panel\Desktop" /v ScreenSaverIsSecure

# W-52: Autologon
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v AutoAdminLogon

# W-59: LAN Manager
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LmCompatibilityLevel

# W-64: 방화벽
Get-NetFirewallProfile | Select Name, Enabled
```
