def calcular_promedio_temperaturas(datos_temperaturas):
  """
  calcular la temperatura promedio de cada ciudad en un conjunto de datos.
  :param datos_temperaturas: diccionario con los datos de temperaturas

  Returns:diccionario con las temperaturas de cada ciudad
  """
  promedios_ciudades = {}
  for ciudad, semanas in datos_temperaturas.items():
    todas_temperaturas=[temperatura for semana in semanas for temperatura in semana]
    promedio=sum(todas_temperaturas)/len(todas_temperaturas)
    promedios_ciudades[ciudad]=promedio
  return promedios_ciudades


# Ejemplo:
Datos_temperaturas= {
   "Quito A":[[19,21,20,18],[22,24,21,21]],
   "CuencaB":[[17,16,18,19],[20,22,21,23]],
   "Manta C":[[24,26,25,23],[27,29,28,26]]
}
resultado=calcular_promedio_temperaturas(Datos_temperaturas)
print(resultado)
