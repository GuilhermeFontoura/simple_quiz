### quiz ###

import os # 'import os' nos permite usar o comando -> os.sytem('cls'), que apaga o console [mas nao apaga o que foi feito na memória]


name = input('Type your name: ')
os.system('cls') # comando que limpa o terminal

choice = input(f'Would you like start the game {name.lower()}? [Y]es or [N]ot: ')
score = 0 # essa variavel foi criada para somar a pontuaçao do participante

os.system('cls')

if choice == 'n'.lower(): # .lower() é um metodo que pode ser aplicado em strings para convertelas para minúsculas

    print('Okay, thank you for participating.')
elif choice == 'y'.lower():

    # questao número 1
    print('Question number 1: ')
    print() # esse print vazio foi criado para criar um espaço entre as frases, uma maneira diferente **
    question_1 = input('Who created GTA? \n(A) Rockstar Games \n(B) Ubisoft \n(C) Activision \n(D) EA \n\nAnswer -> ')
    # \n dentro da string para saltar uma linha, outra maneira de realizar a mesma coias que -> print()

    # pontuaçao da primeira pergunta
    if question_1.lower() == 'a': # essa condicional foi criada para somar 1 ponto caso o participante acerte a primeira questao
        score += 1 # é a mesma coisa que -> score = score + 1 (ou seja, o valor atual de score = 0 + valor da questao acertada +1pt)
    
    else:
        score += 0

    os.system('cls')

    # questao número 2
    print('Question number 2:\n')
    question_2 = input('What is the capital of Korea: \n(A) Rio de Janeiro \n(B) Los Angeles \n(C) Seul \n(D) Paris\n\nAnwser -> ')

    # pontuaçao da segunda pergunta
    if question_2.lower() == 'c':
        score += 1
    else:
        score += 0

    os.system('cls')

    # questao número 3
    print('Question number 3:\n')
    question_3 = input('Where is Tokyo: \n(A) Italy \n(B) Japan \n(C) France \n(D) Brazil \n\nAnswer ->  ')

    # pontuaçao da terceira pergunta
    if question_3.lower() == 'b':
        score += 1
    else:
        score += 0
    
    os.system('cls')

    # resultado final da pontuaçao do candidato
    print(f'{name.capitalize()} your final score is: {score} point(s)!!') # o metodo capitalize deixa a primeira letra maiúscula
    print('Thank you for participating.')
else:

    print('Your answer is invalid, please restart the quiz.')