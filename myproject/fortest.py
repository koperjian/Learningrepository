

#冒泡排序算法
def bubble_sort(lists):
    count=len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists

#插入排序算法
def insert_sort(lists):
    count=len(lists)
    for i in range(1,count):
        key = lists[i]
        j=i-1
        while j >=0 :
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[j]=key
            j=j-1
    return lists


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:
        for i in range(0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group = group // step
    return lists

def select_sort(lists):
    #选择排序
    count=len(lists)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if lists[min] > lists[j]:
                min=j
        lists[i],lists[min]=lists[min],lists[i]
    return lists;



templists=[10,1,5,11,23,3541,531,21,-1,-100,1,10000,122,21432,11,12,134,13,0,331]
print("brforebubllesort:",templists)
select_sort(templists)
print("afterbubllesort:",templists)

