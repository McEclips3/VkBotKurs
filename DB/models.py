import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = sq.Column(sq.BIGINT, primary_key=True)
    name = sq.Column(sq.String(length=70), unique=False)
    second_name = sq.Column(sq.String(length=70), unique=False)
    city = sq.Column(sq.String(length=70), unique=False)
    age = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.String(length=70))


class Favorites(Base):
    __tablename__ = 'favorites'

    fav_id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.BIGINT, sq.ForeignKey('user.user_id'), nullable=False)
    fav_vk_id = sq.Column(sq.BIGINT, nullable=False)

    user = relationship(User, backref='favorites')


class Photo(Base):
    __tablename__ = 'photo'

    photo_id = sq.Column(sq.Integer, primary_key=True)
    fav_id = sq.Column(sq.Integer, sq.ForeignKey('favorites.fav_id'), nullable=False)
    link = sq.Column(sq.String(length=500))

    favorites = relationship(Favorites, backref='photos')


class Blacklist(Base):
    __tablename__ = 'blacklist'

    black_id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.BIGINT, sq.ForeignKey('user.user_id'), nullable=False)
    black_vk_id = sq.Column(sq.BIGINT, nullable=False)

    user = relationship(User, backref='blacklist')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
