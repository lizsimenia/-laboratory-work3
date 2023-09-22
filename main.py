#code
import cmath
import math

def check(num):
    if num.real < 0:
        return -1
    return 1

def output_x(x):
    if x.imag == 0.0:
        return str(x.real)
    else:
        return str(x.real) + " + " + str(x.imag) + "j"


def check_solution(mass, a, b ,c, d):
    for x in mass:
        sample = a*x**3 + b*x**2 + c*x + d
        if round(sample.real, 1) + round(sample.imag, 1)*1j  == 0:
            print(f"Уравнение при x = {output_x(x)}: {a}*x**3 + {b}*x**2 + {c}*x + {d} = 0")
            print("Корень подходит", "\n")


def solve(a, b ,c, d):
    # приведение к квадратному уравнению
    b/=a
    c/=a
    d/=a
    a/=a
    p = (3*a*c - b**2) / 3*a**2
    q = (2*b**3-9*a*b*c+27*a**2*d)/27*a**3

    D = q**2/4 + p**3/27
    temp = b/3*a

    if D < 0:
        if q < 0:f = cmath.atan(cmath.sqrt(-D)*2 / -q)
        elif q > 0: f = cmath.atan(cmath.sqrt(-D)*2 / -q) + math.pi
        else: f = math.pi/2

        y1 = 2*cmath.sqrt(-p/3)*cmath.cos(f/3)
        y2 = 2*cmath.sqrt(-p/3)*cmath.cos(f/3 + 2*math.pi/3)
        y3 = 2*cmath.sqrt(-p/3)*cmath.cos(f/3 + 4*math.pi/3)


    elif D > 0:
        subcortical1 = -q/2 + cmath.sqrt(D)
        subcortical2 = -q/2 - cmath.sqrt(D)
        slag1 = abs(subcortical1)**(1./3.) * check(subcortical1)
        slag2 = abs(subcortical2)**(1./3.) * check(subcortical2)

        y1 =  slag1 + slag2
        y2 = (-1/2) * (slag1 + slag2) + 1j*3**0.5/2*(slag1 - slag2)
        y3 = (-1/2) * (slag1 + slag2) - 1j*3**0.5/2*(slag1 - slag2)

    else:
        y1 = 2*(q/2)**(1./3.) * check(-q/2)
        y2 = y3 = -1*(q/2)**(1./3.) * check(-q/2)

    return [y1 - temp, y2- temp, y3 - temp]


def main():
    a, b ,c, d = map(int, input("\nВведите четыре коэффицента: ").split())
    solutions = list(set(round(i.real, 2)+ round(i.imag, 2)*1j for i in solve(a, b ,c, d)))
    print("Корни уравнения:", ", ".join(output_x(i) for i in solutions), "\n")
    check_solution(solutions, a, b ,c, d)

main()
