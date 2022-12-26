objectg={1056:'商品a',1057:'商品b',1058:'商品c'}# 使商品编号与商品名称对应
price={1056:15,1057:23,1058:5} # 使商品编号与商品价格对应
truth='y'
lista=[]# 这个列表用于存储商品编号
listb=[]# 这个列表用于存储商品的数量
listc=[]# 这个列表用于存储商品名
all_price=0
while truth=='y':# 这个循环用于录入商品
    goods=int (input ('输入商品编号'))
    num=int(input('......'))
    lista.append(goods)
    listb.append(num)
    print('当前购买商品:',lista)
    print ('对应数量:',listb)
    truth=input ('是否继续输入商品(y/n)')
# 接下来要进行计算
for x in range(len(lista)):
    all_price+=price[lista[x]]*listb[x]
# 接下来输出商品名列表，这个功能也能在上面的while循环中实现，也可以与上边的for循环合并
for y in range(len(lista)):    
    	listc.append(objectg[lista[y]])
# 接下来收银
print('购买商品有',listc)
print('对应编号:',lista)
print('对应数量：',listb)
print('总价：',all_price)
money=int(input('收您：'))
print('找您：',money-all_price)