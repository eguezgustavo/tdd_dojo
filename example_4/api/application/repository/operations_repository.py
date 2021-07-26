from .models import db, OperationModel

class OperationsRepository:

    def __init__(self) -> None:
      self.model = OperationModel

    def save(self, operation):
      operation_object = self.model(**operation)
      db.session.add(operation_object)
      db.session.flush()
      db.session.refresh(operation_object)
      db.session.commit()
      return operation_object
      
        
    def query_by_id(self, id):
      operation = self.model.query.filter(self.model.id == id).all()
      results = [
        {
            "id": item.id,
            "operation": item.operation,
            "number1": item.number1,
            "number2": item.number2,
            "result": item.result,
        } for item in operation]
      return results[0]
