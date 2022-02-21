from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/api/test')
def test():
    return 'hey'

@api.route('/test')
def testRoute():
    return test()
