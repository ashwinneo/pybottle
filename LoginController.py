from bottle import route, run, request, get, response, HTTPResponse, post,Bottle
import pymysql, bottle, uuid

app = Bottle()

conn = pymysql.connect(host='127.0.0.1',user='root',password='', port=3306 ,db='python_db')
a = conn.cursor()

@bottle.hook('after_request')
def enableCORSAfterRequestHook():
    print 'After request hook.'
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'

def new_session(userName):
    
    key = str(uuid.uuid4())
    print key
    sql = 'INSERT INTO sessions(cookie_id,user_name)VALUES(%s,%s);'
    #cursor = conn.cursor()
    #cursor.execute(sql, key)
    try:
        a.execute(sql, (key,userName))
        conn.commit()
    except Exception as e:
        print(e)
    response.set_cookie("COOKIE_NAME", key)
 
    return key


def get_session(userName):

    sql = 'SELECT COOKIE_ID FROM SESSIONS WHERE USER_NAME = %s;'
    key = a.execute(sql,userName)
    data = a.fetchone()
    print(data)
    if not data:
        # no existing session so we create a new one
        key = new_session(userName)

    return key
get_session('adith.sudhakhar')
#new_session()

@route('/getLoginDetails')
def getLoginDetails():
    try:
        name = request.query.name
        bottle.response.set_header("Access-Control-Allow-Origin", "*")
        bottle.response.set_header("Access-Control-Allow-Headers", "Origin, Content-Type")
        sql = 'SELECT * FROM USER WHERE USER_NAME = %s;'
        a.execute(sql,name)
        data = a.fetchone()
        my_obj = {
            'id' : data[0],
            'username' : data[1],
            'password' : data[2]
            }
        return {'data': my_obj}
    except Exception as e:
        print(e)
    except:
        theBody = {'errorId': '404', 'errorMessage': 'No Data Found!!!'}
        return HTTPResponse(status=404, body=theBody)
    
    
@post('/login')
def login():
    try:
        username = request.body.read()
        print(username)
        key = 0
        return key
    except Exception as e:
        print("Exception" + e)

@route('/*', method = 'OPTIONS')
def login_options():
    response.set_header("Access-Control-Allow-Origin", "localhost");
    return
    

run()
