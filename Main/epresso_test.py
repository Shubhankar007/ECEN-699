#!/usr/bin/python
from pyeda.inter import *
a, b, c = map(exprvar, 'abc')
z = Or(And(~a, ~b, ~c), And(~a, ~b, c), And(a, ~b, c), And(a, b, c), And(a, b, ~c))
z_min = espresso_exprs(z)
print (z_min)
z_new = ast2expr(z_min)
print (z_new)