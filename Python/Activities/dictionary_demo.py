example_dict = {
    " brand":"ford",
               "model": "Mustang",
               "year":1964
               }
print(example_dict)
x = example_dict["model"]
print(x)

x=example_dict.get("model")
print(x)
x = example_dict["m"]
print(x)

x = example_dict. get("m", 2345)
print(x)

example_dict["year"] = 2018

 for or x, y in example_dict.items():
     print(x,y)
     example_dict ["color"] ="red"
     print(example_dict)
    example_dict.pop("model")
     print(example_dict)