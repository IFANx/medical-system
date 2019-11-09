from app.database import db


class Doctor(db.Model):
    did = db.Column(db.String(10), primary_key=True)  # 医生ID
    name = db.Column(db.String(80))  # 医生名字
    faculty = db.Column(db.String(120))  # 医生的科室
    profession = db.Column(db.String(120))  # 医生的专业职称
    political = db.Column(db.String(120))  # 医生的行政职务
    expertise = db.Column(db.Text)  # 医生的专长
    description = db.Column(db.Text)  # 医生的简介
    status = db.Column(db.String(20))  # 医生的状态
    pinying = db.Column(db.String(80))  # 医生的全拼
    full_surname = db.Column(db.String(40))  # 医生全拼的姓氏
    abbre_surname = db.Column(db.String(20))  # 医生简拼的姓氏
    full_firstname = db.Column(db.String(40))  # 医生全拼的名字
    abbre_firstname = db.Column(db.String(20))  # 医生简拼的名字

    hid = db.Column(db.String(12), db.ForeignKey('hospital.hid'))  # 医院的ID

    def __init__(self, did):
        self.did = did

    def __repr__(self):
        return '<Doctor %r>' % self.name


class Hospital(db.Model):
    hid = db.Column(db.String(12), primary_key=True)  # 医院ID
    hos_name = db.Column(db.String(80))  # 医院名字
    province = db.Column(db.String(40))  # 医院所在省份
    city = db.Column(db.String(40))  # 医院所在城市
    introduction = db.Column(db.Text)  # 医院的介绍
    hos_class = db.Column(db.String(10))  # 医院的等级
    address = db.Column(db.String(256))  # 医院的地址

    def __repr__(self):
        return '<Hospital %r>' % self.hos_name


class Article(db.Model):
    id = db.Column(db.String(10), primary_key=True)  # 文章表ID
    name = db.Column(db.String(80))  # 医生名字
    depart = db.Column(db.String(120))  # 医生单位
    article_id = db.Column(db.String(40))  # 文章ID
    author_order = db.Column(db.String(30))  # 作者次序
    did = db.Column(db.String(10), db.ForeignKey('doctor.did'))  # 医生ID

    def __repr__(self):
        return '<Article ID %r>' % self.id


class Area(db.Model):
    province_name = db.Column(db.String(40))  # 省份名字
    city_name = db.Column(db.String(40))  # 城市名字
    city_code = db.Column(db.String(12))  # 城市代码
    county_name = db.Column(db.String(40))  # 区县名字
    county_code = db.Column(db.String(12), primary_key=True)  # 区县代码

    def __repr__(self):
        return '<County name %r>' % self.countyName
