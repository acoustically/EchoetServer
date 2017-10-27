import src.orm as orm
import unittest
from src.models.user import User

class TestUser(unittest.TestCase):
    def test_session_query_user_assert_equal_true(self):
        session = orm.session
        rows = session.query(User).filter_by(id="test").all()
        result = orm.as_list_dict(rows)
        self.assertEqual(result[0]["id"], "test")
        self.assertEqual(result[0]["password"], "test")
