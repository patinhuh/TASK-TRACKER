import json
import atexit

tarefas = []
tarefas_feitas =[]
tarefas_fazendo = []
tarefas_atrasadas = []

# Salva os dados do programa
def salvar_dados():
    dados = {
         'tarefas': tarefas,
         'tarefas_feitas': tarefas_feitas,
         'tarefas_fazendo': tarefas_fazendo,
         'tarefas_atrasadas': tarefas_atrasadas
    }
    with open('tarefas.json', 'w') as f:
         json.dump(dados, f)

# Carrega os dados do programa
def carregar_dados():
     try:
          with open ('tarefas.json', 'r') as f:
               dados = json.load(f)
               tarefas.extend(dados['tarefas'])
               tarefas_feitas.extend(dados['tarefas_feitas'])
               tarefas_fazendo.extend(dados['tarefas_fazendo'])
               tarefas_atrasadas.extend(dados['tarefas_atrasadas'])
     except FileNotFoundError:
        pass
carregar_dados()
############################

# Mensagem de erro caso o usuário digite algo que não seja um número inteiro
def garantir_int(mensagem):
    while True:
         try:
              return int(input(mensagem))
         except ValueError:
              print("\nEntrada Inválida. Por favor, insira um número inteiro.\n")

def verificar_indice(indice, lista):
    if 0 <= indice < len(lista):
         return True
    else:
         print(f"\nÍndice Inválido. A lista tem {len(lista)} itens.\n")
         return False 
    


# Adiciona tarefas
def add_tarefa():
    tarefa = str(input("Digite a tarefa que gostaria de adicionar: "))
    tarefas.append(tarefa)
    print('')

# Mostra as tarefas
def mostrar_tarefa():
    try:
        esc = int(input("\n1. Mostrar todas as tarefas\n2. Mostras as Tarefas em Andamente\n3. Mostrar as Tarefas Feitas\n4. Mostras as Tarefas Atrasadas\n"))


        if esc == 1:
            if not tarefas:
                print("Não há Tarefas a serem movidas")
            else:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. {tarefa}")
                print('')
        elif esc == 2:
            print("TAREFAS EM PROGRESSO:\n")
            if not tarefas_fazendo:
                print("Não há Tarefas em Progresso\n")
            else:
                for i, tarefa in enumerate(tarefas_fazendo):
                    print(f"{i + 1}. {tarefa}")
                print('')
        elif esc == 3:
            print("TAREFAS FEITAS\n")
            if not tarefas_feitas:
                print("Não há Tarefas sendo Feitas\n")
            else:

                for i, tarefa in enumerate(tarefas_feitas):
                    print(f"{i + 1}. {tarefa}")
                print('')
        elif esc == 4:
            print("TAREFAS ATRASADAS\n")
            if not tarefas_atrasadas:
                print("Não há Tarefas Atrasadas\n")
            else:
                for i, tarefa in enumerate(tarefas_atrasadas):
                   print(f"{i + 1}. {tarefa}")
                print('')


    except IndexError:
        print("\nEntrada Inválida. Por Favor, insira uma das opções acima.\n")

# Move as tarefas entre outras listas
def mover_tarefas():
    print("Mover Tarefas\n")
    
    try:
            indice = garantir_int("\nQual tarefa gostaria de mover: \n") - 1
            escolha = garantir_int("\nPara onde você gostaria de mover essa tarefa?\n1. Fazendo\n2. Feita\n3. Atrasada\n")


            if verificar_indice(indice, tarefas):
                if escolha == 1:        
                    item = tarefas.pop(indice) 
                    tarefas_fazendo.append(item)
                    print('')
                elif escolha == 2:
                     item = tarefas.pop(indice) 
                     tarefas_feitas.append(item)
                     print('')
                elif escolha == 3:
                     item = tarefas.pop(indice)
                     tarefas_atrasadas.append(item)
                     print('')
                else:
                     print("Entrada inválida!")


    except ValueError:
            print("")

# Remove as tarefas
def remover_tarefas():
    print("\n1. Em Progresso\n2. Feitas\n3. Atrasadas\n")
    try:

        esc = garantir_int("Digite o indice da lista que você gostaria de remover o item: \n")


        if esc == 1:
            if not tarefas_fazendo:
                print("\nNenhuma 'Tarefa em Progresso' para remover!\n")
            else:
                for i, tarefa in enumerate(tarefas_fazendo):
                    print(f"{i + 1}. {tarefa}")
                    print('')
                    indice = int(input("Selecione a Tarefa que gostaria de remover: ")) - 1
                    item = tarefas_fazendo.pop(indice)
                    print('')
        elif esc == 2:
            if not tarefas_feitas:
                print("\nNenhuma 'Tarefa Feita' para remorver!\n")
            else:
                for i, tarefa in enumerate(tarefas_feitas):
                    print(f"{i + 1}. {tarefa}")
                    print('')
                    indice = int(input("Selecione a Tarefa que gostaria de remover: ")) - 1
                    item = tarefas_feitas.pop(indice)
                    print('')
        elif esc == 3:
            if not tarefas_feitas:
                print("\nNenhuma 'Tarefa Atrasadas' para remorver!\n")
            else:
                for i, tarefa in enumerate(tarefas_atrasadas):
                    print(f"{i + 1}. {tarefa}")
                    print('')
                    indice = int(input("Selecione a Tarefa que gostaria de remover: ")) - 1
                    item = tarefas_atrasadas.pop(indice)
                    print("")  


    except Exception as e:
        print(f"Erro ao remover tarefa: {e}\n")
        

################################################################
## MENU ##

print("Bem vindo ao Gerenciador de Tarefas\n")



while True:
    print("1. Mostrar Tarefas\n2. Adicionar Tarefas\n3. Mover Tarefas\n4. Remover Tarefas\n")
    escolha = int(input("O que gostaria de fazer: "))
    if escolha == 1:
        mostrar_tarefa()
    elif escolha == 2:
        add_tarefa()
    elif escolha == 3:
        mover_tarefas()
    elif escolha == 4:
        remover_tarefas() 
    else:
         break

##################################################################
# Salvar dados ao sair
atexit.register(salvar_dados)