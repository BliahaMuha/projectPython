from Tasks.tasks1.test import print_clients_devices, engine, Client, Device
from Tasks.tasks2.test import generate_file_names
from sqlalchemy.orm import create_session

session = create_session(bind=engine)


# # ДЛЯ НАПОЛНЕНИЯ БАЗЫ ДАННЫХ НЕОБХОДИМО РАСКОМЕНТИРОВАТЬ КОД НИЖЕ

# # Добавляем данные в таблицу "clients"
# clients_data = [('Татьяна', '89002001020'), ('Анна', '89202202325'),
#                 ('Андрей', '89505205656'), ('Игорь', '89303303236'),
#                 ('Марина', '89562002350'), ('Сергей', '89808564559')]
#
# for name, phone in clients_data:
#     client = Client(name=name, phone=phone)
#     session.add(client)
#     session.commit()

# #Добавляем данные в таблицу "devices"
# devices_data = [('Ноутбук', 1500, 'Татьяна', '89002001020'), ('Смартфон', 500, 'Анна', '89202202325'),
#                 ('Проектор', 300, 'Андрей', '89505205656'), ('Принтер', 750, 'Игорь', '89303303236'),
#                 ('Планшет', 2300, 'Игорь', '89303303236'), ('Смартфон', 1000, 'Андрей', '89505205656'),
#                 ('Ноутбук', 4800, 'Татьяна', '89002001020'), ('Наушники', 780, 'Марина', '89562002350'),
#                 ('Сканер', 550, 'Сергей', '89808564559'), ('Планшет', 1200, 'Анна', '89202202325'),
#                 ('Ноутбук', 1100, 'Игорь', '89303303236'), ('Смартфон', 3500, 'Татьяна', '89002001020')]
#
# for device_name, repair_price, client_name, client_phone in devices_data:
#     # Получаем клиента по имени и телефону
#     client = session.query(Client).filter_by(name=client_name, phone=client_phone).first()
#     # Создаем устройство и связываем его с клиентом
#     device = Device(name=device_name, repair_price=repair_price, client=client)
#     session.add(client)
#     session.add(device)
#
# # Сохраняем изменения в базе данных
# session.commit()

print_clients_devices(session=session)

# Пример использования функции:
names = ['file', 'name', 'long', '_ever', 'banana', 'pineapple', 'rammstain']
generate_file_names(names)
