import json
import os
import re
from typing import Union, List, Dict, Optional

from openpyxl import load_workbook
import logging as lg


logger = lg.getLogger("OrderExport")
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def setup_logger(log_dir: str) -> None:
    log_path = os.path.join(log_dir, "export_orders.log")
    file_handler = lg.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def excel_to_json(excel_file_path: str, output_json_path: str = None) -> Union[List[Dict], None]:

    try:
        wb = load_workbook(excel_file_path)
        ws = wb.active

        rows = list(ws.iter_rows(values_only=True))
        if not rows or len(rows) < 2:
            logger.warning("Excel file is empty or missing data.")
            return None

        headers = rows[0]
        data = [dict(zip(headers, row)) for row in rows[1:]]

        if output_json_path:
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Exported JSON to {output_json_path}")

        return data

    except Exception as e:
        logger.exception(f"Failed to convert Excel to JSON: {e}")
        return None


def excel_to_json_filtered(excel_file_path: str, output_json_path: str = None) -> Union[List[Dict], None]:
    """
    קוראת קובץ אקסל וממירה אותו לרשימת אובייקטים בפורמט JSON,
    אך רק עם שדות מסוימים בשם חדש ומותאם.
    """
    try:
        wb = load_workbook(excel_file_path)
        ws = wb.active

        rows = list(ws.iter_rows(values_only=True))
        if not rows or len(rows) < 2:
            logger.warning("Excel file is empty or missing data.")
            return None

        headers = rows[0]

        # מיפוי של שמות העמודות המקוריים לשמות החדשים בפורמט קטן
        field_mapping = {
            "Business Partner Reference Number": "referenceNumber",
            "Item Name": "itemName",
            "Name": "name",
            "Quantity": "quantity"
        }

        # מציאת אינדקסים של העמודות הרלוונטיות
        header_indexes = {field_mapping[key]: headers.index(key) for key in field_mapping if key in headers}

        filtered_data = []
        for row in rows[1:]:
            item = {
                new_key: row[idx] for new_key, idx in header_indexes.items()
            }
            filtered_data.append(item)

        if output_json_path:
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=2)
            logger.info(f"Exported filtered JSON to {output_json_path}")

        return filtered_data

    except Exception as e:
        logger.exception(f"Failed to convert Excel to filtered JSON: {e}")
        return None


def extract_type_details(line_item: str) -> Optional[str]:
    """
    מחלץ את שם הדגם והכמות מתוך שורת תיאור מוצר.
    מחזיר מחרוזת בפורמט: <design>_<quantity>
    """
    if not line_item or not isinstance(line_item, str):
        return None

    line_item = line_item.strip()

    # תבנית 1: מדבקות שם - חברים - סט מדבקות 52+90
    pattern1 = r"^מדבקות שם\s*-\s*(?P<design>.+?)\s*-\s*(?:סט\s+מדבקות\s*)?(?P<quantity>\d+(?:\+\d+)?)"

    # תבנית 2: מדבקות שם קטנות במיוחד - ברקע חד קרן ללא איורים
    pattern2 = r"ברקע\s+(?P<design>.+?)\s+ללא\s+איורים"

    # תבנית 3: שקופות עם הדפסה ללא איורים
    pattern3 = r"-\s*(?P<design>[^-]+?)\s+ללא\s+איורים"

    match1 = re.search(pattern1, line_item)
    if match1:
        design = match1.group("design").strip()
        quantity = match1.group("quantity").strip()
        return f"{design}_{quantity}"

    match2 = re.search(pattern2, line_item)
    if match2:
        design = match2.group("design").strip()
        quantity_match = re.search(r"(\d+(?:\+\d+)?)", line_item)
        quantity = quantity_match.group(1) if quantity_match else "unknown"
        return f"{design}_{quantity}"

    match3 = re.search(pattern3, line_item)
    if match3:
        design = match3.group("design").strip()
        quantity_match = re.search(r"(\d+(?:\+\d+)?)", line_item)
        quantity = quantity_match.group(1) if quantity_match else "unknown"
        return f"{design}_{quantity}"

    return None





def excel_to_filtered_json(excel_file_path: str, output_json_path: str = None) -> Union[List[Dict], None]:

    try:
        wb=load_workbook(excel_file_path)
        ws=wb.active

        rows = list(ws.iter_rows(values_only=True))
        if not rows or len(rows) < 2:
            logger.warning("Excel file is empty or missing data.")
            return None

        headers = rows[0]

        field_mapping = {
            "Business Partner Reference Number": "referenceNumber",
            "Item Name": "itemName",
            "Quantity": "quantity",
        }

        header_indexes = {field_mapping[key]: headers.index(key) for key in field_mapping if key in headers}

        filtered_data = []
        for row in rows[1:]:
            item = {
                new_key: row[idx] for new_key, idx in header_indexes.items() if idx < len(row)
            }

            item_line_raw = item.get("itemName")
            item_details = extract_type_details(item_line_raw)
            if item_details:
                item["itemName"] = item_details

            filtered_data.append(item)


        if output_json_path:
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=2)
            logger.info(f"Exported filtered JSON to {output_json_path}")

        return filtered_data

    except Exception as e:
        logger.exception(f"Failed to convert Excel to filtered JSON: {e}")
        return None



if __name__ == '__main__':
    excel_to_filtered_json(r"C:\Users\USER\Downloads\sticker.xlsx",r"C:\Users\USER\Downloads\sticker.json")