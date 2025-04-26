# 项目介绍
**Termux + Selenium + Chromium**：在 Android 手机上实现**随时一键签到所有网站**！

注：项目目前还没有实现可以自己添加签到脚本的模块化功能。下面是以[Hifini音乐磁场](https://www.hifini.com/)、[Rousi](https://rousi.zip/index.php)、[远景论坛](https://bbs.pcbeta.com/)三个网站为例。

# 文件准备
需要准备的文件是签到自动登录用的 cookies，并放入模板打包为名为 Auto_Signer.zip 的 zip 压缩包。项目 Release 界面已经准备了模板，可以把它解压后再进行文件添加，然后再压缩。

获取自动登录 cookies 流程如下：
1. 首先打开你的浏览器（建议使用 Edge），进入网站进行登录（若有“自动登录”选项记得勾选）
2. 登录完成后，在 Edge 中下载安装 Cookie-Editor 扩展，并在已登录的网页页面打开该扩展
3. 选择该扩展下方工具栏最右侧的导出（Export），选择 JSON，此时内容会复制到剪贴板上
4. 打开模板 cookies 文件下对应的 json 文件（可以用记事本打开），然后粘贴这些内容
5. 使用有查找和替换功能的记事本进行下列替换："sameSite": null 替换为 "sameSite": "None" ；"sameSite": "lax" 替换为 "sameSite": "Lax"

对所有网站都进行上述操作，最后将包含所有文件的 Auto_Signer 文件夹压缩为 Auto_Signer.zip。

# 安装流程
## 1. 安装 Termux，更换仓库（Repository）为国内源
Github 上搜索 Termux 下载安装。安装完成后打开 Termux，在终端中输入 termux-change-repo，进入换源界面。

↑、↓ 方向键切换选择对象；←、→ 切换 ok 和 cancel；键盘空格表示确定选择（* 号表示已确定的选择）；键盘换行表示点击 ok/cancel。

先选择 Mirror gourp，按回车进入。再切换到 Mirrors in China，按空格确定选择，然后回车。

此时 Termux 会自动检测可用国内源并检查软件包更新。

## 2. 安装 Python 和 chromium
在 Termux 中继续输入 apt install python chromium，此时系统会提示是否继续，键盘输入 Y 然后回车即可。

chromium 软件包中包含了 chromium 浏览器和 chromedriver 浏览器驱动程序。

## 3. 复制脚本文件到 Termux 下
由于 Termux 通常不会在手机上的“文件管理”之类的应用显示自己的目录，因此需要借助 Linux 命令将文件拷贝到其目录中。为了方便，请先按“文件准备”小节准备好所需压缩包，放在手机的 Download 目录中。
先键入命令 termux-setup-storage，然后同意 Termux 访问手机文件。

接下来依次键入下面的命令：

cp ./storage/downloads/Auto_signer.zip ./

unzip Auto_signer.zip

rm Auto_signer.zip（可选，删除解压后的压缩包）

到此，安装基本结束。只要打开终端运行 ./Auto_signer/自动签到.sh 命令，程序就会进行自动签到了！（第一次运行完成以后就可以使用 ↑ 方向键访问历史命令了，选到该条历史后可以直接按回车执行）

## 4. 创建桌面快捷方式（可选）
若想实现在桌面上就能点击签到，需要额外安装 Termux:Widget 应用（Termux 的辅助程序，用于在桌面上创建小组件），可以在 Github 上搜索下载。安装完成后重新打开 Termux 终端，然后执行以下命令：

mkdir ./shortcuts（若提示 File exits，则表明已存在，忽略即可）

cp ./Auto_signer/自动签到.sh ./.shortcuts

然后在桌面上添加 Termux:Widget 2x2 小组件，即可看见脚本已经添加，以后每次只需点击一下签到就行！

# 后记
非常感谢 Termux 项目团队 [termux/termux-app](https://github.com/termux/termux-app) 为 Android 终端模拟器开发做出的贡献！如今 Termux 已经成为 Android 上最强大的终端模拟器，支持 Python、Node.js 等多种编程语言，拥有丰富的软件包仓库，甚至已经能执行许多 Linux 桌面端的程序（包括项目使用的 chromium 浏览器）。

本项目主要提供一种移动设备网页签到思路和参考。若感兴趣可以随时 Fork 本项目仓库进行您的自定义修改。如在使用本项目 Demo 时遇到问题欢迎在 issue 中反馈。
