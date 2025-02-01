rho = float(input("Enter fluid density (kg/m³): "))
velocity = float(input("Enter fluid velocity (m/s): "))
diameter = float(input("Enter pipe diameter (m): "))
mu = float(input("Enter fluid viscosity (Pa·s): "))

Re = (rho * velocity * diameter) / mu

print(f"Reynolds Number: {Re:.2f}")
if Re < 2000:
    print("Flow is Laminar")
elif Re < 4000:
    print("Flow is Transitional")
else:
    print("Flow is Turbulent")
