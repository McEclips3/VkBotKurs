import os
from os.path import join, dirname
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from DB.models import create_tables, User, Favorites, Photo, Blacklist


dotenv_path = join(dirname(__file__), 'loginpass.env')
load_dotenv(dotenv_path)
login = os.environ.get("LOGIN")
password = os.environ.get("PASS")
DSN = f"postgresql://{login}:{password}@localhost:5432/vkbot_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
# session.close()


def new_user(vk_user_id, vk_link, first_name, last_name, gender, city, age):
    session.add(User(
        user_id=vk_user_id,
        link=vk_link,
        sex=gender,
        age=age,
        city=city,
        name=first_name,
        second_name=last_name
    ))

    session.commit()

# def new_favorite(vk_user_id, )

