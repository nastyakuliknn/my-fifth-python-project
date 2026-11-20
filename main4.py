units = {
    "mile": 1609,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}

num, unit_from, _, unit_to = input().split()
result = float(num) * units[unit_from] / units[unit_to]

print(f"{result:.2e}")

