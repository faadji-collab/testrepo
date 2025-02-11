# Exercice  cours 7 :

#def print_cadre(message) :
#     ligne = '='*len(message*2)
#     print(f"|{message}|")
#     print(ligne)

# print_cadre("message")


# def bar(l: list):    
#     l.append(1)
#     l.sort()
#     print(l)

# my_list = [5, 2, 4]
# bar(my_list)
# print(my_list)

# Exercice Chapitre 7 :

#n = int(input("saisir n :"))

# def test_premier(m):
#     for i in range(2,(m+1)**0,5) :
#         if i % m == 0 :
#             return False
#         return True

# def somme_des_nombres(n) :
#     somme = compteur = 0
#     nombre= 2
#     while  compteur < n :
#         if test_premier(nombre) :
#             compteur += 1
#             somme += nombre
#         nombre += 1
#     print(somme)
#     return somme

# Exercice 2 :

#groupe1 = {
#"Marc": 10,
#"John": 11,
#"Serge": 12,
#"Alice": 13,
#"Martine": 1
#}

#groupe2 = {
#"Serge": 10,
#"Alex": 11,
#"Kacem": 12,
#"Bob": 13,
#"John": 14
#}

#groupe3 = {
#"Olson": 10,
#"Martine": 11,
#"Alice": 12,
#"Charlie": 13,
#"Eve": 14
#}

#def trouver_cles_communes(ensemble1,ensemble2) :
    #ensemble1 = set(groupe1.keys())
    #ensemble2 = set(groupe2.keys())
    #return list(ensemble1.intersection(ensemble2))

#print(trouver_cles_communes(groupe1,groupe2))

# Exercice 3 :

#from random import randint
#n = int(input("Saisir le nombre de groupe n :"))
#k = int(input("Saisir le nombre de choffres consectifs k :"))

#def creer_groupements(n,k) :
    #liste = [[i for i in range(k * j + 1, 5 * (j + 1) + 1)] for j in range(n)]
    #return liste

#print(creer_groupements(n,k))

# Exercice 4 :

import string
alphabet = string.ascii_lowercase

phrase = input("Veuiller indiquer votre phrase: ")
lettres = set([char.lower() for char in phrase if char.isalpha()])
ensemble_alphabet = set(alphabet)
print(list(ensemble_alphabet.difference(lettres)))