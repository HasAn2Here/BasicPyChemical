M = float(input("Enter molarity (mol/L): "))
MW = float(input("Enter molecular weight (g/mol): "))
rho_sol = float(input("Enter solution density (g/L): "))

mass_fraction = (M * MW) / rho_sol

print(f"Mass Fraction: {mass_fraction:.4f}")
