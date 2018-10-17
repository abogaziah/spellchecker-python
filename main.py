def function1():
    path = 'Dic.txt'
    dic = open(path,'r')
    list_dic = dic.readlines()
    s = input().lower()
    dic.close()

function1()
