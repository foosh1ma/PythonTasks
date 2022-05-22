from datetime import datetime, timedelta


def date_in_future(integer):
    if not isinstance(integer, int):
        return datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    else:
        return (datetime.today() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))
