import main
import alkupeli
import main2

print('1992 超喜3in1歡玩')
print('快點啟動遊戲吧')
peli_names = ['Lentokenttämonopoli: 1', 'Arvaa tai olla onnekas: 2', 'Lenttokentäagentti: 3']
for peli in peli_names:
    print(peli)

choice = int(input('valitse peli: '))

if choice == 1:
    main2.start()
elif choice == 2:
    main.main() 
elif choice == 3:
    alkupeli.run_alkupeli()
