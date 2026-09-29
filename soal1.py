def convert_temperature(value, unit):
    """Konversi suhu Celsius <-> Fahrenheit.

    value : nilai suhu (angka)
    unit  : 'C' jika value dalam Celsius (hasil Fahrenheit),
            'F' jika value dalam Fahrenheit (hasil Celsius)
    """
    unit = unit.upper()
    if unit == 'C':
        return (value * 9 / 5) + 32
    elif unit == 'F':
        return (value - 32) * 5 / 9
    else:
        return "Unit tidak valid! Gunakan 'C' atau 'F'."


# Contoh pemanggilan
print("100 C =", convert_temperature(100, 'C'), "F")
print("212 F =", convert_temperature(212, 'F'), "C")
print("37 C  =", convert_temperature(37, 'C'), "F")
print("0 K   =", convert_temperature(0, 'K'))
