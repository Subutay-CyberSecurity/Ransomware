# 🔐 Ransomware Simulation Tool

> ⚠️ **WARNING:**  
> This tool is for **educational and ethical hacking purposes only**.  
> **Do NOT** use it on any system or data without **explicit permission**.  
> Misuse may result in **legal consequences**.  
> Author assumes **no responsibility** for damages caused by improper use.

---

## 📘 Description

This project is a simple ransomware **simulation** tool that uses **AES-256 encryption** to lock files and securely delete originals.  
Decryption restores encrypted files if the correct key is provided.

---

## ✨ Features

✅ AES-256 (CBC mode) encryption  
✅ Secure deletion by overwriting files with random data  
✅ Decrypt previously encrypted files  
✅ Targeted file extensions  
✅ Excludes critical system folders  
✅ Simple interactive CLI  
✅ Create or load custom AES key (hex format)  

---

## 📂 Supported File Types

📝 Documents: `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.pdf`, `.txt`, `.csv`, etc.  
🖼️ Media: `.jpg`, `.png`, `.mp3`, `.mp4`, `.avi`, etc.  
🗃️ Archives: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, etc.  
🧠 Backups & Databases: `.sql`, `.bak`, `.accdb`, `.pst`, `.ost`, `.vmdk`, etc.
(Top 300 Most Popular File Types)

---

## 🚫 Automatically Excluded

📁 **Directories:**  
`venv`, `.git`, `__pycache__`, `node_modules`, `windows`, `etc`, `sys`, etc.

📄 **Files:**  
`ransomware.py`, `desktop.ini`, `thumbs.db`, encrypted script itself

---

## ⚙️ Installation

1. 🧱 Make sure you have **Python 3.6+** installed.
2. 📦 Install dependencies:

```bash
pip3 install -r requirements.txt
