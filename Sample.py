from bottle import route, run, template
# 
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
 
 

# @route('/')
# @route('/hello/<name>')
# def greet(name='Stranger'):
#     return template('Hello {{name}}, how are you?', name=name)

run(host='localhost', port=8080)