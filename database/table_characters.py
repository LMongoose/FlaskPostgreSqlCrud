from database import Table

class TableCharacters(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM characters;"

    @Table.query_select
    def select(self, id_):
        command = "SELECT * FROM characters "
        command += f"WHERE characters.id = {id_};"
        return command

    @Table.query_insert
    def insert(self, id_, name, info):
        command = "INSERT INTO characters (id, name, info) "
        command += "VALUES ("
        command += f"{id_},"
        command += f"'{name}',"
        command += f"'{info}');"
        return command

    @Table.query_update
    def update(self, id_, name, info):
        return "UPDATE characters "

    @Table.query_delete
    def delete(self, id_):
        commands = []
        command = "DELETE FROM animeography "
        command += f"WHERE animeography.id_character = {id_};"
        commands.append(command)

        command = "DELETE FROM characters "
        command += f"WHERE characters.id = {id_};"
        commands.append(command)
        return commands