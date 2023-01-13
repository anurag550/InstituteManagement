from django.test import TestCase

# Create your tests here.
# class A:
#     def __init__(x,var):
#         x.var=var
#
#     def m1(x):
#         print(x.var)
# a1=A(10)
# a1.m1()
#
#
# s={1,2,3,4}
# s.add("anurag")
# print(s)

# d={'i':10,'j':50}
# x='i'
# for i in d.keys():
#     if i==x:
#         print(d[x])
#
# class A:
#     z=10
#     def m1(self):
#         self.x=100
#         print(self.x)
#         print(self.z)
# a1=A()
# a1.m1()
# print(a1.z)

#
# tpl=(1,2)
# print(2*tpl)
#
# def mutate(arr):
#     arr[0]=0
# x=[123]
# mutate(x)
# print(x)
#
# print(2**10)
# # class A:
#     def __init__(self,id):
#         self.__id=id
# id=100
# x=A(10)
# print(x.id)

# __str__=1
# _str=10
# __str=100
# print(__str)
# print(_str)
# print(__str__)
#
# on=25
#
# str="hello world"
# print(str[-1:])
# x=['anurag','durga']
# print(x[-1][-1])
#
# x="" and 'b'
# print(x)
#
# print(16.8//2)
#
# print(17/2%2*3**3)

# d={10:'a',1:'a', 2:'c'}
# a=sorted(d)
# print(a)
#
# t=(1,2)
# print(2*t)
#
# print("" and "c")

n=123
r=0
while n>0:
    l=n%10
    r=(r*10)+l
    n=n//10
print(r)