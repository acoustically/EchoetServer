import src.orm as orm
import unittest
from src.models.daily_eat import DailyEat

class TestDailyEat(unittest.TestCase):
    def test_session_query_daily_eat_assert_equal_true(self):
        session = orm.session
        rows = session.query(DailyEat).filter_by(user_id="test", food="test", year = 1, month = 1, date = 1).all()
        result = orm.as_list_dict(rows)
        self.assertEqual(result[0]["user_id"], "test")
        self.assertEqual(result[0]["food"], "test")
        self.assertEqual(result[0]["year"], 1)
        self.assertEqual(result[0]["month"], 1)
        self.assertEqual(result[0]["date"], 1)
