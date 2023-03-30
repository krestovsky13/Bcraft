from datetime import datetime

from sqlalchemy import Column, TIMESTAMP, Integer, BigInteger, DECIMAL, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Statistic(Base):
    __tablename__ = "statistic"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, unique=True)
    views = Column(BigInteger, default=0, nullable=False)
    clicks = Column(BigInteger, default=0, nullable=False)
    cost = Column(DECIMAL(scale=2), default=0, nullable=False)
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.now,
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
