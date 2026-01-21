# 🏛️ Cloud Guardian: Automated FinOps & Security Audit Suite

A powerful Python-based automation suite designed to identify cloud waste, enforce security best practices (IAM), and optimize infrastructure costs across AWS and GCP.

## 🚀 The Problem
Unmanaged cloud environments often lead to "Cloud Swell" — unattached storage, idle instances, and security gaps (like aged IAM keys) that inflate monthly bills and increase risk.

## 🛠️ The Solution
This suite provides a set of specialized scripts to automate the heavy lifting of cloud auditing, transforming manual "cleanups" into a streamlined, code-driven process.

### Core Features:
* **Cost Optimization (FinOps):** Automatically detects idle EC2/GCP instances and orphaned EBS volumes/GCS buckets.
* **Security & Compliance:** Scans for aged IAM access keys, users without MFA enabled, and publicly accessible S3 buckets.
* **Automated Reporting:** Generates clean logs and summaries of potential monthly savings.
* **Multi-Cloud Ready:** Supports both AWS (Boto3) and GCP (Google Cloud SDK).

## 🧰 Tech Stack
* **Language:** Python 3.x
* **SDKs:** Boto3 (AWS), Google Cloud Client Libraries
* **Automation:** CLI-based execution for easy integration into Cron jobs or CI/CD pipelines.

## 📂 Project Structure
```text
├── aws/
│   ├── iam_security_audit.py    # Audits IAM keys & MFA status
│   └── ec2_waste_scanner.py     # Finds unattached EBS & idle instances
├── gcp/
│   ├── gcs_bucket_auditor.py    # Public access & lifecycle checker
│   └── cloud_run_monitor.py     # Analyzes batch job performance/costs
├── utils/
│   └── logger.py                # Centralized reporting tool
└── main.py                      # Master execution script