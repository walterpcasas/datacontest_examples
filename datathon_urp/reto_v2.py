import networkx as nx
import itertools

try:
	ruta_archivo = input('Ingresar el nombre (y la ruta del archivo) [Ejemplo: /home/user/ruta.txt]: ')
	file = open(ruta_archivo,"r")
	Grafo = nx.Graph()

	lista_informacion = []
	ruta_impresion = ''
	path_min = []
	minimo = 100000
	diccionario_path = {}
	ciudades = []
	paths = []

	for row in file:
		informacionEntreCiudades = row.split(' ')

		ciudadOrigen = informacionEntreCiudades[0]
		if ciudadOrigen not in ciudades:
			ciudades.append(ciudadOrigen)

		ciudadDestino = informacionEntreCiudades[2]
		if ciudadDestino not in ciudades:
			ciudades.append(ciudadDestino)

		distanciaCiudades = int(informacionEntreCiudades[4].replace('\\n',''))

		lista_informacion.append((ciudadOrigen,ciudadDestino,distanciaCiudades))

	file.close()
except:
	var = 'Verifica el nombre del archivo y/o ubicacion e intenta nuevamente.'
	print('-'*len(var)+'\n'+var+'\n'+'-'*len(var)+'\n')
	exit()


Grafo.add_weighted_edges_from(lista_informacion)

for elemento in itertools.combinations(ciudades, 2):
	origen = elemento[0]
	destino = elemento[1]
	paths = paths + [x  for x  in nx.all_simple_paths(Grafo, origen,destino)  if len(x) > (len(Grafo)-1)]

for path in paths:
	total_weight = 0
	pairs = zip(path, path[1:])
	
	for pair in pairs:
		an_edge = Grafo.get_edge_data(pair[0], pair[1])
		total_weight += int(an_edge['weight'])
	if total_weight in diccionario_path.keys():
		diccionario_path[total_weight].append(path)
	else:
		diccionario_path[total_weight] = [path]
	print(path)
	print(total_weight)

	if total_weight  < minimo:
		minimo = total_weight
		path_min = path

for ciudad in path:
	if ciudad == destino:
		ruta_impresion += ciudad +' = ' 
	else:
		ruta_impresion += ciudad +' -> ' 
print('El camino mas corto es: '+ruta_impresion+ str(minimo))

