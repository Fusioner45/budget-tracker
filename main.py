def ajouter_dep():
    print("a faire")
def total_cat():
    print("a faire")
def total_gen():
    print("a faire")
def lister():
    print("a faire")

def main():
    categorie = ("Courses","Transport","Loyer","Études","Loisirs","Autre")
    choix = 0
    while True:
        print("1.Ajouter une dépense\n 2.Voir le total par catégorie\n 3.Voir le total général\n 4.Lister toutes les dépenses\n 5.Quitter")
        choix = int(input("Que veut tu faire ? "))
        match choix:
            case 1 :
                ajouter_dep()
            case 2:
                total_cat()
            case 3:
                total_gen
            case 4:
                lister()
            case 5:
                print("Aurevoir!")
                break
                
        
 

if __name__ == '__main__':
    main()