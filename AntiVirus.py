import os, time, sys, random, shutil

def Clear() :
  os.system("clear")
  os.system('cls')
  Titre()

def Titre() : 
  Titre = "AntiVirus \n\n\n "
  new_Titre = (Titre.center(shutil.get_terminal_size(50).columns))
  print(new_Titre)

def Presentation():
  Clear()
  print(" Des bruits courent concernant un nouveau virus. \n Sa progession est rapide et meutrière.\n Il faut faire quelque chose... ET VITE ! \n La survie de l'espèce humaine est entre vos mains, \n arriverez-vous à l'arreter avant qu'il ne soit trop tard ?\n ")

#### MENU PRINCIPAL
def Menu_Principal():
  Presentation()
  Choix_Menu_Principal = ['[1] Nouvelle partie','[2] Règles du jeu','[3] À propos','[4] Quitter']
  for i in Choix_Menu_Principal :
    print(i)
  Choix= (input("\n→ "))
  if Choix== '1':
    AskName()
  elif Choix== '2':
    Regles_Jeu()
  elif Choix== '3':
    About()
  elif Choix== '4':
    Exit()
  else :
    Invalid()
    return Menu_Principal()

 
def Regles_Jeu():
  Clear()
  print("  1. Qu'est ce que AntiVirus")
  print(" AntiVirus est un jeu dans lequel tu incarnes un président pendant la pandémie de Covid-19.\n Tu devras tout faire pour vaincre ce virus\n \n ")
  print("  2. Quel est le but du jeu dans AntiVirus?")
  print(" Pendant différents voyages, tu devras prendre les bonnes décisions afin d'aider ton pays à venir à bout du virus. \n Peut-être ramasseras-tu des items. \n Après cela, un combat contre le virus aura lieu.\n Si tu prends les bonnes décisions et que tu réussis à amaser assez d'items pendant tes voyages,\n tu auras par conséquent plus de chance de gagner.\n \n ")
  print("  3. Comment jouer à AntiVirus")
  print("C'est simple, tu devras toujours choisir parmi différentes possibilités. Surtout, fais attention à ton orthographe!\n \n ")
  Choix= (input("[1] Retour au menu"))
  print(Choix)
  Menu_Principal() == '1'

def About():
  Clear()
  print("Développeurs:")
  print()
  print("Melissande Dizy") 
  print("Cherine Dexpert")
  print("Doriane Farau")
  print()
  print("[1] Retour au menu")
  (input())
  Menu_Principal() == '1'

def Exit():
  Clear()
  print("À bientot!")
 
def Invalid():
  print("Ton choix est invalide, réessaye.")
  time.sleep(2)
  
#### ChoixDU PRENOM
def Moi():
  print("Ecris ton prénom:")
  Blaze = input()
  print("\nOk, super", Blaze, ",", "maintenant, choisis le pays que tu souhaites gouverner :\n ")
  ChoixPays()

def AskName():
  Clear()
  print("\n Ta mission est des plus importante... Devoir prendre les meilleurs décisions \npour vaincre le virus... \n")
  print(" Choisi un personnage : \n")
  Choix_Ask_Name = ['[1] Moi', '[2] Macron','[3] Kim Jong-Un','[4] Poutine','[5] Biden','\n[6] Quitter la partie']
  for i in Choix_Ask_Name :
    print(i)
  Choix= (input("\n→ "))
  if Choix== '1':
    Moi()
  elif Choix== '2':
    France()
  elif Choix== '3':
    Coree()
  elif Choix== '4':
    Russie()
  elif Choix== '5':
    USA() 
  elif Choix== '6':
    Menu_Principal()
  else :
    Invalid()
    return AskName()
    
#### PAYS
def ChoixPays():
  Choix_Pays = ['[1] Coree','[2] Russie','[3] USA','[4] France', '\n[5] Quitter la partie']
  for i in Choix_Pays:
    print(i)
  Choix= (input("\n→ "))
  if Choix== '1' :
    Coree()
  elif Choix== '2':
    Russie()
  elif Choix== '3':
    USA()
  elif Choix== '4' :
    France()
  elif Choix== '5' :
    Menu_Principal
  else :
    Invalid()
    return ChoixPays()
 
##### PARTIE JEU #####
#---------------------------------------------------#

##### XP / GAINS XP / BARRE XP / PIECES / GAINS PIECES / BARRE PIECES

## XP / PIECES
global XPMoi 
XPMoi = 0
global XPVirus
XPVirus = 0
global Pieces
Pieces = 0

## GAINS
Gain1 = 25
Gain2 = 15
def victoire():
  Clear()
  print("Ton pays peut être fier de toi !!!! Tu as reussi a éradiquer le virus de ton territoire...")
  time.sleep(3)
  Exit()
  

def defaite():
  Clear()
  print("Tu as perdu... A cause de toi, Virus a contaminé toute ta population.")
  time.sleep(3)
  Exit()
  

# JAUGE
def chiffres():
  cent = (u"\u2588")*100
  QuatreVingtQuinze = (u"\u2588") * 95 + ("—————")
  QuatreVingtDix =  (u"\u2588") * 90 + ("—————") * 2
  QuatreVingtCinq = (u"\u2588") * 85 + ("—————") * 3
  QuatreVingt = (u"\u2588") * 80 + ("—————") * 4
  SoixanteQuinze = (u"\u2588") * 75 + ("—————") * 5
  SoixanteDix = (u"\u2588") * 70 + ("—————") * 6
  SoixanteCinq = (u"\u2588") * 65 + ("—————") * 7
  Soixante = (u"\u2588") * 60 + ("—————") * 8
  CinquanteCinq = (u"\u2588") * 55 + ("—————") * 9
  Cinquante = (u"\u2588") * 50 + ("—————") * 10
  QuaranteCinq = (u"\u2588") * 45 + ("—————") * 11
  Quarante = (u"\u2588") * 40 + ("—————") * 12
  TrenteCinq = (u"\u2588") * 35 + ("—————") * 13
  Trente = (u"\u2588") * 30 + ("—————") * 14
  VingtCinq = (u"\u2588") * 25 + ("—————") * 15
  Vingt = (u"\u2588") * 20 + ("—————") * 16
  Quinze = (u"\u2588") * 15 + ("—————") * 17
  Dix = (u"\u2588") * 10 + ("—————") * 18
  Cinq = (u"\u2588") * 5 + ("—————") * 19
  Zero = ("—————") * 20

