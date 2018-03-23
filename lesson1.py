x = input()
if x[-1] == 'm':
    y = eval(x[:-1])*39.37
    print("{:.3f}in".format(y))
else:
    y = eval(x[:-2])/39.37
    print("{:.3f}m".format(y))