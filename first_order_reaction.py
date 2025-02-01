k = float(input("Enter rate constant (1/s): "))
CA = float(input("Enter concentration of reactant A (mol/L): "))

rate = k * CA

print(f"Reaction rate: {-rate:.4f} mol/(L·s)")
