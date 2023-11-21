"""
● Carga de datos en una lista para cada una de las entidades relacionados al tema elegido
● Incluir tanto el uso de las estructuras de control while y for.
● Incluir el uso de condicionales con If elif else.
● Incluir el uso de funciones con "return".
● Incluir al menos 2 reportes o listados de las entidades cargadas.
● Incluir cálculo de promedio, de mayor y de menor.
● Uso un menú sencillo (de un solo nivel)
● Incluir comentarios en el código fuente a modo de ayuda
"""
def jugadoresDelEquipo():
    #Con el input se ingresan los nombres de los jugadores por teclado y con el while almacenamos cada ingreso en una lista, luego retornamos dicha lista
    cantidadDeJugadores= 1
    jugadores= []
    while cantidadDeJugadores <= 5:
        nombreDeJugador= input("Ingrese el nombre o apodo del jugador: ")
        if nombreDeJugador !="":
            jugadores.append(nombreDeJugador.upper())
            cantidadDeJugadores = cantidadDeJugadores + 1
        else:
            print("No ingresó ningún nombre o apodo")
    return jugadores


        
def cargarListaDeEquipos():
    equipo=[]
    contador= 1
    #creamos los equipos, usando la funcion para cargar los nombres de los jugadores
    while contador <= 2:
        nombreDeEquipo = input("Ingrese el nombre del equipo: ")
        #nos aseguramos con el dato ingresado por teclado no este vacio
        if nombreDeEquipo != "":
            players= jugadoresDelEquipo()
            if len(players)>0:
                equipo.append([nombreDeEquipo.upper(), players])
            else:
                print("No se han cargado los datos de los jugadores") 
            contador= contador + 1
        else:
            print("No ingresó el nombre de su equipo")
    return equipo

def unPartido(equipos):
    contador = 1
    partido= []
    #cargamos los resultados de los partidos, pero antes nos aseguramos que la informacion del equipo este cargada
    if len(equipos)>0:
        local= equipos[0][0]
        goles_equi_local= int(input("Ingrese la cantidad de goles que hizo "+local+" durante el partido: "))
        visitante= equipos[1][0]
        goles_equi_visit= int(input("Ingrese la cantidad de goles que hizo "+visitante+" durante el partido: "))
        partido =[[local.upper(),goles_equi_local],[visitante.upper(),goles_equi_visit]]
        contador= contador + 1
    else:
        print("No se han cargado los datos del equipo")
    return partido

def resultados_partidos(equipos):
    #cargamos la informacion de cada partido jugado usando la funcion unPartido() para poder almacenarlos en una lista, antes nos aseguramos de preguntar al usuario cuanto partidos se jugaron, y nos aeguramos que la respuesta sea un dato numerico.
    list_resultados=[]
    contador= 1
    partidos= input("Cuántos partidos jugaron: ")
    num = "0123456789"
    cantidad=int(num)
    if partidos in num:
        cantidad = int(partidos)
        while contador <= cantidad:
            match= unPartido(equipos)
            list_resultados.append(match)
            contador= contador + 1
    else:    
        print("El valor ingresado no es un número por favor intente nuevamente")
    return list_resultados
def cantiPartidosGanados(matches):
    suma=0
    suma1=0
    if len(matches)>0:
        for x in matches:
            if x[0][1]> x[1][1]:
                suma=suma+1
            elif x[0][1]< x[1][1]:
                suma1=suma1+1
        print(x[1][0]+" ganó "+ str(suma1) + " partidos")
        print(x[0][0]+" ganó "+ str(suma) + " partidos")   
    else:
        print("No hay información de partidos cargados")
def promedioGoles(matches):
    #Esta funcion retorna el promedio de gol que hay por partido, de esta manera el usuario podra formar su propia espectativa
    suma= 0
    if len(matches)>0:
        for x in matches:
            for i in x:
                suma= suma + i[1]
        promedio= suma/len(matches)
        return "El promedio de goles por partido es: " + str(promedio) + " goles"
    else:
        print("No hay información de partidos cargados")

def equipoMas_goles(matches):
    #Esta funcion retorna al equipo que hizo mas goles en todos los partidos
    suma=0
    suma1=0
    if len(matches)>0:
        for x in matches:   
            suma=suma+x[0][1]
            suma1=suma1+x[1][1]
        if suma1 > suma:
            print(x[1][0]+" es el equipo con más goles, hizo "+ str(suma1) + " en total")
        else:
            print(x[0][0]+" es el equipo con más goles, hizo "+ str(suma) + " en total")
    else:
        print("No hay información de partidos cargados")

