from test_src.models.test_user import TestUser
from test_src.models.test_daily_eat import TestDailyEat

test_user = TestUser()
test_user.test_session_query_user_assert_equal_true()
test_daily_eat = TestDailyEat()
test_daily_eat.test_session_query_daily_eat_assert_equal_true()
