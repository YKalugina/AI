#!/usr/bin/env python
# coding: utf-8
############cherchez #pratique 1"##########
# In[16]:

import numpy as np
array_de_liste =np.array([1,3,2,4])
print(array_de_liste)

import numpy as np
array_range=np.arange(0,10)
print(array_range)

import numpy as np
vec =np.eye(5)
print(vec)


import numpy as np
vec=np.ones(10)
print(vec)

import numpy as np
vec=np.ones((4,3))
print(vec)

#distribution linear from 0 to 9 uniform, 10 otrezkov)
import numpy as np
array_linspace=np.linspace(0,9,10)
print(array_linspace)

import numpy as np
vec=np.full(10,5.0)
print(vec)

import numpy as np
vec=np.zeros(10)
print(vec)

import numpy as np
vec=np.zeros((5,4))
print(vec)


import numpy as np
print(np.random.randn(4) )                  # loi normale centrée réduite
np.random.random(size=(2,2))  # loi uniforme entre 0 et 1
print(np.random.random(size=(2,2)))


rand_gen=np.random.RandomState(seed=12345)  #objet avec une graine fixée
rand_gen2=np.random.RandomState(seed=12345)
print(rand_gen)
print(rand_gen2)


np.random.seed(100)
arr=np.random.randint(0,100,10)
print(arr)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmax())
print(arr.argmin())
arr.reshape(2,5)
print(arr.reshape(2,5))

nb=np.random.randint(0,10)
print(nb)

arr=np.random.randint(0,30,(3,2))
print(arr)


v =np.array([1,2])
print(v.shape)

mat=np.arange(0,20).reshape(2,10)
print(mat)

print(mat[0,1])
print(mat[:,0])
print(mat[1,:])
print(mat[1:2,1:4])


import numpy as np
fichier = np.genfromtxt("data_numpy.csv", delimiter=",")
print(fichier)


import numpy as np
fichier = np.genfromtxt("data_numpy.csv", delimiter=",", dtype="U75", skip_header=1)
print(fichier)

import numpy as np
numbers=np.array([1, 2, 3, 4])
print(numbers.dtype)  

import pandas as pd
frame_list=pd.DataFrame([[2,4,6,7],[3,5,5,9]]) ## deux lignes et quatre colonnes 
print(frame_list.head(1))
print(frame_list.tail(1))

import pandas as pd
##------ réseaux sociaux, budgets, audiences
dico1={"RS" :["Facebook","Twitter","Instagram","Linkedin","Snapchat"],  
            "Budget" :[100,50,20,100,50], "Audience" :[1000,300,400,50,200]}
frame_dico=pd.DataFrame(dico1)
print(frame_dico.head(4))

frame_csv=pd.read_csv("salaires.csv")
print(frame_csv)
frame_csv.to_csv("mon.csv")
frame_csv.describe()

salaire=frame_csv['salaire']
print(salaire)

info=frame_csv[['nom','salaire']]
print(info)

max=frame_csv['salaire'].max()
print(max)

print(frame_csv['salaire']>1000)



#ipd =pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=10')
#print(ipd[['state', 'title', 'updated_at']].head())



import pandas as pd
data ={'state':['Ohio','ohio','Ohio','Nevada','Nevada'], 'year':[2000,2001,2002,2001,2002], 'pop':[1.5,1.7,3.6,2.4,2.9]}

frame2= pd.DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four','five'])

print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)

    
    
from pandas import Series
obj = Series([4,7,-5,3])
print(obj.values)
print(obj.index)

from pandas import Series
import numpy as np
obj2=Series([4,7,-5,3], index=['d','b','a','c'])
print(obj2)
print(obj2.index)
print(obj2['a'])
print(obj2['d'])
print(obj2[['c','a','d']])
print(obj2[obj2>0])
print(obj2*2)
print(np.exp(obj2))

from pandas import Series
ma_serie1= Series(np.random.randn(5), index=["A","B","C","D","E"])
print(ma_serie1)

from pandas import Series
ma_serie2 = Series([8,70,320, 1200], index=["Suisse","France","USA","Chine"])
print(ma_serie2)

from pandas import Series
ma_serie3= Series({"Suisse" :8,"France" :70,"USA" :320,"Chine" :1200})
print(ma_serie3)

from pandas import Series
ma_serie2 = Series([8,70,320, 1200], index=["Suisse","France","USA","Chine"])
print(ma_serie2[:3])

print(ma_serie2[["Suisse","France","USA"]])

print(ma_serie2[ma_serie2>50])

print(ma_serie2[(ma_serie2>500)|(ma_serie2<50)])

from pandas import Series
ma_serie5= Series(np.random.randn(5), index=["A","B","C","D","E"])
ma_serie4= Series(np.random.randn(4), index=["A","B","C","F"])
print(ma_serie5+ma_serie4)

