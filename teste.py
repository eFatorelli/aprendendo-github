from time import sleep

lista = ['eu','você','zubumafu']

print('Testando as parada')
sleep(0.3)

for n in range(1, 4):
    print(n)
    sleep(0.3)

print('Se ta contando até 3, ta funcionando')
print('É, aparentemente está funcionando!')
print()

for cont, i in enumerate(lista):
    sleep(0.3)
    if cont + 1 == len(lista):
        print('e o', end=' ')
    print(i.capitalize())
