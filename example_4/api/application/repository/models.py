from sqlalchemy import Column, Integer, String
from application import db
from flask_migrate import Migrate


migrate = Migrate()

class OperationModel(db.Model):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    operation = Column(String())
    number1 = Column(Integer())
    number2 = Column(Integer())
    result = Column(Integer())

    def __init__(self, operation, number1, number2, result):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.result = result 


    def __repr__(self):
        return f"<Operation.{self.id}({self.name})>"