##BARRE PIECES
  if Pieces > 0 : 
    if Pieces == 100 :
      print("Pieces :", cent, "100")
    if Pieces == 95 : 
      print("Pieces :", QuatreVingtQuinze, "95")
    if Pieces == 90 : 
      print("Pieces :", QuatreVingtDix, "90")
    if Pieces == 85 : 
      print("Pieces :", QuatreVingtCinq, "85")
    if Pieces == 80 : 
      print("Pieces :", QuatreVingt, "80")
    if Pieces == 75 : 
      print("Pieces :", SoixanteQuinze, "75")
    if Pieces == 70 : 
      print("Pieces :", SoixanteDix, "70")
    if Pieces == 65 : 
      print("Pieces :", SoixanteCinq, "65")
    if Pieces == 60 : 
      print("Pieces :", Soixante, "60")
    if Pieces == 55 : 
      print("Pieces :", CinquanteCinq, "55")
    if Pieces == 50 : 
      print("Pieces :", Cinquante, "50")
    if Pieces == 45 : 
      print("Pieces :", QuaranteCinq, "45")
    if Pieces == 40 : 
      print("Pieces :", Quarante, "40")
    if Pieces == 35 : 
      print("Pieces :", TrenteCinq, "35")
    if Pieces == 30 : 
      print("Pieces :", Trente, "30")
    if Pieces == 25 : 
      print("Pieces :", VingtCinq, "25")
    if Pieces == 20 : 
      print("Pieces :", Vingt, "20")
    if Pieces == 15:
      print("Pieces :", Quinze,"15") 
    if Pieces == 10 : 
      print("Pieces :", Dix, "10")
    if Pieces == 5 : 
      print("Pieces :", Cinq, "5")
    if Pieces == 0 : 
      print("Pieces :", Zero, "0")
    if Pieces < 0 :      
      print("Pieces :", Zero, "0")
  else :
    pass
  print()

## BARRE XP      
  if XPMoi or XPVirus == 100 :
    if XPMoi == 100 :
      print("   Moi :", cent, "100 XP")
    if XPVirus == 100 : 
      print(" Virus :", cent, "100 XP")
  
  if XPMoi or XPVirus == 95 : 
    if XPMoi == 95 : 
      print("   Moi :", QuatreVingtQuinze, "95 XP")
    if XPVirus == 95 : 
      print(" Virus :", QuatreVingtQuinze, "95 XP")
  if XPMoi or XPVirus == 90 :
    if XPMoi == 90 : 
      print("   Moi :", QuatreVingtDix, "90 XP")
    if XPVirus == 90 : 
      print(" Virus :", QuatreVingtDix, "90 XP")
  if XPMoi or XPVirus == 85 :
    if XPMoi == 85 : 
      print("   Moi :", QuatreVingtCinq, "85 XP")
    if XPVirus == 85 : 
      print(" Virus :", QuatreVingtCinq, "85 XP")
  if XPMoi or XPVirus == 80 :
    if XPMoi == 80 : 
      print("   Moi :", QuatreVingt, "80 XP")
    if XPVirus == 80 : 
      print(" Virus :", QuatreVingt, "80 XP") 
  if XPMoi or XPVirus == 75 :
    if XPMoi == 75 : 
      print("   Moi :", SoixanteQuinze, "75 XP")
    if XPVirus == 75 : 
      print(" Virus :", SoixanteQuinze, "75 XP")
  if XPMoi or XPVirus == 70 :
    if XPMoi == 70 : 
      print("   Moi :", SoixanteDix, "70 XP")
    if XPVirus == 70 : 
      print(" Virus :", SoixanteDix, "70 XP") 
  if XPMoi or XPVirus == 65 :
    if XPMoi == 65 : 
      print("   Moi :", SoixanteCinq, "65 XP")
    if XPVirus == 65 : 
      print(" Virus :", SoixanteCinq, "65 XP")
  if XPMoi or XPVirus == 60 :
    if XPMoi == 60 : 
      print("   Moi :", Soixante, "60 XP")
    if XPVirus == 60 : 
      print(" Virus :", Soixante, "60 XP")
  if XPMoi or XPVirus == 55 :
    if XPMoi == 55 : 
      print("   Moi :", CinquanteCinq, "55 XP")
    if XPVirus == 55 : 
      print(" Virus :", CinquanteCinq, "55 XP")
  if XPMoi or XPVirus == 50 :
    if XPMoi == 50 : 
      print("   Moi :", Cinquante, "50 XP")
    if XPVirus == 50 : 
      print(" Virus :", Cinquante, "50 XP")
  if XPMoi or XPVirus == 45 :
    if XPMoi == 45 : 
      print("   Moi :", QuaranteCinq, "45 XP")
    if XPVirus == 45 : 
      print(" Virus :", QuaranteCinq, "45 XP")
  if XPMoi or XPVirus== 40 :
    if XPMoi == 40 : 
      print("   Moi :", Quarante, "40 XP")
    if XPVirus == 40 : 
      print(" Virus :", Quarante, "40 XP")
  if XPMoi or XPVirus == 35 :
    if XPMoi == 35 : 
      print("   Moi :", TrenteCinq, "35 XP")
    if XPVirus == 35 : 
      print(" Virus :", TrenteCinq, "35 XP") 
  if XPMoi or XPVirus == 30 :
    if XPMoi == 30 : 
      print("   Moi :", Trente, "30 XP")
    if XPVirus == 30 : 
      print(" Virus :", Trente, "30 XP")
  if XPMoi or XPVirus == 25 :
    if XPMoi == 25 : 
      print("   Moi :", VingtCinq, "25 XP")
    if XPVirus == 25 : 
      print(" Virus :", VingtCinq, "25 XP")
  if XPMoi or XPVirus == 20 :
    if XPMoi == 20 : 
      print("   Moi :", Vingt, "20 XP")
    if XPVirus == 20 : 
      print(" Virus :", Vingt, "20 XP")
  if XPMoi or XPVirus == 15 :
    if XPMoi == 15:
      print("   Moi :", Quinze,"15 XP") 
    if XPVirus == 15 :
      print(" Virus :", Quinze,"15 XP") 
  if XPMoi or XPVirus == 10 :
    if XPMoi == 10 : 
      print("   Moi :", Dix, "10 XP")
    if XPVirus == 10 : 
      print(" Virus :", Dix, "10 XP")
  if XPMoi or XPVirus == 5 :
    if XPMoi == 5 : 
      print("   Moi :", Cinq, "5 XP")
    if XPVirus == 5 : 
      print(" Virus :", Cinq, "5 XP")  
  else :
    pass


