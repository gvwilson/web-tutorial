GET_ROLE = '''
select role_name
from role
where staff_id = ?
'''

GET_STAFF = '''
select personal, family
from staff
where staff_id = ?
'''

PERMISSION = '''
select count(*) as number
from permission join role
on permission.role_name = role.role_name
where (role.staff_id = ?) and (permission.capability = ?)
'''


class PermissionException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'Permission exception: {self.msg}'


def get_role(connection, staff_id):
    '''Get staff member's role.'''
    rows = connection.execute(GET_ROLE, (staff_id,)).fetchall()
    assert (len(rows) == 1) and (len(rows[0]) == 1)
    return rows[0]['role_name']


def get_staff(connection, staff_id):
    '''Get staff name by ID.'''
    rows = connection.execute(GET_STAFF, (staff_id,)).fetchall()
    if not rows:
        return None
    assert (len(rows) == 1) and (len(rows[0]) == 2)
    return rows[0]


def require(connection, user, capability):
    '''Check that user has required permission.'''
    rows = connection.execute(PERMISSION, (user, capability)).fetchall()
    assert (len(rows) == 1) and (len(rows[0]) == 1)
    if rows[0]['number'] != 1:
        raise PermissionException(f'user {user} does not have capability {capability}')
