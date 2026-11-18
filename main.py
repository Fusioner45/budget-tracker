def ajouter_dep(categorie):
    objet = input("Nom de la dépense :")
    print("Choisisez votre catégorie : ","0.Courses","1.Transport","2.Loyer","3.Études","4.Loisirs","5.Autre")
    while True :
        categorie_new = input("Catégorie:")
        if categorie_new.isdigit():
            categorie_new = int(categorie_new)
            if categorie_new <=5 and categorie_new >=0:
                break
            else:
                print("erreur de catégorie")
        else:
            print("on prend que des chiffre donc erreur")
    categorie_new = categorie[categorie_new]
    while True :
            prix =input("Le prix de la dépense")
            if prix.isdigit():
                prix = float(prix)
                if prix > 0:
                    break
                else:
                    print("erreur inférieur a 0")
            else:
                print("on prend que des chiffre donc erreur") 
    return objet,categorie_new,prix

def total_cat(mes_depense,categorie):
    somme = 0
    print("Choisisez votre catégorie : ","0.Courses","1.Transport","2.Loyer","3.Études","4.Loisirs","5.Autre")
    while True :
            categorie_new = input("Catégorie:")
            if categorie_new.isdigit():
                categorie_new = int(categorie_new)
                if categorie_new <=5 and categorie_new >=0:
                    break
                else:
                    print("erreur de catégorie")
            else:
                print("on prend que des chiffre donc erreur")
    categorie_new = categorie[categorie_new]
    for elements in mes_depense:
        if elements[1] == categorie_new:
            somme = somme + elements[2]
    print(f"La catégorie séléctioner est : {categorie_new} est a pour somme : {somme}")


def total_gen(mes_depense):
    somme = 0
    for elements in mes_depense:
        somme = somme + elements[2]
    print(f"La somme général est de : {somme}")


def lister(mes_depense):
    for elements in mes_depense:
        print(f"La catégorie est {elements[1]} , le nom de l'objet est {elements[0]} et il a couter {elements[2]}")

def main():
    categorie = ("Courses","Transport","Loyer","Études","Loisirs","Autre")
    choix = 0
    mes_depense =[]
    depense_unique=()
    while True:
        print("1.Ajouter une dépense\n 2.Voir le total par catégorie\n 3.Voir le total général\n 4.Lister toutes les dépenses\n 5.Quitter")
        while True:
            choix = input("Que veut tu faire ? ")
            if choix.isdigit():
                choix = int(choix)
                if choix >=1 and choix <=5:
                    break
                else:
                    print("nombre invalide")
            else:
                print("on ne prend que des nombre")

        match choix:
            case 1 :
                depense_unique = ajouter_dep(categorie)
                mes_depense.append(depense_unique)
                print(mes_depense)
            case 2:
                total_cat(mes_depense,categorie)
            case 3:
                total_gen(mes_depense)
            case 4:
                lister(mes_depense)
            case 5:
                print("Aurevoir!")
                break
                
        
 

if __name__ == '__main__':
    main()