import re
import tkinter.filedialog
import matplotlib.pyplot as plt
import os
import re

# path=r'F:\share\siyuan_1.18\knowledge\C'
path=r'F:\share\siyuan_1.18'
def findAllFile(base):
    filename=[]
    dirname=[]
    for root, ds, fs in os.walk(base):
        # for f in fs:
        #     yield f
        for f in fs:
            # print(os.path.join(root,f))
            filename.append(os.path.join(root,f))
        for name in ds:
            # print(os.path.join(root,name))
            dirname.append(os.path.join(root,name))

    return filename,dirname

def getSomeFile(root,type=None):
    base= root
    filelist=[]
    namelist=[]
    filelist=findAllFile(root,base)
    # print(f"filelist={filelist}")
    for i in filelist:
        # print(f"i={i}")
        if(type==None):
            namelist.append(i)
        elif (type in i):
            namelist.append(i)
    return namelist;



def test_searchInLine(content:str,key:str):
    if(key in content):
        return 1;
    else:
        return 0;


def test_searchInFile(path:str,key:str):

    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            if(test_searchInLine(line,key)==1):
                print(f"file={path} \n line={line}")

# for i in file_list:
#     test_searchInFile(i,r"{: id=");


file_list,dir_list=findAllFile(path);
print(f"file_list={file_list}")
print(f"dir_list={dir_list}")
for f in file_list:
    if(r'.md' in f):
        print(f)
print('--------endfile--------')
for d in dir_list:
    print(d)
print('enddir')

onefile=r'F:\share\siyuan_1.18\knowledge\C\C函数调用栈.md'
def oneFiletoOthermd(file:str):
    print(f"path={file}")
    res=r'{: id(.*?)}'
    with open(file,'r',encoding='utf-8') as f:
        cont=f.readlines()
        allstr=''
        for i in cont:
            allstr+=i;
    # print(cont);
    # allstr=r'{: id="20211129130447-ywy901n"}'
    allstr=re.sub(res,'',allstr)
    # print(f"your file {file} conttent is :\r\n{allstr}")
    allstr=allstr.replace('\n\n','\n');
    # print(f"your file {file} conttent is :\r\n{allstr}")
    with open(file+'.md','w+',encoding='utf-8') as f:
        f.write(allstr);


def oneFiletoSelfmd(file:str):
    print(f"path={file}")
    res=r'{: id(.*?)}'
    with open(file,'r',encoding='utf-8') as f:
        cont=f.readlines()
        allstr=''
        for i in cont:
            allstr+=i;
    # print(cont);
    # allstr=r'{: id="20211129130447-ywy901n"}'
    allstr=re.sub(res,'',allstr)
    # print(f"your file {file} conttent is :\r\n{allstr}")
    allstr=allstr.replace('\n\n','\n');
    # print(f"your file {file} conttent is :\r\n{allstr}")
    with open(file,'w',encoding='utf-8') as f:
        f.write(allstr);


for f in file_list:
    if(r'.md' in f):
        # oneFiletoOthermd(f);
        oneFiletoSelfmd(f)