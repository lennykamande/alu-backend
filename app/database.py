"""
This module sets up the database that will be used
"""
from contextlib import closing
from flask import current_app
import psycopg2
import os
from app import create_app


def init_db():
    """Set up the database to stode the user data
    """
    db_url = current_app.config['DATABASE_URL']
    # import pdb;pdb.set_trace()
    conn = psycopg2.connect(db_url)
    with conn as conn, conn.cursor() as cursor:
        with current_app.open_resource('users.sql', mode='r') as sql:
            cursor.execute(sql.read())
        conn.commit()
        return conn


def connect_to(url):
    conn = psycopg2.connect(url)
    return conn


def _init_db():
    conn = connect_to(os.getenv('DATABASE_TEST_URL'))
    destroy()
    with conn as conn, conn.cursor() as cursor:
        with current_app.open_resource('users.sql', mode='r') as sql:
            cursor.execute(sql.read())
        conn.commit()
        return conn


def destroy():
    test_url = os.getenv('DATABASE_TEST_URL')
    conn = connect_to(test_url)
    curr = conn.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    queries = [users]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        print("Fail")
