from datetime import datetime


def get_data_atual_e_retorna_periodo():
    time = datetime.now()
    if 6 <= time.hour <= 12:
        return "Manhã"
    elif 12 < time.hour <= 18:
        return "Tarde"
    elif 18 < time.hour > 6:
        return "Noite"
    else:
        return "Não foi possível identificar o período"