from requests_html import HTMLSession
from keep_alive import keep_alive
import datetime
from datetime import date
import time

s = HTMLSession()

url = "https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/date/product/101397570845/lang/en"

# Aca en elegir tenes que poner los partidos que queres buscar por numero(sin la M),
# por ejemplo los de argentina son 8, 24 y 39 (M8, M24 y M39)

elegir = [8, 24, 39, 50, 57]
partidosElegidos = []
partidosTotales = []


def descargarPartidos():
    r = s.get(url)
    partidosHTML = r.html.find('div.perf_details')

    for partidoHTML in partidosHTML:
        partidosTotales.append(partidoHTML.text)


def AñadirPartidos():
    for partido in elegir:
        partidosElegidos.append(partidosTotales[partido - 1])
        


# Consulta los datos y los imprime por consola, y envia un SMS si funk)
data = open("files/data.txt", "r")
f = data.readlines(5)
print(f)
conteo = 230



def consultarPartidos():
    now = datetime.datetime.now()
    print('Time: ' + now.strftime('%H:%M:%S UTC'))
    print("Scraps: " + str(conteo) + "\n")
    file = open("files/data.txt", "w")
    file.write('Time: ' + now.strftime('%H:%M:%S UTC')+"\nScraps: "+ str(conteo))
    file.close()
    i = 0
    while i < len(partidosElegidos):
        if partidosElegidos[i].find("Currently unavailable") != -1:
            print(f"partido M{elegir[i]} no disponible")
            i += 1
        else:
            now = datetime.datetime.now()
            print(f"partido M{elegir[i]} disponible")
            print(f"Hay entradas para el partido M{elegir[i]}. Dia {date.today()} a las {now.strftime('%H:%M:%S UTC')}")
            i += 1

descargarPartidos()
AñadirPartidos()
consultarPartidos()

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
