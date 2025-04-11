# info={
#     "name":"ali",
#     "class" :"iv",
#     "age":8,
#     "sub" :("eng","urd","math","sci"),
#     "events" :["sportsday" ,"Annualfunction"],
#     "is_result_day":"True"
# }
# print(info)
# # want to add new keyvalue pai
# info["f.name"]="Adnan"
# print(info)
# # want to change value of a key or if u wnt to write another age u cannot use the same key"age"
# # bcz it will  not add new key it will overwrite the old age value
# info["age"]=9
# print(info)
# # null dictionary can be made also and in future can add any key vlaue
# null_dict={}
# print (null_dict)
# # can add any value
# null_dict["name"]="naila"
# print(null_dict)
# # nested dictinary
devloper={
    "Staff":"AmeenAlam",
    "faculty":{
        "Hamza syed" : "Deen",
        "AliAftab" : "senior",
        "bilalMuhammad":"junior",
        "AsharibAli":"lead",
    }
}
# print(devloper)
# # but want only faculty dictionary/nested dictionary
# print(devloper["faculty"])
# # but want only asharib ali detail wecan als get it from nested dictionary
# print(devloper["faculty"]["AsharibAli"])
# # can access keys only by using .key method and will return only outer keys not nested keys
# print(devloper.keys())
# # can also accees keys of nested dictionary
# print(devloper["faculty"].keys())
# # if want to type cast it into list we can do so ..it will return keys in list form[]
# print(list(devloper.keys()))
# # can also find length of keys
# print(len(devloper.keys()))
# # can also access length after converting dic to list
# print(len(list(devloper.keys())))
# """can access values just like keys above"""
# # can access values of developer dicionary
# print(devloper.values())
# # only values of faculty nested dictionary
# print(devloper["faculty"].values())
# can also typecast into list it will return a list an dictionary inside
# so we can save a list datatype into dictionary and viceversa
# print(list(devloper.values()))

""".items Always return keyvaluepair in atuple [('Staff', 'AmeenAlam')]"""
# print(devloper.items())
# # can typecast it into list
# print(list(devloper.items()))
# # can alst take length of 
print(len(list(devloper["faculty"].items())))
# # we onvert into list and now can access its values by index no
new_form=(list(devloper["faculty"].items()))
print(new_form[1])
# print()
# print(devloper["safffff"])#it 'll give error if key is wrongs so get function is best toget value of a key
print(devloper.get("Staff"))# by calling with get  function returns none """ameenalam"
