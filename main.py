from classes import Paciente, Consulta

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
      Paciente.cadastrar_paciente()

    elif opcao == 2:
      Paciente.marcar_consulta()

    elif opcao == 3:
      Consulta.cancelar_consulta()

    elif opcao == 4:
      print("Muito obrigado por utilizar nosso programa de consulta! As informações permanecerão salvas.")
      Consulta.salvar_dados()  # Salvando os dados antes de sair
      break

    else:
      print("Por favor escolha apenas um número de 1 a 4.")

  except ValueError:
    print('Aconteceu um erro, por favor tente novamente.')
    continue
