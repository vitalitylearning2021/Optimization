function f = objconstrRastrigin(x)

f.Fval = 0;
for k = 1 : length(x)
    f.Fval = f.Fval + x(k)^2 - 10 * cos(2 * pi * x(k));
end
f.Fval = f.Fval + 10 * length(x);

