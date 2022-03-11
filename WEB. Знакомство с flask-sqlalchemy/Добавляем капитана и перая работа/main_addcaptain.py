from data.users import User
from data import db_session


db_session.global_init("db/users.db")


user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Evans"
user.name = "Thomas"
user.age = 19
user.position = "colonist"
user.speciality = "programmer"
user.address = "module_2"
user.email = "thomasev@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Lewis"
user.name = "Jack"
user.age = 20
user.position = "colonist"
user.speciality = "programmer"
user.address = "module_2"
user.email = "jackle@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Brown"
user.name = "Harry"
user.age = 29
user.position = "colonist"
user.speciality = "biologist"
user.address = "module_3"
user.email = "harrybr@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
