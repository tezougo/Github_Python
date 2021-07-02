
import numpy as np
import math
import sympy
import metodosnumericos.localizacao.teorema_bolzano as teorema
import metodosnumericos.metodosrefinamento.bissecao as mt_bissecao
import metodosnumericos.metodosrefinamento.falsa_posicao as mt_falsa_posicao
import metodosnumericos.metodosrefinamento.newton_phason as mt_newton_phason
import metodosnumericos.metodosrefinamento.secantes as mt_secantes
x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

while(True):
    validando = False
    print(
        "\nInforme os dados necessarios para realizacao dos metodos iterativos, sendo ele a funcao, intervalo [a, b] e sua precisao.")
    print("\nExemplo:", "(2*ln(x**2))/(sqrt(x)-5*e^(-x))", "a:3",
        "b:5", "precisao: 0.0005\n", sep="\n")
    f = (input("Digite a sua funcao: "))
    f = sympy.Lambda(x, sympy.sympify(f))
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    precisao = float(input("Digite precisao: "))

    if(teorema.bolzano(f, a, b) == False):
        print(
            "\nNao e possivel afirma a existencia de uma solucao no intervalo [{},{}], pois pois f({})*f({}) > 0.".format(a, b, a, b))
    else:
        print("\nIntervalo contem pelo menos uma solucao, pois f({})*f({}) < 0.".format(a, b))
        validando = True

    if(validando == True):
        id_metodo = False
        while(id_metodo == False):
            print("\nQual metodo de refinamento deseja utilizar?\n", "'1' Metodo da Bissecao",
                "'2' Metodo das Cordas (Falsa Posicao)", "'3' Metodo de Newton-Raphson", "'4' Metodo das Secantes", sep="\n")
            id_metodo = input(
                "\nDigite o numero do metodo que deseja utilizar: ")
            if(id_metodo == '1'):
                mt_bissecao.bissec(f, a, b, precisao)
            elif(id_metodo == '2'):
                mt_falsa_posicao.cordas(f, a, b, precisao)
            elif(id_metodo == '3'):
                mt_newton_phason.newton(f, a, b, precisao)
            elif(id_metodo == '4'):
                mt_secantes.secant(f, a, b, precisao)
            else:
                id_metodo = False
                print(
                    "\n Por favor digite o numero referente ao metodo desejado. \n Exemplo '1'")
