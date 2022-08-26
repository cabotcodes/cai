def calc_BMI(height, weight, units_height, units_weight):
    if units_height == "in":
        h = height * 2.54
    else:
        h = height
        
    if units_weight == "lbs":
        w = weight / 2.2
    else:
        w = weight


    BMI = round(w/((h/100)**2))

    return BMI


units_height = 'in'
height = 183 / 2.54

units_weight = 'lbs'
weight = 145

print(calc_BMI(height, weight, units_height, units_weight))
