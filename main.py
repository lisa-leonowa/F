from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/" + input())
    for user in session.query(User).filter(User.id):
        print(user)
    # app.run()


if __name__ == '__main__':
    main()
