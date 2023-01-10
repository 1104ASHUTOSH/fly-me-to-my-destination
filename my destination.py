def min_planes(fuel_units: List[int]) -> int:
    planes = 0
    for i in range(len(fuel_units) - 1):
        planes += fuel_units[i] // (i + 1)
        if fuel_units[i] % (i + 1) > 0:
            planes += 1
    if planes > fuel_units[-1]:
        return -1
    return planes