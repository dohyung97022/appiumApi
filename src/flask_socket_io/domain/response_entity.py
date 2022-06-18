from flask import jsonify


# 통일용 응답
class ResponseEntity:

    @classmethod
    def build(cls, data):

        tmp = []
        if isinstance(data, list):
            for element in data:
                tmp.append(element.to_dict())
            data = tmp
        else:
            data = data.to_dict()

        response = jsonify(data)

        # response.headers.add('Access-Control-Allow-Origin', '*')

        return response
