import json
# convert a python dict to json and saving it in file
person={"name":"Rahul","age":25}

with open("data.json","w") as file_obj:
    json.dump(person,file_obj)
