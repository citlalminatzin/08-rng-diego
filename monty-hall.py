from random import random 

def create_game()->int:
    """Escoge la puerta ganadora"""
    puerta = random()
    if puerta < 1/3:
        return 1
    elif 1/3 <= puerta < 2/3:
        return 2
    else:
        return 3

def play_change(n:int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    exito = 0

    for _ in range(n):
        puerta_esc = create_game()
        puerta_gan = create_game()

        puertas_totales = [1, 2, 3]

        opciones_presentador = [p for p in puertas_totales if p != puerta_esc and p != puerta_gan]

        puerta_abierta = choice(opciones_presentador)

        puerta_final = [p for p in puertas_totales if p != puerta_esc and p != puerta_abierta][0]

        if puerta_final == puerta_gan:
            exito += 1

    return exito/n
        

def play_stay(n:int = 1000)->float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    exito = 0 
    for i in range(n):

        puerta_esc = create_game()
        puerta_gan = create_game()
        
        if puerta_esc == puerta_gan:
            exito += 1
    return exito / n


def main():
    n_juegos = 10000
    success_change = play_change(n_juegos)
    success_stay   = play_stay(n_juegos)
    
    print(f"Resultados de la simulación con n = {n_juegos}")
    print("---------------------------------------------")
    print(f"Tasa de éxito al QUEDARSE: {success_stay:.4f}")
    print(f"Tasa de éxito al CAMBIAR:  {success_change:.4f}")


if "__name__" == "__main__":
    main()