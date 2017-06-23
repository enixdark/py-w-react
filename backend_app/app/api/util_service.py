from flask_restful import (
    Resource,
    marshal,
    marshal_with,
    fields,
    reqparse,
    abort)
from flask import request

from ..utils.parse import match

class UtilService(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('text', type=str, required=False)
        self.reqparse.add_argument('subtext', type=str,required=False)

    def get(self):
        args = self.reqparse.parse_args()
        if args['text'] != None and args['subtext'] != None:
            return match(args['text'], args['subtext'])
        return None, 404