# ThanoSQL Error Handling
class ThanoSQLConnectionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ThanoSQLInternalError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
