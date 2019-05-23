# encoding=utf-8
"""
@author huxujun
@date 2019-05-23
"""
import os

print(os.getenv("message1"))
print(os.getenv("message2"))
print(os.getenv("CONTEXT"))
os.putenv("message1", os.getenv("message1") + "1")
os.putenv("message2", os.getenv("message1") + "1")
os.putenv("CONTEXT", os.getenv("CONTEXT") + "1")
