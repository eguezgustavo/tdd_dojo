from flask import jsonify


class OperationResultPersenter:

    def get_json_response(self, result):
        return result