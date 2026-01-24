# mi_primer_script.py

"¡Hola, GitHub!"


def obtener_primos(limite):
    # Creamos una lista de booleanos asumiendo que todos son primos inicialmente
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # El 0 y el 1 no son primos

    # Aplicamos el algoritmo de la Criba de Eratóstenes
    for p in range(2, int(limite**0.5) + 1):
        if primos[p]:
            # Si p es primo, marcamos todos sus múltiplos como no primos
            for i in range(p * p, limite + 1, p):
                primos[i] = False
    
    # Filtramos la lista para obtener solo los números que quedaron como True
    return [num for num, es_primo in enumerate(primos) if es_primo]

# Ejecución
rango_maximo = 1000
lista_primos = obtener_primos(rango_maximo)

print(f"Se encontraron {len(lista_primos)} números primos entre 1 y {rango_maximo}:")
print(lista_primos)
