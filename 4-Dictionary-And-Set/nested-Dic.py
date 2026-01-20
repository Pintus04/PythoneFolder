# Nested Dictionaries

result = {
    "name" : "pintu kumar sharma",
    "class" : 12,
    "role-no" : 3,
    "subject" : {
        "physics" : 78,
        "mathematics" : 98,
        "English" : 34    
    }
}

# print(result["subject"]["physics"]) #print physics marks
# print(result["subject"]) # Printing all subject with marks
# print(result.keys()) #return all keys
# print(result.values()) #return all values
#rint(len(result.keys()))
result["subject"]["chemistry"] = 67 # adding new subject with marks
print(result)