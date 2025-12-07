#basics
print ("hello,world!, Welcome Srihaas, I already updated")


import sys 
print(sys.version)


if 5 > 2:
    print ("five is greater than two!") 
  
l = "what is your name" 
my_name = 'Srihaas'
 
print(l)
print(my_name)

#type of comments
#this is a comment .
print("hello,world")

#print("hello,world!)
print("cheers,mate!")
 
print("hello,world!")  #this is a comment.


#this is a comment.
#write with the colour text.
print("hi_srihaas") 

#variables
x= 5 # an integer 
y= 9 # an string

print(x*10) 
print(y*2)


b,y,l= "srihaas","suryaansh","venkakesh"
print(b)
print(y)
print(l)

a=b=c="srihaas"
print(a)
print(b)
print(c)

family =("venkatesh","anjali","jaya","suryaansh","srihaas")
a,b,c,d,e=family
print(a)
print(b)
print(c)
print(d)
print(e)

a = "surya is a good boy"
print(a)    


s="venkatesh"
k="is"
v="good_dad"
print(s,k,v)

s="venkatesh "
k="is "
v="good_dad"
print(s+k+v)

g=11
m=9
print(g + m)

m="awesome" 
def myfunc(): 
   print("indus valley civilisation is" + m)
   
myfunc() 

s ="good"
def myfunc():
   s="awesome"
   print("my mother is  " +  s)
   
myfunc()

print("my mother is " + s)

b =9
print(type(b))

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#convext from int to a float:
d= float (5)
#convert from float to int:
s=int(2.9)
#convert from int to complex:
z=complex (23)

print(d)
print(s)    
print(z)

print(type(d))
print(type(s))
print(type(z))

import random

print(random.randrange(1, 10))
 
n = int(1) #int will be 1
m = int(5.8) #int will be 5
l = int ("7") # int will be 7
  
print(n)
print(m)
print(l)
 
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

for x in "srihaas":
  print(x) 
  
a="srihaas"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

n = "srihaas"# name of a person 
print(n[3:7])

d ="suryaansh"
print(d[-7:])

r ="venkatesh" 
print(r.upper())

a = "Hello, World!"
print(a.lower())

g ="Jaya"
print(g.strip()) # retens Jaya again 

k="octopus"
print(k.replace("o","a"))

a = "Hello, World!"
print(a.lower())

a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a +" "+ b
print(c)

age = 11
txt = f"my name is srihaas,I am {age} old"
print(txt)

price =100
txt = f"the price of an item is ${price}"
print(txt)

price= 29
txt=f"the cost of an item is ${price:.2f}" 
print(txt)     

txt =" a cost of an item is{2025+2025} rupees"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 334

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a(with the numbers)")
  
print(bool("Hello"))
print(bool(15))

p = "srisuya"
h = 89

print(bool(p))
print(bool(h))

print(bool("djrm"))
print(bool(47369))
print(bool(["watermelon","apple","banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


  
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True

print(myFunction())

d = 458479379
print(isinstance(d,int))

g = "good"
print(isinstance(g,int))




