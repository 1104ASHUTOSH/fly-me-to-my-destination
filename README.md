# fly-me-to-my-destination


def min_planes(fuel_units: List[int]) -> int:
    planes = 0
    for i in range(len(fuel_units) - 1):
        planes += fuel_units[i] // (i + 1)
        if fuel_units[i] % (i + 1) > 0:
            planes += 1
    if planes > fuel_units[-1]:
        return -1
    return planes


This solution iterates through the list of fuel units and keeps track of the number of planes needed in the planes variable. For each airport, it calculates the number of planes needed to reach the next airport by dividing the fuel units available by the distance to the next airport (which is i + 1 because the distance between two consecutive airports is 1). If there is any remainder after dividing the fuel units by the distance, it means that we need to hire an extra plane. Finally, it checks if the number of planes needed is greater than the fuel units available at the final airport. If it is, it means we can't reach the final airport, so it returns -1. Otherwise, it returns the number of planes needed.
