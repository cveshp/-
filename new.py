lista=[16,12,15,57,65,64,93,89,86,75,4]
msg=0
d=0
times=0
while msg!=len(lista)-1:# 当msg值等于lista的长度减一时，说明lista已经完成排序
    for a in range (len (lista)):
        if a==len(lista)-1:# 在每一轮比较完成的时候显示排序，并计算msg值
            times+=1
            print ('这是第',times,'轮比较')
            for d in range(len(lista)-1):# 下面计算msg值
            	    if lista [d]< lista [d+1]: # 若排序正确，则msg值加一
                	    msg+=1
        elif lista [a]>lista[a+1]:# 当值需要调换时进行调换
            b=lista [a]# 这些变量用于暂时存储列表中的数
            c=lista [a+1]
            lista.remove(lista[a])
            lista.remove(lista[a])
            lista.insert(a,c)
            lista.insert(a+1,b)
            print(lista)
            b=0
            c=0
        if a==0:#在每一轮比较开始时重置msg值
            msg=0
