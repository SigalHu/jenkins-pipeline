# encoding=utf-8
"""
@author huxujun
@date 2019-06-03
"""
import os
import shutil
import tarfile


def tar_dir(tar_name: str, target_dir: str, delete_target=False):
    if not os.path.exists(os.path.dirname(tar_name)):
        os.makedirs(os.path.dirname(tar_name))

    target_dir = os.path.abspath(target_dir)
    root_prefix, _ = os.path.split(target_dir)
    with tarfile.open(tar_name, "w:gz") as f:
        for root, _, files in os.walk(target_dir):
            for file in files:
                full_path = os.path.join(root, file)
                f.add(full_path, arcname=full_path.replace(root_prefix, "").lstrip(os.sep))
    if delete_target:
        shutil.rmtree(target_dir)


def unzip_tarfile(filename: str, output_dir=".", delete_tar=False) -> set:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.isdir(output_dir):
        raise Exception("The output_dir must be dir, output_dir=%s" % output_dir)

    unzip_set = set()
    with tarfile.open(filename) as f:
        f.extractall(path=output_dir)
        for unzip_file in f.getnames():
            unzip_set.add(os.path.join(output_dir, str(unzip_file).split(os.sep, 1)[0]))
    if delete_tar:
        os.remove(filename)
    return unzip_set


def list_tarfile(filename: str) -> set:
    tarfile_set = set()
    with tarfile.open(filename) as f:
        for unzip_file in f.getnames():
            tarfile_set.add(str(unzip_file).split(os.sep, 1)[0])
    return tarfile_set


if __name__ == '__main__':
    pass
