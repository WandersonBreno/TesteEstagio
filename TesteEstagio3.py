listanum = []
maiores = 0
for c in range (1, 31):
    listanum.append(float(input(f'Digite a venda do dia {c}: ')))

    menor_valor = min(listanum)
    maior_valor = max(listanum)
    soma_total = sum(listanum)
    media_final = soma_total/ len(listanum)
    maiores if c> = listanum

print('=-' * 30)
print(f'você digitou os valores{listanum}')
print(f'O dia que mais vendeu foi {maior_valor} reais ')
print(f'O dia que menos vendeu foi {menor_valor} reais')
print(f'soma das vendas {soma_total} reais ')
print(f'A média mensal foi de: {media_final} reais')
print(f'Os dias que venderam mais que a média foi: {maiores}')




