import random
import string

maius = list(string.ascii_uppercase) #gera uma lista com todas letras maiusculas
minus = list(string.ascii_lowercase) #gera uma lista com todas letras minusculas
senha = []

outros_caracteres = random.sample(minus,6)
Letras_maisculas = random.sample(maius, 2)
digito = random.choice(string.digits) # digito entre eses 0123456789
simbolo = random.choice(string.punctuation) # simbolos

senha = Letras_maisculas+outros_caracteres
senha.append(digito)
senha.append(simbolo)
random.shuffle(senha)
print(''.join(senha))

# def geradordesenha():
#     #random.randrange(11) #gera numeros inteiro de 0 a 10
#     # random.randrange(0,10,2) # gera numeros inteiros entre 0 e 9 que são divisiveis por 2
#     #random.random() # gera numeros pseudo-aleatorios de 0 a 1
#     #random.randint(0,10) # gera numeros inteiros de 0 até 10
#     #random.shuffle(sequencia) # mistura uma sequencia de elementos / pode usar um parametro "peso" random.suffle(sequencia,peso)
#     #random.choice(sequencia) # escolhe um elemento aleatoriamente da sequencia
#     #random.sample(sequencia, quantia) # escolhe uma "quantia" de elementos aleatorios da sequencia
#     #random.uniform(1,2) # gera numeros pseudo-aleatorios de 1 a 2