from flask import jsonify, make_response


# 통일용 응답
class ResponseEntity:

    @classmethod
    def build(cls, data=None, code: int = 200):
        return make_response(cls.data_to_json(data), code)

    @classmethod
    def data_to_json(cls, data):
        if data is None:
            return {}

        tmp = []
        if isinstance(data, list):
            for element in data:
                tmp.append(element.to_dict())
            data = tmp
        elif isinstance(data, str):
            data = data
        else:
            data = data.to_dict()

        return jsonify(data)
