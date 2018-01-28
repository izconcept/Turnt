from datetime import datetime


def calculate_bac(drinks, weight, start_time, gender):
    alcohol = sum([drink['percentage'] * drink['amount'] for drink in drinks])
    if gender == 'male':
        g_constant = .73
    else:
        g_constant = .66

    time_elapsed = datetime.now() - start_time
    return ((alcohol * 5.14) / weight * g_constant) - (0.15 * time_elapsed.hour)
