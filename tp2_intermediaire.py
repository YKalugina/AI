#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python de Base
## Octobre 8, 2020
###################YULIA KALUGINA###########################

# In[ ]:


#--- Exemple
# Ecrire du code pour demander a l utilisateur s il veut continuer ou sortir
# Solution 1
#continuer = "o"
#while continuer == "o":
#    print("On continue !")
#    continuer = input("Voulez-vous continuer ? o/n ")

# Solution 2
#continuer = "o"
#while continuer == "o":
#    print("On continue !")
#    resultat = input("Voulez-vous continuer ? o/n ")
#    if resultat != "o":
#        break

# Solution 3 avec Python 3.8 uniquement
#while (continuer : = "o") == "o":
#    print("On continue !")
#    if (resultat := input("Voulez-vous continuer ? o/n ")) != "o":
#        break


# In[100]:


##-- Exemple

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste
##(["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")
print(liste)

# Supprimer le dernier element de la liste sans utiliser d index ni
liste.remove(liste[-1])
print(liste)

liste.pop()
print(liste)
# In[94]:

print('--------')
#Exemple
#1 mettre en majuscule les elements de la liste?
my_pets = ['sisi', 'bibi', 'titi', 'carla']

#solution
def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

#1 Ecrire une fonctin pour inverser les elements de la liste?
p=my_pets
p.reverse()
print(p)
# In[ ]:


### Modules

### le fichier du module doit exister dans le meme repertoire que le script (programme)

## Explicit is better than Implicit ( prefixer toujours le nom du module)
## import modulename
## modulename.function/modulename.class

## --------------
## Ne pas utiliser
# ------------------
## 1) le nom du module : ne pas donner un nom de module existant

## 2)
## from modulename import function or class
## function(p)

## 3) from modulename import *
## importe toutes les variables/fonctions/classes directement dans votre script principal

## 4) __name__ : variable magique
## __name__ ==


# In[ ]:
print('--------')

###-- pratique

list1, list2 = [ 'xyz', 'zara', 'abc'], [456, 700, 200]
##-- Écrire une fonction:
## 1) affiche les elements des deux listes
## 2) affiche la somme des elements de chaque liste
## 3) affiche le maximum valeur contenu dans chaque liste
def aff_list(item):
    for i in item:
        print(i)

aff_list(list1)
aff_list(list2)
from functools import reduce
result1=reduce(lambda x,y:x+y, list1)
print(result1)
result2=reduce(lambda x,y:x+y, list2)
print(result2)


print("max list 1: "+str(max(list1)))
# In[ ]:


## -- Programmation Fonctionnelle : Functions (map,filter, zip, reduce)


# In[83]:
print('--------')

##--- Pratique
## Simplifier le code ci-dessous en utilisant la foncion map()
my_list=[1,2,3]
def mult_by_p(item):
    new_list=[]
    for i in item:
        new_list.append(i*2)
    return new_list
print(mult_by_p(my_list))




#solution
my_list=[1,2,3]
def mult_by_p_map(item):
    return item*2
print(list(map(mult_by_p_map,my_list)))

#f=lambda s:s.upper()

# In[ ]:
print('--------')

## --- Pratique
## Simplifier le code ci-dessous en utilisant la foncion map()
def capitalize(string):
    return string.upper()

## solution
print(list(map(capitalize, my_pets)))


# In[91]:

print('--------')
##--- Exemple

# 1) Filtrer les scores superieures a 50 en utilisant la fonction filter ?
# 2) Filtrer les scores superieures entre 50 a 90 en utilisant la fonction filter ?
# 3) Filtrer les scores superieures entre 100 en utilisant la fonction filter et afficher un message si le resultat est vide?

## solution 1)
scores = [73, 20, 65, 19, 76, 100, 88]
def is_smart_student(score):
    return score > 50

def de50a90(score):
    return score >50 and score < 90

def plus100(score):
    return score >100


print(list(filter(is_smart_student, scores)))
print(list(filter(de50a90,scores)))
print(list(filter(plus100,scores)))



# In[32]:

print('--------')
##--- Pratique
## Simplifier le code ci-dessous en utilisant la foncion filter()
my_list=[1,2,3,9,39]

def verif_si_dev_3(item):
    res=[]
    for i in item:
        if i%3==0:
           res.append(i)
    return res

res=verif_si_dev_3(my_list)
print(res)

## solution
def verif_si_dev_3(item):
    return item %3 ==0
