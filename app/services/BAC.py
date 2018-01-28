from datetime import datetime


def calculate_bac(drinks, weight, start_time, gender):
    return ((sum([drink['percentage'] * drink['amount'] for drink in drinks]) * 5.14) / weight * (.73 if gender == 'male' else .66)) - (0.15 * (datetime.now() - start_time).hour)
