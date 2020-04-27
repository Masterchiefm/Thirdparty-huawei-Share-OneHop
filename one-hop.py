#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import popen
from os import system
from qrcode import make
from time import sleep


# In[2]:


def get_sn():
    sn = ''
    a = popen('wmic bios get serialnumber').read()
    for line in a.splitlines():
        if line:
            if 'SerialNumbe' in line:
                pass
            else:
                print('\tSerialNumbe is ',line)
                sn = line.strip()
    if sn == '':
        print('\t***************** \033[1;32;43m test \033[0m!错误！找不到SN....我也不知道怎么解决\033[0m!*****************')
    return sn


# In[3]:



def get_mac():
    mac = ''
    a = popen('ipconfig /all').read().splitlines()
    n = 0
    for i in a:
        n = n + 1
        if 'Bluetooth' in i:
            print('\t',a[n-1])
            print('\t',a[n])
            mac = a[n]
    start = mac.find(':') + 1
    if mac == '':
        print('\t*****************\033[1;32;43m test \033[0m!错误！程序太垃圾，请自己在powershell输入ipconfig /all ，然后自己找\033[0m!*****************')
    else:
        mac = mac[start:].strip().replace('-','')
    return mac


# In[4]:


def get_qr(code):
    img = make(code)
    img.save('test.png')


# In[5]:


def make_qr():
    system('cls')
    print('####################################### 一碰传标签二维码生成器 ###############################################')
    print('随便做的，出错不负责。可以问我，不一定修复\n')
    print('cooapk: 花不语笑人痴')
    sn = get_sn()
    mac = get_mac()
    code = "SN=" + sn + "|MAC=" + mac +"|MODELID=00000506"
    get_qr(code)
    dir = popen('echo %cd%').read().replace('\n', '').replace('\r', '') + "\\test.png"
    print('一碰传助手来自https://github.com/webviewisbad/-apk ，请大家有空帮大佬点小星星')
    print('访问  https://hind.moqiqin.workers.dev/share/PC_Manager/标签制作/  获取一碰传助手.apk。（复制url请务必把结尾的 “/”一起复制，否则无法访问）')
    print('运行结束，获得的代码为:\n',code,'\n二维码保存路径： ',dir)
    system('test.png')
    print('####################################### 一碰传标签二维码生成器 ###############################################\n')


# In[6]:


def disable_apps():
    system('cls')
    #检测是否有adb程序：
    check = 0
    while check < 2:
        check = 0
        adb = system('adb.exe devices')
        if adb == 0:
            check = check + 1
        else:
            print('找不到电脑adb.exe，请确保adb.exe以及相关dll文件在同一目录')
            input('按回车键重试')
            
        devices = popen('adb.exe devices').read().splitlines()
        if devices[1] == '':
            print('找不到ADB设备，请确认是否启动手机ADB调试')
            input('按回车键重试')
        else:
            print("已连接",devices[1])
            check = check + 1
            
    
    #
    
    clean = "adb shell pm clear "
    diss = "adb shell pm disable-user "
    app1 = "com.huawei.android.instantshare"
    app2 = "com.huawei.pcassistant"
    app3 = "com.huawei.iconnect"
    app4 = "com.android.nfc"
    app5 = "com.huawei.android.internal.app"
    
    #禁用程序
    print(popen(diss + app1).read())
    print(popen(diss + app2).read())
    print(popen(diss + app3).read())
    print(popen(diss + app4).read())
    print(popen(diss + app5).read())
    

    print('清理app存储')
    c1 = popen(clean + app1).read()
    c2 = popen(clean + app2).read()
    c3 = popen(clean + app3).read()
    c4 = popen(clean + app4).read()
    c5 = popen(clean + app5).read()
    
    print('wipe ',app1,' data ',c1)
    print('wipe ',app2,' data ',c2)
    print('wipe ',app3,' data ',c3)
    print('wipe ',app4,' data ',c4)
    print('wipe ',app5,' data ',c5)
    
    
    


# In[7]:


def enable_apps():
    #检测是否有adb程序：
    check = 0
    while check < 2:
        check = 0
        adb = system('adb.exe devices')
        if adb == 0:
            check = check + 1
        else:
            print('找不到电脑adb.exe，请确保adb.exe以及相关dll文件在同一目录')
            input('按回车键重试')
            
        devices = popen('adb.exe devices').read().splitlines()
        if devices[1] == '':
            print('找不到ADB设备，请确认是否启动手机ADB调试')
            input('按回车键重试')
        else:
            print("已连接",devices[1])
            check = check + 1
            
    en = 'adb shell pm enable '
    app1 = "com.huawei.android.instantshare"
    app2 = "com.huawei.pcassistant"
    app3 = "com.huawei.iconnect"

    app5 = "com.huawei.android.internal.app"
    print(popen(en + app1).read())
    print(popen(en + app2).read())
    print(popen(en + app3).read())

    print(popen(en + app5).read())
    