from pandas import Series
ma_serie3= Series(np.random.randn(5), index=["A","B","C","D","E"])
ma_serie4=Series(np.random.randn(4), index=["A","B","C","F"])
ma_serie3.add(ma_serie4, fill_value=0)

import requests
user_agent_url = 'https://www.w3schools.com/xml/cd_catalog.xml'
xml_data = requests.get(user_agent_url).content 
#print(xml_data)


####DANS JUPITER#####
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#%matplotlib inline
#x=np.arange(0,10)
#y=x**2
#plt.plot(x,y)

###########################################################TP##############


## -- Numpy et Pandas ( october 20/10/2020)

## --- pratique 1:
## construire un vecteur avec [3,4,5,6]
## assigner resultat a la variable vector
## indice : np.array([3,4,5,6])

import numpy as np
vec=np.array([3,4,5,6])
print(vec)


## --- pratique 2:
## construire une matrice  depuis la liste de listes [[2,5,15],[20,50,50],[34,99,45]]
## Afficher les resultats
## assigner le resultat a la variable matrix 
import numpy as np
matrix=np.array([[2,5,15],[20,50,50],[34,99,45]])
print(matrix)



## --- pratique 3:
## Donner la taille du tableau [1,2,3,4]suivant puis changer sa taille
## Afficher les resultats
## indication : shape, reshape

import numpy as np
vec=np.array([1,2,3,4])
print(vec.shape)
print(vec.reshape(2,2))



## --- pratique 4:
## Donner la taille de la matrice [[5,10,15], [20,25,30], [40,45,50]] suivant puis changer sa taille 
## Afficher les resultats
## indication : shape, reshape


import numpy as np
mat=np.array([[5,10,15], [20,25,30], [40,45,50]])
print(mat.shape)
print(mat.reshape(3,3))


## --- pratique 5:
## Executer le code suivant ( en specifiant le path du fichier)
import numpy as np
fichier = np.genfromtxt("data_numpy.csv", delimiter=",")
print(type(fichier))
## Utiliser les fonctions type() et print() pour afficher le type de fichier 




## --- pratique 6:
## creer un vecteur random ayant 4 valeurs
## creer une matrice random de taille (2X2)

import numpy as np
print(np.random.randn(4)) 
print(np.random.random(size=(2,2)))



##solution
#import numpy as np
#print(np.random.randn(4)) 
#print(np.random.random(size=(2,2)))


## --- pratique 7:
# creer un vecteur depuis la liste[1, 2, 3, 4] et afficher son type
##solution
import numpy as np
numbers=np.array([1, 2, 3, 4])
print(numbers.dtype) 


## --- pratique 8
## Afficher toutes les lignes des 2 premières colonnes de data_numpy à la variable first_two_columns.
# Afficher les 10 premières lignes de la première colonne de data_numpy à la variable first_ten_years.
# Afficher les 10 premières lignes de toutes les colonnes de data_numpy à la variable first_ten_rows.
# Afficher les 20 premières lignes des colonnes d'indice 1 et 2 de data_numpy à la variable first_twenty_regions.
#%%
import numpy as np
fichier = np.genfromtxt("data_numpy.csv", delimiter=",", dtype="U75", skip_header=1)
first_two_columns = fichier[:,0:2]
print(first_two_columns)
first_ten_years=fichier[0:10,0]
print(first_ten_years)
first_ten_rows=fichier[0:10,]
print(first_ten_rows)
first_twenty_regions=fichier[0:20,1:3]
print(first_twenty_regions)
#%%
## solution
#first_two_columns = data_numpy[:,0:2]
#first_ten_years = data_numpy[0:10,0]
#first_ten_rows = data_numpyl[0:10,:]
#first_twenty_regions= data_numpy[0:20,1:3]


## --- pratique 9
#Importer la librairie pandas.
#Utiliser la fonction pandas.read_csv() pour lire le fichier "food_info.csv" 
#Utiliser les fonctions type() et print() pour afficher le type de food_info 
#solution
#import pandas as pd
#food_info = pd.read_csv("food_info.csv")
#print(type(food_info))

#%%
import pandas as pd
fichier=pd.read_csv("food_info.csv")
print(type(fichier))



##--- pratique 10
#Afficher la 1000e ligne du dataframe food_info 
#solution
#row_1000 = food_info.loc[999]
#print(row_1000)

print(fichier.loc[999])#pas bien compris


##--- pratique 11
#Assigner la colonne "protein_(g)" à la variable protein.
#Assigner la colonne "Cholestrl_(mg)" à la variable cholesterol.
#Afficher les résultats.

protein=fichier["Protein_(g)"]
print(protein)
cholesterol=fichier["Cholestrl_(mg)"]
print(cholesterol)
## solution
#protein = food_info["Protein_(g)"]
#cholesterol = food_info["Cholestrl_(mg)"]


