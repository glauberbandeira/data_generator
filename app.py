
import random

data = ''
list_option = ['']

# List
class Listas:
    nomes = [
        'Jose', 'Francisco', 'Maria', 'Ana', 'Tamires'
    ]
    emails = [
        'jose@gmail.com', 'francisco@gmail.com', 'maria@gmail.com', 'ana@gmail.com', 'tamires@gmail.com'
    ]
    telefones = [
        55995459349, 55995456879, 55995423569, 55995671249, 55995784349
    ]
    cidades = [
        'Fortaleza', 'Sao Paulo', 'Rio de janeiro', 'Salvador', 'Curitiba'
    ]
    estados = [
        'Ceara', 'Sao Paulo', 'Rio de janeiro', 'Bahia', 'parana'
    ]

def options():
    print("------------------------------------------------------------------------------------")
    print("Choose one or more options below to be randomly generated")
    print("[1] - Name")
    print("[2] - Email")
    print("[3] - Phone Number")
    print("[4] - City")
    print("[5] - State")
    print("------------------------------------------------------------------------------------")
    # receber a escolha do usuario
    option = input('Enter options: ').replace(',', "")
 
    return option

print('Welcome to the Test Data Generator - To end the program, type "stop".')
print('-'*50)

while True:
    option = options()
    if option != 'stop':
        for item in option:
            if item == '1':
                data = random.choice(Listas.nomes)
                # lista_opcao.append(dado)
                print(data)
            elif item == '2':
                data = random.choice(Listas.emails)
                # lista_opcao.append(dado)
                print(data)
            elif item == '3':
                data = random.choice(Listas.telefones)
                # lista_opcao.append(dado)
                print(data)
            elif item == '4':
                data = random.choice(Listas.cidades)
                # lista_opcao.append(dado)
                print(data)
            elif item == '5':
                data = random.choice(Listas.estados)
                # lista_opcao.append(dado)
                print(data)
            list_option.append(data)
 
 
#SALVANDO ARQUIVO
        save_data = input('Do you want to Generate a .txt file? \n Type it y/n: ')
        if save_data == 'y':
            with open('data.txt','a') as file:
                for option in list_option:
                    file.write(f'{option}\n')
                    list_option['']
    else:
        print("Leaving the program...")
        break