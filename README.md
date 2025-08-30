# JWT Attack PoC – Brute Forcing Weak Secrets

## 🔍 Overview
This repository demonstrates how **weakly signed JSON Web Tokens (JWTs)** can be exploited through brute-force attacks. It includes:
- A script to generate a JWT with a weak secret.
- A proof-of-concept (PoC) brute-force attack to recover the secret.

⚠️ **Disclaimer:** This project is for educational purposes only. Do not use it for illegal activities.

---

## ✅ Features
- Generate JWT tokens using **PyJWT**.
- Brute-force attack on JWT secrets using:
  - Incremental key generation.
  - Custom wordlists.
- Detect weak secret vulnerabilities in JWT authentication systems.

---

## 📦 Requirements
- Python 3.x
- Dependencies:
```bash
pip install pyjwt

# JWT Attack PoC

## Overview
This PoC demonstrates a brute-force attack on a JWT token signed with a weak secret key using `PyJWT`.

## Requirements
- Python 3.x
- Install dependencies:
```bash
pip install pyjwt
```

## Usage
1. Generate or obtain a JWT token.
2. Run the script with your JWT token as an argument:
```bash
python jwt_attack_demo.py <your_jwt_token>
```
3. (Optional) Use a wordlist for keys:
```bash
python jwt_attack_demo.py <your_jwt_token> -w wordlist.txt
```

## Notes
- This script uses a brute-force method for demonstration.
- In real scenarios, attackers use large wordlists like **rockyou.txt**.
- Weak keys make JWT tokens vulnerable to attacks.
