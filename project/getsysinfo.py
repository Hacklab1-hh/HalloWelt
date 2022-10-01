
import os
import socket
import psutil
import netifaces

name = "User01"

def print_sysobyinfo():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def print_sysinfo():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def print_test():
    print(os.environ)
    print(os.environ['COMPUTERNAME'])
    #print(win32netcon.USER_LAST_LOGOFF_INFOLEVEL)
    print("Für alle OS")
    print(socket.gethostbyname(socket.gethostname()))
    print(socket.if_nameindex())
    if os.environ:
        print("Für Windows Powershell")
        addrs = psutil.net_if_addrs()
        print(addrs.keys())
        print(addrs.values().__len__())
    else:
        print("Für Linux")
        #print(os.listdir('/sys/class/net/'))
        #print(if_list = netifaces.interfaces())
        print(netifaces.get_interfaces())

if __name__ == '__main__':
    print_sysinfo()
    print_test()
