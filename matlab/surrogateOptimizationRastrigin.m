% https://en.wikipedia.org/wiki/Rastrigin_function#:~:text=In%20mathematical%20optimization%2C%20the%20Rastrigin,has%20been%20generalized%20by%20Rudolph.

clear all
close all
clc

lb = [-5.12, -5.12];
ub = [ 5.12,  5.12];

trials = [0.5, -0.1];

options = optimoptions('surrogateopt', 'PlotFcn', 'surrogateoptplot', 'InitialPoints', trials);

[x, fval, exitflag] = surrogateopt(@objconstrRastrigin, lb, ub, options)

