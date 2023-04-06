from CRUD_part2 import SQLiteCRUD

my_bank = SQLiteCRUD("myDataBase.db")
my_bank.connect()
my_bank.create_table("users", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name": "TEXT",
    "number": "INTEGER",
})

name = "Joao"
number = 89898989

for i in range(1000000):
    my_bank.insert("users",[
        {"id": None, "name":f"{name+str(i)}", "number":f"{number + i}"}
    ])

# my_bank.insert("users", [
#     {"id": None, "name": "Lucas", "number": 384929221},
#     {"id": None, "name": "Joao", "number": 283323233},
#     {"id": None, "name": "Maria", "number": 234843283},
#     {"id": None, "name": "Augusto", "number": 273739232},
# ])

print(my_bank.select("users"))
