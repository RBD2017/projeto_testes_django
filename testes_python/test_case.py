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

#test_somar()  # Executa o teste
#agente tá testando essa função aqui 
def nome():
    cidadao = 'joel'
    return cidadao

# Teste usando pytest
def test_verificar_nome():
    # Arrange
    nome_is_true = 'joel'
    
    # Act
    nome_esperado = nome()
    
    # Assert , obs: no assert vc N verifica a função q estar sendo testada , mas sim as fases depois dessa 
    assert nome_esperado == nome_is_true


#######################

def numero():
    num = 10
    return num 

#arrange
def test_numero_is_true():
    #arrange
    numero_esperado = 10

    #act
    numero_acao = numero()

    #assert

    assert numero_acao == numero_esperado


#88888888888888888888888888888888888888888

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

#8888888888888888888888888888888888888888888888888888

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
     