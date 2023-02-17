# Pra comentar utilizamos a hashtag (#), para comentários de multilinhas
# pode-se utilizar 3 aspas duplas ou 3 simples, desse modo será reconhecido como
# string porém por não ser atribuido a uma variável o compilador passará direto por ela.
"""
'print()' é usado para mostrar algo para o usuário, colocando o que quer
ser mostrado dentro do parenteses, utiliza-se aspas (simples ou duplas)
para o interpretador entender que se trata de um texto (string).
"""

print("Hello, World!\n") 

'''
Em Python não necessitamos declarar o tipo das variáveis, os tipos são
criados no momento em que você atribui um valor as variáveis.
'''
# criei a variável 'teste', ao decorrer das alterações que forem feitas na variável ela mudará pro tipo correto.
teste = 10 # aqui ela é tipo inteiro (int).
print("Inteiro =", teste)

teste = 10.50 # seu valor foi alterado para real (float).
print("Real =", teste)

teste = 'teste' # foi alterado para texto (string).
print("Texto =", teste)

teste = "Teste" # continua String porém foi utilizado aspas duplas pra mostrar que aceita aspas simples ou duplas para identificar String (primeiro "t" foi alterado para "T").
print("Texto =", teste)

teste = True # foi alterado para valor booleano.
print("Booleano =", teste, "\n") # '\n' é usado para pular linha.

x = 10 # 'x' recebeu o valor 10 portanto foi declarada como tipo inteira (int).
y = 20 # o mesmo acontece com 'y', recebendo 20 e se tornando tipo inteiro (int).
s = x + y # 's' recebeu a soma entre 'x+y' se tornando tipo inteiro também.
'''
Pra imprimir mais de um valor no 'print()' é necessário que coloque virgulas antes e depois de cada valor,
se colocarmos: 'print("soma de" x "+" y "é =" s)' irá dar erro por falta das virgulas. 
Caso queirá fazer um print simples poderiamos usar 'print(s)' exibindo somente o valor final 's'.
'''
print("soma de", x ,"+" ,y ,"é =", s)  
# 'print (type())' é usado quando queremos saber qual o tipo de uma variável, o interpretador retornará se é int, float ou algum outro tipo.
print("s =", s, "que é um valor do tipo ", type(s), "\n")

# Python é Case-Sensitive
a = 10
A = 11
print("a =", a, "A =", A) # 'A' não irá apagar o valor de 'a', são variáveis diferentes por conta do case-sensitive.
print("")

# é possível declarar mais de uma variável e valor ao mesmo tempo utilizando a virgula.
fruta, legume, vegetal = "Maça", "Cenoura", "Alface"
print(fruta, legume, vegetal, "\n")

# é possivel que mais de uma variável receba o mesmo valor colocando o sinal de '=' na frente de cada uma.
vermelho = azul = roxo = "Cores"
print(vermelho, azul, roxo, "\n")