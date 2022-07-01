from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/shop_orm')
print(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name} addresses={self.addresses}"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    user = relationship("User", back_populates="addresses")
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)


Base.metadata.create_all(engine)
session: Session = sessionmaker(bind=engine)()

user_one = User(
    name="John Silver",
    addresses=[
        Address(email="john_silver_1@gmail.com"),
        Address(email="john_silver_2@gmail.com"),
    ]
)

user_two = User(name="Woo Chang")


# session.add(user_one)
# session.add(user_two)
# session.add_all([user_one, user_two])
# session.commit()

# Первый подход через session.query

# res = session.query(User).filter_by(name="John Silver")
# print(res.first())


user_three = User(
    name="John Drake",
    addresses=[Address(email="john_drake@gmail.com"), ])

# session.add(user_three)
# session.commit()

# второй подход через select

from sqlalchemy import select
# statement = select(User).where(User.name.contains("John"))
# res = session.scalars(statement)
# for user in res:
#     print(user)

# statement = select(User).where(User.name.contains("John"))
# res = session.scalars(statement).first()
# print(res)

# Добавим адрес для "Woo Chang"
statement = select(User).where(User.name == "Woo Chang")
user = session.scalars(statement).one()
# user.addresses.append(Address(email="woo_chang@gmail.com"))
# session.commit()

# Если хотим поменять email
# user.addresses[0].email = "woo_chang2022@gmail.com"
# session.commit()


users = session.query(User).filter(User.id.in_([1, 2, 6]))
for user in users:
    print(user)

"""
Дз: 
1. сделать фильтр, который будет возвращать 
2. Сделать  БД shop через ORM подход 
3. Заполнить колонку client через библиотеку faker
"""