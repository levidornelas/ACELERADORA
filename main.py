import json
import datetime
from classes import Paciente, Consulta


# Listas vazias, a serem preenchidas com os inputs do usuário
pacientes_cadastrados = []
agendamentos = []

def cadastrar_paciente():
  nome = input("Digite o nome do paciente: ")
  telefone = input("Digite o telefone do paciente: ")

  # Tratamento de erro: verifica se já existe um número de telefone cadastrado.
  for paciente in pacientes_cadastrados:
    if paciente.telefone == telefone:
      print("Paciente já cadastrado!")
      return

  #Chamando a classe Paciente, e também inserindo os inputs dentro da lista:
  paciente = Paciente(nome, telefone)
  pacientes_cadastrados.append(paciente)
  print("Paciente cadastrado com sucesso!")

def listar_pacientes():
  for i, paciente in enumerate(pacientes_cadastrados, start=1):
    print(f"{i}. {paciente.nome} ({paciente.telefone})")

def marcar_consulta():
  listar_pacientes()

  escolha = int(input("Escolha o número do paciente para agendar a consulta: "))
  paciente = pacientes_cadastrados[escolha - 1] #Ajustando o index do input com '-1'

  data = input("Digite a data da consulta (formato: ano-mês-dia): ")
  hora = input("Digite a hora da consulta: ")

  # Tratamento de erro para verificar se a data da consulta é válida
  try:
    data_consulta = datetime.datetime.strptime(data, "%Y-%m-%d") #Usei a data padrão da biblioteca, a fim de evitar erros e problemas posteriores.
    if data_consulta < datetime.datetime.now():
      print("Só é possível agendar consultas a partir de hoje.")
      return
  except ValueError:
    print("Formato de data inválido.")
    return

  especialidade = input("Digite a especialidade desejada: ")
  consulta = Consulta(paciente, data, hora, especialidade)
  agendamentos.append(consulta)
  print("Consulta agendada com sucesso!")


#Função auxiliar de 'cancelar_consulta'
def listar_agendamentos():
  for i, consulta in enumerate(agendamentos, start=1):
    print(f"{i}. {consulta.paciente.nome} - {consulta.data} às {consulta.hora} ({consulta.especialidade})")

def cancelar_consulta():
  listar_agendamentos()
  escolha = int(input("Escolha o número da consulta para cancelar: "))

  if escolha <= 0 or escolha > len(agendamentos):
    print("Escolha inválida.")
    return

  consulta = agendamentos[escolha - 1]
  print(f"Consulta agendada para {consulta.data} às {consulta.hora} ({consulta.especialidade})")

  confirmacao = input("Deseja cancelar esta consulta? (s/n): ")
  if confirmacao.lower() == "s":
    agendamentos.remove(consulta)
    print("Consulta cancelada com sucesso!")


#Salvando os dados num arquivo JSON, depois do programa ser encerrado com a opção '4':
def salvar_dados():
  dados = {
    'pacientes': [paciente.__dict__ for paciente in pacientes_cadastrados],
    'consultas': [{
      'paciente': consulta.paciente.__dict__,
      'data': consulta.data,
      'hora': consulta.hora,
      'especialidade': consulta.especialidade
    } for consulta in agendamentos]
  }

  caminho_arquivo = 'C:/Users/PC/Desktop/ACELERADORA/banco.json'  #Definindo o caminho com o path inteiro do arquivo, para evitar erros.

  with open(caminho_arquivo, 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=2)


#Menu principal do programa, em loop:
while True:
  try:
    print("Menu:")
    print("1. Cadastrar paciente")
    print("2. Marcar consulta")
    print("3. Cancelar consulta")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
      cadastrar_paciente()

    elif opcao == 2:
      marcar_consulta()

    elif opcao == 3:
      cancelar_consulta()

    elif opcao == 4:
      print("Muito obrigado por utilizar nosso programa de consulta! As informações permanecerão salvas.")
      salvar_dados()  # Salvando os dados antes de sair
      break

    else:
      print("Por favor escolha apenas um número de 1 a 4.")

  except ValueError:
    print('Aconteceu um erro, por favor tente novamente.')
    continue
