import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'])

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

conn.execute('''CREATE TABLE if not exists contacts
(person_email TEXT PRIMARY KEY,
person_first_name TEXT NOT NULL,
person_last_name TEXT NOT NULL,
person_ph_no TEXT NOT NULL);''')
