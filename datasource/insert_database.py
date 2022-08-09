from datasource.request_data import REQUEST
from moudle.connect import MYSQL
import env

res = REQUEST()
run_sql = MYSQL
time = res.time.today()

def get_today_data(url):
    data = res.get_data(url)
    date_list = []
    for i in data:
        for j in data[i]:
            date_list.append(j)
    return date_list


def insert_data(sql,url):
    datas = get_today_data(url)
    if datas:
        for name in datas:
            if name:
                try:
                    run_sql.insert_sql(sql.format(env.data_form, name, time))
                except Exception as e:
                    print(e)
    else:
        return '今日无羊'

