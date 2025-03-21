from app.db.models import init, Database


def init_db_wrapper():
    init()


_db_instance = Database()


def get_db():
    return _db_instance
