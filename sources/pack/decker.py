# please import Gdec.py

import tkinter
from tkinter import messagebox
import hashlib
import os
import time,sys
import warnings
import platform
import pyminizip
import pathlib
import sha3
import copy
import getpass
import tkinter
import tkinter.filedialog
from pack import zipfilejpn
from pack import aes
import traceback
import sys

# ファイルサイズの表記フォーマット

def cc(B):
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2)
   GB = float(KB ** 3)
   TB = float(KB ** 4)
   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   if KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   if MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   if GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   if TB <= B:
      return '{0:.2f} TB'.format(B/TB)

# ファイルサイズの表示ダイアログ生成

def comfilesize(file):
    size=os.path.getsize(file)
    size=cc(size)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('確認', '暗号化しようとしているファイルの容量は'+size+"です。\nファイルのサイズが大きい場合は暗号化に時間がかかります")
    print('')
    root.destroy()
    root.mainloop() 
    return

def filesize(file):
    size=os.path.getsize(file)
    size=cc(size)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('確認', '復号化しようとしているファイルの容量は'+size+"です。\nファイルのサイズが大きい場合は復号化に時間がかかります")
    print('')
    root.destroy()
    root.mainloop() 
    return

# zipファイルの圧縮

def comzip(file,pass1):
    key=copy.copy(pass1)
    pass2=str(key)
    print('')
    # pass1=pass1.lower()
  
    pass2=aes.encrypt(pass1)
    
    if file=="":
        filename=input(' file name >> ')
        filename=os.path.abspath(filename)
    else:
        filename=os.path.abspath(file)
    
    # decファイル名の生成
    
    #filename=filename.replace(' ', '')
    #filename=filename.replace('\'', ' ')
    #filename = filename.strip()
    name,ext = os.path.splitext(filename)
    finame=name+".dec"
    sf=os.path.dirname(filename)
    cdir=os.path.isdir(repr(sf))
        
    os.chdir(sf)
    comfilesize(file)
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    basename_without_ext=basename_without_ext+".dec"
    basefiles=os.path.basename(filename)
    #basefiles="\""+basefiles+"\""
    try :
        # 圧縮関係(英数字以外のファイル名もちゃんと圧縮できる)
        pyminizip.compress(basefiles.encode('cp932'),"\\".encode('cp932'),basename_without_ext.encode('cp932'),pass2,int(9))
    except FileNotFoundError:
        n =0
        return n
    except OSError:
        n=-2
        return n
    except PermissionError:
        n=-3
        return n
    else:
       n=1
    
    return n

def openzip(file,ns,pass1):
    ns=str(ns)
    chef=1
    pass3=str(pass1)
    key=copy.copy(pass3)
    pass2=str(key)
    # pass1=pass1.lower()
    pass2=aes.encrypt(pass1)
    # ファイルPATHを生成して移動
    if file=="":
        filename=input(' File name >> ')
        filename=os.path.abspath(filename)
    else:
        filename=os.path.abspath(file)
    
    #filename=filename.replace(' ', '')
    #filename= filename.replace('\'', ' ')
    #filename = filename.strip()
    sf=os.path.dirname(filename)
    #sf="\""+sf+"\""
    cdir=os.path.isdir(sf)
    try:
        os.chdir(sf)
    except FileNotFoundError:
        n =0
        return n
    filesize(file)
    ext = os.path.splitext(filename)[1]
    name=os.path.splitext(os.path.basename(filename))[0]
    ext=str(ext)
    name=name+".dec"
    cd2=os.path.isfile(filename)
    if filename=="" or name=="":
        filename="file nots"
    
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    try:
        os.chdir(sf)
        k="y"
        if k=="Y" or k=="YES" or k=="y" or k=="":
            if ns=="1":
                zipfilepointer=zipfilejpn.ZipFile(name,"r")# ここから展開関係
                zipfilepointer.extractall(sf)
                zipfilepointer.close() # 展開関係ここで終わり
            else:
                zipfilepointer=zipfilejpn.ZipFile(name,"r")# ここから展開関係
                zipfilepointer.extractall(sf,pwd=bytes(pass2))
                zipfilepointer.close() # 展開関係ここで終わり
    except FileNotFoundError:
        n =0
        return n
    except RuntimeError:
        n=-2
        return n
    except PermissionError:
        n=-3
        return n
    else:
        n=1
        return n
