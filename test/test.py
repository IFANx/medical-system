# from flask import Flask, escape, url_for
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'index'
#
#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# @app.route('/user/name=<username>?<abc>')
# def profile(username, abc):
#     return '{}\'s profile'.format(escape(username))
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe', abc=123))
from urllib import parse
if __name__ == '__main__':
    url = '/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    q = parse.urlsplit(url).query
    r = parse.parse_qs(q)
    print(r)

