#Дана функция f(x) = 0.6x^3+5.5x^2+10x-5

# корни

from sympy import *

x = Symbol('x')
func = 0.6*x**3+5.5*x**2+10*x-5
y = solve(func)
x1 = complex (y[0])
x2 = complex (y[1])
print(x1,x2)

#интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))


#интервалы, на которых функция убывает

print(solve(fd<0))

#график

from sympy import *
from sympy.plotting import plot
init_printing()

f = 0.6*x**3+5.5*x**2+10*x-5
plot(f)
print(f)

#Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=0.6*x*x*x+5.5*x*x+10*x-5
print(top,y)

#промежутки, на котором f > 0

f1 = solve(0<func)
print(f1)

#промежутки, на котором f < 0

f2 = solve(func<0)
print(f2)