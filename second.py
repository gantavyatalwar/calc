
# import random
# number=random.randint(1,100)

# guess=1
# game_over = False

# while not game_over:
#     unum=int(input("enter any no"))
#     if unum==number:
#         print ("correct guess & you took  "+str(guess)+ "\t chances")
#         game_over=True
     
#     else :
#         if unum<number:
#             print("too low")
           
#         else:
#             print("too high") 
#         guess+=1
       ####not req # unum=int(input("enter any no"))


### FUNCTIONS

# def greater (a,b,c):
#     # return a>b
#     if a>b and a>c:
#         return "a is greater"+str(a)
#     return "b is greater"
# print(greater(127,51,76))

# def palin(a):
#     return a[::-1]== a
        
# ram = input("enter string")
# print(palin(ram))
    #  or
# a = input("enter string")
# if  a[::-1]== a:
#     print("yes")
# else:
#     print("no")

#0,1,1,2,3,5,8
# def feb(num):
#     a=0
#     b=1
          
#     if num==1:
#         print (0)
#     elif num==2:
#         print(1) 
#     else:
#         print(0,1,end=" ")
#         # i=1
       
#         # while i <=(num-2):
#         for i in range(1,num-1):
#             c=a+b
#             a=b
#             b=c
#             print (c, end=" ")
       
#             i+=1
# print(feb(10))

# list=[1,232,3,4,"ram","sham"]
# list2=["rose", "cactus"]
# list[1]=["wow"]  #### to insert element
# list.append("vov")
# list.insert(1,"ram")
# list.extend(list2)
# list.append(list2)
# list.pop()
# list.remove("ram")
# del list[3]
# list2.sort()
# print(sorted(list2))
# new=list.copy()
# print(list.count("ram"))
# list.clear()
# list.reverse()
# print(list)
# print(list==list2)
# print(list is list2)
# ram="whatcan ,i,do".split(",")# string to list
# ram=["78","yoyo","hoho"]#list to string
# print(" ".join(ram))
# print(ram)
# print (list.index(4,0,9))
# n= list(range(1,10))
# print (n)
# num=["a","b", "ram","shams"]
# num=[3,2,4,5,2,1,33]
# def numbers(k):
#     square=[]
#     for i in k:
#          square.append(i**2) #[i*i] or[i**2]
#     return square

# print (numbers(num))

# def rev(j):
    # l1=[]
    # for i in range(len(j)):
    #      l1.append (j.pop())
            #or
    ##### poped = j.pop()
        #####  l1.append(poped)

#     i=0
#     while i<len(j):
#         l1.append (j.pop())
#     i+=1
#     return l1
# print(rev(num))
# print(rev(list( range(0,11) ) )  )
# li=["gham","sham","ram","dfd"]
# li=[1,2,3,4,5,6]
# def rev(l):
#     total=[]
#     for i in l:
        # total.append(i [::-1] )
        # total.append(i.reverse())
#     return total
# print (rev(li))

# li=1,2,3,4,5,6
# def square (l):
#     total=[]
#     for i in l:
#         total.append(i**2)
#     return total
# print (square(li))

# l= [1,3,4,53,2,345,3223]
# def ram (li):
#     even=[]
#     odd=[]
#     for i in li:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     # output=[odd,even]
#     od = odd.append(even)
#     return od
# #     # return output
# print (ram(l))
# s=[1,2,3,4]
# d=[2,53,4]
# def com(a,b):
#     co=[]
#     for i in s:
#         if i in d:
#             co.append(i)
#     return co
# print(com(s,d))
# li=[1,23,[6,6,77],[6,7,7],[7,8,8,8]]
# def ty (l):
#     io=0
#     for i in l:
#         if type(i)==list:
#             io+=1
#     return io
# print(ty(li))