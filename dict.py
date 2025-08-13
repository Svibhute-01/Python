thisdict={
    "name":"snehal",
    "age":19,
    "college":"DY."
}
print(thisdict)
print("Get the value for given key name:")
print(thisdict["name"])
print("Adding new key values")
thisdict["country"]="India"
print(thisdict)
print("Remove age")
print(thisdict.pop("age"))
print("Number of key value pairs in dict:",len(thisdict))
print("Returns all keys",thisdict.keys())    
print("Returns all values",thisdict.values())  
print("Returns all key-value pair",thisdict.items()) 
thisdict.update({"country": "India", "age": 22})
print(thisdict)

