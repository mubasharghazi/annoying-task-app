# 📩 TaskExtractor AI

> **Turn chaotic updates, long emails, and Slack threads into structured action items in seconds.**

[![AWS Amplify](https://img.shields.io/badge/AWS_Amplify-FF9900?style=for-the-badge&logo=aws-amplify&logoColor=white)](https://aws.amazon.com/amplify/)
[![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)](https://aws.amazon.com/lambda/)
[![Amazon Bedrock](https://img.shields.io/badge/Amazon_Bedrock-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/bedrock/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Live Demo:** [https://main.dkohc338zhk81.amplifyapp.com/](https://main.dkohc338zhk81.amplifyapp.com/)

---

## 🚀 Overview

**TaskExtractor AI** is a lightweight, zero-maintenance serverless application built for the **AWS Weekend Challenge**. It solves a universal daily chore: sifting through overwhelming walls of text every morning just to find out what needs to be done.

By processing raw context through **Amazon Bedrock Nova models**, TaskExtractor AI instantly returns:
* 📌 **Executive Summary** (3 key bullet points)
* 📝 **Action Item Checklist** (with assigned owners)
* ⚡ **Urgency Score** (High / Medium / Low)

---

## 🏗️ Architecture
[ User Inputs Text ] <br>
│ <br>
▼ <br>
[ Frontend Web UI (AWS Amplify) ] <br>
│ <br>
▼ <br>
[ Amazon API Gateway (POST /extract) ] <br>
│ <br>
▼ <br>
[ AWS Lambda (Python 3.12) ] <br>
│ <br>
▼ <br>
[ Amazon Bedrock (Nova Models) ] <br>
│ <br>
▼ <br>
[ Formatted Action Plan returned to User ] <br>

---

## 🛠️ AWS Services Used

* **AWS Amplify:** Global hosting for the static single-page frontend with automatic CI/CD.
* **Amazon API Gateway:** REST API endpoint handling HTTP requests and CORS permissions.
* **AWS Lambda (Python 3.12):** Serverless business logic formatting prompts and handling Bedrock invocations via `boto3`.
* **Amazon Bedrock (Nova Models):** Fast, low-latency natural language processing and task extraction.

---
