# encoding=utf-8
"""
@author huxujun
@date 2019-05-31
"""
from common import jenkins_helper


def print_dirs():
    print("The workspace is %s" % jenkins_helper.get_workspace())
    print("The build dir is %s" % jenkins_helper.get_build_dir())


if __name__ == '__main__':
    print_dirs()
