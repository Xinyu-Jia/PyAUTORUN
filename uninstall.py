import os
import shutil

print(
    'PyAUTORUN Ver 0.9 卸载程序 By 爱电脑的昕宇\n' + '-' * 10 + '\n注意：如果出现‘程序找不到指定的文件’等报错或闪退，则说明安装失败，请联系作者。\n' + '-' * 10)

if os.path.isfile('C:\\Program Files\\Xysoft\\main.exe'):
    try:
        print('执手相看泪眼，竟无语凝噎。您真的要卸载吗？若是，请')
        os.system('pause')
        t = open('C:\\Program Files\\Xysoft\\test', 'w')
        t.close()
        os.system('taskkill -f -im main.exe')
        shutil.rmtree('C:\\Program Files\\Xysoft\\')
        os.system('reg delete HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v PyAUTORUN /f')
        print('卸载成功。')
        os.system('pause')
    except PermissionError:
        print('我当然可以苟且偷生\n我当然不想失去性命\n但是我还是要告诉你\n请以管理员身份运行(ToT)')
        os.system('pause')
        os._exit(0)

else:
    print('程序尚未安装或已经卸载。')
    os.system('pause')
