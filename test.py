import re
from database import Database
#from pypika import Query, Order


class FieldValidationException(Exception):
    pass


class Table():
    def __init__(self, db: Database):
        assert(hasattr(self, "table_name")), "Table name must be set."
        assert(hasattr(self, "is_pk_serial")), "Table is_pk_serial must be set."
        assert(isinstance(self.is_pk_serial, bool)), "Table is_pk_serial must be boolean."
        assert(hasattr(self, "columns")), "Table columns must be set."
        assert(isinstance(self.table_name, str)
            and len(self.table_name) > 0), "Table name must be a non-empty string."
        assert(isinstance(self.columns, list) 
            and len(self.columns) > 0
            and all([isinstance(item, str) for item in self.columns])
            and all([len(item) > 0 for item in self.columns])), "Table columns must be a non-empty list of strings."
        self.db = db
        self.cursor = self.db.cursor()

    ## TODO:
    #   Syntax: <SELECT|INSERT|UPDATE|DELETE> <fields..> <FROM> <table> [<JOIN>] [WHERE <condition>]
    #   
    #   handle joins on select
    #   handle conditions on select, update, delete
    #   handle rows of table referencied on other tables

    @staticmethod
    def display_fields(fields):
        _display_fields = []
        for field in fields:
            _display_fields.append(" ".join([word.capitalize() for word in field.strip().split("_")]),)
        return _display_fields

    @staticmethod
    def query_select(validator_function_):
        def wrapper(table: Table, fields=None, condition=None):
            if(validator_function_(fields, condition)):
                try:
                    command = "SELECT "

                    if(fields is None):
                        command += "*"
                    else:
                        for i in range(0, len(fields)):
                            command += f"{fields[i]}"
                            if(fields[i] != fields[-1]):
                                command += ", "

                    command += f" FROM {table.table_name}"
                    if(condition is None):
                        command += ";"
                    else:
                        command += f""" WHERE {condition.replace("and", "AND").replace("or", "OR")};"""

                    print(command)
                    #table.cursor.execute(command)
                    result = table.cursor.fetchall()
                    if(len(result) < 2):
                        result = result[0]

                except:
                    return False

                else:
                    table.db.commit()
                    return result, fields
    
            else:
                raise FieldValidationException("The field validation function returned False.")

        return wrapper

    @staticmethod
    def query_insert(validator_function_):
        def wrapper(table: Table, *fields):
            if(validator_function_(table, *fields)):
                try:
                    command = f"INSERT INTO {table.table_name} ("
                    if(table.is_pk_serial):
                        start = 1
                    else:
                        start = 0
                        assert(len(table.columns) == len(fields)), "The number of columns and values does not match."

                    for i in range(start, len(table.columns)):
                        command += f"{table.columns[i]}"
                        if(table.columns[i] != table.columns[-1]):
                            command += ", "

                    command += ") VALUES ("
                    for i in range(0, len(fields)):
                        if(isinstance(fields[i], int) or isinstance(fields[i], float)):
                            command += f"{fields[i]}"
                        else:
                            command += f"\'{fields[i]}\'"
                        if(fields[i] != fields[-1]):
                            command += ", "

                    command += ");"
                    print(command)
                    #table.cursor.execute(command)

                except:
                    return False

                else:
                    table.db.commit()
                    return True

            else:
                raise FieldValidationException("The field validation function returned False.")

        return wrapper

    @staticmethod
    def query_update(validator_function_):
        def wrapper(table: Table, *fields, condition=None):
            if(validator_function_(table, *fields, condition)):
                try:
                    assert(condition is not None), "Can not update without a condition."
                    arg_names = validator_function_.__code__.co_varnames[:validator_function_.__code__.co_argcount]
                    if(fields[0] is not None):
                        command = f"UPDATE {table.table_name} SET"
                        for i in range(0, len(fields)):
                            if(fields[i] is not None):
                                if(isinstance(fields[i], int) or isinstance(fields[i], float)):
                                    command += f""" {re.sub("_$", "", arg_names[i+1])} = {fields[i]}"""
                                else:
                                    command += f""" {re.sub("_$", "", arg_names[i+1])} = \"{fields[i]}\""""
                                if(fields[i] != fields[-1]):
                                    command += ","

                        command += f" WHERE {condition};"
                        #command += " WHERE "
                        #ids_ = []
                        #for i in range(0, len(fields)):
                        #    if(arg_names[i].startswith("id_")):
                        #        ids_.append(i)

                        #for i in ids_:
                        #    command += f"{re.sub("_$", "", arg_names[i])} = {fields[i-1]}"
                        #    if(i != ids_[-1]):
                        #        command += " AND "

                        print(command)
                        #table.cursor.execute(command)

                except:
                    return False

                else:
                    table.db.commit()
                    return True

            else:
                raise FieldValidationException("The field validation function returned False.")

        return wrapper

    @staticmethod
    def query_delete(validator_function_):
        def wrapper(table: Table, condition):
            if(validator_function_(table, condition)):
                try:
                    command = f"DELETE FROM {table.table_name} WHERE {condition};"

                    print(command)
                    #table.cursor.execute(command)

                except:
                    return False

                else:
                    table.db.commit()
                    return True

            else:
                raise FieldValidationException("The field validation function returned False.")

        return wrapper


class TableTest(Table):
    def __init__(self, db):
        self.table_name = "test"
        self.is_pk_serial = False
        self.columns = ["id", "title", "release_date", "episodes"]
        super().__init__(db)

    # Set your custom validations to the fields and conditions. (return True if is ok and false if is not)

    @Table.query_select
    def select(self, fields=None, join=None, conditions=None):
        return True

    @Table.query_insert
    def insert(self, id_, title, date, episodes):
        return True

    @Table.query_update
    def update(self, title, release_date, episodes, condition):
        return True

    @Table.query_delete
    def delete(self, condition):
        return True


class TableTest2(Table):
    def __init__(self, db):
        self.table_name = "test2"
        self.is_pk_serial = True
        self.columns = ["id", "name", "birthday"]
        super().__init__(db)

    # Set your custom validations to the fields and conditions. (return True if is ok and false if is not)

    @Table.query_select
    def select(self, fields=None, join=None, conditions=None):
        return True

    @Table.query_insert
    def insert(self, id_, name, birthday):
        return True

    @Table.query_update
    def update(self, name, birthday, condition):
        return True

    @Table.query_delete
    def delete(self, condition):
        return True


if(__name__ == "__main__"):
    animes = TableTest(Database())
    characters = TableTest2(Database())


    print("Display Columns: " + str(animes.display_fields(animes.columns)))
    print()

    # Select testing
    animes.select()
    animes.select(fields=["title", "eps"])
    animes.select(["id", "title", "release_date", "eps"], "id = 0")
    animes.select(condition="id = 0")
    print()

    # Insert testing
    animes.insert(1, "Re Zero", 2016, 10) # without serial pk
    characters.insert("Subaru", 2016-10-10) # with serial pk
    print()

    # Update testing
    animes.update("Overlord II", "2020-10-12", 12, condition="id = 0")
    print()

    # Delete testing
    animes.delete("id = 0 AND title = \"overlord\"")