import configparser

from sqlalchemy import create_engine


config = configparser.ConfigParser()
config.read('db.env')


def store_df_to_db(df):
    """
    connects to postgres db,
    creates `job_ad` table,
    loads dataframe data to `job_ad`.
    :param df:
    """
    engine = create_engine(config['CONN_STRING'])
    df.to_sql(config['TABLE'], engine, if_exists='replace', index_label='id')
