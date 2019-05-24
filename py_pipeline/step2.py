# encoding=utf-8
"""
@author huxujun
@date 2019-05-24
"""

from common import jenkins_helper

if __name__ == '__main__':
    print("The workspace is %s" % jenkins_helper.get_workspace())
    print("The build dir is %s" % jenkins_helper.get_build_dir())
