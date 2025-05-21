#!/bin/bash

set -e

echo "[*] Memastikan dependensi sistem..."
sudo apt update
sudo apt install -y software-properties-common wget git build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

echo "[*] Menginstal Python 3.11 dari source..."

# Unduh dan compile Python 3.11 jika belum ada
if ! command -v python3.11 &> /dev/null; then
    cd /tmp
    echo "[*] Mengunduh Python 3.11..."
    wget https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz || { echo "[!] Gagal mengunduh Python 3.11"; exit 1; }
    tar -xf Python-3.11.8.tgz
    cd Python-3.11.8
    echo "[*] Menyusun Python 3.11..."
    ./configure --enable-optimizations
    make -j$(nproc) || { echo "[!] Gagal menyusun Python 3.11"; exit 1; }
    sudo make altinstall || { echo "[!] Gagal menginstal Python 3.11"; exit 1; }
else
    echo "[+] Python 3.11 sudah terinstal."
fi

echo "[*] Memastikan pip 3.11 dan venv tersedia..."
python3.11 -m ensurepip --upgrade
python3.11 -m pip install --upgrade pip setuptools
python3.11 -m pip install virtualenv

echo "[*] Membuat virtual environment Routersploit..."
cd ~
if [ ! -d "routersploit" ]; then
    echo "[*] Mengkloning repositori Routersploit..."
    git clone https://github.com/threat9/routersploit.git || { echo "[!] Gagal mengkloning repositori"; exit 1; }
fi
cd routersploit

# Membuat virtual environment dan mengaktifkannya
python3.11 -m virtualenv venv
source venv/bin/activate

echo "[*] Menginstal dependensi pip..."
pip install -r requirements.txt || pip install requests cryptography paramiko scapy future

echo "[*] Memperbaiki bug traceback di interpreter.py..."
INTERPRETER_FILE="routersploit/interpreter.py"
PATCH_LINE="print_error(traceback.format_exc(sys.exc_info()))"
FIXED_LINE="print_error(traceback.format_exc())"
if grep -q "$PATCH_LINE" "$INTERPRETER_FILE"; then
    sed -i "s|$PATCH_LINE|$FIXED_LINE|" "$INTERPRETER_FILE"
    echo "[+] Bug traceback diperbaiki."
else
    echo "[+] Tidak perlu patch, sudah benar atau patch sudah diterapkan."
fi

echo "[*] Menjalankan Routersploit..."
python3.11 rsf.py || { echo "[!] Gagal menjalankan Routersploit"; exit 1; }
