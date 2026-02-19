num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('\nEscolha uma operação:\n', 
      
      '+ para adição\n', 
      '- para subtração\n', 
      '* para multiplicação\n',
      '/ para divisão\n')

operacao = input()

resultado = ' '

if operacao == '+':
    resultado = num1 + num2
    print(f'A soma dos numeros informados é {resultado}')

elif operacao == '-':
    resultado = num1 - num2
    print(f'A subtração dos números informados é {resultado}')

elif operacao == '*':
    resultado = num1 * num2
    print(f'A multiplicação dos números informados é {resultado}')

elif operacao == '/':
    resultado = num1/num2
    print(f'A divisão dos números informados é {resultado:.0f}')            

 