##--- pratique 12
#Sélectionner les colonnes 'Shrt__Desc', 'Selenium_(mcg)' et 'Thiamin_(mg)' 
#et assigner le dataframe résultant à la variable selenium_thiamin.
#Afficher le résultat.

selenium_thiamin=fichier[['Shrt_Desc', 'Selenium_(mcg)', 'Thiamin_(mg)']]
print(selenium_thiamin)


## solution
#selenium_thiamin = food_info[['Shrt_Desc', 'Selenium_(mcg)', 'Thiamin_(mg)']]
#print(selenium_thiamin)

## --- pratique 13
# 1) Sélectionner et afficher seulement les colonnes qui utilisent comme unité de mesure les grammes 
#(c'est à dire qui se terminent par "(g)"). Pour cela:
#Utiliser l'attribut columns pour retourner le nom des colonnes du dataframe food_info 
#et convertir en liste utilisant la méthode tolist()


## 2) Créer une nouvelle liste qu'on nommera gram__columns, contenant seulement les colonnes se terminant 
##  par "(g)". Indice: la méthode endswith() retourne True si l'objet sur lequel on l'applique se termine
## par l'élément entre parenthèses. ex: total_(g).endswith("(g)") retourne True. Une boucle for est fortement conseillé pour parcourir tous les noms de colonne.

## 3) Sélectionner les colonnes de gram_columns pour le dataframe food_info et assigner le dataframe résultat 
## à la variable gram_df 

## 4) Afficher les 3 premières valeurs de ce dataframe gram_df

## solution

col_names = fichier.columns.tolist()
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
        
gram_df = fichier[gram_columns]

gram_df.head(3)

#%%

##--- pratique 14
#Lire le dataset 'fandango_score_comparison' dans le dataframe fandango.
#Retourner un DataFrame contenant seulement la première et la dernière ligne et assigner le résultat à la variable first_last.
#Afficher le résultat.

import pandas as pd
fandango=pd.read_csv('fandango_score_comparison.csv')
first=0
last=fandango.shape[0]-1
print(last)
first_last=fandango.iloc[[first,last]]
print(first_last)
###--- solution
#import pandas as pd
#fandango = pd.read_csv('fandango_score_comparison.csv')
#first = 0
#last = fandango.shape[0] - 1
#first_last = fandango.iloc[[first,last]]
#first_last


##--- pratique 15
#Lire le fichier "fandango_score_comparison.csv" dans un dataframe qu'on nommera fandango.
#Afficher les 2 premières lignes de fandango.
import pandas as pd
fandango=pd.read_csv('fandango_score_comparison.csv')
print(fandango.head(2))
## solution
##import pandas as pd
##fandango = pd.read_csv('fandango_score_comparison.csv')
##fandango.head(2)

##---- pratique 16
##Sélectionner la colonne "FILM" et assigner la à la variable series_film puis afficher les 5 premières valeurs.
#Faire de même avec la colonne "RottenTomatoes" et assigner la à la variable series_rt puis afficher les 5 premières valeurs.
series_film=fandango['FILM']
print(series_film.head(5))
print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
print(series_rt.head(5))
print(series_rt[0:5])
## solution
##series_film = fandango['FILM']
##print(series_film[0:5])
##series_rt = fandango['RottenTomatoes']
##print(series_rt[0:5])


###--- pratique 17
##Créer un objet Series qu'on nommera series_custom qui aura 
##un index de chaines de caractères (basé sur le nom des films 
##qu'on assignera à la variable film_names) et contiendra toutes 
##les notes RottenTomatoes de series_rt qu'on assignera à la variable rt_scores.

## solution
# importer l'objet Series depuis pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(rt_scores, index=film_names)
print(series_custom)


###--- pratique 18
##Créer la liste original_index contenant l'index actuel à partir de l'attribut index.
##Trier cet index en utilisant la méthode sorted() et assigner le résultat à la variable sorted_index.
##Puis appliquer la méthode reindex() à notre Series custom_series afin de réindexer selon l'index de sorted_index.
##Stocker le résultat dans la variable sorted_by_index.
##Afficher le résultat.

## solution
original_index = series_custom.index
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)


###--- pratique 19
##Trier la Series series_custom par index en utilisant la méthode sort_index() et assigner le résultat à la variable sc2.
##Trier la Series series_custom par valeurs et assigner le résultat à la variable sc3.
##Afficher les 10 premières valeurs de sc2 et sc3.

## solution
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10])
print(sc3[0:10])
#%%
###--- pratique 20
##Assigner à la variable criteria_one le critère des valeurs de series_custom supérieurs à 50.
##Assigner à la variable criteria_two le critère des valeurs de series_custom inférieurs à 75.
##Retourner un nouvel objet Series filtré qu'on nommera both_criteria qui contient seulement les valeurs pour lesquelles les 2 critères sont vrais.
##Afficher ce dernier résultat.
criteria_one=series_custom.values>50
print(criteria_one)

##-- solution
criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(both_criteria)



# In[ ]:




