# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import datatypes

import xml.etree.ElementTree as ET


class TestDatatypesClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(datatypes.Datatype('Date', {})),
            '<Datatype type=Date>'
        )

    def test_getDatatype(self):
        self.assertIsInstance(
            datatypes.Datatype('Date', {}).getDatatype(),
            ET.Element
        )

    def test_tostring(self):
        self.assertEqual(
            datatypes.Datatype(
                'Date',
                {
                    'month': '03'
                }
            ).tostring(),
            ET.canonicalize(b'<Date><month>03</month></Date>').encode("utf-8")
        )

    def test_tostring_filter(self):
        cust_filter = datatypes.Datatype('Filter', {'id': '1'})
        self.assertEqual(
            cust_filter.tostring(),
            ET.canonicalize(b'<Filter type="customer"><id>1</id></Filter>').encode("utf-8")
        )

    def test_tostring_addr(self):
        contact = datatypes.Datatype('Contact', {'name': 'John Doe', 'email': 'john.doe@email.com'})
        self.assertEqual(
            contact.tostring(),
            ET.canonicalize(
            b'<Contact><name>John Doe</name><addr><Address>'
            b'<email>john.doe@email.com</email></Address></addr></Contact>'
            ).encode("utf-8")
        )

    def test_tostring_embedded(self):
        date = datatypes.Datatype(
            'Date',
            {
                'month': '03'
            }
        )
        task = datatypes.Datatype(
            'Task',
            {
                'date': date
            }
        )
        self.assertEqual(
            task.tostring(),
            ET.canonicalize(b'<Task><date><Date><month>03</month></Date></date></Task>').encode("utf-8")
        )

    def test_prettify(self):
        self.assertEqual(
            datatypes.Datatype(
                'Date',
                {
                    'month': '03'
                }
            ).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Date>\n'
                b'  <month>03</month>\n'
                b'</Date>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestDatatypesClass)
unittest.TextTestRunner(verbosity=2).run(suite)
