def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se permite división entre 0")
    finally:
        print("Cálculo finalizado")

def raiz_cuadrada(num):
    try:
        if num < 0 :
            raise TypeError ("No se puede raiz de un negativo")

    except TypeError:
        print("Cogñi el error")