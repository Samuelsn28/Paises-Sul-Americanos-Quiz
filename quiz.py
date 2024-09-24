import random

quiz = [   
    ['Maior pais da america latina', 'Brasil'],
    ['Pais perto do sul do Brasil e da Argentina', 'Uruguai'],
    ['Pais popular por ser similar a China em questao de produtos', 'Paraguai'],
    ['Pais com pessima reputacao', 'Venezuela'],
    ['Pais que é jantado em ceia', 'Peru'],
    ['Pais que faz fronteira com o Panama', 'Colombia'],
    ['Pais com capital de nome "la paz"', 'Bolivia'],
    ['Pais com egua com dor', 'Equador'], 
    ['Pais extremamente fino', 'Chile'],
    ['Pais que sofre muito por inflacao', 'Argentina'],
    ['Pais estrangeiro', 'Guiana Francesa'], 
    ['Pais que tem uma "irma" no mesmo continente que foi colonizada pela Franca', 'Guiana']
]

def iniciar_quiz():
    print('------ Quiz dos Paises da America Latina ------')

    pontuacao_adquirida = exibir_perguntas()    

    print('---- Jogo Finalizado ----')
    print('Sua pontuacao:', pontuacao_adquirida)

def exibir_perguntas():
    pontuacao = 0
    num_pergunta = 1

    while len(quiz) != 0:
        num_gerado = random.randint(0, (len(quiz) - 1))
        pergunta = quiz[num_gerado]
        del quiz[num_gerado]

        resultado = exibir_pergunta(num_pergunta, pergunta)

        if resultado:
            pontuacao += 1
        num_pergunta += 1
    return pontuacao

def exibir_pergunta(num_pergunta, pergunta):
    print(str(num_pergunta) + ') ' + pergunta[0])
    resposta = str(input('Voce> '))

    if resposta.lower() == pergunta[1].lower():
        print('\nCerta a Resposta! \n')
        return True
    print('\nErrado! Era', pergunta[1], '\n')

    return False
    

iniciar_quiz()