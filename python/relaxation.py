from ode import *
import math

def model(y, t):
    """ Derivatives for the relaxation system """
    return -y

def analytical_solution(t):
    return math.exp(-t)

compare_ode_methods(model, dt = 0.1, analytical_solution=analytical_solution)