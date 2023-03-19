from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session, relationship

# Создаем объект базы данных
engine = create_engine('sqlite:///service_center.db', echo=True)

session = create_session(bind=engine)

# Создаем базовый класс модели
Base = declarative_base()


# Описываем модель таблицы
class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone = Column(String(20), unique=True)
    devices = relationship('Device', back_populates='client')


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    repair_price = Column(Float)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', back_populates='devices')


Base.metadata.create_all(engine)


def print_clients_devices(session):
    # Выполняем запрос к базе данных, чтобы получить список клиентов и их устройств
    clients = session.query(Client).all()

    # Обрабатываем каждого клиента
    for client in clients:
        # Получаем список устройств клиента
        devices = client.devices
        # Объединяем устройства в одну строку
        devices_str = '; '.join([f'{d.name} - {d.repair_price}' for d in devices])
        # Выводим данные о клиенте и его устройствах на печать
        print(f'{client.name} {client.phone}: {devices_str}')
