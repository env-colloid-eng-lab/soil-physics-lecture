def concentration_gm3_to_percent(concentration_gm3, molar_mass, pressure_kpa, temperature_c, gas_constant=8.3143):
    return concentration_gm3 * (gas_constant * (temperature_c + 273.15)) / (pressure_kpa * 1000.0 * molar_mass) * 100.0


def concentration_percent_to_gm3(concentration_percent, molar_mass, pressure_kpa, temperature_c, gas_constant=8.3143):
    return concentration_percent * pressure_kpa * 1000.0 * molar_mass / ((temperature_c + 273.15) * gas_constant) / 100.0
