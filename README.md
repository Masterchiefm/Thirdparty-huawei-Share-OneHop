# Thirdparty-huawei-Share-OneHop
第三方华为一碰传标签制作工具

功能：
```
1.快速根据你电脑的SN以及蓝牙MAC生成标签制作二维码
2.安装并唤起你手机里制作一碰传标签的工具
3.协助华为手机用户擦除标签以及清理手机内部存储的标签记录
```
主界面：
![](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/raw/master/1.jpg)

**[点击这一行字查看运行截图](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/blob/master/README.md#%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE)**

因为制作华为一碰传标签很麻烦，所以搞这个脚本。无脑确认即可完成一碰传标签制作。
# 直接运行

下载地址: [Release](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/releases)

如果你要制作一碰传标签，请首先确认你的手机可以通过扫码连接电脑管家。如果扫码连接都做不到就别折腾了
在 [Release](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/releases)中下载zip压缩包，解压后双击运行“一碰传标签制作器.exe”即可
程序用pyinstaller打包，启动很慢。大约15秒左右可以显示界面，按照弹出提示操作即可。

## 注意事项

1. 手机未安装"一碰传助手"app的，请务必将手机打开USB调试并用数据线插上电脑，信任电脑
2. 手机已有“一碰传助手”的，直接选择不安装即可，无需连接电脑。
3. 擦除标签的朋友们**请务必开启手机ADB调试，并且一直保持手机与电脑连接，直到最后弹出“退出”选项**  
4.若重启后手机用不了一碰传甚至扫码连接电脑也用不了，重新运行 选项2，**并仔细阅读上一条**


# 从源码运行
自行安装最新adb驱动，或将adb.exe等相关文件放在源码同一目录下。
安装依赖
```
pip install image
pip install qrcode
```
启动
将one-hop.ipynb转换为python文件，或者直接用jupyter notebook打开。建议使用jupyter notebook
```
python one-hop.py
```

# 打赏
如果你觉得这个小程序帮到你了，而且你使用本程序成功了，有着良好的体验，可以考虑请我喝一瓶可乐。

打赏并不是你从我这里购买到什么或者获得什么特权，打赏只是你对我花费的时间的肯定以及你心情愉悦的一种表达方式。
![让我换个好点的贴纸吧](https://moqiqin.cn/wp-content/uploads/2020/04/dashang.png)

# 致谢
不限制SN长度的“一碰传助手”app由 [webviewisbad](https://github.com/webviewisbad/-apk) 修改提供


# 运行截图

主界面
![主界面](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/raw/master/1.jpg)
制作一碰传贴纸
![](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/raw/master/2.jpg)
![](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/raw/master/3.jpg)
辅助华为手机擦除一碰传贴纸
**注意，这里要一直保持手机与电脑的ADB连接**
![](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/raw/master/4.jpg)
