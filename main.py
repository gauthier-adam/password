import re   #j'ai regarder un tuto youtube pour cette exercice, le tuto dit que je dois importer "re" mais je ne sais pas a quoi cela corespond 

def verifier_MDP(MDP):
# je mets les conditions demmendé dans l'exercice 
    if len(MDP) < 8:
        return False
    
    if not any(c.isupper() for c in MDP):
        return False
    
    if not any(c.islower() for c in MDP):
        return False
    
    if not any(c.isdigit() for c in MDP):
        return False
    
    caracteres_speciaux = r'[!@#$%^&*]'
    if not re.search(caracteres_speciaux, MDP):
        return False
    
    return True  

def demander_MDP():
    while True:
        #j'utilise "input" pour pouvoir entrer une chaine de carractère dans le terminal
        MDP = input("saisissez un mot de passe : ")
        if verifier_MDP(MDP):
            print("Mot de passe valide. Merci!")
            break
        else:
            print("Le mot de passe ne respecte pas les conditions demandé. Veuillez réessayer.")

demander_MDP()