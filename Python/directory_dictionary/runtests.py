#!/usr/bin/env python

import unittest, subprocess, os, re, base64, shutil
from testfile import *
import tempfile

class CheckRideTestOne(unittest.TestCase):
    testing_dir = "DirectoryDictionaryTests"
    mt_dir = "MTDirectoryDictionaryTest"
    only_txt_files_dir = "OnlyTxtFiles"
    no_txt_dir = "NoTxtFilesTest"
    mixed_files_dir = "MixedFilesTest"
    txt_file_dat = [
        "Hello.",
        "45 data items",
        "multi\nline\nfile"
    ]
    txt_file_names = [
        "file1.txt",
        "file2.txt",
        "file3.txt"
    ]

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(os.path.join(cls.testing_dir, cls.mt_dir)):
            os.mkdir(os.path.join(cls.testing_dir, cls.mt_dir))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(os.path.join(cls.testing_dir, cls.mt_dir))

    def test_dir_reader_only_txt_files(self):
        file_paths = [path for path in self.txt_file_names]
        file_content = [content for content in self.txt_file_dat]
        output = dir_reader(os.path.join(self.testing_dir, self.only_txt_files_dir))
        self.assertIsInstance(output, dict, msg="Expected a dictionary object")
        self.assertTrue(len(output) > 0, msg="Mismatch in dictionary content")
        for file_path, content in output.items():
            self.assertEqual(os.path.basename(os.path.dirname(file_path)), self.only_txt_files_dir, 
                             msg="Unexpected directory name")
            self.assertIn(os.path.basename(file_path), file_paths, msg="Unexpected file name")
            if os.path.basename(file_path) in file_paths:
                # Avoid matching a second time
                file_paths.remove(os.path.basename(file_path))
            self.assertIn(content, file_content, msg="Mismatch in expected file content")
            if content in file_content:
                # Avoid matching a second time
                file_content.remove(content)
    
    def test_dir_reader_mt_dir(self):
        expected = {}
        result = dir_reader(os.path.join(self.testing_dir, self.mt_dir))
        self.assertIsInstance(result, dict, msg="Expected a dictionary object")
        self.assertDictEqual(expected, result, msg="Mismatch in expected dictionary content")
    
    def test_dir_reader_no_txt_files(self):
        expected = {}
        result = dir_reader(os.path.join(self.testing_dir, self.no_txt_dir))
        self.assertIsInstance(result, dict, msg="Expected a dictionary object")
        self.assertDictEqual(expected, result, msg="Mismatch in expected dictionary content")

    def test_dir_reader_mixed_files(self):
        file_paths = [path for path in self.txt_file_names]
        file_content = [content for content in self.txt_file_dat]
        output = dir_reader(os.path.join(self.testing_dir, self.mixed_files_dir))
        self.assertIsInstance(output, dict, msg="Expected a dictionary object")
        self.assertTrue(len(output) > 0, msg="Mismatch in dictionary content")
        for file_path, content in output.items():
            self.assertEqual(os.path.basename(os.path.dirname(file_path)), self.mixed_files_dir, 
                             msg="Unexpected directory name")
            self.assertIn(os.path.basename(file_path), file_paths, msg="Unexpected file name")
            if os.path.basename(file_path) in file_paths:
                # Avoid matching a second time
                file_paths.remove(os.path.basename(file_path))
            self.assertIn(content, file_content, msg="Mismatch in expected file content")
            if content in file_content:
                # Avoid matching a second time
                file_content.remove(content)


if __name__ == '__main__':
    unittest.main()
