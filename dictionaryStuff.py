orders = {
    "John": [
        {"ordn": 1, "choice" : ["pizza","spag"]},
        {"ordn": 2, "choice" : ["cola","pasta"]}
    ],
    "Pete": [
        {"ordn": 1, "choice" : ["juice","salad"]},
        {"ordn": 2, "choice" : ["cola","pasta"]}
    ]
}
print(orders)
print(orders["John"])
print(orders["John"][0])
print(orders["John"][0]["choice"])
print(orders)




db = [] #array that will store the records
dbrec1 = {
    "sid": 1234,
    "name": "John Smith",
    "dob": "10/01/1980"
}
dbrec2 = {
    "sid": 5678,
    "name": "Peter Smith",
    "dob": "10/01/1982"
}
db.append(dbrec1)
db.append(dbrec2)

print(db,db[0])

