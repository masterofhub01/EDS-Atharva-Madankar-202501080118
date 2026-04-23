#take inputs of mass and velocity
m = float(input("Enter the mass of the object in kg: "))
v = float(input("Enter the velocity of the object in m/s: "))
#define momentum as mass times velocity
p = m * v
#print the value of momentum till two decimal places
print(f"The Momentum of the object is: {p:.2f}kgm/s")
