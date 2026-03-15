#----------multiplication of tables------------
# num = int(input("Enter a number:"))

# print("The multiplication of",num)
# for i in range(1,11):
#     a=num*i
#     print(a) 

#----------------Sum of First n Natural Numbers------------------
# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("The sum of",n,"is",sum)

#-----------table of a number-------------------
# n=int(input("Enter a number:"))
# a=1
# for i in range(1,n+1):
#  a=a*i
# print(a)

#-------------reverse na number----------------------------
# n=int(input("Enter a number:"))
# n=123

# output=0
# while (n/10!=0):
#        last_digit=n%10
#        n=int(n/10)
#        output=output*10 + last_digit
# print(output)

#-----------------to print numbers in descendiing order-----------------
# n=100
# while (n!=0):
#     print(n)
#     n=n-1

# ----------------palindrome of a number----------------------------
# a=n=12876
# last_digit=0
# result=0
# while(n%10!=0):
#     last_digit=n%10
#     n=int(n/10)
#     result=result*10+last_digit
# if (result==a):
#     print("True")
# else:
#     print("False")

# -------------star pattern-----------------
# n=5

# for i in range(1,n+1):
#     for r in range(1,i+1):
#         print("*",end="")
#     print()

#-----------duplicate from list------------------
# n=[1,2,2,3,1,4]
# r=[]
# for i in range(0,len(n)):
#     for j in range(i+1 ,len(n)):
#         if (n[i]==n[j]):
#             r.append(n[j])
# print(r)

# ---------------to print 2d array element-------------------
# a = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# print(a[2][0])

#---------even odd--------------------------
# n=int(input("enter a number"))
# if (n%2==0):
#     print("even")
# else:
#     print("odd")
# print(66/2, 66%2)


#-----------largest number in a list--------------     
# n=[1,2,3,4,5]
# max=0
# for i in n:
#     if (i>max):
#         max=i
# print(max)

#--------------to find second largest number in a list---------------------
# n=[1,3,6,6,5]
# max=0
# r=0
# for i in n:
#     if(i>max):
#         r=max
#         max=i
#     elif (i>r and i!=max):
#         r=i
# print(r)

#-----------------average of list------------------------
# n=[1,2,3,4,5]
# sum=0
# for i in n:
#     sum=sum+i
# print(sum/len(n))

#------------------count number of even odd in a list------------------------------    
# n=[5,7,4,6,7,8,2,5,9,1] 
# r=[]
# p=[]
# for i in n:
#     if(i%2==0):
#         r.append(i)
#     else:
#         p.append(i)
# print(len(r))
# print(len(p))
# a=b=0
# for i in n:
#     if(i%2==0):
#         a+=1
#     else:
#         b+=1
# print(a,b)

#-------------to see how nuber is incremented by 2 for (i start point, i end point , i++)--------------
# n=[1,2,3,3,4,5,1]
# for i in range(0,len(n),2):
#     print(n[i])

#-------------reverse a list-------------------------
# n=[5,7,5,4,4,6]
# for i in range(1,len(n)):
#       print(n[i])
# a=[]
# for i in range(len(n)-1,0,-1):
#         a.append(n[i])
#         # print(i)
# print(a)  
# 

#---------------remove duplicates from list--------------
# n=[5,7,5,4,4,6]
# a=[]
# b
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]==n[j]):
#             #print(n[i])
#            n.pop(j)
#            j-=1
       
#----------to find duplicate elements in two lists and printing them-----------      
# print(n)
# a=[1,2,3,4,5]
# b=[3,3,4,5,6]
# c=[]
# for i in range(0,len(a)):
#     for j in range(0,len(b)):
#         if (a[i] not in c and a[i]==b[j]):
#             c.append(a[i])
        
# print(c)

#--------to place all the zeros at the end-----------------
# n=[0,3,6,1,0,0,4,0,1,0]
# a=[]
# b=[]
# c=[]
# for i in range(0,len(n)):
#     if (n[i]==0):
#         a.append(n[i])
#     else:
#         b.append(n[i])

# c=b
# # for j in range(0,len(a)):
# for j in a:
#     print(j)
#     c.append(a[j])
# # c=b.append(a)
# print(c)

#------------------------count how many times each element appears--------------------------
# n=[4,2,1,1,3,4,8,4,2,7,9,1,1,4]
# r = {}

# for i in range(0,len(n)):
#     if n[i] in r:
#         r[n[i]] += 1
#     else:
#         r[n[i]] = 1

# print(r)

# ---------check if string is palindrome------------

# s="kikik  kikik"
# a=''
# for i in range(len(s)-1,-1,-1):
#     a+=s[i]
# # print (a)
# if s==a:
#     print("true")
# else:
#     print("false")


# a=[1,2,4,2,1,]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])

# flag=0
# for i in range(0,len(a)):
#     if(a[i]!=b[i]):
#         flag=1

# if(flag==1):
#     print("false")
# else:
#     print("true")
    
# -----------reverse a string----------------
# n="hello"
# a=''
# for i in range(len(n)-1,-1,-1):
#     a=a+(n[i])
# print(a)

# ---------count vowels--------------
# n='ketki'
# a=b=0
# for i in n:
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         a+=1
#     else:
#         b+=1
# print(a,b)

# --------count char in string----------
# n='ketki'
# a={}
# for i in n:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print(a)

# ----------------------------remove space from string usin replace fn--------------------
# n="hi my name is kk"
# # s=n.replace(" ","")
# # print(s)
# ----------------or using for loop------------------
# s=''
# for i in n:
#     if i!=" ":
#         s+=i
# print(s)

# f---------------ind first on repeating char-------------------------

# n="swiss"
# a={}
# for i in range(0,len(n)):
#         if n[i] in a:
#             a[n[i]]+=1
#         else:
#             a[n[i]]=1
# # print(a)
# for i in a:
#     #  print(i,a[i])
#      if a[i]==1:
#           print(i)
#           break
a=2
b=3

def func():
    c=a+b

    d=a+c
    
    return c



result = func()
print(c)

#comment 2
#asdf hello




