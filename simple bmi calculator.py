weight = float(input('Enter your weight (KG) :'))
height = float(input('Enter your height (Meter):'))

bmi = weight / (height**2)
print ("tomar bmi holo", round(bmi,2))

if bmi  < 18.5:
    print('tumi underweight.')
elif bmi  < 25:
    print ('tumi normar weight e acho.')
elif bmi  < 30:
    print('Tumi overweght acho.')
else:
    print('Tumi obssed a acho.')
