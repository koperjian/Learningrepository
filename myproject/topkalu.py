import sys
import re
import os

def mergesortlist(lista,listb):
    lena=len(lista)
    lenb=len(listb)
    mergelist=[]
    i,j,k=0,0,0
    while(i<lena and j<lenb):
        if lista[i]<listb[j]:
            mergelist.append(lista[i])
            k=k+1
            i=i+1
        else:
            mergelist.append(listb[j])
            k=k+1
            j=j+1
    if(i<lena):
        mergelist+=lista[i:]
    if(j<lenb):
        mergelist+=listb[j:]
    return mergelist


def _get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    return "1920x1080"

lista=[1,5,7,9,10]
listb=[2,3,4,8]
print(sys.path[0])

print(_get_screen_size())
print(mergesortlist(lista,listb))


