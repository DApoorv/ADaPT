from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery
from flask import current_app, g


class DBFactory:
    _dbase = SQLAlchemy(model_class=Model, query_class=BaseQuery)

    def get_dbase(self):
        """:returns uninitialised sqlalchemy instance.
        Returned Instance to be used for creating models only."""
        return self._dbase

    @staticmethod
    def get_db():
        """:returns an initialised sqlalchemy instance
        Works only inside app_context. Use instance for views
        interaction with the database"""
        if 'db' not in g:
            g.db = SQLAlchemy(current_app)
        return g.db

    @staticmethod
    def close_db(e=None):
        """:returns Nothing
        Use method to destroy initialised sqlalchemy instance"""
        db = g.pop('db', None)
        if db is not None:
            del db


dbf_obj = DBFactory()
print(dbf_obj.get_dbase())

