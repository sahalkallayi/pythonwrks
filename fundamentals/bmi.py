#write a program to calculate bmi

#bmi=(weight_in_kg/height_in_meter square)

weight_in_kg=55

height_in_cm=150

height_in_meter=height_in_cm/100

bmi=weight_in_kg/height_in_meter**2

print(f"bmi of person with height{height_in_cm} weight {weight_in_kg}={bmi}")