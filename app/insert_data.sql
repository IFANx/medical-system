load data local infile '/home/ground/share/medical-system/raw_data/hospital.csv'
    into table hospital
    fields terminated by ','
    optionally enclosed by '"'
    lines terminated by '\r\n'
    ignore 1 lines;

load data local infile '/home/ground/share/medical-system/raw_data/doctor.csv'
    into table doctor
    fields terminated by ','
    optionally enclosed by '"'
    lines terminated by '\r\n'
    ignore 1 lines;

load data local infile '/home/ground/share/medical-system/raw_data/article.csv'
    into table article
    fields terminated by ','
    optionally enclosed by '"'
    lines terminated by '\r\n'
    ignore 1 lines;