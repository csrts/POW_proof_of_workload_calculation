import requests
import base64
import time
import gzip
from hashlib import md5
from functools import reduce
import sys
import os,signal
import io
from tqdm import tqdm

from Crypto.Cipher import AES
from Crypto.Util import Counter

def Decrypt(key: str, text: str) -> str:
    if len(key) < 32:
        key += ' ' * (32 - len(key))
    elif len(key) > 32:
        key = key[0:32]
    Cipher = AES.new(key.encode(), AES.MODE_CTR, counter=Counter.new(128))
    src = str(gzip.decompress(bytes.strip(cipher.decrypt(base64.b64decode(text)))), encoding='utf-8')
    print(src)
    return src

import itertools

def dcode(key):
    try:
        # print(key)
        Decrypt(key, "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")
        print("key: ", key)
        os.killpg(os.getpgid(os.getpid()), signal.SIGKILL)
    except Exception as e:
        # print(e)
        pass

def try_keys(keys):
    for key in keys:
        dcode(key)

def run_process():
    from multiprocessing import Process
    li = []
    t = 1
    a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = charts = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'][::-1]
    for x in tqdm(itertools.product(a1, a2, a3, a4, a5, a6, a7, a8), total=4294967296):
        key =   "0" * 24 + "".join(x)
        # dcode(key)
        li.append(key)
        if t % 10000 == 0:
            Process(target=try_keys, args=(li,)).start()
            li.clear()
        t += 1

if __name__ == '__main__':
    print("欢迎来到Hacking8信息流邀请码挑战题！\n本题一共有五关，通关前四关会得到hacking8的邀请码，通关第五关可以加我微信，拉你到hacking8交流群～\n")
    run_process()