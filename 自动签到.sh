#!/data/data/com.termux/files/usr/bin/sh

source /data/data/com.termux/files/usr/etc/profile

# 定义目标目录路径
TARGET_DIR="$HOME/Auto_Signer"

# 启动 main.py
python main.py
python email_alert.py