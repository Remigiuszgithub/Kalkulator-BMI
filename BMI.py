print('Program oblicza współczynnik BMI i interpretuje jego wartość')
waga=float(input('Podaj swoją wagę: '))
wzrost=float(input('Podaj swój wzrost: '))
if wzrost>2.3 or wzrost<0.5 or waga<20 or waga>300:
    print("Coś ci się pomyliło z danymi")
else:
 BMI=waga/(wzrost**2)
print('Twój współczynnik BMI wynosi: ',round(BMI,2))
if BMI<22:
    print('Masz niedowagę')
elif BMI<25:
     print('Twoja waga jest w normie')
else:
        print("Masz nadwagę")
