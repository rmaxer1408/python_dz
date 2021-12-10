# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек
duration = int(input('Введите время в секундах: '))
days = duration // 86400
hours = duration % 86400 // 3600
minutes = duration % 86400 % 3600 // 60
sec = duration % 86400 % 3600 % 60
if duration // 60 == 0:
    print(f'{sec} сек')
elif duration // 60 < 60:
    print(f'{minutes} мин {sec} сек')
elif duration // 60 < 1440:
    print(f'{hours} час {minutes} мин {sec} сек')
else:
    print(f'{days} дн {hours} час {minutes} мин {sec} сек')
