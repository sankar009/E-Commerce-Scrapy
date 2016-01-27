from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class FlipkartProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "flipkartdata"

    id = Column(Integer, primary_key=True)
    images = Column('images', String)
    mainImage = Column('mainImage', String)
    apparelURL = Column('apparelURL', String)
    title = Column('title', String)
    rating = Column('rating', String)
    finalPrice = Column('finalPrice', String)
    initialPrice = Column('initialPrice', String)
    discount = Column('discount', String)


class JabongProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "jabongdata"

    id = Column(Integer, primary_key=True)
    product_link = Column('product_link', String)
    image_320 = Column('image_320', String)
    image_500 = Column('image_500', String)
    image_768 = Column('image_768', String)
    image_1024 = Column('image_1024', String)
    image_1280 = Column('image_1280', String)
    brand = Column('brand', String)
    name = Column('name', String)
    previous_price = Column('previous_price', String)
    standard_price = Column('standard_price', String)
    discount = Column('discount', String)


class PolyvoreProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "polyvoredata"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)