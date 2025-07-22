# Ransomware Simulation Tool

## Description
This project is a simple ransomware simulation tool that encrypts and decrypts files using the AES encryption algorithm.  
It targets specific file extensions, encrypts files by appending the `.enc` extension, and securely deletes the original files.  
Decryption restores the original files and removes the encrypted versions.

**WARNING:**  
This tool is intended for educational and testing purposes only.  
Using it in real environments or for malicious purposes is illegal and can have serious consequences.

---

## Features

- AES-256 encryption with CBC mode  
- Encrypts and decrypts files with specific extensions (office documents, media files, archives, etc.)  
- Secure file deletion by overwriting files with random data before removal  
- Simple command-line interface  
- Generate a new AES key or load an existing one (hex format)  
- Recursively process directories and their subdirectories  
- Excludes system folders and important files from encryption/decryption to avoid damage

---

## Supported File Extensions

- Office Documents: `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.ppt`, `.pdf`, `.txt`, `.rtf`, `.csv`, `.log`  
- Data Formats: `.xml`, `.json`, `.html`, `.htm`, `.pub`, `.vsd`, `.vsdx`  
- Databases & Backups: `.mdb`, `.accdb`, `.sql`, `.bak`, `.qbw`, `.qbb`  
- Adobe Files: `.psd`, `.ai`, `.indd`  
- Images: `.jpeg`, `.jpg`, `.png`, `.gif`, `.tiff`, `.tif`, `.bmp`  
- Audio & Video: `.mp3`, `.wav`, `.mp4`, `.avi`, `.mov`, `.wmv`  
- Archives: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.tgz`, `.bz2`, `.xz`  
- Disk Images & Virtual Machines: `.iso`, `.vmdk`, `.vhd`, `.vhdx`  
- Outlook Files: `.ost`, `.pst`  

---

## Excluded Directories and Files

The program automatically skips these directories and files to avoid encrypting system or critical files:

**Directories:**  
`venv`, `__pycache__`, `.git`, `node_modules`, `$recycle.bin`, `system volume information`, `program files`, `windows`, `boot`, `recovery`, `drivers`, `etc`, `dev`, `proc`, `sys`, `run`, `tmp`, `var`, `mnt`, `media`, `usr`, `lib`, `bin`, `sbin`, `opt`, `srv`, `root`, `lost+found`, `downloads`

**Files:**  
`ransomware.py`, `ransomware.py.enc`, `desktop.ini`, `thumbs.db`

---

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python 3.6 or higher installed.
3. Install required dependencies using pip:

```bash
pip install -r requirements.txt
