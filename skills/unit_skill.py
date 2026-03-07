def convert_units(value, from_unit, to_unit):
    conversions = {
        ("km", "m"): 1000,
        ("m", "km"): 0.001,
        ("kg", "g"): 1000,
        ("g", "kg"): 0.001
    }

    key = (from_unit, to_unit)

    if key in conversions:
        return str(value * conversions[key])
    else:
        return "Conversion not supported."