def get_season(date):
    """
    Retorna a estação do ano correspondente a uma data fornecida.
    """
    date_tuple = (date.month, date.day)

    if (3, 21) <= date_tuple <= (6, 20):
        return 2.0  # verao
    elif (6, 21) <= date_tuple <= (9, 22):
        return 3.0  # outono
    elif (9, 23) <= date_tuple <= (12, 20):
        return 4.0  # inverno
    else:
        return 1.0  # primavera
