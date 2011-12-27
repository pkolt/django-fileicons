# coding: utf-8

import unittest
from fileicons.templatetags.fileicons_filters import get_name_fileicon, get_url_fileicon

class FileIconsTest(unittest.TestCase):
    """
    Тестирование приложения `fileicons`
    """
    def setUp(self):
        self.path = '/media/uploads/main/document.doc'

    def test_blank_ext(self):
        path = '/media/uploads'
        name = get_name_fileicon(path)
        self.assertEqual(name, '')

    def test_filename(self):
        name = get_name_fileicon(self.path)
        self.assertEqual(name, 'document')

    def test_fileicon(self):
        url = get_url_fileicon(self.path)
        self.assertEqual(url, 'fileicons/img/doc.png')

