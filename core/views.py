from django.shortcuts import render

from django.shortcuts import render

# Данные из задания (вставляем в начало файла)
masters = [
    {"id": 1, "name": "Эльдар 'Бритва' Рязанов"},
    {"id": 2, "name": "Зоя 'Ножницы' Космодемьянская"},
    {"id": 3, "name": "Борис 'Фен' Пастернак"},
    {"id": 4, "name": "Иннокентий 'Лак' Смоктуновский"},
    {"id": 5, "name": "Раиса 'Бигуди' Горбачёва"},
]

services = [
    "Стрижка под 'Горшок'",
    "Укладка 'Взрыв на макаронной фабрике'",
    "Королевское бритье опасной бритвой",
    "Окрашивание 'Жизнь в розовом цвете'",
    "Мытье головы 'Душ впечатлений'",
    "Стрижка бороды 'Боярин'",
    "Массаж головы 'Озарение'",
    "Укладка 'Ветер в голове'",
    "Плетение косичек 'Викинг'",
    "Полировка лысины до блеска"
]

# Статусы заявок
STATUS_NEW = 'новая'
STATUS_CONFIRMED = 'подтвержденная'
STATUS_CANCELLED = 'отмененная'
STATUS_COMPLETED = 'выполненная'

# Тестовые данные заявок
orders = [
    {
        "id": 1,
        "client_name": "Пётр 'Безголовый' Головин",
        "services": ["Стрижка под 'Горшок'", "Полировка лысины до блеска"],
        "master_id": 1,
        "date": "2025-03-20",
        "status": STATUS_NEW
    },
    # ... остальные заявки из задания
]

# Функции представлений
def landing(request):
    """Главная страница"""
    context = {
        'masters': masters,
        'services': services
    }
    return render(request, 'landing.html', context)

def thanks(request):
    """Страница благодарности"""
    return render(request, 'core/thanks.html')

def orders_list(request):
    """Список всех заявок"""
    context = {
        'orders': orders,
        'masters': masters
    }
    return render(request, 'core/orders_list.html', context)

def order_detail(request, order_id):
    """Детальная информация о заявке"""
    # Находим заявку по ID
    order = None
    for o in orders:
        if o['id'] == order_id:
            order = o
            break
    
    # Находим мастера для этой заявки
    master = None
    if order:
        for m in masters:
            if m['id'] == order['master_id']:
                master = m
                break
    
    context = {
        'order': order,
        'master': master
    }
    return render(request, 'core/order_detail.html', context)