
articles = [("Pommes",50, 0.5),("Banane", 30, 0.3), ("Orange", 20, 0.6),("Clementine", 20, 0.5),("Kiwi", 10, 0.8)]


# afficher l'inventaire

# Ajouter un article 

# Supprimer un article

# Rechercher un article par nom

# 1 afficher le menu avec un while

get_choice = True
while get_choice :
  print("Choississez une option : \n 1 - Afficher l'inventaire \n 2 - Ajouter un article \n 3 - Supprimer un article \n 4 - Rechercher un article \n 5 - Quitter"  )
  
  choice = input()
  choice = int(choice)
  
  if(choice > 0) and (choice < 6 ) :
    get_choice = False

  if(choice == 1) :
      
      for article in articles :
         print(f"Article : {article[0]} Quantité : {article[1]} Prix : {article[2]} €")
         type(article[0])
         type(article[1])
         print("")
      get_choice=True