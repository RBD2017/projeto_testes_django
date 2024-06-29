def somar(a, b):
    return a + b

def test_somar():
    # Arrange
    valor1 = 5
    valor2 = 3
    resultado_esperado = 8

    # Act
    resultado = somar(valor1, valor2)

    #Assert
    assert resultado == resultado_esperado, f"A soma de {valor1} e {valor2} deveria ser {resultado_esperado}, mas foi {resultado}"


def nome():
    cidadao = 'joel'
    return cidadao


def test_verificar_nome():
    # Arrange
    nome_is_true = 'joel'
    
    # Act
    nome_esperado = nome()
    
   
    assert nome_esperado == nome_is_true

def numero():
    num = 10
    return num 


def test_numero_is_true():
    #arrange
    numero_esperado = 10

    #act
    numero_acao = numero()

    #assert

    assert numero_acao == numero_esperado




def menos():
    sub = 45 
    return sub

#arrange

def test_subtracao():
    valor_negativo = 37

    #act 
    valor_real = menos()

    #assert 

    assert valor_negativo != valor_real



def telefone():
    lista = 123456789
    return lista

def test_verifica_telefone():
    
    #arrange
    carcteres = 12344545

    #act
    execucao = telefone()

    #assert
    assert execucao != carcteres

def nome_is_false():
    pessoa = 'felipe'
    return pessoa

def test_verifica_if_nome_is_false():

    #arrange 
    preparacao = 'bruno'

    #act
    executar_nome = nome_is_false()

    #assert 
    assert executar_nome not in preparacao

def divisao():
    multiplicacao = 45*2
    return multiplicacao

def test_verifica_divisao(): 
    #arrange 
    preparacao = 90   

    #act
    acao = divisao()

    #assert
    assert acao is preparacao

print ('deu certo')
     