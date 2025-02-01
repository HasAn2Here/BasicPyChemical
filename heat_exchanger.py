mass_flow = float(input("Enter mass flow rate (kg/s): "))
Cp = float(input("Enter specific heat capacity (J/kg·K): "))
T_in = float(input("Enter inlet temperature (°C): "))
T_out = float(input("Enter outlet temperature (°C): "))

Q = mass_flow * Cp * (T_out - T_in)

print(f"Heat transferred: {Q:.2f} J/s (Watts)")
