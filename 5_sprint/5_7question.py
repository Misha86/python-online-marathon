"""7 question 5 sprint"""
import cmath


def solve_quadric_equation(a, b, c):
    try:
        D = float(b)**2 - 4*float(a)*float(c)
        if D != 0:
            x1 = (-b - cmath.sqrt(D))/(2 * a)
            x2 = (-b + cmath.sqrt(D))/(2*a)
            return f"The solution are {x1=} and {x2=}"
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError:
        return "Could not convert string to float"


if __name__ == '__main__':
    print(solve_quadric_equation(1, 5, 6))  # output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"
    print(solve_quadric_equation(0, 8, 1))  # output:   "Zero Division Error"
    print(solve_quadric_equation(1, "abc", 5))  # output:   "Could not convert string to float"
    print(solve_quadric_equation(1, 3, -4))
