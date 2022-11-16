import os

print('PyAUTORUN Ver 0.9 安装程序 By 爱电脑的昕宇\n' + '-'*10 + '\n注意：如果出现‘程序找不到指定的文件’等报错或闪退，则说明安装失败，请联系作者。\n' + '-' * 10)

if not os.path.isfile('C:\\Program Files\\Xysoft\\main.exe'):
    try:
        os.makedirs('C:\\Program Files\\Xysoft\\')
    except PermissionError:
        print('俗话说“巧妇难为无米之炊”，请以管理员身份运行！')
        os.system('pause')
        os._exit(0)
    except FileExistsError:
        pass
    os.system('copy "resource\\main.exe" "C:\\Program Files\\Xysoft\\"')
    os.system('reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v PyAUTORUN '
              '/d "C:\\Program Files\\Xysoft\\main.exe"')
    os.startfile("C:\\Program Files\\Xysoft\\main.exe")
    os.system('pause')
else:
    print('程序已经正确安装到您的计算机，无需再次执行此操作。')
    os.system('pause')
