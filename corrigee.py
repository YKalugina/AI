#1-2----
print("Solution 1-2")
def carree(a):
 return(a**2)

def somme(a,b):
 return a+b

def produit(a,b):
 return a*b

def devision(a,b):
 return a/b

a=1
b=2
print ("a=",a,"b=",b)
print(carree(somme(a,b)),carree(produit(a,b)),carree(devision(a,b)))

#3-4-------
print("Solution 3-4")
def cub(a):
    return a*a*a

print(cub(somme(a,b)),cub(produit(a,b)),cub(devision(a,b)))

#5-----
print("Solution 5!")




def somme(n):
    if (n==1):
        return 1
    elif (n==0):
        return 0
    else:
        return n+somme(n-2)

print(somme(10))
print(somme(20))
print(somme(7))
#6----


print("Solution 6")
list1=[1,2,1]
list2=[3,4,1]

if len(list1)==len(list2):
    for i in range(0,len(list1)):
        t=(list1[i]*list2[i])
        print(t)
else:
    print("ERROR! len(list1) not equal to len(list2)")
#7-----
print("Solution 7")

print(list(range(8,88,8)))
