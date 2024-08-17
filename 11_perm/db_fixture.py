import pytest
import sqlite3


def dict_factory(connection, row):
    fields = [column[0] for column in connection.description]
    return {key: value for key, value in zip(fields, row)}


CREATE = '''
CREATE TABLE staff (
	staff_id BIGINT, 
	personal TEXT, 
	family TEXT
);
CREATE TABLE experiment (
	sample_id BIGINT, 
	kind TEXT, 
	start TEXT, 
	"end" TEXT
);
CREATE TABLE performed (
	staff_id BIGINT, 
	sample_id BIGINT
);
CREATE TABLE permission (
        role_name TEXT,
        capability TEXT
);
CREATE TABLE role (
        staff_id BIGINT,
        role_name TEXT
);
'''

AL_PHA = 3
BE_TA = 5
GAM_MA = 7

STAFF = (
    (AL_PHA, 'Al', 'Pha'),
    (BE_TA, 'Be', 'Ta'),
    (GAM_MA, 'Gam', 'Ma'),
)
EXPERIMENTS = (
    (10, 'ELISA', '2024-05-23', '2024-05-27'),
    (20, 'ELISA', '2024-06-12', '2024-06-14'),
    (30, 'ELISA', '2024-06-12', None),
    (40, 'JESS', '2024-06-13', '2024-06-13'),
)
PERFORMED = (
    (AL_PHA, 20),
    (BE_TA, 30),
    (AL_PHA, 40),
    (BE_TA, 40),
    (GAM_MA, 10),
)
PERMISSION = (
    ('admin', 'add'),
    ('admin', 'delete'),
    ('admin', 'invalidate'),
    ('admin', 'view'),
    ('user', 'add'),
    ('user', 'invalidate'),
    ('user', 'view'),
    ('viewer', 'view'),
)
ROLE = (
    (AL_PHA, 'admin'),
    (BE_TA, 'user'),
    (GAM_MA, 'viewer'),
)


@pytest.fixture
def small_db():
    connection = sqlite3.connect(':memory:')
    connection.row_factory = dict_factory
    connection.executescript(CREATE)
    connection.executemany('insert into staff values(?, ?, ?)', STAFF)
    connection.executemany('insert into experiment values(?, ?, ?, ?)', EXPERIMENTS)
    connection.executemany('insert into performed values(?, ?)', PERFORMED)
    connection.executemany('insert into permission values(?, ?)', PERMISSION)
    connection.executemany('insert into role values(?, ?)', ROLE)
    return connection
