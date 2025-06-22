import json


def load_data():
    with open("stickers_data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_stickers():
    data = load_data()
    return [item for item in data if item.get("productType") == "sticker"]


print("get_all_stickers")
print(get_all_stickers())


def get_stickers_by_name(item_name):
    data = load_data()
    return [item for item in data if item.get("productType") == "sticker" and item_name in item.get("itemName", "")]


print("get_stickers_by_name: מדבקות שם")
print(get_stickers_by_name("מדבקות שם"))


def get_names_stickers_by_model(model):
    data = load_data()
    return [
        {
            "dbId": item["dbId"],
            "itemName": item["itemName"],
            "graphicStatus": item["graphicStatus"],
            "orderStatus": item["orderStatus"]
        }
        for item in data
        if item.get("productType") == "sticker" and item.get("model") == model
    ]


print("get_names_stickers_by_model:90x52")
print(get_names_stickers_by_model("90x52"))
