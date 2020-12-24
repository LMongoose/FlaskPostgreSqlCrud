import os, re
import urllib.parse as ulib
import psycopg2


DATA_TYPES = {
    "16": "BOOL",
	"17": "BYTEA",
	"18": "CHAR",
	"20": "INT8",
	"21": "INT2",
	"23": "INT4",
	"24": "REGPROC",
	"25": "TEXT",
	"628": "LINE",
	"700": "FLOAT4",
	"701": "FLOAT8",
	"702": "ABSTIME",
	"703": "RELTIME",
	"704": "TINTERVAL",
	"705": "UNKNOWN",
	"790": "CASH",
	"829": "MACADDR",
	"869": "INET",
	"650": "CIDR",
	"1007": "INT4ARRAY",
	"1042": "BPCHAR",
	"1043": "VARCHAR",
	"1082": "DATE",
	"1083": "TIME",
	"1114": "TIMESTAMP",
	"1184": "TIMESTAMPTZ",
	"1186": "INTERVAL",
	"1266": "TIMETZ",
	"1560": "BIT",
	"1562": "VARBIT",
	"1700": "NUMERIC",
	"2275": "CSTRING",
	"2276": "ANY",
	"2277": "ANYARRAY"
}


class Database():
    def __init__(self):
        _url = ulib.urlparse(os.environ.get("DB_URL"))
        self.connection = psycopg2.connect(database = _url.path[1:],
            user = _url.username, password = _url.password,
            host = _url.hostname, port = _url.port
        )

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def get_columns(self, cursor):
        _columns = []
        for colobj in cursor.description:
            _columns.append({
                "name": colobj.name,
                "display_name": " ".join([word.capitalize() for word in colobj.name.strip().split("_")]),
                "data_type": DATA_TYPES[str(colobj.type_code)]
            })
        return _columns

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        return self.connection.commit()

    def rollback(self):
        return self.connection.rollback()

    def close(self):
        return self.connection.close()


class Table():
    def __init__(self, db: Database):
        self.db = db
        self.cursor = self.db.cursor()
        ## TODO: get from constructor
        #self.table_name = None
        #self.columns = []
        ##assert(self.table_name is not None)
        ##assert(self.columns is not None)


    @staticmethod
    def query_list_all(function_):
        def wrapper(table: Table, *args, **kwargs):
            try:
                command = function_(table, *args, **kwargs)
                table.cursor.execute(command)

                columns = table.db.get_columns(table.cursor)
                result = table.cursor.fetchall()

            except:
                return False

            else:
                table.db.commit()
                return result, columns

        return wrapper

    @staticmethod
    def query_select(function_):
        def wrapper(table: Table, *args, **kwargs):
            try:
                command = function_(table, *args, **kwargs)
                table.cursor.execute(command)

                columns = table.db.get_columns(table.cursor)
                result = table.cursor.fetchall()
                if(len(result) < 2):
                    result = result[0]

            except:
                return False

            else:
                table.db.commit()
                return result, columns

        return wrapper

    @staticmethod
    def query_insert(function_):
        def wrapper(table: Table, *args, **kwargs):
            try:
                command = function_(table, *args, **kwargs)
                table.cursor.execute(command)

            except:
                return False

            else:
                table.db.commit()
                return True

        return wrapper

    @staticmethod
    def query_update(function_):
        def wrapper(table: Table, *args, **kwargs):
            try:
                arg_names = function_.__code__.co_varnames[:function_.__code__.co_argcount]
                if(args[2] is not None):
                    command = function_(table, *args, **kwargs)
                    command += f"SET"
                    for i in range(0, len(args)):
                        if(args[i] is not None):
                            if(isinstance(args[i], int) or isinstance(args[i], float)):
                                command += f" {re.sub('_$', '', arg_names[i+1])} = {args[i]}"
                            else:
                                command += f" {re.sub('_$', '', arg_names[i+1])} = '{args[i]}'"
                            if(args[i] != args[-1]):
                                command += ","

                    command += " WHERE "
                    ids_ = []
                    for i in range(0, len(args)):
                        if(arg_names[i].startswith("id_")):
                            ids_.append(i)

                    for i in ids_:
                        command += f"{re.sub('_$', '', arg_names[i])} = {args[i-1]}"
                        if(i != ids_[-1]):
                            command += " AND "

                    table.cursor.execute(command)

            except:
                return False

            else:
                table.db.commit()
                return True

        return wrapper

    @staticmethod
    def query_delete(function_):
        def wrapper(table: Table, *args, **kwargs):
            try:
                result = function_(table, *args, **kwargs)
                if(isinstance(result, list)):
                    for command in result:
                        table.cursor.execute(command)

                elif(isinstance(result, str)):
                    table.cursor.execute(result)

            except:
                return False

            else:
                table.db.commit()
                return True

        return wrapper