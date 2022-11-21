def multi(num, num2n, *args):
    if len(args) >= 1:
        res = 1
        for i, argum in enumerate(args):
            res *= argum
        return res * num * num2n
    return num * num2n * args
mul = multi(10, 10, 40)
print(mul)


def parimpar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'


e_par_ou_impar = parimpar(3)
print(e_par_ou_impar)