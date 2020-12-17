import os
import re
import time

print('正在检测您的虚拟桌面使用环境(view.xxx.com.cn)...')

res = os.popen('nslookup baidu.com').read()
res_dns = re.findall(r'Address:  (.*?)\n.*?Address:  (.*?)\n', res, re.S)

if res_dns != []:
    print('您使用的DNS服务器是：', res_dns[0][0])
    print('您使用的虚拟桌面公网地址是：', res_dns[0][1], '\n')
else:
    print('DNS解析错误！')

res_ct = os.popen('ping 1.1.1.1').read()
res_cnc = os.popen('ping 2.2.2.2').read()
res_cmcc = os.popen('ping 3.3.3.3').read()

res_ct2 = re.findall(r'.*?丢失 = (.*?) .*?平均 = (.*?)ms', res_ct, re.S)
res_cnc2 = re.findall(r'.*?丢失 = (.*?) .*?平均 = (.*?)ms', res_cnc, re.S)
res_cmcc2 = re.findall(r'.*?丢失 = (.*?) .*?平均 = (.*?)ms', res_cmcc, re.S)

if res_ct2 != [] and res_cnc2 != [] and res_cmcc2 != []:
    print('访问虚拟桌面电信地址丢包量和网络延时分别为：', res_ct2[0])
    print('访问虚拟桌面联通地址丢包量和网络延时分别为：', res_cnc2[0])
    print('访问虚拟桌面移动地址丢包量和网络延时分别为：', res_cmcc2[0], '\n')

    miss_ct, miss_cnc, miss_cmcc = int(res_ct2[0][0]), int(res_cnc2[0][0]), int(res_cmcc2[0][0])
    delay_ct, delay_cnc, delay_cmcc = int(res_ct2[0][1]), int(res_cnc2[0][1]), int(res_cmcc2[0][1])

    if miss_ct == 0 and delay_ct <= delay_cnc and delay_ct <= delay_cmcc:
        print('建议通过电信地址访问虚拟桌面(1.1.1.1)')
        try:
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', encoding='utf-8', errors='ignore') as f:
                res_writehosts = f.write('\n1.1.1.1 view.xxx.com.cn\n')
                print('已绑定电信地址1.1.1.1,写入hosts文件!')
        except:
            print('写入hosts文件失败！(电信)')
    elif miss_cnc == 0 and delay_cnc <= delay_ct and delay_cnc <= delay_cmcc:
        print('建议通过联通地址访问虚拟桌面(2.2.2.2)')
        try:
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', encoding='utf-8', errors='ignore') as f:
                res_writehosts = f.write('\n2.2.2.2 view.xxx.com.cn\n')
                print('已绑定联通地址2.2.2.2,写入hosts文件!')
        except:
            print('写入hosts文件失败！(联通)')
    elif miss_cmcc == 0 and delay_cmcc <= delay_ct and delay_cmcc <= delay_cnc:
        print('建议通过移动地址访问虚拟桌面(3.3.3.3)')
        try:
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', encoding='utf-8', errors='ignore') as f:
                res_writehosts = f.write('\n3.3.3.3 view.xxx.com.cn\n')
                print('已绑定移动地址3.3.3.3,写入hosts文件!')
        except:
            print('写入hosts文件失败！(移动)')

    if miss_ct != 0 and miss_cnc != 0 and miss_cmcc != 0:
        print('网络质量差，请联系管理员！(错误代码-1)')
else:
    print('网络质量差，请联系管理员！(错误代码-2)')

print('检测完成,窗口稍后自动关闭...')
time.sleep(60)
