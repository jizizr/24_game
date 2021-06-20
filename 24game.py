from random import *

def judge(a):
    b=0
    for i in a:
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            b=1
            break
    if b==1:
        return False
    else:
        return True

def output(a,b,c,d,e,f,g):
    if b=="/":
        x="*"
    elif b=="-":
        x="+"
    else:
        x=b
    if d=="/":
        y="*"
    elif d=="-":
        y="+"
    else:
        y=d
    if f=="/":
        z="*"
    elif f=="-":
        z="+"
    else:
        z=f
    if x==y and y==z or x=="*" and z=="+":
        return("{0}{1}{2}{3}{4}{5}{6}".format(a,b,c,d,e,f,g))
    elif x=="+"and y=="*":
        return("({0}{1}{2}){3}{4}{5}{6}".format(a,b,c,d,e,f,g))
    else:
        return("({0}{1}{2}{3}{4}){5}{6}".format(a,b,c,d,e,f,g))

def output2(a,b,c,d,e,f,g):
    if b=="/":
        x="*"
    elif b=="-":
        x="+"
    else:
        x=b
    if d=="/":
        y="*"
    elif d=="-":
        y="+"
    else:
        y=d
    if f=="/":
        z="*"
    elif f=="-":
        z="+"
    else:
        z=f
    if x=="+" and y=="+" or x=="*" and y==z or x=="*"and z=="*":
        return("{0}{1}{2}{3}{4}{5}{6}".format(a,b,c,d,e,f,g))
    elif y==z:
        return("({0}{1}{2}){3}{4}{5}{6}".format(a,b,c,d,e,f,g))
    elif x==z:
        return("({0}{1}{2}){3}({4}{5}{6})".format(a,b,c,d,e,f,g))
    else:
        return("{0}{1}{2}{3}({4}{5}{6})".format(a,b,c,d,e,f,g))

def f(a,b,c):
    if c=="+":
        return(a+b)
    elif c=="-":
        return(a-b)
    elif c=="*":
        return(a*b)
    else:
        if b!=0:
            return(a/b)
        else:
            return(5555555543.250520/47)

def g():
    k=["+","-","*","/"]
    a=[]
    for x1 in k:
        for x2 in k:
            for x3 in k:
                a.append([x1,x2,x3])
    return a
                    

def h(arr):
    length = len(arr)
    if length == 1:
        return [arr]

    result = []
    fixed = arr[0]
    rest = arr[1:]

    for _arr in h(rest):
        for i in range(0, length):
            new_rest = _arr.copy()  
            new_rest.insert(i, fixed)
            result.append(new_rest)
    return result

def judge(a1,a2,a3,a4):
    y=0
    A=0
    a=h([a1,a2,a3,a4])
    b=g()
    for c in a:
        for d in b:
            e=c[0]
            for z in range(3):
                e=f(e,c[z+1],d[z])
                if z==2 and e==24:
                    return True
                    y=1
                    break
                l=f(f(c[0],c[1],d[0]),f(c[2],c[3],d[2]),d[1])
                if l==24:
                    return True
                    y=1
                    break
            if y==1:
                break
            A+=1
        if y==1:
            break
        if A==len(a)*len(b):
            return False

def answer(a1,a2,a3,a4):
    y=0
    A=0
    a=h([a1,a2,a3,a4])
    b=g()
    for c in a:
        for d in b:
            e=c[0]
            for z in range(3):
                e=f(e,c[z+1],d[z])
                if z==2 and e==24:
                    print(output(c[0],d[0],c[1],d[1],c[2],d[2],c[3]))
                    y=1
                    break
                l=f(f(c[0],c[1],d[0]),f(c[2],c[3],d[2]),d[1])
                if l==24:
                    print(output2(c[0],d[0],c[1],d[1],c[2],d[2],c[3]))
                    y=1
                    break
            if y==1:
                break
            A+=1
        if y==1:
            break
        if A==len(a)*len(b):
            return False

def timu():
    global a,b,c,d
    while True:
        a=randint(0,12)
        b=randint(0,12)
        c=randint(0,12)
        d=randint(0,12)
        if judge(a,b,c,d):
            ss=[a,b,c,d]
            return ss
            break
            

def panduan(A):
    A=''.join(A)
    a=''
    A+='*'
    b=[]
    for i in A:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            a+=i
        elif len(a)!=0 :
            b.append(int(a))
            a=''
    b.sort()
    return b

print('-----------------a simple 24 point game from jizizr---------------------')
print('使用说明：')
print('1. 题目肯定有解')
print('2. 输入a获取答案')
print('3. Ctrl+c 可以退出游戏')
print('------------------------------------------------------------------------')
while True:
    aa=timu()
    a=aa[0]
    b=aa[1]
    c=aa[2]
    d=aa[3]
    print('请用四则运算使得下列数结果为24')
    print('题目为：{0}  {1}  {2}  {3}'.format(a,b,c,d))
    while True:
        e=input('输入您的算式：')
        aa.sort()
        if e=="a":
            answer(a,b,c,d)
            print('------------------------------------------------------------------------')
            break
        p=0
        for i in e:
            if i in ["(",")"]:
                p+=1
        if p%2!=0:
            print('括号错了')
            print('')
            continue
        elif aa!=panduan(e):
            print('你用的不是这4个数！请重输！')
            print('')
        elif eval(e)!=24:
            print('错了！')
            print('')
        else:
            print('正确！')
            print('请接受下一组挑战！')
            print('------------------------------------------------------------------------')
            break
