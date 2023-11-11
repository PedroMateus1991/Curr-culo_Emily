dias_da_semana = ('segunda','terça','quarta','quinta','sexta','sábado','domingo')
print(dias_da_semana[:3])

print("\n")
dias_da_semana = [1,2,5,10,20,100]
print(sum(dias_da_semana))

soma = len(dias_da_semana)
print(soma)


print("*"*20)

dias_da_semana = ['pedro', 'casa', 'oculos']
# print(sum(dias_da_semana))

soma = len(dias_da_semana)
print(soma)

print("*"*20)
frutas = ['maça', 'banana', 'uva', 'laranja']
frutas.remove('maça')
print(frutas)

print("*"*20)
futebol = ('PALMEIRAS', 'CORINTHIANS', 'FLAMENGO')
print(futebol)
excluir = input("Escolha um time para escluir? ").upper()
futebol = list(futebol)
futebol.remove(excluir)
futebol = tuple(futebol)
print(futebol)
print("*"*20)

notas = (8, 7, 9, 6)
media = sum(notas)/len(notas)
print(media)
