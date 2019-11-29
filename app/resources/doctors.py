from flask import Blueprint, request
from app.models import Doctor, Article
from app.utils.to_json import doctors_to_json, doctor_to_json
from sqlalchemy import func, or_
from app.database import db

bp = Blueprint('doctors', __name__, url_prefix='/doctors')


'''/doctors?q={query}&faculty={}&hid={}&order={article}&area={}&page={uint}'''
@bp.route('', methods=['GET'])
def doctors():
    if request.method == 'GET':
        q = request.args.get('q')
        faculty = request.args.get('faculty')
        hid = request.args.get('hid')
        order = request.args.get('order')
        page = request.args.get('page')

        d = db.session.query(Doctor).join(Doctor.articles).group_by(Doctor.did)
        if q:
            d = d.filter(or_(Doctor.name.like('%' + q + '%'), Doctor.description.like('%' + q + '%'),
                             Doctor.expertise.like('%' + q + '%')))
        if faculty:
            d = d.filter(Doctor.faculty == faculty)
        if hid:
            d = d.filter(Doctor.hid == hid)
        if order == 'article':
            d = d.order_by(func.count(Article.article_id).desc())

        # 页面控制
        try:
            page = int(page)
            if page < 1:
                page = 1
        except:
            page = 1
        result = d.limit(20).offset(20 * (page - 1))

        return doctors_to_json(result)


@bp.route('/<did>', methods=['GET'])
def doctor(did):
    if request.method == 'GET':
        d = Doctor.query.filter_by(did=did).first()
        return doctor_to_json(d)


@bp.route('/<did>/<path>', methods=['GET'])
def doctor_info(did, path):
    if request.method == 'GET':
        return 'not found', 404
