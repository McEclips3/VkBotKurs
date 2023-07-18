import os
from os.path import join, dirname
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables


if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), 'loginpass.env')
    load_dotenv(dotenv_path)
    login = os.environ.get("LOGIN")
    password = os.environ.get("PASS")
    DSN = f"postgresql://{login}:{password}@localhost:5432/vkbot_db"
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.close()


