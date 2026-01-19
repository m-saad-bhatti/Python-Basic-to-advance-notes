info = {
    "name": "Saad",
    "age":  21,
    "uni": "SMIU",
    "city": "Karachi",
    "height": 5.11,
    "subjects": ["python", "C++", "C", "IS"],
    "is_adult": True
}
print(info)
print(info["name"])
# changing the value of a key
info["name"]="Saad Munir"
print(info)

# adding a new key-value pair
info["dateofbirth"] = "24-07-2003"
print(info)

# deleting a key-value pair
del info["city"]
print(info)

# nested dictionary
nes_dic = {
    "street": {
        "house_no": 4,
        "block": 62,
        "street_num": 13
    },
    "city": "Karachi",
    "country": "Pakistan"
}
print(nes_dic)
print(nes_dic["street"]["house_no"])
print(nes_dic["street"]["block"])

# methods in dictionary
print(info.keys())
print(info.values())
print(info.items()) 
print(info.get("uni"))

# difference between get and [] operator
#print(info["name2"]) #this will give an error 
# program will stop here
print(info.get("name2")) #this will not give an error
# program will continue to run but will print None
info.update({"Branch": "Software Engineering"})
print(info)

dict1={
    "table": {"a piece of furniture", "a list of data"},
    "cat": {"an animal"},
}
print(dict1["table"])