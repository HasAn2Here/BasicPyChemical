R = 0.0821  # Universal Gas Constant (L·atm/(mol·K))

P = float(input("Enter pressure (atm): "))
V = float(input("Enter volume (L): "))
T = float(input("Enter temperature (K): "))

n = (P * V) / (R * T)  # Ideal gas law formula
print(f"Number of moles: {n:.3f} mol")
