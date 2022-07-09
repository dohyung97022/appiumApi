from flask import jsonify


# 통일용 응답
class ResponseEntity:

    @classmethod
    def build(cls, **kwargs):

        data = kwargs['data']

        if data is None:
            return {'code': 200}

        tmp = []
        if isinstance(data, list):
            for element in data:
                tmp.append(element.to_dict())
            data = tmp
        else:
            data = data.to_dict()

        response = jsonify(data)

        return response
