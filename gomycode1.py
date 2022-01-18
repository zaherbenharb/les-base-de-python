#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


nom=str  #exercie 1
prenom=str
print ('ecrire votre nom')
x= input (nom)
print ('ecrire votre prenom')
t= input (prenom)
print ('votre nom est',t,x)


# In[4]:


#exercice2
i= input("entre n")
i= int(i)
print(i + i*11 + i*111)


# In[ ]:





# In[ ]:





# In[3]:


#exercie 3
n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
   print("est Paire")
else:
   print( "est Impaire")


# In[6]:


#exercie 4
for i in range(2000,3201):
    if (i % 5) != 0 and (i % 7) == 0:
        print (i)


# In[7]:


#exercie5
nbr = int(input('Entrez un nombre : '))
x = 1
for i in range(1, nbr+1):
    x = x * i
print (nbr,'! = ',x)


# In[8]:


#exercie7
nbr = int(input('Entrez un nombre : '))
if nbr >= 500 :
    print("le prix apres solde ",nbr*0.5)
elif nbr <500 and nbr>=200:
     print("le prix apres solde ",nbr*0.3)
else : print ("le prix apres solde",nbr*0.1)


# In[ ]:




