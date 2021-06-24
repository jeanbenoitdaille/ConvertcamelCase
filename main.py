phrase = "Phrase en camel case"
phrase_split = phrase.split()
     
resultat = [phrase_split.pop(0).lower()]
     
for mot in phrase_split:
        resultat.append(mot.capitalize())
     
resultat_formate = "".join(resultat)
     
print(resultat_formate)