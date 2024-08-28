def calcular_velocidad(distancia, tiempo, velocidad_maxima):
    # Validar entradas
    if not distancia or not tiempo or not velocidad_maxima:
        return "Error: Debe ingresar todos los valores (distancia, tiempo, velocidad máxima)."

    distancia = float(distancia)
    tiempo = float(tiempo)
    velocidad_maxima = float(velocidad_maxima)

    if distancia <= 0 or tiempo <= 0:
        return "La distancia y el tiempo deben ser valores positivos."

    # Realizar el cálculo de la velocidad
    velocidad = float(distancia / 1000) / (tiempo / 60)
    porcentaje = 20
    porcentaje1 = float(velocidad_maxima * (porcentaje / 100))
    velocidad_con_porcentaje = velocidad_maxima + porcentaje1

    # Determinar el estado según la velocidad calculada
    if velocidad < velocidad_maxima:
        estado = "OK"
    elif velocidad < velocidad_con_porcentaje:
        estado = "MULTA"
    elif velocidad >= velocidad_con_porcentaje:
        estado = "MULTA Y CURSO DE SENSIBILIZACION"
    else:
        estado = "Error"

    # Mostrar los resultados en la consola
    resultado = (
        f"Distancia: {distancia} km\n"
        f"Tiempo: {tiempo} minutos\n"
        f"Velocidad máxima: {velocidad_maxima} km/h\n"
        f"Velocidad calculada: {velocidad} km/h\n"
        f"Estado: {estado}\n"
        f"Velocidad con porcentaje: {velocidad_con_porcentaje} km/h"
    )
    
    return resultado


if __name__ == '__main__':
    # Solicitar datos al usuario
    distancia = input("Ingrese la distancia en metros: ")
    tiempo = input("Ingrese el tiempo en minutos: ")
    velocidad_maxima = input("Ingrese la velocidad máxima en km/h: ")
    
    # Realizar el cálculo y mostrar el resultado
    resultado = calcular_velocidad(distancia, tiempo, velocidad_maxima)
    print(resultado)
