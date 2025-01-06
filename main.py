
# Creation d'une liste de tulpe, pour exercice car sinon il y aurait eu creation d'un dictionnaire.
articles = [("Pommes",50, 0.5),("Banane", 30, 0.3), ("Orange", 20, 0.6),("Clementine", 20, 0.5),("Kiwi", 10, 0.8)]

# Fonction pour mettre en pause le script
def continuer() :
  global get_choice
  get_choice = True
  input("Pour continuez appuyer sur entrée " )
  
  return  get_choice

# Fonction qui recherche un article
def trouver_article(nom) :
  for index, article in enumerate(articles) :
    if article[0].lower() == nom.lower() :
      return article, index
  return None, None

# Fonction pour afficher l'inventaire 
def afficher_inventaire() :
  print("--- Inventaire ---")
  for article in articles :
    print(f"Article : {article[0]} | Quantité : {article[1]} | Prix : {article[2]} €")
  return 

# Fonction pour ajouter un article
def ajouter_un_article() :
  nom = input("Entrez le nom de l'article à ajouter : ").strip()
  index, _ = trouver_article(nom)
  if index is not None :
    print(f"L'article '{nom}' existe déjà.")
    return
  
  try : 
    nom = nom.capitalize()
    quantite = int(input("Entrez la quantité de l'article à ajouter : ").strip())
    prix = float(input("Entrez le prix unitaire (€) : "))
    articles.append((nom, quantite, prix))
    print(f"L'article '{nom}' ajouté avec succès !")
  except ValueError :
    print("Entrée invalide. Veillez entrer des nombres pour la quantité et le prix.")

# Fonction pour supprimer un article
def supprimer_article():
  nom = input("Entrez le nom de l'article à supprimer : ").strip()
  index, _ = trouver_article(nom)
  if index is not None :
    articles.pop(index)
    print("L'article '{nom}' a été supprimé.")
  else :
    print(f"L'article '{nom}' n'a pas été trouvé.")

# Fonction pour rechercher un article
def rechercher_article():
  nom = input("Entrez le nom de l'article à rechercher : ").strip()
  _, article = trouver_article(nom)
  if article :
    print(f"Article trouvé : {article[0]} | Quantité : {article[1]} | Prix : {article[2]:.2f} €")
  else :
    print(f"L'article '{nom}' n'a pas été trouvé.")
  
# Fonction qui affiche le menu 
def menu() :

  while True :
    print("Choississez une option : \n 1 - Afficher l'inventaire \n 2 - Ajouter un article \n 3 - Supprimer   un article \n 4 - Rechercher un article \n 5 - Quitter"  )
    print("entrez votre choix")
    choix = input( ).strip()
  

  # Voir l'inventaire

    if choix == "1" :
      afficher_inventaire()
      
    
# ajouter un article 

    elif choix == "2" : 
      ajouter_un_article()
      
    
  # effacer un article
    elif choix == "3" :
      supprimer_article()
      

  
    elif choix == "4" :
      rechercher_article()
      
    
    elif choix == "5" :
      print("Au revoir")
      break
    
    else :
      print("Choix invalide. Veuillez réessayer.")
  
    continuer()

# Lancer le programme 
menu()

    