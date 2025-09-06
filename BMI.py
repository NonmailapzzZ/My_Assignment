## Create a variable to recive a data from USER
weight = input("Input your weight : ") 
weight = float(weight)

hight = input("Input your hight : ") 
hight = float(hight)

# define a fuction for calculate weight and hight
def Body_mass_index (weight, hight):
    BMI = weight / (hight ** 2) # formular to calculate "Body Mass Index"
    
    if BMI >= 40 :
        shape = 'Very fat'
    elif BMI >= 35 :
        shape = 'Fat level 2'
    elif BMI >= 28.5 :
        shape = 'Fat level 1'
    elif BMI >= 23.5 :
        shape = 'Overweight'
    elif BMI >= 18.5 :
        shape = 'Normal'
    else :
        shape = 'Underweight'

    return shape



BMI = Body_mass_index(weight,hight)
print(BMI)