print(list(filter(verif_si_dev_3,my_list)))


# In[87]:


##--- Exemple
print('--------')
# Rassembler deux listes dans une liste de tuples, et trier les nombres par ordre croissant puis par ordre decroissant
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
p=my_strings+sorted(my_numbers)
print(p)
# Modifier le code pour rassembler n listes ?
print(sorted(my_strings,key = len))
print(sorted(my_numbers,reverse=False))
print(sorted(my_numbers,reverse=True))
## indication : sorted() fonction pour trier
## sorted(iterable, key, reverse=False)
## sorted(Liste ou Set ou Tuple ou Dictionnaire, reverse = True) ou sorted(Liste, reverse = False)
## sorted(Liste, key = len))


##nom_list.sort(key, reverse=False)
# sort ne retourne pas de resultat,

## solution
print(list(zip(my_strings, sorted(my_numbers))))


# In[86]:

print('--------')
##--- Pratique
## Creer une liste de tuple en utilisant la fonction zip pour les trois listes suivantes
list_numero_tel =['514-234-3423','514-234-1000', '514-100-1020','650-234-1000']
list_nom_personnes =['spider-man','batman','joker']
list_pays=['Montreal','Boston', 'New-york']

## solution
print(list(zip(list_numero_tel, list_nom_personnes,list_pays)))


# In[82]:

print('--------')
import functools  ## module de la programmation fonctionnelle
print(dir(functools))##( pour voir ce qu il ya dans le module)

##--- Exemple
## utiliser la fonction reduce pour donner le nombre d'heures totales travaillees pendant toute la semaine
## solution
from functools import reduce
travail_chaque_jour_semaine=[8, 5, 6,10, 14]
def func(accum,item):
    print(accum, item)
    return accum + item
# ExplicationL: reduce(function, sequence, valeur_initial)
print((reduce(func,travail_chaque_jour_semaine, 0)))


# In[98]:

print('--------')
##--- Pratique
## utiliser la fonction reduce pour donner la quantite de produits consommer pendant les mois de janvier et fevrier?
## sachant que pour les autres mois de l annee la quantite est de 100kg
from functools import reduce
qtes_produits_mois_janvier = [73, 20, 65, 19, 76, 100, 88]
qtes_produits_mois_fevrier= [50,46,32,20,10]

## solution
#def accumulator(acc, item):
#    print(acc, item)
#    return acc + item
#print(reduce(accumulator, (qtes_produits_mois_janvier + qtes_produits_mois_fevrier), 100))

print((reduce(func,qtes_produits_mois_janvier+qtes_produits_mois_fevrier,100)))
# In[ ]:
print('--------')

### --- Pratique
## Enonce: le code suivant a un probleme. ameliorer le pour indiquer que le calcul ne s est pas fait sur tous les elements
##de la liste
## indication avec if elif else
a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

def func(x,y,z):
    if len(y)==len(x) and len(z)==len(x):
        print(list(map(lambda x, y, z : 2.5*x + 2*y - z,x,y,z))) 
    else:
        print("Verifier la longuer des listes, elle doit etre la meme pour les 3 listes")
    
func(a,b,c)
# In[ ]:


###  Expression Lambda


# In[53]:
print('--------')

##--- Exemple 1---
##--- Changer la fonction suivante en expression lambda
def sayHello(message):
    print(message)
    
sayHello("hello_1_avec_fonction")

#solution:

sayHello1= lambda m:print(m)
sayHello1("hello_2_avec_expression_lambda")


# In[57]:

print('--------')
##--- Exemple 2---
##--- Changer la fonction suivante en expression lambda
def sommer(p1,p2):
     return p1+p2
 
print("avec fonction: "+str(sommer(23,24)))
## solution


somme =lambda p1,p2: p1+p2
print("avec expression lambda: "+str(somme(23,24)))


# In[74]:


##--- Exemple 3:
# le module random permet de generer des nombres aleatoire
# randint(a,b): renvoie un entier choisi aleatoirement dans [a,b] avec randrange(a, b+1)
# random():renvoie un flottant choisi dans l'intervalle [0;1]
# uniform :renvoie un flottant choisi dans l'intervalle[a;b]

import random
print('---------')
print("exemple random(): "+str(random.random()))
print("exemple uniform(): "+str(random.uniform(2.5, 10.0)))
print('---------')
#--Écrire une lambda expression qui génère un nombre aléatoire (soit 4, 5,6)

