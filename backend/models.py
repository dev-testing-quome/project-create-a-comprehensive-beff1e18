import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Permit(Base):
    __tablename__ = 'permits'
    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey('users.id'))
    permit_type = Column(String)
    status = Column(String)
    description = Column(Text)
    application_date = Column(DateTime, default=datetime.datetime.utcnow)
    approval_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    applicant = relationship("User", backref="permits")

# Add other models as needed (e.g., Documents, Fees, etc.)
