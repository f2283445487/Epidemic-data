from flask import Flask, jsonify, request
from flask_cors import *
# import pymysql
# import env
# from read_config import read_yaml

app = Flask(__name__)


@app.route('/find_data', methods=['POST', 'GET'])
@cross_origin()
def find_data():
    # db = pymysql.connect(host=read_yaml().get('db').get('host'),
    #                      user=read_yaml().get('db').get('user'),
    #                      password=read_yaml().get('db').get('password'),
    #                      database=read_yaml().get('db').get('database'))
    # run_sql = db.cursor(pymysql.cursors.DictCursor)
    if request.method == 'GET':
        if request.args is not None:
            # get_data = request.args.to_dict()
            # subdistrict = get_data.get('subdistrict')
            # run_sql.execute("select * from subdistrict_info where subdistrict like '%{}%'".format(subdistrict))
            # datas = run_sql.fetchall()
            # if datas:
            #     return jsonify(datas)
            # else:
            msg = {"msg": '无'}
            return jsonify(msg)
        else:
            msg = {
                "msg": '我是一哥'
            }
            return jsonify(msg)
    else:
        msg = {
            "msg": '我是前端一哥'
        }
        return jsonify(msg)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
