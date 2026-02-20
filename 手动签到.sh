#!/data/data/com.termux/files/usr/bin/sh

# 定义优雅退出函数
graceful_exit() {
    local message="$1"
    local exit_code=${2:-0}
    if [ -n "$message" ]; then
        echo -e "\n$message" >&2
    fi
    read -p "操作完成，按回车键退出..."
    exit $exit_code
}

# 定义目标目录路径
TARGET_DIR="$HOME/Auto_Signer"

# 检查目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    graceful_exit "错误：目标目录不存在 $TARGET_DIR" 1
fi

# 进入目标目录（带有错误检查）
cd "$TARGET_DIR" || graceful_exit "错误：无法进入目录 $TARGET_DIR" 1

# 检查main.py是否存在
if [ ! -f "main_terminal.py" ]; then
    graceful_exit "错误：未找到 main_terminal.py 文件" 1
fi

# 执行Python脚本并捕获退出状态
python main_terminal.py
EXIT_STATUS=$?

# 根据执行结果显示不同提示
if [ $EXIT_STATUS -eq 0 ]; then
    MESSAGE="✅ 程序执行成功"
else
    MESSAGE="⛔ 程序异常退出 (代码: $EXIT_STATUS)"
fi

# 优雅退出并传递状态码
graceful_exit "$MESSAGE" $EXIT_STATUS