def equipoMenos_goles(matches):
     #Esta funcion retorna al equipo que hizo mas goles en todos los partidos
    suma=0
    suma1=0
    if len(matches)>0:
        for x in matches:
            suma=suma+x[0][1]
            suma1=suma1+x[1][1]
        if suma1 < suma:
            print(x[1][0]+" es el equipo con menos goles, hizo "+ str(suma1) + " en total")
        else:
            print(x[0][0]+" es el equipo con menos goles, hizo "+ str(suma) + " en total")        
    else:
        print("No hay información de partidos cargados")
     
def exportar_a_excel(lista_datos, nombre_archivo):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Encabezados
    for equi in lista_datos:
        sheet.append([equi[0]])
    # Datos
        for datos in equi[1]:
            sheet.append([datos])

    # Guardar el archivo
    workbook.save(nombre_archivo)
    return nombre_archivo

def enviaremail(excel):
    yag= yagmail.SMTP(user= os.getenv("USER"), password = os.getenv("PASSWORD"))

    listaDedestinatarios= []
    #a medida que el usuario ingrese los mails, los se iran guardando en una lista, hasta que ingrese "zzz"
    destinatario= input("Ingrese su correo electronico: ").lower()
    while destinatario != "zzz":
        listaDedestinatarios.append(destinatario)
        destinatario= input("Ingrese su correo electronico: ").lower()    
    asunto = "Partidos entre amigos"
    mensaje= "Resultados"
    imagen= ".\Captura de pantalla 2023-11-17 012507.jpg "
    archivo= "./futbolAmigos - copia.zip"
    informe= "./2023_TPFI_Com17_ElizabethTaboada.docx"
    codigo="./sistema_de_partidos_de _futbol_amigos.docx"
    #por parametros enviamos lo que queremos mandar al mail
    yag.send(listaDedestinatarios, asunto, [mensaje, imagen], attachments=[archivo,excel, informe, codigo])

def opcionesMenu():
    #Definimos una funcion de opciones para luego poder invocarle en el menu
    print("1-Lista de equipos")
    print("2-Resultados de partidos")
    print("3-Cantidad de partidos ganados por cada equipo")
    print("4-Promedio de goles por partido")
    print("5-Equipo con más goles")
    print("6-Equipo con menos goles")
    print("7-Enviar información de los partidos por mail")
    print("8-SALIR")

#definimos la funcion menu que recibe por parametro la lista de equipos y la lista de partidos
def menu(list_equipos,partidos):
    opcionesMenu()
    opciones= input("Ingrese una opción del menú: ")
    while opciones != "8":
        if opciones == "1": 
            print(" ")
            if len(list_equipos)>0:#nos aseguramos que la lista de equipos no este vacia para poder mostrarla de una forma ordenada, en caso de estar vaca, devuelve un mensaje de error
                for i in list_equipos:
                    print(i[0])
                    for x in i[1]:
                        print(x)
            else:
                print("No se han cargado los datos del equipo")
            print(" ")
        elif opciones == "2":
            print(" ")
            if len(partidos)>1:#nos aseguramos que la lista de partidos no este vacio para poder mostrarla de forma ordenada, en caso de estar vacio devolvera un mensaje de error
                for x in partidos:
                    print(x[0][0]+ ": "+str(x[0][1])+ " vs " + x[1][0]+ ": "+str(x[1][1]))
            else:
                print("No hay información de partidos cargados")
            print(" ")
        elif opciones == "3":
            print(" ")
            cantiPartidosGanados(partidos)
            print(" ")
        elif opciones == "4":
            print(" ")
            print(promedioGoles(partidos))
            print(" ")
        elif opciones == "5":
            print(" ")
            equipoMas_goles(partidos)
            print(" ")
        elif opciones == "6":
            print(" ")
            equipoMenos_goles(partidos)
            print(" ")
        elif opciones == "7":
            print(" ")
            print("La carga de mails finaliza cuando se ingrese 'zzz'")
            exportarEquipos= exportar_a_excel(list_equipos,"equipos.xlsx")
            enviaremail(exportarEquipos)
            print("El mail fue enviado con éxito")
            print(" ")
        else:
            print(" ")
            print("La opción ingresada no corresponde al menú")
            print(" ")
        opcionesMenu()
        opciones= input("Ingrese una opción del menú: ")
#ejecuciones

listaDeEquipos=cargarListaDeEquipos()
dopartis= resultados_partidos(listaDeEquipos)

import openpyxl  
import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

#antes de ejecutar el menu nos aseguramos de que toda la informacion esta cargada correctamente, caso contrario, el usuaio cuenta con la opcion de volver a ingresar todo nuevamente
if len(dopartis)>0 and len(listaDeEquipos)>0:
    menu(listaDeEquipos,dopartis)
else:
    recargar_Equipos=cargarListaDeEquipos()
    recargar_partidos=resultados_partidos(recargar_Equipos)
    menu(recargar_Equipos,recargar_partidos)