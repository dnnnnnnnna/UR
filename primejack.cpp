#include <iostream>
#include <cstdlib> // Para rand() y srand()
#include <ctime>   // Para time()
#include <vector>
#include <algorithm> // Para std::find

using namespace std;

int main() {
    srand(time(0)); // Inicializa la semilla para los números aleatorios

    // Variables iniciales
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23};
    const int max_score = 23;
    int num_players;

    // Pregunta al usuario cuántos jugadores habrá
    cout << "¿Cuántos jugadores van a jugar? ";
    cin >> num_players;

    vector<pair<int, int>> scores; // Almacena el número de jugador y su puntaje
    bool prime_winner_found = false; // Bandera para detectar si ya hay un ganador con número primo

    // Bucle principal para los jugadores
    for (int player = 1; player <= num_players; ++player) {
        if (prime_winner_found) {
            // Si ya hay un ganador con número primo, se detiene el juego
            break;
        }

        cout << "\nTurno del Jugador " << player << endl;

        // Lanzamiento inicial
        cout << "Presiona Enter para lanzar los dados...";
        cin.ignore();
        cin.get();

        int dice_roll = rand() % 6 + 1 + rand() % 6 + 1;
        int score = dice_roll;
        cout << "Primer lanzamiento: " << dice_roll << ". Puntaje total ahora: " << score << endl;

        // Manejo del 12
        if (score == 12) {
            cout << "Presiona Enter para lanzar un dado adicional...";
            cin.get();
            dice_roll = rand() % 6 + 1;
            score += dice_roll;
            cout << "Lanzamiento adicional: " << dice_roll << ". Puntaje total ahora: " << score << endl;
        }

        // Proceso de turnos
        while (score <= max_score) {
            string action;
            cout << "¿Deseas lanzar de nuevo? (sí/no): ";
            cin >> action;

            if (action == "sí") {
                dice_roll = rand() % 6 + 1 + rand() % 6 + 1;
                score += dice_roll;
                cout << "Lanzamiento adicional: " << dice_roll << ". Puntaje total ahora: " << score << endl;

                // Manejo del 12 después de lanzar nuevamente
                if (score == 12) {
                    cout << "Presiona Enter para lanzar un dado adicional...";
                    cin.ignore();
                    cin.get();
                    dice_roll = rand() % 6 + 1;
                    score += dice_roll;
                    cout << "Lanzamiento adicional: " << dice_roll << ". Puntaje total ahora: " << score << endl;
                }

                // Verifica si el jugador se pasó de 23
                if (score > max_score) {
                    cout << "Te pasaste de 23." << endl;
                    break;
                }
            } else if (action == "no") {
                break;
            } else {
                cout << "Entrada no válida. Responde con 'sí' o 'no'." << endl;
            }
        }

        // Manejo de dobles
        if (score % 2 == 0) { // Asumimos que los dobles se presentan con puntajes pares para la simulación
            cout << "Presiona Enter para lanzar 3 dados adicionales...";
            cin.ignore();
            cin.get();
            dice_roll = rand() % 6 + 1 + rand() % 6 + 1 + rand() % 6 + 1;
            score += dice_roll;
            cout << "Lanzamiento de 3 dados adicionales: " << dice_roll << ". Puntaje total ahora: " << score << endl;
        }

        // Verificar si el jugador tiene un número primo y detener el juego si es así
        if (find(primes.begin(), primes.end(), score) != primes.end()) {
            cout << "¡El Jugador " << player << " obtuvo un número primo (" << score << ") y gana automáticamente!" << endl;
            prime_winner_found = true;
            break;
        }

        // Registra el puntaje del jugador
        scores.push_back(make_pair(player, score));
    }

    // Si ningún jugador ha sacado un número primo, determina el ganador por el puntaje más cercano a 23
    if (!prime_winner_found) {
        int winning_score = -1;
        int winner = -1;

        cout << "\nDeterminando el ganador..." << endl;
        for (int i = 0; i < scores.size(); ++i) {
            int player = scores[i].first;
            int score = scores[i].second;

            if (score <= max_score && (winning_score < 0 || max_score - score < max_score - winning_score)) {
                winning_score = score;
                winner = player;
            }
        }

        if (winner != -1) {
            cout << "\nEl ganador es el Jugador " << winner << " con el puntaje más cercano a 23 sin pasarse: " << winning_score << endl;
        } else {
            cout << "No se determinó un ganador." << endl;
        }
    }

    return 0;
}
