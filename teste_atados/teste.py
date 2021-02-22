palavra = input('Insira a palavra: ')

def is_isogram(palavra):
	result = True
	palavra =  palavra.lower()
	if palavra:
		for letra in palavra:
			if (palavra.count(letra) > 1) or (letra.isdigit()):
				result = False

	return print(result)

is_isogram(palavra)