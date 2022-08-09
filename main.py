from datasource import weixin_url
from datasource.insert_database import insert_data
import env
import sys
import os


def main():
    # news_url = weixin_url.get_url()
    news_url = 'https://mp.weixin.qq.com/s/7tHJuJUtYEEIqGlywmWpBg'
    if news_url:
        insert_data(sql=env.sql, url=news_url)
        print(1)


def start():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(str(base_dir))
    from api import find_data
    find_data.app.run('0.0.0.0', debug=True)


if __name__ == '__main__':
    # main()
    start()

    # scheduler = BlockingScheduler()
    # scheduler.add_job(main, 'interval', seconds=60)
    # scheduler.start()
