import pandas as pd

from constants import HEYJOBS_JOB_URL
from db import store_df_to_db
from scrapper import parse_page


def extract_and_load_job_info():
    """
    this is the main controller of the app.
    this method parse the page and send the extracted data to data frames,
    and then store the data frames to db.
    """
    uuids, titles = parse_page(HEYJOBS_JOB_URL)

    job_ad_df = add_data_to_df(uuids, titles)
    print(job_ad_df)
    store_df_to_db(job_ad_df)


def add_data_to_df(uuids, titles):
    """
    create the panda dataframe and add uuids n titles of the job into it.
    :param uuids: list of uuids of the job.
    :param titles: list of title of the job.
    :return: a dataframe containing job uuid and title.
    """
    job_info_df = pd.DataFrame({
        'uuid': uuids,
        'title': titles
    })

    # start record id from 1 instead of 0.
    job_info_df.index = job_info_df.index + 1
    return job_info_df
