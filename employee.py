import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base =  declarative_base() 

class Employee(Base):
    __tablename__="Employee"
    name = Column(String(250),primary_key=True)
    id = Column(Integer)
    
class Address(Base):
    __tablename__="Address"
    Street = Column(String(80),nullable = False)
    Zip = Column(String(5), nullable = False)
    id = Column(Integer,primary_key=True)
    employee_id = Column(Integer, ForeignKey('Employee.id'))
    employee  = relationship(Employee)
    
engine = create_engine('sqlite:///employee.db')

Base.metadata.create_all(engine)     