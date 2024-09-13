import random

# Variables iniciales
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
max_score = 23

# Pregunta al usuario cuántos jugadores habrá
num_players = int(input("¿Cuántos jugadores van a jugar? "))

# Inicialización de la lista de puntuaciones
scores = []

# Bucle principal para los jugadores
for player in range(1, num_players + 1):
    print(f"\nTurno del Jugador {player}")

    # Lanzamiento inicial
    input("Presiona Enter para lanzar los dados...")
    dice_roll = random.randint(1, 6) + random.randint(1, 6)
    score = dice_roll
    print(f"Primer lanzamiento: {dice_roll}. Puntaje total ahora: {score}")

    # Manejo del 12
    if score == 12:
        input("Presiona Enter para lanzar un dado adicional...")
        dice_roll = random.randint(1, 6)
        score += dice_roll
        print(f"Lanzamiento adicional: {dice_roll}. Puntaje total ahora: {score}")

    # Proceso de turnos
    while score <= max_score:
        action = input("¿Deseas lanzar de nuevo? (sí/no): ").strip().lower()
        
        if action == 'sí':
            dice_roll = random.randint(1, 6) + random.randint(1, 6)
            score += dice_roll
            print(f"Lanzamiento adicional: {dice_roll}. Puntaje total ahora: {score}")
            
            # Manejo del 12 después de lanzar nuevamente
            if score == 12:
                input("Presiona Enter para lanzar un dado adicional...")
                dice_roll = random.randint(1, 6)
                score += dice_roll
                print(f"Lanzamiento adicional: {dice_roll}. Puntaje total ahora: {score}")

            # Verifica si el jugador se pasó de 23
            if score > max_score:
                print("Te pasaste de 23.")
                break
        elif action == 'no':
            break
        else:
            print("Entrada no válida. Responde con 'sí' o 'no'.")

    # Manejo de dobles
    if score % 2 == 0:  # Asumimos que los dobles se presentan con puntajes pares para la simulación
        input("Presiona Enter para lanzar 3 dados adicionales...")
        dice_roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        score += dice_roll
        print(f"Lanzamiento de 3 dados adicionales: {dice_roll}. Puntaje total ahora: {score}")

    # Registra el puntaje del jugador
    scores.append((player, score))

# Determinación del ganador
winning_score = -1
winner = None

print("\nDeterminando el ganador...")
for player, score in scores:
    if score in primes:
        if score == max_score:
            print(f"El Jugador {player} ganó con el puntaje perfecto de 23!")
            winner = player
            break
    if score <= max_score and (winning_score < 0 or max_score - score < max_score - winning_score):
        winning_score = score
        winner = player

if winner is not None:
    print(f"\nEl ganador es el Jugador {winner} con el puntaje más cercano a 23 sin pasarse: {winning_score}")
else:
    print("No se determinó un ganador.")
