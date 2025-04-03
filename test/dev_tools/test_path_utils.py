import unittest

from dev_tools.path_utils import find_nearest_parent


class TestFindNearestParent(unittest.TestCase):

    def test_parent_found(self):
        # Case where the parent exists
        current_path = "/path/to/A/B/C"
        parent_name = "A"
        result = find_nearest_parent(parent_name, current_path, "/")
        self.assertEqual("/path/to/A", result)

    def test_parent_not_found(self):
        # Case where the parent does not exist
        current_path = "/path/to/A/B/C"
        parent_name = "Z"
        result = find_nearest_parent(parent_name, current_path, "/")
        self.assertIsNone(result)

    def test_current_directory_is_parent(self):
        # Case where the current directory is the parent
        current_path = "/path/to/A"
        parent_name = "A"
        result = find_nearest_parent(parent_name, current_path, "/")
        self.assertEqual("/path/to/A", result)


    def test_windows_path(self):
        # Case where the current directory is the parent
        current_path = "C:\\A\\B\\C"
        parent_name = "A"
        result = find_nearest_parent(parent_name, current_path, "\\")
        self.assertEqual("C:\\A", result)
