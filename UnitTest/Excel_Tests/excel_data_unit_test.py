import os
import tempfile
import unittest
from openpyxl import Workbook
from excel.excel_data import excel_to_dict


class MyTestCase(unittest.TestCase):
    def create_excel_file(self, headers, rows):
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
        wb = Workbook()
        ws = wb.active

        ws.append(headers)
        for row in rows:
            ws.append(row)

        wb.save(temp.name)
        return temp.name

    def test_basic_excel(self):
        headers = ["Name", "Age"]
        rows = [["Alice", 30], ["Bob", 25]]
        file_path = self.create_excel_file(headers, rows)
        result = excel_to_dict(file_path)
        expected = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
        self.assertEqual(result, expected)
        os.unlink(file_path)

    def test_only_headers(self):
        headers = ["Name", "Age"]
        rows = []
        file_path = self.create_excel_file(headers, rows)
        result = excel_to_dict(file_path)
        self.assertEqual(result, [])
        os.unlink(file_path)

    def test_empty_cells(self):
        headers = ["Name", "Age"]
        rows = [["Alice", None], [None, 22]]
        file_path = self.create_excel_file(headers, rows)
        result = excel_to_dict(file_path)
        expected = [{"Name": "Alice", "Age": None}, {"Name": None, "Age": 22}]
        self.assertEqual(result, expected)
        os.unlink(file_path)

    def test_partial_rows(self):
        headers = ["Name", "Age", "City"]
        rows = [["Alice", 30], ["Bob"]]
        file_path = self.create_excel_file(headers, rows)
        result = excel_to_dict(file_path)
        expected = [
            {"Name": "Alice", "Age": 30, "City": None},
            {"Name": "Bob", "Age": None, "City": None}
        ]
        self.assertEqual(result, expected)
        os.unlink(file_path)

    def test_mixed_types(self):
        headers = ["Name", "BirthYear", "Registered"]
        rows = [["Alice", 1993, True], ["Bob", 1990, False]]
        file_path = self.create_excel_file(headers, rows)
        result = excel_to_dict(file_path)
        expected = [
            {"Name": "Alice", "BirthYear": 1993, "Registered": True},
            {"Name": "Bob", "BirthYear": 1990, "Registered": False}
        ]
        self.assertEqual(result, expected)
        os.unlink(file_path)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            excel_to_dict("nonexistent_file.xlsx")



if __name__ == '__main__':
    unittest.main()
