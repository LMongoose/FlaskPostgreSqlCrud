from database import Table

class TablePeople(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM people;"

    @Table.query_select
    def select(self, id_):
        command = "SELECT * FROM people "
        command += f"WHERE people.id = {id_};"
        return command

    @Table.query_insert
    def insert(self, id_, name, birthday):
        command = "INSERT INTO people (id, name, birthday) "
        command += "VALUES ("
        command += f"{id_},"
        command += f"'{name}',"
        command += f"'{birthday}');"
        return command

    @Table.query_update
    def update(self, id_, name, birthday):
        return "UPDATE people "

    @Table.query_delete
    def delete(self, id_):
        commands = []
        command = "DELETE FROM staff "
        command += f"WHERE staff.id_people = {id_};"
        commands.append(command)

        command = "DELETE FROM people "
        command += f"WHERE people.id = {id_};"
        commands.append(command)
        return commands