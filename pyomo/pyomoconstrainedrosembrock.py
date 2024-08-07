# -*- coding: utf-8 -*-
"""pyomoConstrainedRosembrock.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQwZ-UjuLRVfWVG6XLWO7I3uIvPqjf-_
"""

!pip install -q pyomo

!wget -N -q "https://github.com/thomasfork/ipopt_linux/raw/main/ipopt-linux64.zip"
!unzip -o -q ipopt-linux64

import numpy as np
from pyomo.environ import *

def rosembrock(model):
  return (1 - model.x[1])**2 + 100. * (model.x[2] - model.x[1]**2)**2

def constraint1(model):
  return (model.x[1] - 1.)**3 - model.x[2] + 1 <= 0.

def constraint2(model):
  return model.x[1] + model.x[2] - 2. <= 0.

# --- Create a model
model             = ConcreteModel()

model.x           = Var((1, 2), within = Reals)

model.x[1].value  = 3.
model.x[2].value  = -4.

model.x[1].lower  = -1.5
model.x[1].upper  = 1.5
model.x[2].lower  = -0.5
model.x[2].upper  = 2.5

# --- Declare objective function
model.objfun      = Objective(rule = rosembrock, sense = minimize)

model.Constraint1 = Constraint(rule = constraint1)
model.Constraint2 = Constraint(rule = constraint2)

model.pprint()

SolverFactory('ipopt', executable='/content/ipopt').solve(model).write()
#SolverFactory('multistart').solve(model, strategy = 'rand_guess_and_bound', solver = 'ipopt', iterations = 50).write()

# display solution
print('\nObjective function = ', model.objfun)

print('\nDecision Variables')
for i in model.x:
  print(model.x[i]())