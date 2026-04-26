# 🔐 Cryptographic Password Generator

A high-entropy, cryptographically secure password generation utility built with Python. This tool moves beyond standard pseudo-random generators by leveraging the `secrets` module for industry-standard security.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Security](https://img.shields.io/badge/Security-Cryptographic-red?style=flat)](https://docs.python.org/3/library/secrets.html)

## 🌟 Why Cryptographic?
Most basic password generators use the `random` module, which is based on the Mersenne Twister algorithm. While fast, it is **deterministic** and predictable. 

This project uses the **`secrets` module**, which generates tokens suitable for managing secrets such as passwords, account authentication, and security tokens. It utilizes the highest quality of randomness provided by the underlying operating system.

## ✨ Key Features
- **CS-PRNG:** Uses Cryptographically Secure Pseudo-Random Number Generators.
- **Complexity Enforcement:** Guaranteed inclusion of:
  - Upper & Lowercase letters
  - Digits (0-9)
  - Special characters (!@#$%^&*)
- **Input Validation:** Prevents crashes from invalid user input.
- **Customizable Length:** Generates secure strings of any user-defined length (recommended 16+).

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `secrets`, `string` (Standard Library - no external dependencies required)

## 📂 Installation & Usage
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Shivam-044/Password-Generator.git](https://github.com/Shivam-044/Password-Generator.git)
