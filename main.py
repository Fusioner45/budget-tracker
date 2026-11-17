def ajouter_dep(categorie):
    objet = input("Nom de la dépense :")
    print("Choisisez votre catégorie : ","0.Courses","1.Transport","2.Loyer","3.Études","4.Loisirs","5.Autre")
    categorie_new = int(input("Catégorie:"))
    categorie_new = categorie[categorie_new]
    prix = float(input("Le prix de la dépense"))
    return objet,categorie_new,prix

def total_cat(mes_depense,categorie):
    somme = 0
    print("Choisisez votre catégorie : ","0.Courses","1.Transport","2.Loyer","3.Études","4.Loisirs","5.Autre")
    categorie_new = int(input("Catégorie:"))
    categorie_new = categorie[categorie_new]
    for elements in mes_depense:
        if elements[1] == categorie_new:
            somme = somme + elements[2]
    print(f"La catégorie séléctioner est : {categorie_new} est a pour somme : {somme}")


def total_gen():
    print("a faire")
def lister():
    print("a faire")

def main():
    categorie = ("Courses","Transport","Loyer","Études","Loisirs","Autre")
    choix = 0
    mes_depense =[]
    depense_unique=()
    while True:
        print("1.Ajouter une dépense\n 2.Voir le total par catégorie\n 3.Voir le total général\n 4.Lister toutes les dépenses\n 5.Quitter")
        choix = int(input("Que veut tu faire ? "))
        match choix:
            case 1 :
                depense_unique = ajouter_dep(categorie)
                mes_depense.append(depense_unique)
                print(mes_depense)
            case 2:
                total_cat(mes_depense,categorie)
            case 3:
                total_gen()
            case 4:
                lister()
            case 5:
                print("Aurevoir!")
                break
                
        
 

if __name__ == '__main__':
    main()