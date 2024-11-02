print("BIENVENIDOS A PIEDRA, PAPEL O TIJERAS")
print("JUGADOR 1 ESCOJA ENTRE PIEDRA PAPEL O TIJERAS")
jugador1 = input("yo escojo: ").lower()
print("JUGADOR 2 ESCOJA ENTRE PIEDRA PAPEL O TIJERAS")
jugador2 = input("yo escojo: ").lower()

if jugador1 == jugador2:
    print("empate")
elif (jugador1 == ("piedra") and jugador2 == ("tijera") ) or (jugador1 == ("papel") and jugador2 == ("piedra")) or (jugador1 == ("tijera") and jugador2 == ("papel")):
    print('GANADOR jugador 1!',)
else:
    print('GANADOR jugador 2!',)
