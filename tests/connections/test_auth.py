# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections

import xml.etree.ElementTree as ET


class TestAuthClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(connections.Auth('company', 'username', 'p@ssw0rd')),
            '<Auth company=company username=username>'
        )

    def test_auth(self):
        self.assertIsInstance(
            connections.Auth('company', 'username', 'p@ssw0rd').auth(),
            ET.Element
        )

    def test_tostring(self):
        self.assertEqual(
            connections.Auth('company', 'username', 'p@ssw0rd').tostring(),
            ET.canonicalize(b'<Auth><Login><company>company</company><user>username</user><password>p@ssw0rd</password></Login></Auth>').encode("utf-8")
        )

    def test_prettify(self):
        self.assertEqual(
            connections.Auth('company', 'username', 'p@ssw0rd').prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Auth>\n'
                b'  <Login>\n'
                b'    <company>company</company>\n'
                b'    <user>username</user>\n'
                b'    <password>p@ssw0rd</password>\n'
                b'  </Login>\n'
                b'</Auth>\n'
             )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestAuthClass)
unittest.TextTestRunner(verbosity=2).run(suite)
