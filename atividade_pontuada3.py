#ALUNOS: DAVI FREITAS E ARIANE LEITE

import os
os.system("clear" / "cls")
from dataclasses import dataclass



@dataclass
class Reserva:
    numero_aviao: int
    nome: str
    idade: int
    cpf: str



#  FUNÇÃO DO MENU

def exibir_menu():
    print("""
===========================================
           MENU SWEET FLIGHT
===========================================
1) Registrar o numero de cada aviao
2) Registrar o quantitativo de assentos disponiveis em cada aviao 
3) Reservar passagem aerea 
4) Realizar consulta por aviao
5) Realizar consulta por passageiro 
6) Encerrar
===========================================
""")



def sistema_de_reservas():

    # Vetores 
    avioes = [None] * 4
    assentos = [0] * 4

    # Lista de reservas
    reservas = []

    

    contador_reservas = 0
    limite_reservas = 20

    while True:

        exibir_menu()
        opcao = input("Escolha uma opçao: ")

        match opcao:

        
            case "1":
                print("\nCadastro dos avioes:")
                for i in range(4):
                    avioes[i] = int(input(f"Digite o número do avião {i+1}: "))
                print("Aviões registrados com sucesso!")

            
            case "2":
                print("\nCadastro de assentos:")
                for i in range(4):
                    if avioes[i] is None:
                        print("Registre os aviões primeiro!")
                        break
                    assentos[i] = int(input(f"Digite os assentos do avião {avioes[i]}: "))
                print("Assentos registrados!")

            
            case "3":
                print("\nReserva de passagem:")

                if contador_reservas >= limite_reservas:
                    print("Limite de 10 reservas atingido.")
                    continue

                numero = int(input("Número do avião desejado: "))

                if numero not in avioes:
                    print("Este avião não existe!")
                    continue

                indice = avioes.index(numero)

                if assentos[indice] <= 0:
                    print("Não há assentos disponíveis!")
                    continue

                # Solicitar dados do passageiro
                nome = input("Nome do passageiro: ")
                idade = int(input("Idade: "))
                cpf = input("CPF: ")

                # Registrar reserva
                reservas.append(Reserva(numero, nome, idade, cpf))
                assentos[indice] -= 1
                contador_reservas += 1

                print("Reserva realizada com sucesso!")

            
            case "4":
                numero = int(input("Número do avião para consulta: "))

                if numero not in avioes:               
                    print("Este avião não existe!")
                    continue

                print(f"\nReservas do avião {numero}:")
                encontrou = False

                for r in reservas:
                    if r.numero_aviao == numero:
                        print(f"Passageiro: {r.nome} | Idade: {r.idade} | CPF: {r.cpf}")
                        encontrou = True

                if not encontrou:
                    print("Não há reservas para este avião.")

            
            case "5":
                nome_busca = input("Nome do passageiro: ")
                encontrou = False

                print("\nResultado da consulta:")

                for r in reservas:
                    if r.nome.lower() == nome_busca.lower():
                        print(f"Avião: {r.numero_aviao} | Idade: {r.idade} | CPF: {r.cpf}")
                        encontrou = True

                if not encontrou:
                    print("Não há reservas para este passageiro.")

            
            case "6":
                print("Encerrando o sistema... Obrigado!")
                break

            
            case _:
                print("Opção inválida, tente novamente!")


# Executa o sistema
sistema_de_reservas()

