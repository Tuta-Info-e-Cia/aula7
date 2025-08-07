#lista vazia
#usuario quem informa o que será incluido na lista

print ('Lista de Frutas Master Top')
frutas =[]
for i in range (3):
    fruta = input (f'Digite o nome da {i+1}ª fruta da sua lista')
    frutas.append(fruta)
#fruta = input (f 'Digite o nome da {i}ª fruta da sua lista' ) - assim fica visualemnte feio pois a lista começaria na zero fruta e nao é esse o objetivo por isso se poe i+1 na fstring
print(f'Sua Lista de Frutas Master Top é: {frutas} ')
