from app.models import Doctor, Hospital
from flask import jsonify

def doctor_to_dict(doctor):
    assert type(doctor) == Doctor, 'Not a Doctor'
    return {
        'name': doctor.name,
        'profession': doctor.profession,
        'expertise': doctor.expertise,
        'hid': doctor.hid,
        'pinying': doctor.pinying,
        'abbre_surname': doctor.abbre_surname,
        'abbre_firstname': doctor.abbre_firstname,
        'faculty': doctor.faculty,
        'did': doctor.did,
        'political': doctor.political,
        'description': doctor.description,
        'status': doctor.status,
        'full_surname': doctor.full_surname,
        'full_firstname': doctor.abbre_firstname
    }


def doctor_to_json(doctor):
    return jsonify(doctor_to_dict(doctor))


def doctors_to_json(doctors):
    return jsonify([doctor_to_dict(d) for d in doctors])


def hospital_to_dict(hospital):
    assert type(hospital) == Hospital, 'Not a Hospital'
    return {
        'hid': hospital.hid,
        'name': hospital.hos_name,
        'province': hospital.province,
        'hos_class': hospital.hos_class,
        'city': hospital.city,
        'introduction': hospital.introduction,
        'address': hospital.address
    }


def hospital_to_json(hospital):
    return jsonify(hospital_to_dict(hospital))


def hospitals_to_json(hospitals):
    return jsonify([hospital_to_dict(h) for h in hospitals])