nbre_aleatoire =lambda a,b:random.randint(a,b)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))
random.seed(a=None, version=2)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))
random.seed(a=None, version=1)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))


##----------#--Écrire une lambda expression qui génère une probabilite de valeurs entre 20% et 80%?
count=0
n=101
for i in range(0,n):
     a=random.random()
     if a>=0.2 and a<=0.8:
         count+=1
     else:
         pass
print(count,n)


#print(map(lambda x,y: random.uniform(x,y), range(1,101)))


l=lambda x,y: x/y *100

print("probabilite des valuers 0.2-0.8 est "+str( l(count,n))+ " %")     
# In[ ]:


### ---- Pratique
## Ecrire un code qui genere deux nombres aleatoires et indique a l utilisateur lequel
## des deux nombres est le plus grand

nbre_aleatoire =lambda a,b:random.randint(a,b)
l=[str(nbre_aleatoire(0,10)),str(nbre_aleatoire(0,10))]
print(l)
print("le plus grand nombre est " +str(reduce(lambda x,y: x if x>y else y,l)))
# In[65]:


### ---- Pratique
#--Écrire une lambda expression qui affiche la plus grande valeur de deux nombres?
func=lambda x,y:x if x>y else y
a=4
b=2    
print(func(a,b))   

#--Écrire une lambda expression qui affiche la plus grande valeur de trois nombres?
a=2
b=3
c=9

l=[a,b,c]
print(str(reduce(func,l)))

#--Écrire une lambda expression qui permet de classer deux nombres par ordre croissant?
func=lambda x,y: print(x,y) if x<y else print(y,x)

func(9,8)
#--Écrire une lambda expression qui permet de calculer la valeur absolue d’un parametre?
a=-10
func=lambda x: abs(x)
print(func(a))
 
#-- Écrire une lambda expression qui permet de mettre en majuscule les elements de la liste?

func=lambda string:string.upper()

l=['abc','def']

print(list(map(func,l)))

#-- Écrire une lambda expression qui permet d inverser les elements de la liste?
func=lambda lst:sorted(lst,reverse=True)
l=[1,2,3,4,5]
print(list(func(l)))

## -----------
#--  Écrire une lambda expression qui permet de calculer la somme des n premiers nombres entiers
#--  positifs  ( proposer deux versions ):
#--  version 1:  Somme = N + (N-1) + (N-2) + …+ 2+1
func=lambda N:1 if N==1 else N+func(N-1) 
N=4
print('version1 somme = '+str(func(N)))
#--  version 2:  Somme = 1+2+…+(N-1)+N
func=lambda x,y:x+y
N=4
print('version2 somme = '+str(reduce(func,range(0,N+1))))
## -----------
#-- Écrire une lambda expression permet d’afficher les n termes de nombres
#-- naturels impairs et leur somme. Ce programme aura pour entrées
#--(inputs : le nombre de termes)
N=int(input('le nombre de termes a afficher, N:'))
print(N)

def fun(a):
    s=[]
    for i in range(1,a+1):
       s.append(1+(i-1)*2)
    print(s)
    return reduce(lambda x,y:x+y, s)    
    

print(fun(N))


# In[ ]:


###  Expression Lambda avec les fonctions map, filter, zip and reduce


# In[77]:


## --- Pratique
## utiliser l expression lambda et la fonction reduce pour donner le nombre d'heures totales
## travaillees pendant toute la semaine

## -- Simplifier le code ci-dessous
travail_chaque_jour_semaine=[8, 5, 6,10, 14]

print("solution avec fonction")
def func(accum,item):
    return accum + item
#reduce(function, sequence, valeur_initial)
print((reduce(func,travail_chaque_jour_semaine, 0)))

## solution 1
print("solution 1 avec lambda expression")
func =lambda accum, item: accum+item
print((reduce(func,travail_chaque_jour_semaine, 0)))

## solution 2
print("solution 2 avec lambda expression")
print((reduce(lambda accum, item: accum+item,travail_chaque_jour_semaine, 0)))


# In[89]:


## --- Pratique
## Simplifier le code suivant avec lambda expression. Proposer un menu a l utilisateur. s il choisit sin, appeler la fonction sin
##   ect...
from math import sin, cos, tan, pi
def map_functions(x, functions):
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))




