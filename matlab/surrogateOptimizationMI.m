% https://towardsdatascience.com/mixed-integer-linear-programming-formal-definition-and-solution-space-6b3286d54892

clear all
close all
clc

lb = [-1, -1];
ub = [ 10, 15];

trials = [0 0];

options = optimoptions('surrogateopt', 'PlotFcn', 'surrogateoptplot', 'InitialPoints', trials);

[x, fval, exitflag] = surrogateopt(@objconstrMI, lb, ub, [1 2], [], [], [], [], options)

