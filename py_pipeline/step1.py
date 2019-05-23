# encoding=utf-8
"""
@author huxujun
@date 2019-05-23
"""
import os

print("[INFO] message1=%s" % os.getenv("message1"))
print("[WARN] message2=%s" % os.getenv("message2"))
print("[ERROR] CONTEXT=%s" % os.getenv("CONTEXT"))
