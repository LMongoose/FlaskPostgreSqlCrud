from database import Table

class TableAnimes(Table):
    def __init__(self, db):
        super().__init__(db)

    @Table.query_list_all
    def list_all(self):
        return "SELECT * FROM animes;"

    @Table.query_select
    def select(self, id_):
        command = "SELECT * FROM animes "
        command += f"WHERE animes.id = {id_};"
        return command

    @Table.query_insert
    def insert(self, id_, title, type_, synopsis, release_date, episodes):
        command = "INSERT INTO animes (id, title, type, synopsis, release_date, episodes) "
        command += "VALUES ("
        command += f"{id_},"
        command += f"'{title}',"
        command += f"'{type_}',"
        command += f"'{synopsis}',"
        command += f"'{release_date}',"
        command += f"'{episodes}');"
        return command

    @Table.query_update
    def update(self, id_, title, type_, synopsis, release_date, episodes):
        return "UPDATE animes "

    @Table.query_delete
    def delete(self, id_):
        commands = []
        command = "DELETE FROM staff "
        command += f"WHERE staff.id_anime = {id_};"
        commands.append(command)

        command = "DELETE FROM animeography "
        command += f"WHERE animeography.id_anime = {id_};"
        commands.append(command)

        command = "DELETE FROM animes "
        command += f"WHERE animes.id = {id_};"
        commands.append(command)
        return commands