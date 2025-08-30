# jwt-attack-poc
jwt-attack-poc demonstrates a proof-of-concept brute-force attack on JWT tokens signed with weak secrets. Includes scripts to generate tokens, crack weak keys, and a research report on common JWT vulnerabilities, real-world CVEs, and security best practices. For educational and research use only.

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
