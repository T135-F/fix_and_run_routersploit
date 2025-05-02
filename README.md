# ⚙️ RouterSploit Fix Installer 🛠️

📡 A fully automated script to **install**, **patch**, and **run [RouterSploit](https://github.com/threat9/routersploit)** with modern **Python 3.11+** support on Kali Linux and Debian-based systems.

🔗 Repo: [T135-F/fix_and_run_routersploit](https://github.com/T135-F/fix_and_run_routersploit)

---

## 🚀 Features

✅ Installs Python 3.11 from source (if not available)  
✅ Creates isolated virtualenv for clean execution  
✅ Automatically installs missing modules like `cryptography`, `requests`, `paramiko`  
✅ Fixes traceback bug (`traceback.format_exc(sys.exc_info())`)  
✅ Launches RouterSploit ready to use

---

## 📦 Requirements

- Kali Linux / Debian-based OS
- `git`, `wget`, `build-essential` (installed automatically)
- Internet connection

---

## 🛠️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/T135-F/fix_and_run_routersploit.git
cd fix_and_run_routersploit

# Make it executable
chmod +x fix_and_run_routersploit.sh

# Run the script
./fix_and_run_routersploit.sh
