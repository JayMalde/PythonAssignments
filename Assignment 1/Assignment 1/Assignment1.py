#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hello World")


# In[3]:


for num in range(2000,3200):
    if num%7==0 and num%5!=0:
        print(num,end=',')


# In[47]:


first_name=input("Enter First Name :")
last_name=input("Enter Last Name :")
for n in first_name,last_name:
    print(n[::-1],end=' ')


# In[20]:


diameter=int(input("Enter Diameter :"))
radius=diameter/2
volume=(4/3)*(3.141592)*(radius**3)
print(volume)


# In[36]:


numbers=input("Enter Comma Seperated Numbers :")
list1=numbers.split(',')
print(list1)


# In[40]:


rows=int(input("Enter Number Of Rows :"))
for i in range(rows):
    for j in range(rows):
        if j<i:
            print("*",end='')
    print()
for i in range(rows):
    for j in range(rows):
        if j<rows-i:
            print("*",end='')
    print()


# In[9]:


word=input("Enter A Word :")
for i in range(len(word)-1,-1,-1):
    print(word[i],end='')


# In[22]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,!\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:




