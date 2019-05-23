# encoding=utf-8
"""
@author huxujun
@date 2019-05-23
"""
import os

print(os.environ["message1"])
print(os.environ["message2"])
print(os.environ["CONTEXT"])
os.environ["CONTEXT"] += "1"
