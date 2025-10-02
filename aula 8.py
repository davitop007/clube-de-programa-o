def quadrado ():
    lado = int(input('digite o valor do lado:'))
    area = lado * lado
    return area
    

def retangulo ():
    base = int(input('digite o valor da base:'))
    altura = int(input('digite o valor da altura:'))
    area = base * altura
    return area


def triangulo ():
    base =  int(input('digite o valor da base:'))
    altura = int(input('digite o valor da altura:'))
    area = base * altura / 2
    return area


def circulo ():
    pi = 3.14
    raio = int(input('digite o raio:'))
    area = pi * (raio**2)
    return area


def trapezio ():
    Base = int(input('digite o valor da Base:')) 
    base =  int(input('digite o valor da base:'))
    altura =  int(input('digite o valor da altura:'))
    area = (Base + base)* altura/2
    return area

def menu():
    opcao = input('qual area voce quer caucular')
    
    if opcao == 'quadrado':
        area = quadrado()
    elif opcao == 'retangulo':
        area = retangulo()
        
    print(area)
