# encoding=utf-8
"""
@author huxujun
@date 2019-05-31
"""
import os

import paramiko


def ssh_connect():
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("127.0.0.1", username=os.getenv("ACCESS_KEY_USR"), key_filename=os.getenv("ACCESS_KEY"))

        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp.put("LICENSE", "jenkins_pipeline_LICENSE")
        print("SFTP listdir start...")
        for dir_str in sftp.listdir():
            print(dir_str)
        print("SFTP listdir end.")

        stdin, stdout, stderr = ssh.exec_command("ls")
        print("SSH ls start..")
        for line in stdout.readlines():
            print(str(line).replace("\n", ""))
        print("SSH ls end.")


if __name__ == '__main__':
    ssh_connect()
