from bottle import route, run, request, get
# 
#
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='', port=3306 ,db='python_db')
a = conn.cursor()

@get('/getLoginDetails')
def getLoginDetails():
    try:
        name = request.query.name
        sql = 'SELECT * FROM USER WHERE USER_NAME = %s;'
        a.execute(sql,name)
        data = a.fetchone()
        my_obj = {
            'id' : data[0],
            'username' : data[1],
            'password' : data[2]
            }
        return {'data': my_obj}
    except:
        return {'errorId': '404', 'errorMessage': 'No Data Found!!!'}


run()
