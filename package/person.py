from flask_restful import Resource, Api, request
from package.model import conn


class People(Resource):
    def get(self):
        person_all = conn.execute("SELECT * FROM contacts").fetchall()
        return person_all


    def post(self):
        personInput = request.get_json(force=True)
        person_email=personInput['person_email']
        person_first_name=personInput['person_first_name']
        person_last_name = personInput['person_last_name']
        person_ph_no = personInput['person_ph_no']
        personInput['person_id']=conn.execute('''INSERT INTO contacts(person_email,person_first_name,person_last_name,person_ph_no)
            VALUES(?,?,?,?,?)''', (person_email, person_first_name, person_last_name, person_ph_no)).lastrowid
        conn.commit()
        return personInput

class Person(Resource):

    def get(self, email):
        person = conn.execute("SELECT * FROM contacts WHERE person_email=?",(email,)).fetchall()
        return person

    def delete(self, email):
        conn.execute("DELETE FROM contacts WHERE person_email=?",(email,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self, email):
        personInput = request.get_json(force=True)
        person_email = personInput['person_email']
        person_first_name = personInput['person_first_name']
        person_last_name = personInput['person_last_name']
        person_ph_no = personInput['person_ph_no']
        conn.execute("UPDATE contacts SET person_first_name=?,person_last_name=?,person_ph_no=?, WHERE person_email=?",
                     (person_first_name, person_last_name, person_ph_no, person_email))
        conn.commit()
        return personInput

    def post(self):
        personInput = request.get_json(force=True)
        person_email=personInput['person_email']
        person_first_name=personInput['person_first_name']
        person_last_name = personInput['person_last_name']
        person_ph_no = personInput['person_ph_no']
        personInput['person_id']=conn.execute('''INSERT INTO contacts(person_email,person_first_name,person_last_name,person_ph_no)
            VALUES(?,?,?,?,?)''', (person_email, person_first_name, person_last_name, person_ph_no)).lastrowid
        conn.commit()
        return personInput
