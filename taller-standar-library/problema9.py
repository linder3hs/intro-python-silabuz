"""
Recolectar los feriados del 2022.

Al ingresar una fecha inicial y días 
hábiles Generar un código que permita encontrar 
la fecha siguiente sin considerar 
fines de semana (sábado y domingo) ni feriados.
"""

"""
hoy: 26/10 + 5
Recerden que en la suma no cuenta sabado, domingo, feriados
res: 03/11
"""




from datetime import datetime, timedelta
def date_by_adding_business_days(current_date, add_days, holidays):
    business_days_to_add = add_days

    while business_days_to_add > 0:
        current_date += timedelta(1)

        if current_date.weekday() >= 5 or current_date in holidays:
            continue

        business_days_to_add -= 1

    return current_date.strftime("%d/%m/%Y")


holidays = [datetime(2022, 10, 3), datetime(2012, 10, 4)]

print(date_by_adding_business_days(datetime(2022, 10, 26), 5, holidays))
