# DML -> MANPILACAO DE DADOS
import sqlite3 as sql

def commit_close(func):
    def decorator(*args):
        connect = sql.connect('mybase.db')
        cursor = connect.cursor()
        sql_ = func(*args)
        cursor.execute(sql_)
        connect.commit()
        connect.close()
    return decorator

@commit_close
def db_insert(name, phone, email):
    new_response = f"""
    INSERT INTO users (name, phone, email)
    VALUES('{name}', {phone}, '{email}')
    """
    return new_response


@commit_close
def db_update(dado_a_ser_mudado, novo_dado, identificador,id_data):
    new_data = f"""
    UPDATE users SET {dado_a_ser_mudado} = '{novo_dado}' WHERE {identificador} = '{id_data}'
    """
    return new_data


@commit_close
def db_delete(del_id):
    data_del = f"""
    DELETE FROM users WHERE email={del_id}
    """
    return data_del


def db_select(data, em_qual_campo):
    connect = sql.connect('mybase.db')
    cursor = connect.cursor()
    busca = f"""
    SELECT id, name, phone, email
    FROM users
    WHERE {em_qual_campo}={data}
"""
    cursor.execute(busca)
    data_ = cursor.fetchone()
    connect.close()
    return data_


