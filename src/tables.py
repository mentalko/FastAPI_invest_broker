import sqlalchemy as sa
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'Account'

    _id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String)
    registration_date = sa.Column(sa.Date)
    tariff = sa.Column(sa.String)
    deposited_usd = sa.Column(sa.Numeric(10, 2))

class Share(Base):
    __tablename__ = 'Share'

    _id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    ticker = sa.Column(sa.String)
    currency = sa.Column(sa.String)
    close_price =  sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)

class Transaction(Base):
    __tablename__ = 'Transaction'

    _id = sa.Column(sa.Integer, primary_key=True)
    account_id = sa.Column(sa.String)
    share_id = sa.Column(sa.String)
    deal_price =  sa.Column(sa.Numeric(10, 2))
    deal_date = sa.Column(sa.Date)
