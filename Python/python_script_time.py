#! /usr/bin/python3.8
print("Ievadiet skaitli: ")
# a=2**2000000

#a=int( input() )

#if (type(a) == int): 
#	print("a**10000000")
#	print("complete")

#if (a == 5): 
#	print(a**100)

#if isinstance(a, int): #works
#	print(a**100)
#	print("complete")

paziime = False
#Šie trīs ir derīgi varianti
#while paziime==False: #(while paziime is False)
#while paziime!= True: #(while paziime not True)
while not paziime:
    try:
        a = int( input() )
        paziime = True
    except:
        print("Diemžēl, cienījamais lietotāj, to, kas ievdīts, nevar",\
"pārveidot par vesela tipa skaitli :-( ")
        print("Lūdzu ievadiet skaitli vēlreiz")

if (a == 5):
    print(a**100)
    print("Aprēķins ir gatavs")
print("Šis teksts atrodas ārpus darbību bloka - pierakstīts bez",\
      "atstarpēm priekšā, tāpēc tas parādīsies jebkurā gadījumā")

#paziime = True
#while paziime:
#    try:
#        a = int(input())
#        paziime = False
#    except:
#        print("Diemžēl, cienījamais lietotāj, to, kas ievdīts, nevar",\
#"pārveidot par vesela tipa skaitli :-( ")
#        print("Lūdzu ievadiet skaitli vēlreiz")

