# 🛡️ Ransomware Simulation Tool

> **❗ WARNING – FOR EDUCATIONAL PURPOSES ONLY**  
> This repository contains a **ransomware simulation tool** designed solely for **educational use, cybersecurity training, and malware analysis research**.  
> Any **unauthorized or malicious use** of this code is **strictly prohibited** and may lead to **legal consequences**.  
> The author assumes **no responsibility** for any misuse or damages caused by this tool.

---

## 📌 About the Project

This tool simulates a typical ransomware attack by **encrypting files** in a specified directory

### 🔍 Purpose:

- Teach students how ransomware works
- Allow researchers to test and study malware behavior in a **safe, controlled environment**
- Support red team operations and cybersecurity labs

⚠️ **This tool does NOT contain real malicious payloads, backdoors, or network communication. It does not contact any external servers or perform unauthorized actions.**

---

## 📦 Features

- 🔐 **AES-256 encryption** of files in a target directory
- 📁 Configurable file targets (via CLI)
- 🗃️ Encrypted files renamed with `.locked` extension
- ❌ Deletion of original files
- 🔄 Decryption feature (optional)

---

## 🧰 Requirements

This tool is written in **Python 3.8+** and uses the following libraries:

- `cryptography`
- `argparse`
- `os`, `sys`, `shutil`
- `logging`
- `colorama` (for styled terminal output – optional)

Install dependencies with:

```bash
pip install -r requirements.txt
