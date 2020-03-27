class Query:
    """
    Class representing a single query to be executed on the database.
    """
    def __init__(self):
        self.__select = "*"
        self.__from = None
        self.__where = None
        self.__group_by = None
        self.__having = None
        self.__order_by = None
        self.__limit = None

    def select(self, value: str):
        self.__select = value

    def from_(self, value: str):
        self.__from = value

    def where(self, value: str):
        self.__where = value

    def group_by(self, value: str):
        self.__group_by = value

    def having(self, value: str):
        self.__having = value

    def order_by(self, value: str):
        self.__order_by = value

    def limit(self, value: int):
        self.__limit = value

    def validate(self):
        if not self.__select:
            raise QueryException("The SELECT clause must be present in order to execute the query.")

        if not self.__from:
            if self.__where:
                raise QueryException("The FROM clause must be present in order to have a WHERE clause.")
            if self.__group_by:
                raise QueryException("The FROM clause must be present in order to have a GROUP BY clause.")
            if self.__order_by:
                raise QueryException("The FROM clause must be present in order to have a ORDER BY clause.")

        if self.__having:
            if not self.__group_by:
                raise QueryException("The GROUP BY clause must be present in order to have a HAVING clause.")

    def __repr__(self):
        current_value = "select "+self.__select
        if self.__from:
            current_value += " from "+self.__from
        if self.__where:
            current_value += " where "+self.__where
        if self.__group_by:
            current_value += " group by "+self.__group_by
        if self.__having:
            current_value += " having "+self.__having
        if self.__order_by:
            current_value += " order by "+self.__order_by
        if self.__limit:
            current_value += " limit "+str(self.__limit)

        return current_value

    def __str__(self):
        return self.__repr__()


class QueryBuilder:
    def __init__(self):
        self.__current_query = Query()

    def select(self, value):
        self.__current_query.select(value)
        return self

    def from_(self, value):
        self.__current_query.from_(value)
        return self

    def where(self, value):
        self.__current_query.where(value)
        return self

    def group_by(self, value):
        self.__current_query.group_by(value)
        return self

    def having(self, value):
        self.__current_query.having(value)
        return self

    def order_by(self, value):
        self.__current_query.order_by(value)
        return self

    def limit(self, value):
        self.__current_query.limit(value)
        return self

    def execute(self):
        self.__current_query.validate()
        # TODO complete execution code
        pass

    def __repr__(self):
        return self.__current_query.__repr__()

    def __str__(self):
        return self.__current_query.__str__()


class QueryException(Exception):
    pass
