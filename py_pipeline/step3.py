# encoding=utf-8
"""
@author huxujun
@date 2019-05-24
"""
import os

import paramiko

if __name__ == '__main__':
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("127.0.0.1", username=os.getenv("ACCESS_KEY_USR"), key_filename=os.getenv("ACCESS_KEY"))

        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp.put("py_pipeline/step2.py", "py_pipeline_step2.py")
        print("SFTP listdir start...")
        for dir_str in sftp.listdir():
            print(dir_str)
        print("SFTP listdir end.")

        stdin, stdout, stderr = ssh.exec_command("ls")
        print("SSH ls start..")
        for line in stdout.readlines():
            print(str(line).replace("\n", ""))
        print("SSH ls end.")
