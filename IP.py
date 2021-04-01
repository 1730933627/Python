#IP地址
import socket,uuid,os

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
print("IP:"+ip)
print("计算机名："+hostname)
print("Mac地址："+get_mac_address())

os.system('pause')
