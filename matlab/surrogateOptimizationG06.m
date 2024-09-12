% https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781119136507.app2

clear all
close all
clc

lb = [ 13,   0];
ub = [100, 100];

trials = [13.5, 0.5];

options = optimoptions('surrogateopt', 'PlotFcn', 'surrogateoptplot', 'InitialPoints', trials);

[x, fval, exitflag] = surrogateopt(@objconstrG06, lb, ub, options)

