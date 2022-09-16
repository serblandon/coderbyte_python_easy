weight = float(input("what is your weight?"))

measure = input("(k)g or (l)bs")

if measure == 'k':
    weight *= 2.20462262
elif measure == 'l':
    weight /= 2.20462262

print(weight)