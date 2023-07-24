def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    if not all(isinstance(p, tuple) and len(p) == 2 for p in permanence_period):
        return None

    arrivals, departures = set(), set()

    for arrive, depart in permanence_period:
        if not (isinstance(arrive, int) and isinstance(depart, int)):
            return None
        arrivals.add(arrive)
        departures.add(depart)

    counter = sum(1 for arrive, depart in permanence_period if arrive <= target_time <= depart)
    
    return counter


# Teste com os mesmos exemplos:
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 5))  # Saída: 3
print(study_schedule(permanence_period, 4))  # Saída: 3
print(study_schedule(permanence_period, 3))  # Saída: 2
print(study_schedule(permanence_period, 2))  # Saída: 4
print(study_schedule(permanence_period, 1))  # Saída: 2
