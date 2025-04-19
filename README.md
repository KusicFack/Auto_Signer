# 项目介绍
现今不少网站要求通过签到保证账号活跃或者获取其虚拟货币，网站一多了每天也懒得去点😵‍💫。桌面端倒是有较成熟的自动化方案（诸如定时模拟点击浏览器之类的），但要求电脑不关机或者每天打开电脑，对于作者来说这样还是太吃操作了☹️

手机是现在大家**每天使用**且**随身携带**的电子设备，那有没有在手机上实现**随时一键签到所有网站**的方法呢？🤔

有的兄弟，有的🤓

**Termux + Selenium + Firefox** 或许正是上述问题的一个好的解决方案！全小白向的说明 + 配置流程见下。

注：项目目前还没有实现可以自己添加签到脚本的模块化功能，现在算是 Demo 阶段。下面是以[吾爱破解](https://www.52pojie.cn/)、[Hifini音乐磁场](https://www.hifini.com/)、[Rousi](https://rousi.zip/index.php)、[远景论坛](https://bbs.pcbeta.com/)四个网站为例。

# 工具简介
## Termux
官方简介：“Termux 是一个适用于 Android 的终端模拟器，其环境类似于 Linux 环境。 无需 Root 或设置即可使用。Termux 会自动进行最小安装 - 使用 APT 包管理器即可获得其他软件包。”关于 Termux 的进一步详细介绍[点这](https://termux.dev/cn/index.html)。

简单理解就是 Termux 在你的手机上搭建了一个 Linux 样的终端（可以把终端理解为一个软件的界面），然后你就可以**像操作 Linux 设备**一样操作你的安卓手机（即使用 Termux 时应该是这样的：你发送的 Linux 命令 → 安卓系统 → 完成你要求的操作）。
不过 Termux 也不是什么命令都能执行，一些涉及修改系统核心的操作是会被安卓系统阻止的（当然可以通过 Root 解决，这里就不介绍了）。

Termux 在项目中的用途就是提供 Python 环境（Selenium 需要）和 Linux 版的 Firefox 浏览器。

## Selenium
百度百科：Selenium 是一个用于 Web 应用程序测试的工具。它直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括 IE，Firefox，Safari，Chrome，Opera，Edge 等。关于 Selenium 的进一步详细介绍[点这](https://www.selenium.dev/zh-cn/documentation/overview/)

简单理解就是 Selenium 借助编程语言（这里使用 Python）在浏览器（这里使用 Firefox）上模拟你平时使用浏览器的操作（其实还能模拟一些更高级的、平时使用不会接触到的操作）。

## Firefox
换个名字：火狐浏览器。

# 文件准备
第一次安装时需要准备一些文件，并打包为名为 Auto_Signer.zip 的 zip 压缩包。项目 Release 界面已经准备了模板，可以把它解压后再进行文件添加，然后再压缩。

以吾爱破解为例，下面的操作都在电脑上进行：
1. 首先打开你的浏览器（建议使用 Edge），进入吾爱破解官网进行登录（请记住勾选“自动登录”）
2. 登录完成后，在 Edge 中下载安装 Cookie-Editor 扩展，并在已登录的网页页面打开该扩展，如下图
   ![image](https://github.com/user-attachments/assets/506ea9ca-ccdc-4cbb-b046-2f53bcd11fff)
3. 选择下方工具栏最右侧的导出（Export），选择 JSON，此时内容会复制到你的剪贴板上
4. 打开模板 cookies 文件下对应的 json 文件（可以用记事本打开），然后粘贴这些内容
5. 使用有查找和替换功能的记事本进行下列替换："sameSite": null 替换为 "sameSite": "None" ；"sameSite": "lax" 替换为 "sameSite": "Lax"

对所有网站都进行上述操作，最后将包含所有文件的 Auto_Signer 文件夹压缩为 Auto_Signer.zip。

# 安装流程
## 1. 安装 Termux，更换仓库（Repository）为国内源
Github 上搜索 Termux 下载安装。安装完成后打开 Termux，在终端中输入 termux-change-repo，进入换源界面。

↑、↓ 方向键切换选择对象；←、→ 切换 ok 和 cancel；键盘空格表示确定选择（* 号表示已确定的选择）；键盘换行表示点击 ok/cancel。

先选择 Mirror gourp，按回车进入。再切换到 Mirrors in China，按空格确定选择，然后回车。

此时 Termux 会自动检测可用国内源并检查软件包更新。

## 2. 安装 Python、Firefox 和 Geckodriver
在 Termux 中继续输入 apt install python firefox geckodriver，此时系统会提示是否继续，键盘输入 Y 然后回车即可。

补充：geckodriver 是 Firefox 的调试工具，被 selenium 调用。我们需要通过它来实现自动化。

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
非常感谢 Termux 项目团队 [termux/termux-app](https://github.com/termux/termux-app) 做出的贡献！想想几年前 Termux 不支持浏览器和 geckodriver 时这样的方法还需要通过 proot-distro 容器安装 Linux 发行版再安装
浏览器，那要写教程可太折磨了，且折腾也太麻烦了😖目前原生 Termux 的发展逐渐让其支持了很多桌面 Linux 发行版才有的功能，期待未来安卓设备可以真正变成“掌上 Linux 电脑”的一天！

本项目与其说是完整脚本程序开发，不如说是给相同想法的人提供一种思路和参考。若感兴趣可以随时 Fork 本项目仓库进行您的自定义修改。如您在使用本项目 Demo 时遇到问题欢迎在 issue 中反馈。祝您有个美好的一天！😉
