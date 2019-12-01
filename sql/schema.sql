DROP TABLE article;
DROP TABLE doctor;
DROP TABLE hospital;

CREATE TABLE hospital (
        hid VARCHAR(12) NOT NULL,
        hos_name VARCHAR(80) NOT NULL,
        province VARCHAR(80),
        city VARCHAR(80),
        introduction TEXT,
        hos_class VARCHAR(20),
        address VARCHAR(256),
        PRIMARY KEY (hid)
);

CREATE TABLE doctor (
        did VARCHAR(10) NOT NULL,
        name VARCHAR(120) NOT NULL,
        faculty VARCHAR(120),
        profession VARCHAR(120),
        political VARCHAR(120),
        expertise TEXT,
        description TEXT,
        hid VARCHAR(12),
        status VARCHAR(80),
        pinying VARCHAR(80),
        full_surname VARCHAR(80),
        abbre_surname VARCHAR(80),
        full_firstname VARCHAR(80),
        abbre_firstname VARCHAR(80),
        PRIMARY KEY (did),
        FOREIGN KEY(hid) REFERENCES hospital (hid)
);

CREATE TABLE article (
        id INTEGER NOT NULL AUTO_INCREMENT,
        tid VARCHAR(50),
        name VARCHAR(80),
        depart VARCHAR(120),
        article_id VARCHAR(80),
        author_order VARCHAR(30),
        did VARCHAR(10),
        PRIMARY KEY (id),
        FOREIGN KEY(did) REFERENCES doctor (did)
);
