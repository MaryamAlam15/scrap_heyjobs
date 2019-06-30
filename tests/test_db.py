import unittest
from unittest import mock

import pandas as pd

from db import store_df_to_db


class TestDB(unittest.TestCase):
    def setUp(self) -> None:
        self.uuids = ['uuid-1', 'uuid-2', 'uuid-3']
        self.titles = ['title 1', 'title 2', 'title 3']

    def test_store_df_to_db(self):
        with mock.patch('db.create_engine') as mocked_create_engine:
            mocked_create_engine.return_value = mock.Mock()

            df = pd.DataFrame({'uuid': self.uuids, 'title': self.titles})
            mocked_to_sql = df.to_sql = mock.Mock()
            store_df_to_db(df)

            mocked_create_engine.assert_called_once()
            mocked_to_sql.assert_called_once()
