from ex090_sqlite_DML import db_update, db_insert, db_select, db_delete

# db_insert('Maria', '32032803', 'weldas@gmail.com')
# db_insert('Fabricio', '2926311', 'fab@gmail.com')
# db_insert('Ricardo', '29127102', 'ricardodas@gmail.com')
# db_insert('Marcio', '21713461391', 'Marcio@gmail.com')
# db_insert('Marcio', '21713461391', 'Marcio1@gmail.com')
# db_insert('Marcio', '21713461391', 'Marcio2@gmail.com')
# db_insert('Marcio', '21713461391', 'Marcio3@gmail.com')
# db_insert('Marcio', '21713461391', 'Marcio4@gmail.com')

print(db_select(data='21713461391', em_qual_campo='phone'))