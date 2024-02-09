def f(x):
    return x ** 3 + 3


def f_prime(x):
    return 3 * x ** 2


def newtons_method(initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    iteration = 0

    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= tolerance:
        return x
    else:
        return None  # If max_iterations exceeded without convergence


initial_guess = 1.0  # Initial guess for Newton's method
root = newtons_method(initial_guess)

if root is not None:
    print("Root found at x =", root)
    print("Function value at root f(x) =", f(root))
else:
    print("Newton's method did not converge within the maximum number of iterations.")
