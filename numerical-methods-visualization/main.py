import numerical_methods as nm
import functions as funcs

if __name__ == '__main__':
    #nm.bisection(funcs.f1, -10, 10)
    #nm.bisection(funcs.f2, -4, 5)
    #nm.bisection(funcs.f3, -4, 4)
    nm.false_position(funcs.f4, 5, 11, show_iter_info=True)
