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
        equipo.append([nombreDeEquipo,posicion, puntaje, golesAfavor, golesEnContra, diferenciaDegol, jugadores])
        print(equipo) 
        contador= contador + 1
        nombreDeEquipo = input("Ingrese el nombre del equipo: ")
    return equipo

def unPartido():
    partido=[]
    contador = 1
    while contador < 2:
        local= input("Elija el equipo local: ")
        goles_equi_local= int(input("Ingrese la cantidad de goles que hizo el equipo local durante el partido: "))
        visitante= input("Elija el equipo visitante: ")
        goles_equi_visit= int(input("Ingrese la cantidad de goles que hizo el equipo visitante durante el partido: "))
        partido.append([[local,goles_equi_local],[visitante,goles_equi_visit]])
        contador= contador + 1
    return partido
    

def resultados_partidos(equipos):
    list_resultados=[]
    length=len(equipos)/2
    contador= 1
    print("LISTA DE EQUIPOS")
    for x in equipos:
        print(x[0].upper())
    while contador <= length:
        match=unPartido()
        list_resultados.append(match)
        contador= contador + 1
    return list_resultados
        
def estadisticas(partidos,equipos):
    for x in equipos:
        for i in partidos:
            for h in i:
                if x[0] in h:
                    print("hola")
                    x[3]= x[3] + h[1]
                    print(x[3])
            
    return equipos       

#ejecuciones
#listEquipos= cagarListaDeEquipos()
listEquipos= [["river",0 , 0, 0, 0, 0,[]],["san lorenzo",0 , 0, 0, 0, 0,[]],["boca",0 , 0, 0, 0, 0,[]],["racing",0 , 0, 0, 0, 0,[]]]
matchs= [[['river', 2], ['boca', 2]], [['racing', 1], ['san lorenzo', 1]]]
#print(resultados_partidos(listEquipos))
print(estadisticas(matchs,listEquipos))
#listaDeEquipos= cagarListaDeEquipos()
#print(unPartido())


