# Função para exibir o menu e capturar a operação do usuário
def exibir_menu():
    print("\nEscolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    return int(input("Digite o número da operação (1/2/3/4): "))

# Captura os números do usuário
def capturar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

# Executa a operação escolhida
def calculadora():
    while True:
        operacao = exibir_menu()
       
        if operacao in [1, 2, 3, 4]:  # Verifica se a operação é válida
            num1, num2 = capturar_numeros()
           
            if operacao == 1:  # Soma
                print(f"O resultado é: {num1 + num2:.2f}")
            elif operacao == 2:  # Subtração
                print(f"O resultado é: {num1 - num2:.2f}")
            elif operacao == 3:  # Multiplicação
                print(f"O resultado é: {num1 * num2:.2f}")
            elif operacao == 4:  # Divisão
                if num2 != 0:
                    print(f"O resultado é: {num1 / num2:.2f}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Por favor, tente novamente.")
           
        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando a calculadora. Até mais!")
            break

# Executa a calculadora
calculadora()
