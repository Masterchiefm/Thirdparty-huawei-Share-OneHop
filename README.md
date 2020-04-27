# Thirdparty-huawei-Share-OneHop
制作第三方华为一碰传标签

因为制作华为一碰传标签很麻烦，所以搞这个脚本。无脑确认即可完成一碰传标签制作。
# 直接运行
如果你要制作一碰传标签，请首先确认你的手机可以通过扫码连接电脑管家。如果扫码连接都做不到就别折腾了

在 [Release](https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop/releases)中下载zip压缩包，解压后双击运行“一碰传标签制作器.exe”即可

程序用pyinstaller打包，启动很慢。大约15秒左右可以显示界面，按照弹出提示操作即可。

擦除标签的朋友们请务必先开启手机ADB调试，并且一直保持手机与电脑连接，直到最后弹出“退出”选项。


# 从源码运行
自行安装最新adb驱动，或将adb.exe等相关文件放在源码同一目录下。
安装依赖
```
pip install image
pip install qrcode
```
启动
```
python one-hop.py
```

# 打赏
如果你觉得这个小程序帮到你了，而且你使用本程序成功了，有着良好的体验，可以考虑请我喝一瓶可乐。

打赏并不是你从我这里购买到什么或者获得什么特权，打赏只是你对我花费的时间的肯定以及你心情预约的一种表达方式。
![让我换个好点的贴纸吧](https://moqiqin.cn/wp-content/uploads/2020/04/dashang.png)
