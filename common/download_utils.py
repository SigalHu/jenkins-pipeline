# encoding=utf-8
"""
@author huxujun
@date 2019-06-03
"""
import os
import sys
from urllib import request


def __schedule(block_num, block_size, total_size):
    recv_size = block_num * block_size
    percent = recv_size / total_size
    if percent > 1:
        percent = 1

    if int(recv_size / 1024 / 1024) == int((recv_size - block_size) / 1024 / 1024) and percent < 1:
        return

    percent_str = "%.2f%%" % (percent * 100)
    n = round(percent * 50)
    s = ('#' * n).ljust(50, ' ')
    f = sys.stdout
    f.write(percent_str.ljust(8, ' ') + '[' + s + ']')
    f.flush()
    f.write('\r')


def download_file(url: str, download_dir=".", progress_bar=True) -> str:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    if not os.path.isdir(download_dir):
        raise Exception("The download_dir must be dir, download_dir=%s" % download_dir)

    download_path = os.path.join(download_dir, os.path.basename(url))
    return request.urlretrieve(url, download_path, __schedule)[0] if progress_bar \
        else request.urlretrieve(url, os.path.basename(url))[0]


if __name__ == '__main__':
    pass
