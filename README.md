# 🛡️ Ransomware Simulation Tool

> **❗ WARNING – FOR EDUCATIONAL PURPOSES ONLY**  
> This repository contains a **ransomware simulation tool** designed solely for **educational use, cybersecurity training, and malware analysis research**.  
> Any **unauthorized or malicious use** of this code is **strictly prohibited** and may lead to **legal consequences**.  
> The author assumes **no responsibility** for any misuse or damages caused by this tool.

---

## 📌 About the Project

This tool simulates a typical ransomware attack by **encrypting files** in a specified directory and generating a **ransom note**.

### 🔍 Purpose:

- Teach students how ransomware works
- Allow researchers to test and study malware behavior in a **safe, controlled environment**
- Support red team operations and cybersecurity labs

⚠️ **This tool does NOT contain real malicious payloads, backdoors, or network communication. It does not contact any external servers or perform unauthorized actions.**

---

## 📦 Features

- 🔐 **AES-256 encryption** of files in a target directory
- 📁 Configurable file targets (via CLI)
- 📝 Automatic ransom note creation
- 🗃️ Encrypted files renamed with `.locked` extension
- 📜 Logging of encrypted files
- ❌ Optional deletion of original files
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

    You can also install manually:

pip install cryptography colorama

💻 Installation
Option 1: Clone from GitHub

git clone https://github.com/YOUR_USERNAME/ransomware-simulator.git
cd ransomware-simulator

Option 2: Download ZIP

    Go to the GitHub repo

    Click Code → Download ZIP

    Extract the archive and open in your preferred Python environment

🚀 How to Use
🧪 Safe Setup

For ethical testing, always use this tool in an isolated environment, such as:

    Virtual Machines (VirtualBox, VMware)

    Docker containers

    Offline sandbox folders

Never run on your main PC or on sensitive data.
🔧 Example Usage

python simulate.py --target ./test_folder

Available Parameters:
Argument	Description
--target	Path to the folder containing files to simulate encryption
--keyfile	Optional path to save the encryption key
--delete-original	Delete original files after encryption (⚠️ Dangerous)
--ransom-note	Custom message for ransom note
--decrypt	Decrypt files in a folder using saved key
🔐 Sample Encryption

python simulate.py --target ./test_folder --keyfile ./key.bin

This command will:

    Encrypt all files inside test_folder

    Save the key as key.bin

    Create a ransom note in the folder

🔓 Sample Decryption

python simulate.py --target ./test_folder --keyfile ./key.bin --decrypt

📝 Sample Ransom Note

Your files have been encrypted by a ransomware simulation.
To decrypt your files, use the provided decryption script and key.
This is NOT a real attack. No data was transmitted or stolen.

✅ Best Practices & Warnings

    ✅ Only run in a sandbox environment

    ✅ Backup your data before testing

    ✅ Never use against unauthorized systems

    ❌ Do not upload real malware variants

    ❌ Do not hide or obfuscate malicious behavior

📚 Legal Notice

This project is provided under the terms of the MIT License, but:

        You may only use it for ethical, academic, or research purposes

        You may not use it to harm, extort, or damage any third party

        All usage must comply with local laws and regulations

By using this tool, you agree to be held responsible for your actions.
🧠 Future Improvements

Add GUI interface

Support for recursive encryption in nested directories

Better logging and incident reporting

    Ransomware behavior emulation with user prompts

👨‍💻 Author

Subutay Batuhan
Cybersecurity Researcher | Ethical Hacker
he/him

    GitHub: https://github.com/YOUR_USERNAME

    Email: your.email@example.com

📝 License

This project is licensed under the MIT License – see the LICENSE file for details.