##### INCREMENTATIONS XP
def Plus_Plus():
  global XPMoi
  global XPVirus
  XPMoi += 25
  XPVirus += Gain2
  chiffres()
def Moins():
  global XPMoi
  global XPVirus
  XPMoi += Gain2
  XPVirus += 25
  chiffres()
def Plus_Special():
  global XPMoi
  global XPVirus
  XPMoi += Gain2
  XPVirus += Gain2
  chiffres()

##### DECISIONS
def Assemblee_Nationale(): #+Special
  Clear()
  print("\nTu te rends à l'Assemblée Nationale. Un confinement est annoncé à la population de ton pays. Cela te fait remporter ", Gain2," XP.\n")
  Plus_Special()
def Maison_Bleue():#-
  Clear
  print("\nQu’est ce que je fais là ? C’est la coiffure qui me fait vibrer, tu quittes ton poste. Grace à toi, Virus remporte ",Gain1,".XP.\n")
  Moins()
def OMS():#++
  Clear()
  print("\nTu te rends à la OMS pour annoncer qu'une attestation est à présent obligatoire pour se déplacer. Cela te fait remporter ", Gain1,"XP.\n")
  Plus_Plus()
def Restaurant():#-
  Clear()
  print("\nTu es au restaurant, profites bien. Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Aeroport():#-
  Clear()
  print("\nTrop de pression, tu te rends à l'aéroport et décides de prendre des vacances. Grace à toi, Virus remporte",Gain1," XP.\nTes vacances sont maintenant terminées.\n")
  Moins()
def Conference():#+Special
  Clear()
  print("\nTu annonces lors d'une conférence l'interdiction des regroupements de plus de 6 personnes. Cela te fait remporter", Gain2,". XP\n")
  Plus_Special()
def Discours():#++
  Clear()
  print("\nTu annonces lors d'un discours le port du masque obligatoire dans tous les lieux. Cela te fait remporter", Gain1," XP.\n")
  Plus_Plus()
def Montagne():#-
  Clear()
  print("\nTrop de pression, un peu de détente ne te feras pas de mal. Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Hopital(): #++
  Clear()
  print("\nTu annonces plus de lits dans les hopitaux. Cela te fait remporter", Gain1," XP.\n")
  Plus_Plus()
def Musee():#-
  Clear()
  print("\nTrop de pression, un peu de détente ne te feras pas de mal. Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Congres(): #+Special
  Clear()
  print("\nTu te rends au Congrès. Un confinement est annoncé à la population de ton pays. Cela te fait remporter", Gain2," XP.\n")
  Plus_Special()
def Maison_Blanche():#-
  Clear()
  print("\nMais qu’est ce que je fais là ? C’est la coiffure qui me fait vibrer... Grace à toi, Virus remporte",Gain1,"XP.\n")
  Moins()
def Hammam():#-
  Clear()
  print("\nTrop de pression, un peu de détente ne te feras pas de mal. Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Elysee():#-
  Clear()
  print("\nMais qu’est ce que je fais là ? C’est la coiffure qui me fait vibrer... Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Palais_Du_Senat():#-
  Clear()
  print("\nMais qu’est ce que je fais là ? C’est la coiffure qui me fait vibrer... Grace à toi, Virus remporte",Gain1," XP.\n")
  Moins()
def Douma_d_Etat():#+Special
  Clear()
  print("\nTu te rends à la Douma d'État. Un confinement est annoncé à la population de ton pays. Cela te fait remporter", Gain2," XP.\n")
  Plus_Special()
###### DEPLACEMENTS
## FRANCE
def France() :
  Clear()
  print(" La France est en danger... On te reclame dans tout le pays,\n choisi où tu veux te rendre en premier :\n")
  villes_non_visites = ['[1] Nord','[2] Sud','[3] Est', '\n[4] Quitter la partie']
  def afficher_choix():
    if len(villes_non_visites) > 1:
      print('\nOù souhaites-tu aller ?')
      for ville in villes_non_visites:
        print(ville)
      Choix= (input("\n→ "))
      valider_choix(Choix)
    else  :
      print("\n On te reclame à la capitale !!!! Tu y seras d'ici 5 secondes...")
      time.sleep(6)
      Paris()

  def valider_choix(Choix):
    if Choix== '1' :
      Lille()
    elif Choix== '2' :
      Marseille()
    elif Choix== '3' :
      Lyon()
    elif Choix== '4' :
      Menu_Principal()
    else:
      Invalid()
      return France() 
  
  def Choix_Enigmes():
    if len(villes_non_visites) == 3 :
      Enigme1() 
    elif len(villes_non_visites) == 2 :
      Enigme2()
    elif len(villes_non_visites) == 1 :
      Enigme3()
  
  def Lille():
    Clear()
    print(" Tu es maintenant à Lille.\n ") 
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi remoporteront minimum 15 XP. \n Si tu ne sais pas, tu peux toujours demander à Albert de choisir pour toi... \n")
    Decisions_restantes = ['[1] Faire une conference', '[2] Faire un discours', "[3] Allez à l'aeroport", '[4] Allez chez Albert', '\n[5] Quitter la partie\n']
    for i in Decisions_restantes:
      print(i)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix == '1':
        Conference()
        Choix_Enigmes()
      elif Choix== '2':
        Discours()
      elif Choix =='3':
        Aeroport()
      elif Choix == '4':
        Albert()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()   
    
    def Albert():
      rdm = random.choice(["Conference","Discours","Aeroport"])
      if rdm == "Conference" :
        Conference()
        Choix_Enigmes()
      if rdm == "Discours" :
        return Discours()
      else:
        return Aeroport() 

    villes_non_visites.remove('[1] Nord')
    Choix_decision()
    afficher_choix()

  def Marseille():
    Clear()
    print(" Tu es maintenant à Marseille.\n ")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi remoporteront minimum 15 XP. \n Si tu ne sais pas, tu peux toujours demander à Albert de choisir pour toi... \n")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", '[2] Faire une conference', '[3] Aller au hammam', '[4] Allez chez Albert', '\n[5] Quitter la partie\n']
    for i in Decisions_restantes:
      print(i)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '3':
        Hammam()
      elif Choix== '4':
        Albert()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()  
  
    def Albert():
      rdm = random.choice(["Hammam","Hopital","Conference"])
      if rdm == "Hammam" :
        return Hammam()
      elif rdm == "Hopital":
        return Hopital() 
      else :
        Conference()
        Choix_Enigmes()
    
    villes_non_visites.remove('[2] Sud')
    Choix_decision()
    afficher_choix()

  def Lyon():
    Clear()
    print(" Tu es maintenant à Lyon.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi remoporteront minimum 15 XP. \n Si tu ne sais pas, tu peux toujours demander à Albert de choisir pour toi... \n")
    Decisions_restantes = ["[1] Se rendre à l'OMS", '[2] Donner une conference', '[3] Aller au restaurant', '[4] Aller chez Albert', '\n[5] Quitter la partie\n']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        OMS() 
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '3':
        Restaurant()
      elif Choix== '4':
        Albert()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()   
    
    def Albert():
      rdm = random.choice(["OMS","Restaurant","Conference"])
      if rdm == "OMS" :
        return OMS()
      elif rdm == "Restuaurant":
        return Restaurant() 
      else :
        Conference()
        Choix_Enigmes()
  
    villes_non_visites.remove('[3] Est')
    Choix_decision()
    afficher_choix()

  def Paris():
    Clear()
    print(" Tu es maintenant à Paris.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi remoporteront minimum 15 XP. \n Si tu ne sais pas, tu peux toujours demander à Albert de choisir pour toi... \n")
    Decisions_restantes = ["[1] Faire une visite officielle à l'Hopital", "[2] Aller à l'assemblee nationale", "[3] Aller à l'Elysee", '[4] Aller chez Albert', '\n[5] Quitter la partie\n']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Assemblee_Nationale()
        Enigme4()
      elif Choix== '3':
        Elysee()
      elif Choix== '4':
        Albert()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision() 
      
    def Albert():
      rdm = random.choice(["Hopital","Assemblee Nationale","Elysee"])
      if rdm == "Elysee" :
        return Elysee()
      elif rdm == "Assemblee Nationale":
        Assemblee_Nationale()
        Enigme4()
      else :
        return Hopital()
    
    Choix_decision()
    print("\n\n Il semplerait que le Virus ait pris une forme humaine, tu vas devoir le combattre...")
    time.sleep(5)
    Inventaire()
    
  afficher_choix()

## RUSSIE
def Russie():
  Clear()
  print(" La Russie est en danger... On te reclame dans tout le pays,\n choisi où tu veux te rendre en premier :\n")
  villes_non_visites = ['[1] Nord', '[2] Sud', '[3] Est', '\n[4] Quitter la partie']
  
  def afficher_choix():
    if len(villes_non_visites) > 1 :
      print('\n Où souhaites-tu aller ?')
      for ville in villes_non_visites:
        print(ville)
      Choix= (input("\n→ "))
      valider_choix(Choix)
    else :
      print("\n On te reclame à la capitale !!!! Tu y seras d'ici 5 secondes...")
      time.sleep(6)
      Moscou()
     
  def valider_choix(Choix):
      if Choix== '1':
          StPetersbourg()
      elif Choix== '2':
          Novossibirsk()
      elif Choix== '3':
          Iekaterinbourg()
      elif Choix== '4' :
        Menu_Principal()
      else:
        Invalid()
        return Russie()

  def Choix_Enigmes():
    if len(villes_non_visites) == 3 :
      Enigme1() 
    elif len(villes_non_visites) == 2 :
      Enigme2()
    elif len(villes_non_visites) == 1 :
      Enigme3()
  def StPetersbourg():
    Clear()
    print(" Tu es maintenant à Saint Petersbourg.\n") 
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Dmitri de choisir pour toi...\n ")
    Decisions_restantes = ['[1] Donner une conference', '[2] Faire un discours', "[3] Allez à l'aeroport" , '[4] Aller chez Dmitri', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Conference()
        Choix_Enigmes()
      elif Choix== '2':
        Discours()
      elif Choix== '3':
        Aeroport()
      elif Choix== '4':
        Dmitri()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision() 
       
    def Dmitri():
      rdm = random.choice(["Conference","Discours","Aeroport"])
      if rdm == "Conference" :
        Conference()
        Choix_Enigmes()
      if rdm == "Discours" :
        return Discours()
      else:
        return Aeroport() 
      
    villes_non_visites.remove('[1] Nord')
    Choix_decision()
    afficher_choix()

  def Novossibirsk():
    Clear()
    print(" Tu es maintenant à Novossibirsk.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP. Si tu ne sais pas, tu peux toujours demander à Dmitri de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", '[2] Donner une conference', '[3] Aller au Musee', '[4] Allez chez Dmitri', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Conference()
      elif Choix== '3':
        Musee()
      elif Choix== '4':
        Dmitri()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision() 

    def Dmitri():
      rdm = random.choice(["Conference","Hopital","Musee"])
      if rdm == "Musee" :
        return Musee()
      elif rdm == "Hopital":
        return Hopital() 
      else :
        Conference()
        Choix_Enigmes()
     
    villes_non_visites.remove('[2] Sud')
    Choix_decision()
    afficher_choix()

  def Iekaterinbourg():
    Clear()
    print(" Tu es maintenant à Iekaterinbourg.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Dmitri de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Se rendre à l'OMS", '[2] Donner une conference', '[3] Allez au restaurant', '[4] Allez chez Dmitri', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        OMS() 
      elif Choix== '3':
        Restaurant()
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '4':
        Dmitri()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()   

    def Dmitri():
      rdm = random.choice(["OMS","Restaurant","Conference"])
      if rdm == "OMS" :
        return OMS()
      elif rdm == "Restuaurant":
        return Restaurant() 
      else :
        Conference()
        Choix_Enigmes()
    
    villes_non_visites.remove('[3] Est')
    Choix_decision()
    afficher_choix()

  def Moscou():
    Clear()
    print(" Tu es maintenant à Moscou.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Dmitri de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Faire une visite officielle à l'Hopital", "[2] Allez au Douma d'Etat", '[3] Palais du Senat', '[4] Dmitri', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== "2":
        Douma_d_Etat()
        Enigme4()
      elif Choix== '3':
        Palais_Du_Senat()
      elif Choix== '4':
        Dmitri()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()

    def Dmitri():
      rdm = random.choice(['Hopital', "Douma d'Etat", 'Palais du Senat'])
      if rdm == "Hopital" :
        return Hopital()
      elif rdm == "Douma d'Etat":
        Douma_d_Etat() 
        Enigme4
      else :
        return Palais_Du_Senat()

    Choix_decision()
    print("\n\n Il semplerait que le Virus ait pris une forme humaine, tu vas devoir le combattre...")
    time.sleep(4)
    Inventaire()
    
  afficher_choix()

## USA
def USA():
  Clear()
  print(" Les Etats-Unis sont en danger... On te reclame dans tout le pays,\n choisi où tu veux te rendre en premier :\n")
  villes_non_visites = ['[1] Nord', '[2] Sud', '[3] Ouest', '\n[4] Quitter la partie']
  
  def afficher_choix():
    if len(villes_non_visites) > 1:
      print('\n Où souhaites-tu aller ?')
      for ville in villes_non_visites:
        print(ville)
      Choix= (input("\n→ "))
      valider_choix(Choix)
    else :
      print("\n On te reclame à la capitale !!!! Tu y seras d'ici 5 secondes...")
      time.sleep(6)
      Washington()

  def valider_choix(Choix):
      if Choix== '1':
          Chicago()
      elif Choix== '2':
          Houston()
      elif Choix== '3':
          Los_Angeles()
      elif Choix== '4' :
        Menu_Principal()
      else:
        Invalid()
        return USA()  

  def Choix_Enigmes():
    if len(villes_non_visites) == 3 :
      Enigme1() 
    elif len(villes_non_visites) == 2 :
      Enigme2()
    elif len(villes_non_visites) == 1 :
      Enigme3()
  
  def Chicago():
    Clear()
    print(" Tu es maintenant à Chicago.\n") 
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Georges de choisir pour toi...\n ")
    Decisions_restantes = ['[1] Donner une conference', '[2] Faire un discours', "[3] Aller à l'aeroport", '[4] Aller chez Georges', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Conference() 
        Choix_Enigmes()
      elif Choix== '2':
        Discours()
      elif Choix== '3':
        Aeroport()
      elif Choix== '4':
        Georges()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()   

    def Georges():
      rdm = random.choice(["Conference","Discours","Aeroport"])
      if rdm == "Conference" :
        Conference()
        Choix_Enigmes()
      if rdm == "Discours" :
        return Discours()
      else:
        return Aeroport() 
      
    villes_non_visites.remove('[1] Nord')
    Choix_decision()
    afficher_choix()

  def Houston():
    Clear()
    print(" Tu es maintenant à Houston.\n ")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Georges de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", '[2] Donner une conference', '[3] Se rendre au musee', '[4] Aller chez Georges','\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '3':
        Musee()
      elif Choix== '4':
        Georges()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()  
    
    def Georges():
      rdm = random.choice(["Conference","Hopital","Musee"])
      if rdm == "Musee" :
        return Musee()
      elif rdm == "Hopital":
        return Hopital() 
      else :
        Conference()
        Choix_Enigmes()
      
    villes_non_visites.remove('[2] Sud')
    Choix_decision()
    afficher_choix()

  def Los_Angeles():
    Clear()
    print("Tu es maintenant à Los Angeles.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Georges de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Aller à l'OMS", '[2] Donner une conference', '[3] Se rendre au restaurant', '[4] Aller chez Georges', '\n[5] Quitter la partie']
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        OMS() 
      elif Choix== '3':
        Restaurant()
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '4':
        Georges()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()     
    
    def Georges():
      rdm = random.choice(["OMS","Restaurant","Conference"])
      if rdm == "OMS" :
        return OMS()
      elif rdm == "Restuaurant":
        return Restaurant() 
      else :
        Conference()
        Choix_Enigmes()
      
    villes_non_visites.remove('[3] Ouest')
    Choix_decision()
    afficher_choix()

  def Washington():
    Clear()
    print(" Tu es maintenant à Washington.")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Georges de choisir pour toi...\n ")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", '[2] Se rendre au Congres', '[3] Se rendre à la Maison Blanche', '[4] Aller chez Georges', "\n[5] Quitter la partie"]
    for Decisions in Decisions_restantes:
      print(Decisions)
    
    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Congres()
        Enigme4()
      elif Choix== '3':
        Maison_Blanche()
      elif Choix== '4':
        Georges()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision() 

    def Georges():
      rdm = random.choice(["Hopital","Congres","Maison blanche"])
      if rdm == "Maisie blanche" :
        return Maison_Blanche()
      elif rdm == "Congres":
        Congres() 
        Enigme4()
      else :
        return Hopital()

    Choix_decision()
    print("\n\n Il semplerait que le Virus ait pris une forme humaine, tu vas devoir le combattre...")
    time.sleep(4)
    Inventaire()
    
  afficher_choix()

## COREE
def Coree():
  Clear()
  print(" La Coree du nord est en danger... On te reclame dans tout le pays,\n choisi où tu veux te rendre en premier :\n")
  villes_non_visites = ['[1] Ouest', '[2] Nord', '[3] Est', '\n[4] Quitter la partie']
  
  def afficher_choix():
    if len(villes_non_visites) > 1:
      print('\n Où souhaites-tu aller ?')
      for ville in villes_non_visites:
        print(ville)
      Choix= (input("\n→ "))
      valider_choix(Choix)
    else :
      print("\n On te reclame à la capitale !!!! Tu y seras d'ici 5 secondes...")
      time.sleep(6)
      Pyongyang()
      
  def valider_choix(Choix):
      if Choix== '1':
          Nampho()
      elif Choix== "2":
          Chongjin()
      elif Choix== '3':
          Hamhung()
      elif Choix== '4' :
        Menu_Principal()
      else:
        Invalid()
        return Coree()

  def Choix_Enigmes():
    if len(villes_non_visites) == 3 :
      Enigme1() 
    elif len(villes_non_visites) == 2 :
      Enigme2()
    elif len(villes_non_visites) == 1 :
      Enigme3() 
  
  def Nampho():
    Clear()
    print(" Tu es maintenant à Nampho.\n") 
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Shin de choisir pour toi...\n")
    Decisions_restantes = ['[1] Donner une conference', '[2] Donner un discours', "[3] Aller à l'aeroport", '[4] Aller chez Shin', "\n[5] Quitter la partie"]
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Conference()
        Choix_Enigmes()
      elif Choix== '2':
        Discours()
      elif Choix== '3':
        Aeroport()
      elif Choix== '4':
        Shin()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()  
    
    def Shin():
      rdm = random.choice(["Conference","Discours","Aeroport"])
      if rdm == "Conference" :
        Conference()
        Choix_Enigmes()
      if rdm == "Discours" :
        return Discours()
      else:
        return Aeroport() 
    
    villes_non_visites.remove('[1] Ouest')
    Choix_decision()
    afficher_choix()

  def Chongjin():
    Clear()
    print(" Tu es maintenant à Chongjin.")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Shin de choisir pour toi...\n")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", '[2] Donner une conference', '[3] Se balader en montagne', '[4] Aller chez Shin', "\n[5] Quitter la partie"]
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== '3':
        Montagne()
      elif Choix== '4':
        Shin()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()  

    def Shin():
      rdm = random.choice(["Montagne","Hopital","Conference"])
      if rdm == "Montagne" :
        return Montagne()
      elif rdm == "Hopital":
        return Hopital() 
      else :
        Conference()
        Choix_Enigmes()
      
    villes_non_visites.remove('[2] Nord')
    Choix_decision()
    afficher_choix()

  def Hamhung():
    Clear()
    print(" Tu es maintenant à Hamhung.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Shin de choisir pour toi...\n")
    Decisions_restantes = ["[1] Se rendre à l'OMS", '[2] Donner une conference', '[3] Aller au restaurant', '[4] Aller chez Shin', "\n[5] Quitter la partie"]
    for Decisions in Decisions_restantes:
      print(Decisions)
  
    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        OMS() 
      elif Choix== '3':
        Restaurant()
      elif Choix== '2':
        Conference()
        Choix_Enigmes()
      elif Choix== 'Shin':
        Shin()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()   
  
    def Shin():
      rdm = random.choice(["OMS","Restaurant","Conference"])
      if rdm == "OMS" :
        return OMS()
      elif rdm == "Restuaurant":
        return Restaurant() 
      else :
        Conference()
        Choix_Enigmes()
      afficher_choix()
      
    villes_non_visites.remove('[3] Est')
    Choix_decision()
    afficher_choix()

  def Pyongyang():
    Clear()
    print(" Tu es maintenant à Pyongyang.\n")
    print(" Plusieurs décisions s'offrent à toi et te permettront d'emporter des XP.\n Quelque soit ton choix, le Virus et toi ganeront 15 XP.\n Si tu ne sais pas, tu peux toujours demander à Shin de choisir pour toi...\n")
    Decisions_restantes = ["[1] Faire une visite officielle à l'hopital", "[2] Se rendre à l'assemblee nationale", '[3] Aller à la Maison Bleue', '[4] Aller chez Shin', "\n[5] Quitter la partie"]
    for Decisions in Decisions_restantes:
      print(Decisions)

    def Choix_decision():
      Choix= (input("\n→ "))
      if Choix== '1':
        Hopital() 
      elif Choix== '2':
        Assemblee_Nationale()
        Enigme4()
      elif Choix== '3':
        Maison_Bleue()
      elif Choix== 'Shin':
        Shin()
      elif Choix== '5' :
        Menu_Principal()
      else:
        Invalid()
        return Choix_decision()    
    
    def Shin():
      rdm = random.choice(["Hopital","Assemblee Nationale","Maison bleue"])
      if rdm == "Maison bleue" :
        return Maison_Bleue()
      elif rdm == "Assemblee Nationale":
        Assemblee_Nationale()
        Enigme4
      else :
        return Hopital()
    
    Choix_decision()
    print("\n\n Il semplerait que le Virus ait pris une forme humaine, tu vas devoir le combattre...")
    time.sleep(5)
    Inventaire()
  afficher_choix()

#### INVENTAIRE

## ITEMS
global Items
Items = []

global Choix1

def Inventaire():
  Clear()
  print(" Veux tu ouvrir ton inventaire avant le combat? Les items peuvent t'aider à le gagner.\n")
  Decisions_restantes = ["[1] Oui", "[2] Non"]
  for Decisions in Decisions_restantes:
    print(Decisions)

  Choix= (input("\n→ "))
  if Choix== "1":
    print("Voici ton inventaire:", Items)
    if len(Items) == 0:
      print(" Ton inventaire est vide... place au combat.")
      time.sleep(2)
      combat()
    else:
      print(" Voici ton inventaire:", Items)
      ChoixItem()
  elif Choix== "2":
    combat()
  else : 
    Invalid()
    Inventaire()
    
def ChoixItem():
  print(" \nVeux tu utiliser un item? \n")
  Decisions_restantes = ["[1] Oui", "[2] Non"]
  for Decisions in Decisions_restantes:
    print(Decisions)
  global Choix1
  Choix1 = (input("\n→ "))
  global Pieces
  global Items
  
  if Choix1 == "1":
    if len(Items) == 0:
      print(" Ton inventaire est vide. \n Maintenant tu es prêt...")
      time.sleep(6)
      combat()
    else : 
      while len(Items) >=0 : 
        print("Quel item veux tu choisir :",Items)
        PrendItem = (input("\n→ "))
        if PrendItem == "Gants":
          print("\n L'utilisation des gants te fait gagner 15 pièces !")
          Pieces += 15
          chiffres()
          Items.remove("Gants")

        elif PrendItem == "Masques":
          print("\n L'utilisation des masques te fait gagner 25 pièces !")
          Pieces += 25
          chiffres()
          Items.remove("Masques")

        elif PrendItem == "Gel hydroalcolique":
          print("\n L'utilisation du gel hydroalcolique te fait gagner 30 pièces !")
          Pieces += 30
          chiffres()
          Items.remove("Gel hydroalcolique")

        elif PrendItem == "Chloroquine":
          print("\n L'utilisation de la chloroquine te fait gagner 50 pièces !")
          Pieces += 50
          chiffres()
          Items.remove("Chloroquine")
        if len(Items) == 0:
          print(" Ton inventaire est vide. Place au combat...")
          time.sleep(4)
          combat()

  elif Choix1 == "2":
    combat()
  else: 
    Invalid()
    ChoixItem()

#### ENIGMES 

def Enigme():
  print("\n Très bonne décision ! Réponds à cette enigme pour tenter de gagner des pièces.")

def Enigme1():
  Enigme()
  global Items
  print(" \n On la tourne pour avancer ; mais quand on l’est, cela signifie être branché. Qui est-elle ?\n")
  Decisions_restantes = ["[1] La manivelle", "[2] La page", "[3] La prise"]
  for Decisions in Decisions_restantes:
    print(Decisions)
  Choix= (input("\n→ "))
  if Choix == '2':
    print("\n Félicitations ! Tu as trouvé la bonne réponse !")
    print(" Tu viens de débloquer un nouvel item : des gants en latex pour protéger des citoyens !\n Tu les retrouveras plus tard dans ton inventaire.")
    Items.append("Gants")
  else :
    print("\nRaté, quel dommage ...")

def Enigme2():
  Enigme()
  global Items
  print("\n Combien de gouttes d'eau peut-on mettre dans un verre vide ?\n ")
  Decisions_restantes = ["[1] 1", "[2] 25cl", "[3] 30cl", "[4] 0 "]
  for Decisions in Decisions_restantes:
    print(Decisions)

  Choix= (input("\n→ "))
  if Choix== "1":
    print("\n Félicitations ! Tu as trouvé la bonne réponse !")
    print(" Tu viens de débloquer un nouvel item : des gants en latex pour protéger des citoyens !\n Tu les retrouveras plus tard dans ton inventaire.")
    Items.append("Masques")
  else :
    print("\nRaté, quel dommage ...")

def Enigme3():
  Enigme()
  global Items
  print("\n Qu'est-ce qui apparaît dans le jour, dans la nuit, mais jamais dans la semaine ni le week-end ?\n ")
  Choix= (input("\n→ "))
  if Choix== "u":
    print("\n Félicitations ! Tu as trouvé la bonne réponse !")
    print(" Tu viens de débloquer un nouvel item : des gants en latex pour protéger des citoyens !\n Tu les retrouveras plus tard dans ton inventaire.")
    Items.append("Gel hydroalcolique")
  else :
    print("\nRaté, quel dommage ...\n")

def Enigme4():
  Enigme()
  global Items
  print("\n Quel nombre divisé par lui-même donne son double ?\n ")
  Choix= (input("\n→ "))
  if Choix== "0.5" or Choix== "0,5":
    print("\n Félicitations ! Tu as trouvé la bonne réponse !")
    print(" Tu viens de débloquer un nouvel item : des gants en latex pour protéger des citoyens !\n Tu les retrouveras plus tard dans ton inventaire.")
    Items.append("Chloroquine")
  else :
    print("\n Raté, quel dommage ...")
    print()

#### COMBAT

## INCREMENTATIONS XP / PIECES
Win1 = 10
Win2 = 15
global Super_Coup
Super_Coup = 35

def Coup1():
  Selection = [10, 15]
  Select = random.choice(Selection)
  global XPMoi
  global XPVirus
  global Win1
  global Win2
  XPMoi -= Select
  XPVirus -= Win1
  if XPVirus > 0 :
    time.sleep(2)
    print("\n Le coup de ton adversaire t'a fait perdre", Select, " XP\n")
  if XPMoi == 0 : 
    defaite()
  if XPVirus == 0:
    victoire()
  chiffres()
  
def Coup2():
  Selection = [10, 15]
  Select = random.choice(Selection)
  global XPMoi
  global XPVirus
  global Win1
  global Win2
  XPMoi -= Select
  XPVirus -= Win2
  if XPVirus > 0 :
    time.sleep(2)
    print("\n Le coup de ton adversaire t'a fait perdre", Select, " XP. \n")
  if XPMoi == 0 : 
    defaite()
  if XPVirus == 0:
    victoire()
  chiffres()

def Coup3():
  Selection = [10, 15]
  Select = random.choice(Selection)
  global XPMoi
  global XPVirus
  global Win1
  global Win2
  XPMoi -= Select
  XPVirus -= Super_Coup
  if XPVirus > 0 :
    time.sleep(2)
    print(" \nLe coup de ton adversaire t'a fait perdre", Select, "XP\n")
  global Pieces
  Pieces -= 35
  if XPMoi == 0 : 
    defaite()
  if XPVirus == 0:
    victoire()
  chiffres()

## MODE DE COMBAT

def combat():
  Clear()
  print(" Choisi ton mode de combat : \n")
  style_combat = ['[1] Boxe Thai', '[2] Combat de rue', '[3] Ninja', '\n[4] Quitter la partie\n']
  def combat_choix():
    if len(style_combat) > 0:
      for combat in style_combat:
        print(combat)
      reponse = (input("\n→ "))
      valider_combat_choix(reponse)
  
  def valider_combat_choix(reponse):
    if reponse == '1':
      Boxe_Thai()
    elif reponse == '2':
      Combat_De_Rue()
    elif reponse == '3':
      Ninja()
    elif reponse == '4':
      Menu_Principal()
    else:
      Invalid()
      return combat_choix()
      
  combat_choix()

# BOXE THAI
def Boxe_Thai(): 
  if XPVirus == 0 : 
    victoire()
  if XPMoi == 0 : 
    defaite()
  print("\n Choisi ton attaque : \n")
  Choix_coup = ["[1] Swing ","[2] Frontkick","[3] Uppercut (-35 pièces)"]
  
  if XPVirus > 0 and XPMoi > 0 :
    for coup in Choix_coup :
      print(coup)
    print("À ton tour:")
    Choix = (input("\n→ "))
    if Choix == '1':
      print("Tu as mis un Swing au Virus. Il a perdu 10 XP")
      Coup1()
    elif Choix == '2':
      print("Tu as mis un Frontkick au Virus. Il a perdu 15 XP")
      Coup2()
    elif Choix == '3':
      if Pieces >= 35: 
        print("Tu as mis un super-coup au Virus. Il a perdu", Super_Coup,"XP")
        Coup3()
      else:
        print("tu n'as pas assez de pièces pour utiliser le super coup")
        Boxe_Thai()
    else:
      Invalid()
      Boxe_Thai()

  Boxe_Thai()

# COMBAT DE RUE
def Combat_De_Rue():
  if XPVirus == 0 : 
    victoire()
  if XPMoi == 0 : 
    defaite()
  print("\n Choisi ton attaque : \n")
  Choix_coup = ["[1] Balayette ","[2] Poing americain","[3] Coup de boule (-35 pièces)"]

  if XPVirus > 0 and XPMoi > 0 :
    for coup in Choix_coup :
      print(coup)
    print("À ton tour:")
    Choix = (input("\n→ "))
    if Choix == '1':
      print("Tu as mis une Balayette au Virus. Il a perdu 10 XP")
      Coup1()
    elif Choix == '2':
      print("Tu as mis un Poing americain au Virus. Il a perdu 15 XP")
      Coup2()
    elif Choix == '3':
      if Pieces >= 35: 
        print("Tu as mis un super-coup au Virus. Il a perdu", Super_Coup,"XP")
        Coup3()
      else:
          print("tu n'as pas assez de pièces pour utiliser le super coup")
          print()
          Combat_De_Rue()
    else:
      Invalid()
      Combat_De_Rue()
  
  Combat_De_Rue()

# NINJA

def Ninja():
  if XPVirus == 0 : 
    victoire()
  if XPMoi == 0 : 
    defaite()
  print("\n Choisi ton attaque : \n") 
  Choix_coup = ["[1] Nunchaku ","[2] Shuriken","[3] Katana (-35 pièces)"]
  
  if XPVirus > 0 and XPMoi > 0 :
    for coup in Choix_coup:
      print(coup)
    print("À ton tour:")
    Choix = (input("\n→ "))
    if Choix == '1':
      print("Tu as lancé un Nunchaku au Virus. Il a perdu 10 XP")
      Coup1()
    elif Choix == '2':
      print("Tu as mis un Shuriken au Virus. Il a perdu 15 XP")
      Coup2()
    elif Choix == '3':
      if Pieces >= 35: 
        print("Tu as mis un super-coup au Virus. Il a perdu", Super_Coup,"XP")
        Coup3()
      else:
        print("tu n'as pas assez de pièces pour utiliser le super coup")
        Ninja()
    else:
      Invalid()
      Boxe_Thai()

  Ninja()

Menu_Principal()