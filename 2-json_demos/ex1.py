import json
# convert a python dict tp json

person={"name":"Rahul","age":25}
json_str=json.dumps(person)
print(json_str)