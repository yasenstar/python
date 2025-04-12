from math import log as ln

def present_amount(P, r, n):
    return P*(1+r/100)**n

def initial_amount(A, r, n):
    return A*(1+r/100)**(-n)

def years( P, A, r):
    return ln(A/P)/ln(1+r/100)

def annual_rate(P, A, n):
    return 100*((A/P)**(1.0/n)-1)

if __name__ == '__main__':
    print("this is financial culculator")
    A = 2.31525
    P = 2.0
    r = 5
    n = 3
    A_ = present_amount(P, r, n)
    P_ = initial_amount(A, r, n)
    n_ = years(P, A, r)
    r_ = annual_rate(P, A, n)
    print(
        f'A={A_} ({A})\nP={P_} ({P})\nn={n_} ({n})\nr={r_} ({r})'
    )