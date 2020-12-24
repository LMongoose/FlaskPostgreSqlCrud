from database import Table

class TableUsers(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM users;"

    @Table.query_select
    def select(self, id_):
        command = "SELECT * FROM users "
        command += f"WHERE users.id = {id_};"
        return command

    @Table.query_insert
    def insert(self, id_, username, password, email):
        command = "INSERT INTO users (id, username, password, email) "
        command += "VALUES ("
        command += f"{id_},"
        command += f"'{username}',"
        command += f"'{password}',"
        command += f"'{email}');"
        return command

    @Table.query_update
    def update(self, id_, username, password, email):
        return "UPDATE users "

    @Table.query_delete
    def delete(self, id_):
        command = "DELETE FROM users "
        command += f"WHERE users.id = {id_};"
        return command