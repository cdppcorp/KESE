# 클라우드 점검 스크립트

## 1. 운영 관리
```bash
# AWS
aws iam list-users
aws iam get-credential-report
aws ec2 describe-security-groups
aws s3api get-bucket-encryption --bucket <bucket>
aws cloudtrail describe-trails

# Azure
az ad user list
az network nsg list
az storage account list

# GCP
gcloud iam service-accounts list
gcloud compute firewall-rules list
```
