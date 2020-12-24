from database import Table

class TableStaff(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM staff;"

    @Table.query_select
    def select(self, id_anime, id_people):
        command = "SELECT * FROM staff "
        command += f"WHERE staff.id_anime = '{id_anime}' "
        command += f"AND staff.id_people = '{id_people}';"
        return command

    @Table.query_insert
    def insert(self, id_anime, id_people, role):
        command = "INSERT INTO staff (id_anime, id_people, role) "
        command += "VALUES ("
        command += f"{id_anime},"
        command += f"{id_people},"
        command += f"'{role}');"
        return command
    
    @Table.query_update
    def update(self, id_anime, id_people, role):
        return "UPDATE staff "

    @Table.query_delete
    def delete(self, id_anime, id_people):
        command = "DELETE FROM staff "
        command += f"WHERE staff.id_anime = '{id_anime}' "
        command += f"AND staff.id_people = '{id_people}';"
        return command