import numpy as np
import matplotlib.pyplot as plt

#coefficients in order [d, u, alpha, gamma, b]
pars = [1,0.31,1.2,-1.3,0]

def euler(f):
    return lambda t, x, h: h*f(t,x)
def heun(f):
    return lambda t, x, h: (lambda k1: h * f( t + h/2, x + k1/2))(h*f(t,x))
def rk4(f):
    return lambda t, x, h: (lambda k1: (lambda k2: (lambda k3: (lambda k4: (k1 + 2*k2 + 2*k3 + k4)/6)( h * f( t + h  , x + k3 )))( h * f( t + h/2, x + k2/2 )))( h * f( t + h/2, x + k1/2)))( h * f( t, x) )
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

def plot(t_0, t_1, x_0, h, f, name=""):
    t, x = t_0, x_0
    res_t, res_x0, res_x1 = [], [], []
    if x_0[0]==x_0[1]:
        opinion = "same opinions"
    else:
        opinion = "opposing opinions"
    while t <= t_1:
        res_t.append(t)
        res_x0.append(x[0])
        res_x1.append(x[1])
        t, x = t + h, x + f(t, x, h)
    plt.plot(res_t, res_x0,"r-")
    plt.plot(res_t, res_x1, "b:")
    plt.legend(("$x_0$", "$x_1$"))
    plt.xlabel("$t$")
    plt.ylabel("$x(t)$")
    plt.title(f"{name}-method, {opinion}, \n $x_0$ starting at {x_0[0]}, $x_1$ starting at {x_0[0]}, $h={h}$")
    plt.show()
    
#plot(0,7,np.array([-1.,-1.]), 1e-3, euler(rhs), "Euler")
#plot(0,7,np.array([-1.,-1.]), 5e-1, euler(rhs), "Euler")
#plot(0,7,np.array([-1.,-1.]), 5e-1, heun(rhs), "Heun")
#plot(0,7,np.array([-1.,-1.]), 5e-1, rk4(rhs), "Runge-Kutta")
#plot(0,7,np.array([1.,-1.]), 1e-3, euler(rhs), "Euler")
#plot(0,7,np.array([1.,-1.]), 5e-1, euler(rhs), "Euler")
#plot(0,7,np.array([1.,-1.]), 5e-1, heun(rhs), "Heun")
#plot(0,7,np.array([1.,-1.]), 5e-1, rk4(rhs), "Runge-Kutta")
