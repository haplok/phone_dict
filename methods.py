import sqlite3


def db_create():
    conn = sqlite3.connect("phone_db.db")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE person (
	person_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20),
	surname VARCHAR(20),
	patronymic VARCHAR(20),
	telephone_1 INT(11),
	telephone_2 INT(11),
    organization VARCHAR(50)
);
"""
    )
    conn.commit()


db_create()