family_of_functions = [sin, cos, tan]
f=int(input("fonction a choisir (0-sin, 1-cos, 2-tan): "))
func=lambda x,y: y(x)
print(str(func(pi,family_of_functions[f])))

# In[ ]:


##--- Pratique
## Simpifier ce code en utilisant l expression lambda
from functools import reduce
qtes_produits_mois_janvier = [73, 20, 65, 19, 76, 100, 88]
qtes_produits_mois_fevrier= [50,46,32,20,10]

## solution
#def accumulator(acc, item):
#    print(acc, item)
#    return acc + item
#print(reduce(accumulator, (qtes_produits_mois_janvier + qtes_produits_mois_fevrier), 100))

func=lambda x,y:x+y
print(reduce(func,(qtes_produits_mois_janvier+qtes_produits_mois_fevrier),100))
# In[ ]:


# Python  OO
## Octobre 8, 2020


# In[ ]:

#%%
##--- Exemple

## Corriger le code ci-dessous
class Chien:
    def __init__(self, race):
        self.race = race

    @property
    def taille(self):
        return 100

class Chihuahua(Chien):
    def __init__(self, nom,race):
        self.nom = nom
        Chien.__init__(self,race)
        
chien1 = Chihuahua('Lily','chihuahua')
print(chien1.nom)
print(chien1.race)
#%%
# In[ ]:


## ---- Exemple
## Que remarquez vous dans ce code?

class this_is_class:
    def show(in_place_of_self):
        print("Collecte et stockage de donnees ")

object = this_is_class()
## il n'y a pas de constructeur


# In[ ]:


## ---- Exemple

#Programme avec quatre classes différentes
#Personne
#Enseignant
#Chercheur
#Étudiant

## creer un sequelette d'heritage pour ces quates classes ( heritage simple, heritage multiple, multi-niveaux)
#%%
class Personne:
    def __init__(self, nom):
            self.nom = nom

class Chercheur(Personne):
    def __init__(self, tr):
        self.tr=profession
        Personne.__init__(self,nom)        


class Etudiant(Personne):
    def __init__(self, numero_etu,nom):
            self.numero_etu=numero_etu
            Personne.__init__(self,nom)            
            
class Enseignant(Chercheur, Etudiant):
    def __init__(self, cours):
            self.cours=cours
            Chercheur.__init__(self,tr)
            Etudiant.__init__(self,numero_etu,nom)
            
#     Personne
#chercheur   Etudiant (multiple)
#     Enseignant


class Employe(Personne):
    def __init__(self, prof,nom):
        self.prof=prof
        Personne.__init__(self,nom)
        
class Professeur(Employe):
    def __init__(self, cours,prof,nom):
            self.cours=cours
            Employe.__init__(self, prof,nom)
            Personne.__init__(self,nom)
        
etud1=Etudiant(6171034,"Yulia Kalugina")
etud2=Etudiant(6171035,"Autre Personne")

emp1=Employe('Professor',"Hassina Bounif")
emp2=Employe('Assistant',"XXX Personne")

print("DA: "+str( etud1.numero_etu),"      Nom Etudiant: "+str(etud1.nom))      
print("DA: "+str( etud2.numero_etu),"      Nom Etudiant: "+str(etud2.nom))      

print("Position: "+str( emp1.prof),"      Nom Employe: "+str(emp1.nom))      
print("Position: "+str( emp2.prof),"      Nom Employe: "+str(emp2.nom))  

prof1=Professeur('Stoccage de donnees','Professeur',"Hassina Bounif")
prof2=Professeur('SQL lab','Assistant',"XXX Personne")

print("Cours: "+str( prof1.cours),"      Position : "+str(prof1.prof),"      Nom : "+str(prof1.nom))      
print("Cours: "+str( prof2.cours),"      Position : "+str(prof2.prof),"      Nom : "+str(prof2.nom))
 

#             Personne
#     Etudiant        Employe
#                    Proffeseur
#%%
 
# In[ ]:


##--- Pratique
# La classe Etudiant hérite de la classe Personne.
# La classe Professeur hérite de la classe Employé et la classe Employé hérite de la classe Personne.
# Un Etudiant est une Personne.
# Un Professeur est un Employé et un Employé est une Personne.
# Travail à faire 
# Ecrire du code pour les classes
# Chaque classe doit contenir un constructeur d'initialisation.
# Creer : 1) deux objets étudiants 2) deux objets employés 3) deux objets professeurs.
# 4) afficher les informations de chaque personne. 