# In[8]:


def touchshare():
    if input('安装一碰传助手？ y/n ') == 'y':
        #检测是否有adb程序：
        check = 0
        while check < 2:
            check = 0
            adb = system('adb.exe devices')
            if adb == 0:
                check = check + 1
            else:
                print('找不到电脑adb.exe，请确保adb.exe以及相关dll文件在同一目录')
                input('按回车键重试')
                
            devices = popen('adb.exe devices').read().splitlines()
            if devices[1] == '':
                print('找不到ADB设备，请确认是否启动手机ADB调试')
                input('按回车键重试')
            else:
                print("已连接",devices[1])
                check = check + 1
        
        system('adb install touchshare.apk')
    else:
        pass
    
        
    system("adb.exe shell am start -n com.huawei.touchshare/.ui.MainActivity")


# In[9]:


def nfctool():
    if input('安装NFC Tool 以擦除标签？ y/n ') == 'y':
        #检测是否有adb程序：
        check = 0
        while check < 2:
            check = 0
            adb = system('adb.exe devices')
            if adb == 0:
                check = check + 1
            else:
                print('找不到电脑adb.exe，请确保adb.exe以及相关dll文件在同一目录')
                input('按回车键重试')
                
            devices = popen('adb.exe devices').read().splitlines()
            if devices[1] == '':
                print('找不到ADB设备，请确认是否启动手机ADB调试')
                input('按回车键重试')
            else:
                print("已连接",devices[1])
                check = check + 1
        
        system('adb install nfctool.apk')
    else:
        pass
    
    system("adb.exe shell am start -n com.wakdev.nfctools.pro/com.wakdev.nfctools.pro.MainActivityPro")
    
    print(popen('adb shell pm enable com.android.nfc').read())
    print('请手动开启NFC')
    print('请在NFC Tools应用中选择 “其它”-“删除标签”')


# In[16]:


def main_menu():
    system('cls')
    print('####################################### 一碰传标签二维码生成器 ###############################################')
    print('coolapk:花不语笑人痴')
    print('免费软件，不收费。\n 本程序源代码请访问 https://github.com/Masterchiefm/Thirdparty-huawei-Share-OneHop ')
    print('一碰传助手来自 https://github.com/webviewisbad/-apk')
    print('有条件的同学帮我GitHub点个小星星')
    
    print('\n\t 1.制作标签')
    print('\t 2.擦除标签以及清除手机标签记录')
    print('\t 3.清除手机标签记录（没调试。用不了就直接运行2也可以达到一样效果）')
    print('####################################### 一碰传标签二维码生成器 ###############################################')
    opt = int(input('\n\t输入选项: '))
    if opt == 1:
        touchshare()
        make_qr()
    elif opt == 3:
        disable_apps()
        system('adb shell pm enable com.android.nfc')
        enable_apps()
    elif opt == 2:
        print('\t风险告知: \n\t 1.你的手机将会被我重启 \n\t 2.本程序会冻结多个程序  \n\t 3.多次冻结会有一定几率导致程序BUG而需要手机恢复出厂(目前没遇到过)')
        input('回车继续...')
        disable_apps()
        print('不要慌，是我在帮你重启手机')
        system('adb reboot')
        input('重启完成就按回车...')
        disable_apps()
        
        nfctool()
        input('标签删除了吗？删除了就回车继续吧...')
        if input('要启动制作新标签的进程吗？ y/n ') == 'y':
            touchshare()
            make_qr()
        else:
            pass
        
        
        input('搞完了就回车...')
        enable_apps()
        system('adb reboot')
        input('重启完成就按回车...')
        
        system('adb shell pm enable com.android.nfc')
        enable_apps()
        print('自己打开NFC')
        


# In[ ]:





# In[17]:


s = 'a'
while s != 'y':
    system('cls')
    main_menu()
    
    print('如果你使用本程序成功了，而且体验良好，可以考虑给我打赏一杯矿泉水吗？\n打赏不意味着你可以向我购买什么或者获得什么特权，而且用来表达你成功后的喜悦心情')
    print('二维码 https://moqiqin.cn/wp-content/uploads/2020/04/dashang.png')
    s = input('退出？ y/n ')


# In[ ]:




