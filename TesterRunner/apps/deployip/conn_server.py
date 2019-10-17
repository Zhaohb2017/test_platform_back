import paramiko
import os

def ssh_connect(ip,port,user,pswd,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip,port=int(port),username=user,password=pswd,timeout=5)
        stdin, stdout, stderr = ssh.exec_command(command)
    except Exception as e:
        return e
    return True

def data_dict(a):
    '''数据换行'''
    data = "{"
    for k, v in a.items():
        data += '"%s"' % k + ':['
        for i in range(len(v)):
            data += '"%s"' % v[i]
            if i != len(v) - 1:
                data += ","
        data += "],\n"
    data += "}"
    return  data

