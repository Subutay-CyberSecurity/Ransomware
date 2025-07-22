# 🛡️ Ransomware Simulation Tool – For Educational Use Only

> **⚠️ WARNING:**  
> This project is a **ransomware simulation tool** built for **educational, ethical hacking, and red team training purposes only**.  
> It must **never** be used against any system without **explicit permission**.  
> Misuse can result in **legal consequences**.  
> The author takes **no responsibility** for any damage caused by improper usage.

---

## 📘 Description

This tool simulates the behavior of a ransomware attack by encrypting files in a given directory and optionally displaying a ransom note.  
It is intended for:

- Cybersecurity students and educators  
- Malware researchers  
- Red team simulation labs

It does **not** connect to any command & control servers, nor does it perform any real malicious network activity.

---

## ⚙️ Features

- File encryption using AES (or specify your method)  
- Configurable target directories  
- Simulated ransom note generation  
- Logging system to track file operations  
- **No real payloads or data exfiltration**

---

## 🚀 Getting Started

> ⚠️ Do NOT run this tool on any production or personal system.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ransomware-sim
cd ransomware-sim

# Install dependencies
pip install -r requirements.txt

# Run the simulation
python simulate.py --target test_folder/
