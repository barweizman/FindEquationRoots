# Bar Weizman - 206492449
# Bar Sela - 206902355
import math
import sympy as sp
from sympy.utilities.lambdify import lambdify

def Bisection_Method(f, start_point, end_point, e):
    a = start_point
    b = end_point
    iterations = 0
    error = - ((math.log(e/(b-a))) / math.log(2))
    while (abs(b-a) > e) and (iterations+1 < error):
        iterations += 1
        c = (a+b) / 2
        if f(a)*f(c) > 0:
            a = c
        else:
            b = c
    return {c: iterations}

def Check_0(f):
    if f(0) == 0:
        return {0: 0}
    #check if none?

def Newton_Raphson(f, start_point, end_point, e):
    pass

def Secant_Method(f, start_point, end_point, e):
    pass

def CalcRoots():
    roots = {}
    epsilon = 0.0001
    start_point = -5  # start range
    end_point = 6  # end range
    div_num = (abs(start_point)+abs(end_point)) / 0.1  # will represent the number of iterations we will check the sign change - f(x1)*f(x2)<0
    choice = 0
    while choice != '1' and choice != '2' and choice != '3':
        print("Which method would you like to choose in order to find the equation roots?")
        print("1.Bisection method")
        print("2.Newton-Raphson method")
        print("3.Secant method")
        choice = input()

    for i in range(int(div_num)):
        if i == 0:  # first iteration
            x1 = start_point
            x2 = start_point+0.1
        else:
            x1 = x2
            x2 = x1 + 0.1

        if f(x2) == 0:  # holds the issue when there is a sign change before and after the 0
            roots.update({x2: 0})

        if f(x1)*f(x2) < 0:  # if there is a sign change
            if choice == '1':
                if Check_0(f) is not None:
                    roots.update(Check_0(f))  # 0 can be a root, and is a special check
                roots.update(Bisection_Method(f, x1, x2, epsilon))  # roots that are crossover points(function)
                point = Bisection_Method(fprime(f), x1, x2, epsilon)  # roots that are touching points(function-prime)
                c, iterations = list(point.items())[0]
                if f(c) == 0:  # if the root of the function-prime reset the equation, than its a function root
                    roots.update(point)
            if choice == '2':
                Newton_Raphson(f, x1, x2, epsilon)
            if choice == '3':
                Secant_Method(f, x1, x2, epsilon)


    # printing all roots , with thier number of iterations
    for root, iterations in roots.items():
        print("The root is:", round(root, 6), "| number of iterations:", iterations)


def f(x):
    return x ** 2 - 2 * x + 1

# return x ** 4 + x ** 3 - 3 * (x ** 2)


def fprime(f):
    x = sp.symbols('x')
    f = f(x)
    f_prime = f.diff(x)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    return f_prime



CalcRoots()