# encoding=utf-8
"""
@author huxujun
@date 2019-05-24
"""
import os


def get_build_dir() -> str:
    build_dir = os.path.join(os.getenv('JENKINS_HOME'), 'jobs', os.getenv('JOB_NAME').replace('/', '/branches/'),
                             'builds',
                             os.getenv('BUILD_NUMBER'))
    if not os.path.isdir(build_dir):
        raise Exception('The build_dir is not dir, build_dir=%s' % build_dir)
    return build_dir


def get_workplace() -> str:
    workplace = os.getenv('WORKSPACE')
    if not os.path.isdir(workplace):
        raise Exception('The workplace is not dir, workplace=%s' % workplace)
    return os.getenv('WORKSPACE')


if __name__ == '__main__':
    pass
