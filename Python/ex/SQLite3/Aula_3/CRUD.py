import sqlite3

#
# class SQLiteCRUD:
#     def __init__(self, db_file):
#         self.conn = sqlite3.connect(db_file)
#         self.cursor = self.conn.cursor()
#
#     def create_table(self, table_name, columns):
#         """
#         Cria uma tabela no banco de dados.
#
#         :param table_name: nome da tabela a ser criada
#         :param columns: lista de colunas da tabela, no formato (nome_coluna, tipo_coluna)
#         """
#         query = f"CREATE TABLE {table_name} ("
#         for col in columns:
#             query += f"{col[0]} {col[1]}, "
#         query = query[:-2] + ")"
#         self.cursor.execute(query)
#         self.conn.commit()
#
#     def insert_data(self, table_name, data):
#         """
#         Insere dados em uma tabela.
#
#         :param table_name: nome da tabela onde os dados serão inseridos
#         :param data: dicionário com os dados a serem inseridos, no formato {nome_coluna: valor}
#         """
#         cols = ", ".join(data.keys())
#         values = ", ".join([f"'{v}'" for v in data.values()])
#         query = f"INSERT INTO {table_name} ({cols}) VALUES ({values})"
#         self.cursor.execute(query)
#         self.conn.commit()
#
#     def select_data(self, table_name, columns=None, where=None):
#         """
#         Seleciona dados de uma tabela.
#
#         :param table_name: nome da tabela a ser consultada
#         :param columns: lista de colunas a serem selecionadas, ou None para selecionar todas as colunas
#         :param where: condição WHERE da consulta, ou None para retornar todos os registros
#         :return: lista de tuplas com os registros selecionados
#         """
#         cols = "*"
#         if columns is not None:
#             cols = ", ".join(columns)
#         query = f"SELECT {cols} FROM {table_name}"
#         if where is not None:
#             query += f" WHERE {where}"
#         self.cursor.execute(query)
#         return self.cursor.fetchall()
#
#     def update_data(self, table_name, set_values, where):
#         """
#         Atualiza dados em uma tabela.
#
#         :param table_name: nome da tabela a ser atualizada
#         :param set_values: dicionário com os valores a serem atualizados, no formato {nome_coluna: novo_valor}
#         :param where: condição WHERE da atualização
#         """
#         set_query = ", ".join([f"{k}='{v}'" for k, v in set_values.items()])
#         query = f"UPDATE {table_name} SET {set_query} WHERE {where}"
#         self.cursor.execute(query)
#         self.conn.commit()
#
#     def delete_data(self, table_name, where):
#         """
#         Deleta dados de uma tabela.
#
#         :param table_name: nome da tabela a ser atualizada
#         :param where: condição WHERE da deleção
#         """
#         query = f"DELETE FROM {table_name} WHERE {where}"
#         self.cursor.execute(query)
#         self.conn.commit()
#
#     def close_connection(self):
#         """
#         Fecha a conexão com o banco de dados.
#         """
#         self.conn.close()
#
#
# myCrudInSQLite = SQLiteCRUD("myDataBase.db")


import sqlite3

class SQLiteCRUD:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.conn.execute("PRAGMA foreign_keys = 1;")
        self.conn.commit()

    def execute_query(self, query, parameters={}):
        cursor = self.conn.cursor()
        cursor.execute(query, parameters)
        self.conn.commit()
        return cursor

    def insert(self, table, data):
        fields = ', '.join(data.keys())
        placeholders = ', '.join(':' + key for key in data.keys())
        query = f"INSERT INTO {table} ({fields}) VALUES ({placeholders})"
        self.execute_query(query, data)

    def select_all(self, table):
        query = f"SELECT * FROM {table}"
        cursor = self.execute_query(query)
        return cursor.fetchall()

    def select(self, table, where=None, parameters={}):
        if where:
            query = f"SELECT * FROM {table} WHERE {where}"
        else:
            query = f"SELECT * FROM {table}"
        cursor = self.execute_query(query, parameters)
        return cursor.fetchall()

    def update(self, table, data, where, parameters={}):
        fields = ', '.join(f"{key} = :{key}" for key in data.keys())
        query = f"UPDATE {table} SET {fields} WHERE {where}"
        self.execute_query(query, {**data, **parameters})

    def delete(self, table, where, parameters={}):
        query = f"DELETE FROM {table} WHERE {where}"
        self.execute_query(query, parameters)

    def __del__(self):
        self.conn.close()