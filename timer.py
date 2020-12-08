import timeit

mysetup = '''
import numpy as np

pars = [1,0.31,1.2,-1.3,0]

def rk4(f):
    return lambda t, x, h: (lambda k1: (lambda k2: (lambda k3: (lambda k4: (k1 + 2*k2 + 2*k3 + k4)/6)( h * f( t + h  , x + k3 )))( h * f( t + h/2, x + k2/2 )))( h * f( t + h/2, x + k1/2)))( h * f( t, x) )

def rhs(t,x,par=pars):
    d = par[0]
    u = par[1]
    alpha = par[2]
    gamma = par[3]
    b = par[4]
    return np.array([-d*x[0]+u*np.tanh(alpha*x[0]+gamma*x[1])+b, -d*x[1]+u*np.tanh(alpha*x[1]+gamma*x[0])+b])

t = 0
x = [1,-1]
h = 5e-1
'''

mysetup2 = '''
import numpy as np

pars = [1,0.31,1.2,-1.3,0]

def rk4a(f, t, x, h):
    k1 = f(t,x)
    k2 = f(t + 0.5*h, x + 0.5*h*k1)
    k3 = f(t + 0.5*h, x + 0.5*h*k2)
    k4 = f(t + h, x + h*k3)
    return (h*(k1 + 2*k2 + 2*k3 + k4)/6)

def rhs(t,x,par=pars):
    d = par[0]
    u = par[1]
    alpha = par[2]
    gamma = par[3]
    b = par[4]
    return np.array([-d*x[0]+u*np.tanh(alpha*x[0]+gamma*x[1])+b, -d*x[1]+u*np.tanh(alpha*x[1]+gamma*x[0])+b])

t = 0
x = [1,-1]
h = 5e-1
'''
mycode = '''
while t <= 7:
    t, x = t + h, x + rk4(rhs)(t, x, h)
'''

mycode2 = '''
while t <= 7:
    t, x = t + h, x + rk4a(rhs, t, x, h)
'''


counter_lambda = 0
counter_classic = 0
for i in range(100):
    time_lambda = timeit.timeit(setup = mysetup, stmt = mycode, number=10000)
    time_classic = timeit.timeit(setup = mysetup2, stmt = mycode2, number=10000)
    if time_lambda < time_classic:
        counter_lambda += 1
    else:
        counter_classic += 1

print(f"Out of 100 runs, the lambda function is faster {counter_lambda} times and the classical method is faster {counter_classic} times.")