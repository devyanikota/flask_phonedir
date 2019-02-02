#!/usr/bin/python
import unittest
from package import People, Person

class ContactTest(unittest.TestCase):
    def test_person(self):
        test_person = People(1)
        test_firstname = 'Devyani'
        test_lastname = 'Kota'
        test_email = 'devyani@somemail.com'
        test_ph_no = '987654321'
        test_person = People(test_firstname, test_lastname, test_email,test_ph_no)
        for test in range(3):
            test_slot+=1
            test_person.post(test_slot, test_person)

        self.assertTrue(test_person.test_email)
        test_person.delete(test_person.test_email)

if __name__ == '__main__':
    unittest.main()
