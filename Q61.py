import dbm
db1 =  dbm.open("captions", "c")

db1["puppy.png"] = "licks my face"
db1["sunshine.png"] = "so bright and light"
db1["cadyn.png"] = "she is beautiful"

for item in db1:
    print(item, db1[item])
