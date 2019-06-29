import configparser

from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('db.env')

DB = config['DATABASE']
PG_DOCKER = config['PG_DOCKER_IMG']


def store_df_to_db(df):
    """
    connects to postgres db,
    creates `job_ad` table,
    loads dataframe data to `job_ad`.
    :param df:
    """
    conn_str = f'postgresql://{DB["USER"]}:{DB["PWD"]}@{PG_DOCKER["HOST"]}:{PG_DOCKER["PORT"]}/{DB["NAME"]}'
    engine = create_engine(conn_str)
    # create table, replace if already exists. index field should be named `id`.
    df.to_sql(DB['TABLE'], engine, if_exists='replace', index_label='id')
