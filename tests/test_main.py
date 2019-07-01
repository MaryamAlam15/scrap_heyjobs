import unittest
from unittest import mock

import pandas as pd

from constants import HEYJOBS_JOB_URL
from main import add_data_to_df, extract_and_load_job_info


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.web_link = HEYJOBS_JOB_URL
        self.uuids = ['uuid-1', 'uuid-2', 'uuid-3']
        self.titles = ['title 1', 'title 2', 'title 3']

    def test_add_data_to_df(self):

        df = add_data_to_df(self.uuids, self.titles)

        self.assertIsInstance(df, pd.DataFrame)

    def test_extract_and_load_job_info(self):
        with mock.patch('main.parse_page') as mocked_parse_page:
            with mock.patch('main.add_data_to_df') as mocked_add_data_to_df:
                with mock.patch('main.store_df_to_db') as mocked_store_df_to_db:

                    mocked_parse_page.return_value = self.uuids, self.titles
                    mocked_add_data_to_df.return_value = df = pd.DataFrame({'uuid': self.uuids, 'title': self.titles})

                    extract_and_load_job_info()

                    mocked_parse_page.assert_called_once_with(self.web_link)
                    mocked_add_data_to_df.assert_called_once_with(self.uuids, self.titles)
                    mocked_store_df_to_db.assert_called_once_with(df)
