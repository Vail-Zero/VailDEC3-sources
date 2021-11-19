# 同名のファイルがあるか判定
def FileWarnings(file):
    import glob
    import os
    basedir=os.path.dirname(file)
    ext = os.path.splitext(os.path.basename(file))[0]
    checkfile=basedir+"/"+ext+".*"
    c=glob.glob(checkfile)
    i=-1
    if len(c)==2:
        c=True
    else:
        c=False
    return c

def FileWarnings2(file):
    import glob
    import os
    basedir=os.path.dirname(file)
    ext = os.path.splitext(os.path.basename(file))[0]
    checkfile=basedir+"/"+ext+".*"
    c=glob.glob(checkfile)
    i=-1
    if len(c)==2:
        c=True
    else:
        c=False
    return c
