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
    cantidadDeJugadores= 0
    jugadores= []
    while cantidadDeJugadores <= 8:
        nombreDeJugador= input("Ingrese el nombre y apellido del jugador: ")
        jugadores.append(nombreDeJugador)
        cantidadDeJugadores = cantidadDeJugadores + 1
    return jugadores


        
def cagarListaDeEquipos():
    equipo=[]
    nombreDeEquipo = input("Ingrese el nombre del equipo: ")
    contador= 0
    while nombreDeEquipo.upper() != "zzz".upper():
        jugadores = jugadoresDelEquipo()
        posicion = 0
        golesAfavor = 0
        golesEnContra = 0
        diferenciaDegol= 0
        puntaje = 0
        equipo.append([posicion, nombreDeEquipo.upper(), puntaje, golesAfavor, golesEnContra, diferenciaDegol, jugadores])
        print(equipo) 
        contador= contador + 1
        nombreDeEquipo = input("Ingrese el nombre del equipo: ")
    return equipo

def unPartido():
    contador = 1
    partido= []
    while contador < 2:
        local= input("Elija el equipo local: ")
        goles_equi_local= int(input("Ingrese la cantidad de goles que hizo el equipo local durante el partido: "))
        visitante= input("Elija el equipo visitante: ")
        goles_equi_visit= int(input("Ingrese la cantidad de goles que hizo el equipo visitante durante el partido: "))
        partido =[[local.upper(),goles_equi_local],[visitante.upper(),goles_equi_visit]]
        contador= contador + 1
    return partido
    

def resultados_partidos(equipos):
    list_resultados=[]
    length=len(equipos)/2
    contador= 1
    print("LISTA DE EQUIPOS")
    for x in equipos:
        print(x[1].upper())
    while contador <= length:
        match=unPartido()
        list_resultados.append(match)
        contador= contador + 1
    return list_resultados
        
def goles_favor(partidos,equipos):
    for x in equipos:
        for i in partidos:
            for h in i:
                if x[1] in h:
                    x[3]= x[3] + h[1]
    return equipos   

def goles_contra(partidos,equipos):
    for x in equipos:
        for i in partidos:
            if x[1] in i[0]:
                x[4]= i[1][1]
            elif x[1] in i[1]:
                x[4]= i[0][1]
    return equipos   

def diferencia_gol(equipos):
    diferencia= 0
    for x in equipos:
        diferencia = x[3]-x[4]
        x[5]= diferencia
    return equipos  

def puntaje(partidos,equipos):
    for x in equipos:
        for p in partidos:
            if x[1] in p[0]:
                if p[0][1] > p[1][1]:
                    x[0] = x[0]+3
                elif p[0][1] == p[1][1]:
                    x[0] = x[0]+1
            elif x[1] in p[1]:
                if p[1][1] > p[0][1]:
                    x[0] = x[0]+3
                elif p[0][1] == p[1][1]:
                    x[0] = x[0]+1
    return equipos

def posicion(equipos):
    equipos.sort(reverse=True)
    for x in range(1,len(equipos)+1):
        print(str(x) + " " +equipos[x-1][1])
        
def fecha(equipos):
    contador=int(input("Ingrese un numero del 1 al 7 para ver la fecha: "))
    while contador != 8:
        if contador == 1:
            print("Fecha 1")
            print(equipos[0][1]+ " vs "+equipos[4][1] )
            print(equipos[1][1]+ " vs "+equipos[5][1] )
            print(equipos[2][1]+ " vs "+equipos[6][1] )
            print(equipos[3][1]+ " vs "+equipos[7][1] )
                
        elif contador == 2:
            print("Fecha 2")
            print(equipos[0][1]+ " vs "+equipos[5][1] )
            print(equipos[1][1]+ " vs "+equipos[6][1] )
            print(equipos[2][1]+ " vs "+equipos[7][1] )
            print(equipos[3][1]+ " vs "+equipos[4][1] )
                
        elif contador == 3:
            print("Fecha 3")
            print(equipos[0][1]+ " vs "+equipos[6][1] )
            print(equipos[1][1]+ " vs "+equipos[7][1] )
            print(equipos[2][1]+ " vs "+equipos[4][1] )
            print(equipos[3][1]+ " vs "+equipos[5][1] )
                
        elif contador == 4:
            print("Fecha 4")
            print(equipos[0][1]+ " vs "+equipos[7][1] )
            print(equipos[1][1]+ " vs "+equipos[4][1] )
            print(equipos[2][1]+ " vs "+equipos[5][1] )
            print(equipos[3][1]+ " vs "+equipos[6][1] )
                
        elif contador == 5:
            print("Fecha 5")
            print(equipos[0][1]+ " vs "+equipos[1][1] )
            print(equipos[2][1]+ " vs "+equipos[3][1] )
            print(equipos[4][1]+ " vs "+equipos[5][1] )
            print(equipos[6][1]+ " vs "+equipos[7][1] )
                
        elif contador == 6:
            print("Fecha 6")
            print(equipos[0][1]+ " vs "+equipos[2][1] )
            print(equipos[1][1]+ " vs "+equipos[3][1] )
            print(equipos[5][1]+ " vs "+equipos[7][1] )
            print(equipos[4][1]+ " vs "+equipos[6][1] )
                
        elif contador == 7:
            print("Fecha 7")
            print(equipos[0][1]+ " vs "+equipos[3][1] )
            print(equipos[1][1]+ " vs "+equipos[2][1] )
            print(equipos[4][1]+ " vs "+equipos[7][1] )
            print(equipos[5][1]+ " vs "+equipos[6][1] )
        else:
            print("La fecha ingresada no existe")
        contador=int(input("Ingrese un numero del 1 al 7 para ver la fecha: "))  
#ejecuciones
#listEquipos= cagarListaDeEquipos()
listEquipos= [[0,"RIVER",0 , 0, 0, 0,[]],[0,"SAN LORENZO",0 , 0, 0, 0,[]],[0,"BOCA",0 , 0, 0, 0,[]],[0,"RACING",0 , 0, 0, 0,[]],[0,"ROSARIO CENTRAL",0 , 0, 0, 0,[]],[0,"INDEPENDIENTE",0 , 0, 0, 0,[]],[0,"ESTUDIANTES",0 , 0, 0, 0,[]],[0,"VELEZ",0 , 0, 0, 0,[]]]
matchs= [[['RIVER', 4], ['BOCA', 4]], [['RACING', 2], ['SAN LORENZO', 4]]]
#match=[['RIVER', 3], ['BOCA', 1]]
#matchs=resultados_partidos(listEquipos)
print(goles_favor(matchs,listEquipos))
#print(goles_contra(matchs,listEquipos))
gol_cont= goles_contra(matchs,listEquipos)

dif=diferencia_gol(gol_cont)
#print(puntaje(matchs,dif))
punt= puntaje(matchs,dif)
#listaDeEquipos= cagarListaDeEquipos()
#print(unPartido())
posicion(punt)

fecha(listEquipos)
