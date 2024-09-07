# definimos las dimenciones de la matriz
ciudades= 3 # numeros de ciudades
dias= 7     # dias de la semana
semanas =4  # numeros de semana
# creamos una matriz 3D para almacenar datos
temperaturas = [
    [ # ciudad 1
        [29,31,30,28,27,26,25], # semana 1
        [30,32,31,29,28,27,26], # semana 2
        [31,33,32,30,29,28,27], # semana 3
        [32,34,33,31,30,29,28]  # semana 4
    ],
    [ # ciudad 2
        [24,25,26,27,28,29,30], # semana 1
        [25,26,27,28,29,30,31], # semana 2
        [26,27,28,29,30,31,32], # semana 3
        [27,28,29,30,31,32,33]  # semana 4
    ],
    [ # ciudad 3
        [19,20,21,22,23,24,25], # semana 1
        [20,21,22,23,24,25,26], # semana 2
        [21,22,23,24,25,26,27], # semana 3
        [22,23,24,25,26,27,28]  # semana 4
    ]
]

# calculamos y mostramos el promedio de temperaturas para cada ciudad por semana
for ciudad in range (ciudades):
    print(f"ciudad {ciudad + 1}:")
    for semana in range (semanas):
        suma_temperaturas=0
        for dia in range (dias):
            suma_temperaturas+=temperaturas[ciudad][semana][dia]
        promedio=suma_temperaturas/dias
        print(f" semana {semana +1}: promedio de temperatura={promedio:.2f}c")

