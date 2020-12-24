from database import Table

class TableAnimeography(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM animeography;"

    @Table.query_select
    def select(self, id_anime, id_character):
        command = "SELECT * FROM animeography "
        command += f"WHERE animeography.id_anime = '{id_anime}' "
        command += f"AND animeography.id_character = '{id_character}';"
        return command

    @Table.query_insert
    def insert(self, id_anime, id_character, role):
        command = "INSERT INTO animeography (id_anime, id_character, role) "
        command += "VALUES ("
        command += f"{id_anime},"
        command += f"{id_character},"
        command += f"'{role}');"
        return command

    @Table.query_update
    def update(self, id_anime, id_character, role):
        return "UPDATE animeography "

    @Table.query_delete
    def delete(self, id_anime, id_character):
        command = "DELETE FROM animeography "
        command += f"WHERE animeography.id_anime = '{id_anime}' "
        command += f"AND animeography.id_character = '{id_character}';"
        return command