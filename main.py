
# creation d'une liste de tulpe, pour exercice car sinon il y aurait eu creation d'un dictionnaire.

articles = [("Pommes",50, 0.5),("Banane", 30, 0.3), ("Orange", 20, 0.6),("Clementine", 20, 0.5),("Kiwi", 10, 0.8)]

# condition pour la boucle while 
get_choice = True

# index pour definir quel ligne effacer valeur int 
index = 0

#  condition afin de definir si la valeur rechercher à été trouver 
found = False

# fonction pour mettre en pause le script

def continuer() :
  global get_choice
  get_choice = True
  input("Pour continuez appuyer sur entrée " )
  
  return  get_choice

# fonction de la boucle for in et ses effets 

def search_in_inventory(value, choice) :
  global found
  
  for article in articles :
    if choice == 1 : 
        print(f"Article : {article[0]} Quantité : {article[1]} Prix : {article[2]} €")

    elif choice == 2 :
        if article[0].lower() == value.lower() :
          print(f"{value} est déja existant dans la base de donnée")
          exist = True
          return exist

    elif choice == 3 :
      global index
      if value.lower() == article[0].lower() :
        found = True
        articles.pop(index)
        print(f"{value} à bien été supprimer à l'index {index}")
      index += 1 

    elif choice == 4 :
      if get_article.lower() == article[0].lower() :
        found = True
        search_article = print(f"Article : {article[0]} Quantité : {article[1]} Prix : {article[2]} €")
      return search_article



while get_choice :
  print("Choississez une option : \n 1 - Afficher l'inventaire \n 2 - Ajouter un article \n 3 - Supprimer un article \n 4 - Rechercher un article \n 5 - Quitter"  )
  print("entrez votre choix")
  choice = input( )
  print(f"le type de la variable choice est {type(choice)}")
  test_input = isinstance(choice, str)

  
  if choice == "1" or choice == "2" or choice == "3" or  choice == "4" or  choice == "5" :

    choice = int(choice)
    
  
  elif test_input :
      print("La valeur saisie n'est pas un chiffre")
      get_choice = True
      continuer()
  else :
    if(choice > 0) and (choice < 6 ) :
      get_choice = False

  # Voir l'inventaire

  if(choice == 1) :
      
    search_in_inventory(None, choice)
    continuer()
    
# ajouter un article 

  if choice == 2 : 

    exist = False
    print("entrez l'article à ajouter")
    new_article = input( )
    
    #recherche si l'article existe deja existant
    search_in_inventory(new_article, choice)
    
    if not exist :
      print("entrez la quantité du stock de l'article")
      quantity = input( )
      print("entrez la valeur unitaire de l'article (en €)")
      price = input( )
      articles.append((new_article, quantity, price))
      print(f"{quantity} {new_article} au prix de {price} € ont bien été ajouté à la base de donnée")
    continuer()


  # effacer un article

  if(choice == 3) :
    print("Quel article voulez vous effacer ? ")
    get_delete_article = input( )
    
    
    search_in_inventory(get_delete_article, choice)
    
    if not found :
      print(f"{get_delete_article} not found")
    continuer()

  
  if choice == 4 :

    found = False
    search_article = None

    print("Quel article voulez vous consulter ?")
    get_article = input( )

    search_in_inventory(get_article, choice)
    
    if found : 
      search_article
    else :
      print("Article non trouvé")
    continuer()
    

    