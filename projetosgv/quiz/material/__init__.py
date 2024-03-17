def linha(msg):
    print('-'*len(msg))

def titulo(msg=''):
    linha(msg)
    print(msg.center(len(msg)))
    linha(msg)

def pergunta():
    todasperguntas = [
    'Você é uma pessoa extrovertida e gosta de chamar a atenção nos eventos sociais?',
    'Você é conhecido por ser o líder do grupo e tomar decisões importantes em situações difíceis?',
    'Você é o tipo de pessoa que sempre procura ajudar os outros e se preocupa com o bem-estar dos seus amigos?',
    'Você costuma ser muito competitivo e está sempre buscando ser o melhor em tudo que faz?'
    ]
    return todasperguntas







