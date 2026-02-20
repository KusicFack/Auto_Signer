# 项目介绍
**Termux + Selenium + Chromium**：在 Android 手机上实现**随时一键签到所有网站**！📱

注：项目可以自己添加签到脚本。目前提供[吾爱破解](https://www.52pojie.cn/)、[Rousi](https://rousi.pro/)、[AGSVPT]（https://www.agsvpt.com/）、[Hifini](https://www.hifiti.com/)、[远景论坛](https://bbs.pcbeta.com/)、[科研通](https://www.ablesci.com/)六个网站签到的 Demo。

# 文件准备
需要签到自动登录用的 cookies 或 tokens，并放入打包为 Auto_Signer.zip 中的 cookies 目录下。项目 Release 界面已经准备了该压缩包，可以把它解压后再进行文件添加，然后再压缩。

获取自动登录 cookies 流程如下：
1. 首先打开你的浏览器（请使用 Edge 或 Chrome），进入网站进行登录（若有“自动登录”选项记得勾选）
2. 登录完成后，在 Edge/Chrome 中下载安装 Cookie-Editor 扩展，并在已登录的网页页面打开该扩展
3. 选择该扩展下方工具栏最右侧的导出（Export），选择 JSON，此时内容会复制到剪贴板上
4. 打开模板 cookies 文件下对应的 json 文件（可以用记事本打开），然后粘贴这些内容
5. 使用有查找和替换功能的记事本进行下列替换："sameSite": null 替换为 "sameSite": "None" ；"sameSite": "lax" 替换为 "sameSite": "Lax"，保存文件

获取自动登录 tokens 流程如下：
1. 首先打开你的浏览器（请使用 Edge 或 Chrome），进入网站进行登录（若有“自动登录”选项记得勾选）
2. 登录完成后，在当前页面打开“开发者工具”，切换到“控制台”选项卡，输入“JSON.stringify(localStorage)”，控制台会返回 json 化 token 文本
3. 打开模板 cookies 文件下对应的 json 文件（可以用记事本打开），然后粘贴这些内容（注意去掉 json 字符串开头和末尾的单引号），保存文件

注：有些网站可能没有永久自动登录的功能，如遇过期还请自行重新生成 cookie.json 或 token.json。

对所有网站都进行上述操作，最后将包含所有文件的 Auto_Signer 文件夹压缩为 Auto_Signer.zip。

# 安装流程
## 1. 安装 Termux，更换仓库（Repository）为国内源
Github 上搜索 Termux 下载安装。安装完成后打开 Termux，在终端中输入 termux-change-repo，进入换源界面。

↑、↓ 方向键切换选择对象；←、→ 切换 ok 和 cancel；键盘空格表示确定选择（* 号表示已确定的选择）；键盘换行表示点击 ok/cancel。

先选择 Mirror gourp，按回车进入。再切换到 Mirrors in China，按空格确定选择，然后回车。

此时 Termux 会自动检测可用国内源并检查软件包更新。

## 2. 安装 Python 和 Chromium
在 Termux 中继续输入 apt install python chromium python-pip tigervnc，此时系统会提示是否继续，键盘输入 Y 然后回车即可。

chromium 软件包中包含了 chromium 浏览器和 chromedriver 浏览器驱动程序。

接下来安装 selenium 和 pyvirtualdisplay 包，输入 pip install selenium pyvirtualdisplay，等待 pip 程序完成包安装。 

## 3. 复制脚本文件到 Termux 下
由于 Termux 通常不会在手机上的“文件管理”之类的应用显示自己的目录，因此需要借助 Linux 命令将文件拷贝到其目录中。为了方便，请先按“文件准备”小节准备好所需压缩包，放在手机的 Download 目录中。
先键入命令 termux-setup-storage，然后同意 Termux 访问手机文件。

接下来依次键入下面的命令：

cp ./storage/downloads/Auto_signer.zip ./

unzip Auto_signer.zip

rm Auto_signer.zip（可选，删除解压后的压缩包）

到此，安装基本结束。只要打开终端运行 ./Auto_signer/自动签到.sh 命令，程序就会进行自动签到了！（第一次运行完成以后就可以使用 ↑ 方向键访问历史命令了，选到该条历史后可以直接按回车执行）

## 4. 添加 Chromium 参数至 .bashrc 文件（可选，强烈推荐）
虽然本项目签到方式不同于常规脚本签到，通过控制浏览器操作来模拟人工签到以防止被网站识别阻拦，但仍有可能在签到过程中会被某些网站莫名阻止（例如**吾爱破解**，该网站以反爬规则之严格而著名，即使是使用 VNC 人工操作手机签到都会被阻拦😅）。因此，我们需要在 .bashrc 文件中添加一些 Chromium 的参数来规避某些检测。

首先在 Termux 的家目录（~）下创建一个名为 .bashrc 的文本文件，然后输入以下内容：
export CHROMIUM_USER_FLAGS="--disable-webgl --disable-gpu --disable-blink-features=AutomationControlled"

重启 Termux 后该参数会全局有效。如果只想将参数用于签到也可考虑将其添加到 main.py 文件中。

## 5. 创建桌面快捷方式（可选）
若想实现在桌面上就能点击签到，需要额外安装 Termux:Widget 应用（Termux 的辅助程序，用于在桌面上创建小组件），可以在 Github 上搜索下载。安装完成后重新打开 Termux 终端，然后执行以下命令：

mkdir ./shortcuts（若提示 File exits，则表明已存在，忽略即可）

cp ./Auto_signer/自动签到.sh ./.shortcuts

然后在桌面上添加 Termux:Widget 2x2 小组件，即可看见脚本已经添加，以后每次只需点击一下签到就行！

# 后记
非常感谢 Termux 项目团队 [termux/termux-app](https://github.com/termux/termux-app) 为 Android 终端模拟器开发做出的贡献！如今 Termux 已经成为 Android 上最强大的终端模拟器，支持 Python、Node.js 等多种编程语言，拥有丰富的软件包仓库，甚至已经能执行许多 Linux 桌面端的程序（包括项目使用的 Chromium 浏览器）。

本项目主要提供一种移动设备网页签到思路和参考。若感兴趣可以随时 Fork 本项目仓库进行您的自定义修改。如在使用本项目 Demo 时遇到问题欢迎在 issue 中反馈。
