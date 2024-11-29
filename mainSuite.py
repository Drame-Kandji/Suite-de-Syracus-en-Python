from BibliothequeSuite import collatz, syracuse, temps_parcouru, altitude

n=int(input("Donner la valeur de x :"))

print("Suite de Syracuse pour", n)
syracuse(n,False)
print("Temps parcouru :", temps_parcouru(n))
print("Altitude maximale :", altitude(n))
