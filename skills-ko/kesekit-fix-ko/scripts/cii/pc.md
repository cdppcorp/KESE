# PC 점검 스크립트

## 1. 비밀번호 최대 사용기간 (PC-01)
```powershell
net accounts | findstr "최대"
```

## 2. 공유 폴더 (PC-04)
```powershell
net share
```

## 3. 백신 (PC-13~14)
```powershell
Get-MpComputerStatus
```

## 4. 방화벽 (PC-15)
```powershell
Get-NetFirewallProfile | Select Name, Enabled
```

## 5. 화면보호기 (PC-16)
```powershell
reg query "HKCU\Control Panel\Desktop" /v ScreenSaveTimeOut
```
