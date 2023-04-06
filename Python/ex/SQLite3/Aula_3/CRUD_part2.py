import sqlite3


class SQLiteCRUD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)

    def create_table(self, table_name, columns):
        """
        Cria uma tabela no banco de dados com as colunas especificadas.

        Args:
        - table_name (str): nome da tabela a ser criada.
        - columns (dict): dicionário com os nomes e tipos das colunas da tabela.
            Exemplo: {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'}
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column_name, column_type in columns.items():
            query += f"{column_name} {column_type}, "
        query = query[:-2] + ")"

        self.conn.execute(query)
        self.conn.commit()

    def insert(self, table_name, items):
        """
        Insere vários itens na tabela especificada.

        Args:
        - table_name (str): nome da tabela onde os itens serão inseridos.
        - items (list of dict): lista de dicionários com os valores a serem inseridos.
            Cada dicionário representa um item a ser inserido, com as chaves sendo os nomes
            das colunas e os valores sendo os valores a serem inseridos.
            Exemplo: [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Mary'}]
        """
        columns = list(items[0].keys())
        values = []
        for item in items:
            values.append(tuple(item.values()))

        placeholders = "(" + ",".join(["?" for _ in range(len(columns))]) + ")"
        columns_str = "(" + ",".join(columns) + ")"
        query = f"INSERT INTO {table_name} {columns_str} VALUES {placeholders}"

        self.conn.executemany(query, values)
        self.conn.commit()

    def select(self, table_name, columns=None, where=None):
        """
        Seleciona itens da tabela especificada com as colunas e condições especificadas.

        Args:
        - table_name (str): nome da tabela a ser selecionada.
        - columns (list): lista com os nomes das colunas a serem selecionadas. Se não for
            especificado, todas as colunas serão selecionadas.
        - where (str): condição para filtrar os resultados. Deve ser uma string com a
            sintaxe do SQL.
            Exemplo: "age > 18"

        Returns:
        - list of dict: lista de dicionários com os itens selecionados. Cada dicionário
            representa um item, com as chaves sendo os nomes das colunas e os valores sendo
            os valores dos itens selecionados.
        """
        if columns is None:
            columns_str = "*"
        else:
            columns_str = ",".join(columns)

        query = f"SELECT {columns_str} FROM {table_name}"
        if where is not None:
            query += f" WHERE {where}"

        cursor = self.conn.execute(query)
        rows = cursor.fetchall()

        items = []
        for row in rows:
            item = {}
            for i, column_name in enumerate(cursor.description):
                item[column_name[0]] = row[i]
            items.append(item)

        return items