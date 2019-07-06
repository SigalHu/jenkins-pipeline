# encoding=utf-8
"""
@author huxujun
@date 2019-07-06
"""
import logging
import os
import sys

import requests

from common import assert_utils, io_utils

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s")
    jenkins_home = os.getenv("JENKINS_HOME")
    job_name = os.getenv("JOB_NAME")
    assert_utils.all_not_empty(jenkins_home=jenkins_home, job_name=job_name)
    config_file = os.path.join(jenkins_home, "jobs", job_name, "config.xml")
    config_content = io_utils.load_file(config_file)
    print("message3=" + os.getenv("message3"))
    config_content.replace("test123", os.getenv("message3"))
    print("content=" + config_content)
    io_utils.save_file(config_file, config_content)
    requests.post("http://{}:{}@localhost:8080/job/{}/config.xml".format(sys.argv[1], sys.argv[2], job_name),
                  data="@" + config_file, headers={"Content-Type": "text/xml"})
