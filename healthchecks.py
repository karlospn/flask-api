from healthcheck import HealthCheck
from .database.models import db


def health_functions():
    return health_database_status()


def health_database_status():
    is_database_working = True
    output = 'database is ok'

    try:
        session = db.session
        session.execute('SELECT 1')
        is_database_working
    except Exception as e:
        output = str(e)
        is_database_working = False

    return is_database_working, output


def health_redis_status():
    return True


health = HealthCheck()
health.add_check(health_functions)
