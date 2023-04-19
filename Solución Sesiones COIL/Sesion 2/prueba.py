array=["PEP 8", "PEP 248", "PEP 257"]
def obtenerNumerosCaracteres(list):
 aux=0
 for item in range(len(list)):
  aux+=len(list[item])
 return print(aux)
obtenerNumerosCaracteres(array)