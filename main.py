#code
import cmath
import math

def check(num):
    if num.real < -1:
        return -1
    return 1

def lalal_x(x):
    if x.imag == 0.0:
        return str(x.real)
    else:
        return str(x.real) + " + " + str(x.imag) + "j"



def main():
    a, b ,c, d = map(int, input("\nВведите четыре коэффицента: ").split())
    solutions = list(set(round(i.real, 2)+ round(i.imag, 2)*1j for i in solve(a, b ,c, d, e, f, g)))
    print("Корни уравнения:", ", ".join(output_x(i) for i in solutions), "\n")
    check_solution(solutions, a, b ,c, d)

main()
