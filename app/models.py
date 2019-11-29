from app.database import db


class Doctor(db.Model):
    __tablename__ = 'doctor'

    did = db.Column(db.String(10), primary_key=True)  # 医生ID
    name = db.Column(db.String(120), nullable=False)  # 医生名字
    faculty = db.Column(db.String(120))  # 医生的科室
    profession = db.Column(db.String(120))  # 医生的专业职称
    political = db.Column(db.String(120))  # 医生的行政职务
    expertise = db.Column(db.Text)  # 医生的专长
    description = db.Column(db.Text)  # 医生的简介
    hid = db.Column(db.String(12), db.ForeignKey('hospital.hid'))  # 医院的ID
    status = db.Column(db.String(80))  # 医生的状态
    pinying = db.Column(db.String(80))  # 医生的全拼
    full_surname = db.Column(db.String(80))  # 医生全拼的姓氏
    abbre_surname = db.Column(db.String(80))  # 医生简拼的姓氏
    full_firstname = db.Column(db.String(80))  # 医生全拼的名字
    abbre_firstname = db.Column(db.String(80))  # 医生简拼的名字

    articles = db.relationship('Article', backref='doctor', lazy='dynamic')

    def __repr__(self):
        return '<Doctor %r>' % self.name


class Hospital(db.Model):
    __tablename__ = 'hospital'

    hid = db.Column(db.String(12), primary_key=True)  # 医院ID
    hos_name = db.Column(db.String(80), nullable=False)  # 医院名字
    province = db.Column(db.String(80))  # 医院所在省份
    city = db.Column(db.String(80))  # 医院所在城市
    introduction = db.Column(db.Text)  # 医院的介绍
    hos_class = db.Column(db.String(20))  # 医院的等级
    address = db.Column(db.String(256))  # 医院的地址

    doctors = db.relationship('Doctor', backref='hospital', lazy='dynamic')

    def __repr__(self):
        return '<Hospital %r>' % self.hos_name


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tid = db.Column(db.String(50))  # 文章表ID
    name = db.Column(db.String(80))  # 医生名字
    depart = db.Column(db.String(120))  # 医生单位
    article_id = db.Column(db.String(80))  # 文章ID
    author_order = db.Column(db.String(30))  # 作者次序
    did = db.Column(db.String(10), db.ForeignKey('doctor.did'))  # 医生ID

    def __repr__(self):
        return '<Article ID %r>' % self.id
