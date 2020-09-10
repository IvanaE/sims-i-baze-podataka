from util.sql_handler import SqlHandler

class GenericRepository(SqlHandler):
    def __init__(self, table, key, metapath):
        self.table = table
        self.key = key
        self.metapath = metapath
        super().__init__(table, key, metapath)