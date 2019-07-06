# encoding=utf-8
"""
@author huxujun
@date 2019-06-17
"""
import configparser
import html
import logging
import os
import shutil
import tempfile
from urllib import parse


def load_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        logging.exception("Error to read file %s", filename)


def save_file(filename, content=""):
    try:
        filedir = os.path.dirname(filename)
        if filedir and not os.path.exists(filedir):
            os.makedirs(filedir)
        with open(filename, "w") as f:
            f.write(content)
    except:
        logging.exception("Error to write file %s", filename)


def copy_file(src_file, dest_file):
    try:
        shutil.copyfile(src_file, dest_file)
        return True
    except:
        logging.exception("Error to copy src_file %s to dest_file %s", src_file, dest_file)
        return False


def unescape_file(filename):
    template_name = "{}.tmp".format(filename)
    try:
        with open(filename) as f, open(template_name, "w") as t:
            for line in f:
                line = html.unescape(line)
                line = parse.unquote(line)
                t.write(line)
        os.rename(template_name, filename)
    except:
        logging.exception("Error to unescape file %s", filename)
        os.remove(template_name)


def load_properties_file(filename):
    cf = configparser.ConfigParser()
    with open(filename) as d, tempfile.NamedTemporaryFile("w+") as t:
        t.write("[default]\n{}".format(d.read()))
        t.flush()
        cf.read(t.name)
        return dict(cf.items("default"))


def load_cfg_file(filename):
    assert os.path.isfile(filename), "The file {} must be exist!".format(filename)
    cf = configparser.ConfigParser()
    cf.read(filename)
    return cf


if __name__ == '__main__':
    pass
