from requests_html import HTMLSession
from keep_alive import keep_alive
import datetime
from datetime import date
import time

s = HTMLSession()

urlFifa = "https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/101437163918/lang/en"
urlResale = 'https://resale-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/101437163918/lang/en'

# consulta directamente el text de availability
# def consultarTix():
#     r = s.get(url)
#     categ = r.html.find('td.quantity div')

#     for cat in categ:
#         print(cat.text)

def consultarFifa():
    r = s.get(urlFifa)
    categ = r.html.find('th.category.semantic-no-styling')
    print("FIFA CAT AVAILABILITY\n")
    for cat in categ:
        print(cat.text+"\n")

def consultarResale():
    r = s.get(urlResale)
    categ = r.html.find('th.category.semantic-no-styling')
    print("\n\nRESALE CAT AVAILABILITY\n")
    for cat in categ:
        print(cat.text+"\n")



data = open("files/data.txt", "r")
f = data.readlines(5)
conteo = 230



def printDatetime():
    now = datetime.datetime.now()
    print('Time: ' + now.strftime('%H:%M:%S UTC'))
    # print("Scraps: " + str(conteo) + "\n")
    # file = open("files/data.txt", "w")
    # file.write('Time: ' + now.strftime('%H:%M:%S UTC')+"\nScraps: "+ str(conteo))
    # file.close()        

printDatetime()
consultarFifa()
consultarResale()

# keep_alive()
# while (True):
#     now = datetime.datetime.now()
#     descargarPartidos()
#     AñadirPartidos()
#     consultarPartidos()
#     conteo += 1
#     if (conteo % 720 == 0):
#         print(
#             f"El botardo esta funcionando. Dia {date.today()} a las {now.strftime('%H:%M:%S')} UTC. Scraps: {conteo}")        
#     partidosElegidos = []
#     partidosTotales = []
#     time.sleep(60)
