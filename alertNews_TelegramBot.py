#Code mis à jour la dernière fois le 06.10.2019
#Pour vérifier le contenu de la table :
# "use NomBaseDeDonnée" et ensuite "select date_detection, url from tableLiens;"

import feedparser
import requests
import time
import schedule
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(host="",user="",password="", database="")
cursor = conn.cursor()
#conn.close()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tableLiens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_detection DATETIME,
    url VARCHAR(300)
);
""")

def telegram_bot_sendtext(bot_message):

    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def check_alert():

    #On récupère le RSS
    d = feedparser.parse('VOTRE-LIEN-XML')
    #On récupère la date et l'heure et on la formate
    dateBrut = datetime.now()
    timeNow = dateBrut.strftime('%Y-%m-%d %H:%M:%S')

    #DEBUG
    #print("Début de la vérification des topics")
    for i in range(0,25):
      titre = d.entries[i].title
      lien = d.entries[i].link
      #Formate le titre pour la détection de mots clés
      formatitre = titre.lower()
      res = formatitre.split()
      #DEBUG
      #print(res)
      #Récupère tous les éléments de notre table
      cursor.execute('SELECT url FROM tableLiens')
      alltableliens = cursor.fetchall()
      #Formate le lien pour le mettre dans la forme qu'il sort de la BDD
      mylink = "('{}',)"
      my_formatlink = mylink.format(lien)

      if ('[alerte]' in res and "l’iran" in res or
         '[alerte' in res and "l’iran" in res or
         'alerte' in res and "l’iran" in res or
         'alerte!' in res and "l’iran" in res or
         '[alerte]' in res and "l'iran" in res or
         '[alerte' in res and "l'iran" in res or
         'alerte' in res and "l'iran" in res or
         'alerte!' in res and "l'iran" in res or
         '[alerte]' in res and "iran" in res or
         '[alerte' in res and "iran" in res or
         'alerte' in res and "iran" in res or
         'alerte!' in res and "iran" in res or
         '[alerte]' in res and "attentat" in res or
         '[alerte' in res and "attentat" in res or
         'alerte' in res and "attentat" in res or
         'alerte!' in res and "attentat" in res or
         '[alerte]' in res and "tuerie" in res or
         '[alerte' in res and "tuerie" in res or
         'alerte' in res and "tuerie" in res or
         'alerte!' in res and "tuerie" in res or
         '[alerte]' in res and "militaire" in res or
         '[alerte' in res and "militaire" in res or
         'alerte' in res and "militaire" in res or
         'alerte!' in res and "militaire" in res or
         '[alerte]' in res and "militaires" in res or
         '[alerte' in res and "militaires" in res or
         'alerte' in res and "militaires" in res or
         'alerte!' in res and "militaires" in res or
         '[alerte]' in res and "pape" in res or
         '[alerte' in res and "pape" in res or
         'alerte' in res and "pape" in res or
         'alerte!' in res and "pape" in res or
         '[alerte]' in res and "bombe" in res or
         '[alerte' in res and "bombe" in res or
         'alerte' in res and "bombe" in res or
         'alerte!' in res and "bombe" in res or
         '[alerte]' in res and "bombes" in res or
         '[alerte' in res and "bombes" in res or
         'alerte' in res and "bombes" in res or
         'alerte!' in res and "bombes" in res or
         '[alerte]' in res and "terroriste" in res or
         '[alerte' in res and "terroriste" in res or
         'alerte' in res and "terroriste" in res or
         'alerte!' in res and "terroriste" in res or
         '[alerte]' in res and "terroristes" in res or
         '[alerte' in res and "terroristes" in res or
         'alerte' in res and "terroristes" in res or
         'alerte!' in res and "terroristes" in res or
         '[alerte]' in res and "guerre" in res or
         '[alerte' in res and "guerre" in res or
         'alerte' in res and "guerre" in res or
         'alerte!' in res and "guerre" in res or
         '[alerte]' in res and "tempête" in res or
         '[alerte' in res and "tempête" in res or
         'alerte' in res and "tempête" in res or
         'alerte!' in res and "tempête" in res or
         '[alerte]' in res and "orage" in res or
         '[alerte' in res and "orage" in res or
         'alerte' in res and "orage" in res or
         'alerte!' in res and "orage" in res or
         '[alerte]' in res and "orages" in res or
         '[alerte' in res and "orages" in res or
         'alerte' in res and "orages" in res or
         'alerte!' in res and "orages" in res or
         '[alerte]' in res and "tempete" in res or
         '[alerte' in res and "tempete" in res or
         'alerte' in res and "tempete" in res or
         'alerte!' in res and "tempete" in res or
         '[alerte]' in res and "canicule" in res or
         '[alerte' in res and "canicule" in res or
         'alerte' in res and "canicule" in res or
         'alerte!' in res and "canicule" in res or
         '[alerte]' in res and "température" in res or
         '[alerte' in res and "température" in res or
         'alerte' in res and "température" in res or
         'alerte!' in res and "température" in res or
         '[alerte]' in res and "températures" in res or
         '[alerte' in res and "températures" in res or
         'alerte' in res and "températures" in res or
         'alerte!' in res and "températures" in res or
         '[alerte]' in res and "tremblement" in res or
         '[alerte' in res and "tremblement" in res or
         'alerte' in res and "tremblement" in res or
         'alerte!' in res and "tremblement" in res or
         '[alerte]' in res and "séisme" in res or
         '[alerte' in res and "séisme" in res or
         'alerte' in res and "séisme" in res or
         'alerte!' in res and "séisme" in res or
         '[alerte]' in res and "séismes" in res or
         '[alerte' in res and "séismes" in res or
         'alerte' in res and "séismes" in res or
         'alerte!' in res and "séismes" in res or
         '[alerte]' in res and "crise" in res or
         '[alerte' in res and "crise" in res or
         'alerte' in res and "crise" in res or
         'alerte!' in res and "crise" in res or
         '[alerte]' in res and "big" in res or
         '[alerte' in res and "big" in res or
         'alerte' in res and "big" in res or
         'alerte!' in res and "big" in res or
         '[alerte]' in res and "explosion" in res or
         '[alerte' in res and "explosion" in res or
         'alerte' in res and "explosion" in res or
         'alerte!' in res and "explosion" in res or
         '[alerte]' in res and "banque" in res or
         '[alerte' in res and "banque" in res or
         'alerte' in res and "banque" in res or
         'alerte!' in res and "banque" in res or
         '[alerte]' in res and "fusillade" in res or
         '[alerte' in res and "fusillade" in res or
         'alerte' in res and "fusillade" in res or
         'alerte!' in res and "fusillade" in res or
         '[alerte]' in res and "fusillades" in res or
         '[alerte' in res and "fusillades" in res or
         'alerte' in res and "fusillades" in res or
         'alerte!' in res and "fusillades" in res or
         '[alerte]' in res and "faille" in res or
         '[alerte' in res and "faille" in res or
         'alerte' in res and "faille" in res or
         'alerte!' in res and "faille" in res or
         '[alerte]' in res and "ovni" in res or
         '[alerte' in res and "ovni" in res or
         'alerte' in res and "ovni" in res or
         'alerte!' in res and "ovni" in res or
         '[alerte]' in res and "trump" in res or
         '[alerte' in res and "trump" in res or
         'alerte' in res and "trump" in res or
         'alerte!' in res and "trump" in res or
         '[alerte]' in res and "poutine" in res or
         '[alerte' in res and "poutine" in res or
         'alerte' in res and "poutine" in res or
         'alerte!' in res and "poutine" in res or
         '[alerte]' in res and "erdogan" in res or
         '[alerte' in res and "erdogan" in res or
         'alerte' in res and "erdogan" in res or
         'alerte!' in res and "erdogan" in res or
         '[alerte]' in res and "musk" in res or
         '[alerte' in res and "musk" in res or
         'alerte' in res and "musk" in res or
         'alerte!' in res and "musk" in res or
         '[alerte]' in res and "tesla" in res or
         '[alerte' in res and "tesla" in res or
         'alerte' in res and "tesla" in res or
         'alerte!' in res and "tesla" in res or
         '[alerte]' in res and "crash" in res or
         '[alerte' in res and "crash" in res or
         'alerte' in res and "crash" in res or
         'alerte!' in res and "crash" in res or
         '[alerte]' in res and "avion" in res or
         '[alerte' in res and "avion" in res or
         'alerte' in res and "avion" in res or
         'alerte!' in res and "avion" in res or
         '[alerte]' in res and "d'avion" in res or
         '[alerte' in res and "d'avion" in res or
         'alerte' in res and "d'avion" in res or
         'alerte!' in res and "d'avion" in res or
         '[alerte]' in res and "avions" in res or
         '[alerte' in res and "avions" in res or
         'alerte' in res and "avions" in res or
         'alerte!' in res and "avions" in res or
         '[alerte]' in res and "disparition" in res or
         '[alerte' in res and "disparition" in res or
         'alerte' in res and "disparition" in res or
         'alerte!' in res and "disparition" in res or
         '[alerte]' in res and "messie" in res or
         '[alerte' in res and "messie" in res or
         'alerte' in res and "messie" in res or
         'alerte!' in res and "messie" in res or
         '[alerte]' in res and "météorite" in res or
         '[alerte' in res and "météorite" in res or
         'alerte' in res and "météorite" in res or
         'alerte!' in res and "météorite" in res or
         '[alerte]' in res and "astéroide" in res or
         '[alerte' in res and "astéroide" in res or
         'alerte' in res and "astéroide" in res or
         'alerte!' in res and "astéroide" in res or
         '[alerte]' in res and "astéroïde " in res or
         '[alerte' in res and "astéroïde " in res or
         'alerte' in res and "astéroïde " in res or
         'alerte!' in res and "astéroïde " in res or
         '[alerte]' in res and "satellite" in res or
         '[alerte' in res and "satellite" in res or
         'alerte' in res and "satellite" in res or
         'alerte!' in res and "satellite" in res or
         '[alerte]' in res and "espace" in res or
         '[alerte' in res and "espace" in res or
         'alerte' in res and "espace" in res or
         'alerte!' in res and "espace" in res or
         '[alerte]' in res and "spacex" in res or
         '[alerte' in res and "spacex" in res or
         'alerte' in res and "spacex" in res or
         'alerte!' in res and "spacex" in res or
         '[alerte]' in res and "russie" in res or
         '[alerte' in res and "russie" in res or
         'alerte' in res and "russie" in res or
         'alerte!' in res and "russie" in res or
         '[alerte]' in res and "russe" in res or
         '[alerte' in res and "russe" in res or
         'alerte' in res and "russe" in res or
         'alerte!' in res and "russe" in res or
         '[alerte]' in res and "turquie" in res or
         '[alerte' in res and "turquie" in res or
         'alerte' in res and "turquie" in res or
         'alerte!' in res and "turquie" in res or
         '[alerte]' in res and "usa" in res or
         '[alerte' in res and "usa" in res or
         'alerte' in res and "usa" in res or
         'alerte!' in res and "usa" in res or
         '[alerte]' in res and "israel" in res or
         '[alerte' in res and "israel" in res or
         'alerte' in res and "israel" in res or
         'alerte!' in res and "israel" in res or
         '[alerte]' in res and "israël" in res or
         '[alerte' in res and "israël" in res or
         'alerte' in res and "israël" in res or
         'alerte!' in res and "israël" in res or
         '[alerte]' in res and "chine" in res or
         '[alerte' in res and "chine" in res or
         'alerte' in res and "chine" in res or
         'alerte!' in res and "chine" in res or
         '[alerte]' in res and "chinois" in res or
         '[alerte' in res and "chinois" in res or
         'alerte' in res and "chinois" in res or
         'alerte!' in res and "chinois" in res or
         '[alerte]' in res and "google" in res or
         '[alerte' in res and "google" in res or
         'alerte' in res and "google" in res or
         'alerte!' in res and "google" in res or
         '[alerte]' in res and "gafa" in res or
         '[alerte' in res and "gafa" in res or
         'alerte' in res and "gafa" in res or
         'alerte!' in res and "gafa" in res or
         '[alerte]' in res and "économique" in res or
         '[alerte' in res and "économique" in res or
         'alerte' in res and "économique" in res or
         'alerte!' in res and "économique" in res or
         '[alerte]' in res and "bourse" in res or
         '[alerte' in res and "bourse" in res or
         'alerte' in res and "bourse" in res or
         'alerte!' in res and "bourse" in res or
         '[alerte]' in res and "deutsche" in res or
         '[alerte' in res and "deutsche" in res or
         'alerte' in res and "deutsche" in res or
         'alerte!' in res and "deutsche" in res or
         '[alerte]' in res and "faillite" in res or
         '[alerte' in res and "faillite" in res or
         'alerte' in res and "faillite" in res or
         'alerte!' in res and "faillite" in res or
         '[alerte]' in res and "wall" in res and "street" in res or
         '[alerte' in res and "wall" in res and "street" in res or
         'alerte' in res and "wall" in res and "street" in res or
         'alerte!' in res and "wall" in res and "street" in res or
         '[alerte]' in res and "chimique" in res or
         '[alerte' in res and "chimique" in res or
         'alerte' in res and "chimique" in res or
         'alerte!' in res and "chimique" in res or
         '[alerte]' in res and "chimiques" in res or
         '[alerte' in res and "chimiques" in res or
         'alerte' in res and "chimiques" in res or
         'alerte!' in res and "chimiques" in res or
         '[alerte]' in res and "radioactive" in res or
         '[alerte' in res and "radioactive" in res or
         'alerte' in res and "radioactive" in res or
         'alerte!' in res and "radioactive" in res or
         '[alerte]' in res and "radioactif" in res or
         '[alerte' in res and "radioactif" in res or
         'alerte' in res and "radioactif" in res or
         'alerte!' in res and "radioactif" in res or
         '[alerte]' in res and "nucléaire" in res or
         '[alerte' in res and "nucléaire" in res or
         'alerte' in res and "nucléaire" in res or
         'alerte!' in res and "nucléaire" in res or
         '[alerte]' in res and "pandémie" in res or
         '[alerte' in res and "pandémie" in res or
         'alerte' in res and "pandémie" in res or
         'alerte!' in res and "pandémie" in res or
         '[alerte]' in res and "pandemie" in res or
         '[alerte' in res and "pandemie" in res or
         'alerte' in res and "pandemie" in res or
         'alerte!' in res and "pandemie" in res or
         '[alerte]' in res and "incendie" in res or
         '[alerte' in res and "incendie" in res or
         'alerte' in res and "incendie" in res or
         'alerte!' in res and "incendie" in res or
         '[alerte]' in res and "incendies" in res or
         '[alerte' in res and "incendies" in res or
         'alerte' in res and "incendies" in res or
         'alerte!' in res and "incendies" in res or
         '[alerte]' in res and "bitcoin" in res or
         '[alerte' in res and "bitcoin" in res or
         'alerte' in res and "bitcoin" in res or
         'alerte!' in res and "bitcoin" in res or
         '[alerte]' in res and "btc" in res or
         '[alerte' in res and "btc" in res or
         'alerte' in res and "btc" in res or
         'alerte!' in res and "btc" in res or
         '[alerte]' in res and "malware" in res or
         '[alerte' in res and "malware" in res or
         'alerte' in res and "malware" in res or
         'alerte!' in res and "malware" in res or
         '[alerte]' in res and "virus" in res or
         '[alerte' in res and "virus" in res or
         'alerte' in res and "virus" in res or
         'alerte!' in res and "virus" in res or
         '[alerte]' in res and "bactérie" in res or
         '[alerte' in res and "bactérie" in res or
         'alerte' in res and "bactérie" in res or
         'alerte!' in res and "bactérie" in res or
         '[alerte]' in res and "bactéries" in res or
         '[alerte' in res and "bactéries" in res or
         'alerte' in res and "bactéries" in res or
         'alerte!' in res and "bactéries" in res or
         '[alerte]' in res and "missile" in res or
         '[alerte' in res and "missile" in res or
         'alerte' in res and "missile" in res or
         'alerte!' in res and "missile" in res or
         '[alerte]' in res and "missiles" in res or
         '[alerte' in res and "missiles" in res or
         'alerte' in res and "missiles" in res or
         'alerte!' in res and "missiles" in res or
         '[alerte]' in res and "ia" in res or
         '[alerte' in res and "ia" in res or
         'alerte' in res and "ia" in res or
         'alerte!' in res and "ia" in res or
         '[alerte]' in res and "contamination" in res or
         '[alerte' in res and "contamination" in res or
         'alerte' in res and "contamination" in res or
         'alerte!' in res and "contamination" in res or
         '[alerte]' in res and "éruption" in res or
         '[alerte' in res and "éruption" in res or
         'alerte' in res and "éruption" in res or
         'alerte!' in res and "éruption" in res or
         '[alerte]' in res and "soleil" in res or
         '[alerte' in res and "soleil" in res or
         'alerte' in res and "soleil" in res or
         'alerte!' in res and "soleil" in res or
         '[alerte]' in res and "robot" in res or
         '[alerte' in res and "robot" in res or
         'alerte' in res and "robot" in res or
         'alerte!' in res and "robot" in res or
         '[alerte]' in res and "yellowstone" in res or
         '[alerte' in res and "yellowstone" in res or
         'alerte' in res and "yellowstone" in res or
         'alerte!' in res and "yellowstone" in res or
         '[alerte]' in res and "fuite" in res or
         '[alerte' in res and "fuite" in res or
         'alerte' in res and "fuite" in res or
         'alerte!' in res and "fuite" in res or
         '[alerte]' in res and "tsunami" in res or
         '[alerte' in res and "tsunami" in res or
         'alerte' in res and "tsunami" in res or
         'alerte!' in res and "tsunami" in res or
         '[alerte]' in res and "sécheresse" in res or
         '[alerte' in res and "sécheresse" in res or
         'alerte' in res and "sécheresse" in res or
         'alerte!' in res and "sécheresse" in res or
         '[alerte]' in res and "ouragan" in res or
         '[alerte' in res and "ouragan" in res or
         'alerte' in res and "ouragan" in res or
         'alerte!' in res and "ouragan" in res or
         '[alerte]' in res and "cyclone" in res or
         '[alerte' in res and "cyclone" in res or
         'alerte' in res and "cyclone" in res or
         'alerte!' in res and "cyclone" in res or
         '[alerte]' in res and "hack" in res or
         '[alerte' in res and "hack" in res or
         'alerte' in res and "hack" in res or
         'alerte!' in res and "hack" in res or
         '[alerte]' in res and "hackeur" in res or
         '[alerte' in res and "hackeur" in res or
         'alerte' in res and "hackeur" in res or
         'alerte!' in res and "hackeur" in res or
         '[alerte]' in res and "blackout" in res or
         '[alerte' in res and "blackout" in res or
         'alerte' in res and "blackout" in res or
         'alerte!' in res and "blackout" in res or
         '[alerte]' in res and "panne" in res or
         '[alerte' in res and "panne" in res or
         'alerte' in res and "panne" in res or
         'alerte!' in res and "panne" in res or
         '[alerte]' in res and "ethereum" in res or
         '[alerte' in res and "ethereum" in res or
         'alerte' in res and "ethereum" in res or
         'alerte!' in res and "ethereum" in res):
              #numItem permet dans notre boucle le même nombre de fois qu'il y a de lien déjà inséré dedans
              print ("Un mot sensible a été détecté")
              numItem = 0
              insertCheck = False

              for value in alltableliens:
                #DEBUG
                #print(numItem)
                #print(my_formatlink)
                #print(alltableliens[numItem])
                if my_formatlink==str(alltableliens[numItem]):
                    insertCheck = True
                numItem +=1

              if insertCheck == True:
                  print ("Topic déjà envoyé sur Telegramm (" + titre + ")")
              if insertCheck == False:
                  print ("Ajout de l'URL dans la BDD... ("+lien+")")
                  cursor.execute("INSERT INTO tableLiens (date_detection, url) VALUES(%s, %s)", (timeNow, lien))
                  conn.commit()
                  myPhrase = "{}\n({})"
                  my_message = myPhrase.format(titre, lien)
                  print ("Envoi du topic sur telegramm (" + titre + ")")
                  telegram_bot_sendtext(my_message)

#A voir le temps (1min, 85sec, 2min...) entre chaque vérification pour ne pas permettre trop de fausses alertes (sachant que les topics fakes coulent généralement très vite)
schedule.every(2).minutes.do(check_alert)
#DEBUG
#schedule.every(85).seconds.do(check_alert)

while True:
    schedule.run_pending()
    time.sleep(1)