#!/usr/bin/env python
# coding: utf-8

# In[3]:


#No Idea!
#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=false
io = input().split()
m = int(io[0])
n = int(io[1])

storage = list()
count = 0

storage = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)


# In[5]:


#Introduction to Sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=false
def average(array):
    # Introduction to Sets in Python - Hacker Rank Solution START
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;
    # Introduction to Sets in Python - Hacker Rank Solution END

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[13]:


#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Symmetric Difference in Python - Hacker Rank Solution
numbers1 = int(input())
set1 = set(map(int,input().split()))
numbers2 = int(input())
set2 = set(map(int,input().split()))
set3 = (set1.difference(set2)).union(set2.difference(set1))
for i in sorted(list(set3)):
        print (i)


# In[14]:


#Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=false&h_r=next-challenge&h_v=zen
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())

print(len(countries))


# In[16]:


#Set .union() Operation
#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
# set.union() Operators in Python - Hacker Rank Solution START
N1 = int(input())
storage1 = set(input().split());
N2 = int(input())
storage2 = set(input().split());
storage3 = storage1.union(storage2)
print(len(storage3))


# In[17]:


#Set .intersection() Operation
#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(map(int,input().split()))
m=int(input())
r=set(map(int,input().split()))
print(len(s.intersection(r)))


# In[18]:


#Set .difference() Operation
#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=false
n=int(input())
s=set(map(int,input().split()))
m=int(input())
r=set(map(int,input().split()))
print(len(s.difference(r)))


# In[19]:


#Set .symmetric_difference() Operation
#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=input()
li1 = input().split()
s1 = set(li1)
n2=input()
li2 = input().split()
s2 = set(li2)
s1s2 = s1.symmetric_difference(s2)
print(len(s1s2))


# In[20]:


#Set Mutations
#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(map(int, input().split())) 

for _ in range(int(input())):
    args = input().strip().split()
    nw= set(map(int, input().split())) 
    eval("s." + args[0] + "(  nw  )")
print(sum(s))


# In[21]:


#The Captain's Room
#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
ROOM_LIST = input().split()
ROOM_SET = set(ROOM_LIST)
for ele in list(ROOM_SET):
    ROOM_LIST.remove(ele)
CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
print(CAPTAIN_ROOM_NUM)


# In[22]:


#Check Subset
#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=false
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

for i in range(n):
    
    s,A=int(input()),set(map(int,input().split()))
    r,B=int(input()),set(map(int,input().split()))
    if A-B==set():
        print(True)
    else:
        print(False)


# In[23]:


#Check Strict Superset
#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=false
storage = set(input().split())
N = int(input())
output = True

for i in range(N):
    storage2 = set(input().split())
    if not storage2.issubset(storage):
        output = False
    if len(storage2) >= len(storage):
        output = False

print(output)


# In[ ]:




