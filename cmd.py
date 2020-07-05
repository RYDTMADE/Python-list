
import os


cmd = 'ipconfig'
os.system(cmd)
print(os.popen('dir').read())

# import socket
#
# print("����ǰ��������Ϊ" + socket.gethostname())
#
# print("����ǰ��IP��ַΪ" + socket.gethostbyname(socket.gethostname()))