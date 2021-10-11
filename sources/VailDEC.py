
# Copyright (c) 2020 Vail-Zero. All Rights Resarved.

# 必要なライブラリーインポート                
from tkinter import messagebox
from pack import decker
import tkinter
import threading
import os
import sys
from pack import passgen
# from pack import config
# from pack import GUIl
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import webbrowser
# from pack import regkey
global txt

# 画像の後ろの背景色設定
backclr="#9aff9a"

var = {'Theme': "None", 'online':True,'cash':"None"}
# リソース読み込み関数
def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)

# ボタンクリック後の処理

# 暗号化
def btn_click(pass1):
    iDir = ""
    # window.withdraw()
    # var=config.loadconf()
    var = {'Theme': "None", 'online':True,'cash':"None"}
    fTyp = [("", "*")]
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
    import shutil
    import tempfile
    if file=="":
        # window.deiconify()
        return
    if file=="":
        # window.deiconify()
        return
    if (" " in file):
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。\nこのソフトウェアはパス内の空白を処理できません')
        # window.deiconify()
        return
    n=decker.comzip(file,pass1)
    if n==0:
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。\nこのソフトウェアはパス内の空白を処理できません')
    if n==1:
        messagebox.showinfo('確認', '暗号化が終了しました!')
    if n==-3:
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
    if n==-2:
        messagebox.showerror('エラー', '対応していないファイルの可能性があります')        
    # window.deiconify()
    return 


def btn5_click(file,pass1):
    iDir = ""
     
   # pass1=getpass.getpass(' DEC File Password (英数字のみ) >> ')
    fTyp = [("", "*")]
    if file=="":
        # window.deiconify()
        return
    try:
        n=decker.comzip(file,pass1)
    except:
        n=0
    if n==1:
         
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showinfo('確認', '暗号化が終了しました!')
        root.destroy()
        root.mainloop() 
    if n==-3:
         
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
        root.destroy()
        root.mainloop() 
    if n==-2:
         
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', '対応していないファイルの可能性があります')
        root.destroy()
        root.mainloop() 
    return 

# 復号化関数
def btn2_click(pass1):
    iDir = ""
    n=-1
    #window.withdraw()
    var = {'Theme': "None", 'online':True,'cash':"None"}
    fTyp = [("DEC Files", "*.dec")]
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
    import shutil
    import tempfile
    if file=="":
        #window.deiconify()
        return
    ns=0
    n=decker.openzip(file,ns,pass1)
    if n==0:
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。\nこのソフトウェアはパス内の空白を処理できません')
    if n==1:
         
        messagebox.showinfo('確認', '復号化が終了しました!')
         
    if n==-2:
         
        messagebox.showerror('エラー', 'パスワードが間違っています')
         
    if n==-3:
         
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
    # window.deiconify()
    return

def btn4_click(file,pass1):
    iDir = ""
     
    # pass1=getpass.getpass(' DEC File Password (英数字のみ) >> ')

    if file=="":
        window.deiconify()
        return
    ns=0
     
   
    n=decker.openzip(file,ns,pass1)
    if n==1:
         
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showinfo('確認', '復号化が終了しました!')
         
        root.destroy()
        root.mainloop()      
         
    if n==-2:
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'パスワードが間違っています')
         
        root.destroy()
        root.mainloop()
         
    if n==-3:
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
         
        root.destroy()
        root.mainloop()
         
    # os.system('clear')
    #window.deiconify()
    return
        
# 以下スレッド化
def btn():
    pass1=txt.get()
    if pass1=="":
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'パスワードを入力してください')
        root.destroy()
        root.mainloop()
        return
    thread1 = threading.Thread(target=btn_click,args=([pass1]))
    thread1.start()
    txt.delete(0, tkinter.END)
    return

def btn2():
    pass1=txt.get()
    if pass1=="":
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'パスワードを入力してください')
        root.destroy()
        root.mainloop()
        return
    thread1 = threading.Thread(target=btn2_click,args=([pass1]))
    thread1.start()
    txt.delete(0, tkinter.END)
    return

# ここまで

def btn04():
    import pyperclip
    txt.delete(0, tkinter.END)   
    import random
    cc=random.randint(5,20)
    bpass=passgen.gen(cc)
    b=messagebox.askyesno('確認', bpass+'\n 生成したパスワードをパスワードボックスに入れますか?\n 「OK」をクリックした場合、パスワードはクリップボードにコピーされます。')                
    if b==False:
        return
    pyperclip.copy(bpass)
    txt.insert(tkinter.END,bpass)
    return
 
# ここまで

# ログインの判定
v=False
#v=regkey.read_reg()
if (v==True):
    i=0
    
    while True:
        GUIl.LoginView()
        if (GUIl.checkregdata()==False):
             
            i=i+1
            root = tkinter.Tk()
            root.attributes("-topmost", True)
            root.withdraw()
            messagebox.showerror('エラー', 'ユーザー名かパスワードが間違っています')
             
            root.destroy()
            root.mainloop()
            
            if i==3:
                
                root = tkinter.Tk()
                root.withdraw()
                root.attributes("-topmost", True)
                messagebox.showerror('エラー', '認証エラーが三回以上続きました。\n ソフトウェアを終了します')
                GUIl.delcheck()
                 
                root.destroy()
                root.mainloop()
                sys.exit(1)
            else:                
                continue
        else:
            break


def btn05():
    
    root = tkinter.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    b=messagebox.askyesno('確認', '認証サーバを切り替えますか？')                
    if b==False:
        root.destroy()

        return
    regkey.write_websource()
    root.destroy()
    root.mainloop()

# 画面初期化
def put(event):
    import pyperclip
    txt.insert(tkinter.END,pyperclip.paste())
    return

# GUIl.delcheck()

# メインウインドウを作成

window = tkinter.Tk()
window.geometry("400x253")
window.title("VailDEC ファイル暗号化ソフト")
window.configure(bg=backclr)
window.resizable(False, False)

# 背景画像とアイコンの設定
iconfile = 'IMG_8776.ICO'
# window.iconphoto(False, tkinter.PhotoImage(file=iconfile))
window.attributes("-topmost", False)
try:
    
    if (var['Theme']=="None"):        
        background =tkinter.PhotoImage(file=resourcePath('resources/img.png'))
    else:
        background =tkinter.PhotoImage(file=var['Theme'])

    bg = tkinter.Canvas(window,width=400,height=253)
    bg.pack()
    bg.config(borderwidth = -2)
    bg.create_image(200,130,image=background)
except:
    pass

txt = tkinter.Entry(font=("",10),show='*')
txt.place(x=130, y=200)
label2 = ttk.Label(window, text='パスワード')
label2.place(x=65, y=200)

btn4 = tkinter.Button(window, text="パスワード生成",command = btn04)

btn4.place(x=278, y=18)

btn = tkinter.Button(window, text="暗号化",command = btn,font=("", 20))

btn.place(x=150, y=50)

btn2 = tkinter.Button(window, text="復号化",command = btn2,font=("", 20))

btn2.place(x=150, y=140)
window.mainloop()
