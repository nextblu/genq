from unittest import TestCase
from genq import QueryBuilder, QueryException


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.query_builder = QueryBuilder()

    def test_select(self):
        query = self.query_builder.select("1")
        self.assertEqual("select 1", str(query))

    def test_from(self):
        query = self.query_builder.select("1").from_("dummy")
        self.assertEqual("select 1 from dummy", str(query))

    def test_where(self):
        query = self.query_builder.select("1").from_("dummy").where("n = 1")
        self.assertEqual("select 1 from dummy where n = 1", str(query))

    def test_group_by(self):
        query = self.query_builder.select("1").from_("dummy").group_by("n")
        self.assertEqual("select 1 from dummy group by n", str(query))

    def test_having(self):
        query = self.query_builder.select("1").from_("dummy").group_by("n").having("n > 0")
        self.assertEqual("select 1 from dummy group by n having n > 0", str(query))

    def test_bad_where(self):
        self.query_builder.from_(None)
        with self.assertRaises(QueryException) as e:
            self.query_builder.select("1").where("n = 1").execute()
