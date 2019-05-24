# encoding=utf-8
"""
@author huxujun
@date 2019-05-24
"""
import os

import paramiko

if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('127.0.0.1', username=os.getenv('ACCESS_KEY_USR'), key_filename=os.getenv('ACCESS_KEY'))
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    attr = sftp.put("py_pipeline/step2.py", "py_pipeline_step2.py")
    sftp.close()
    ssh.close()