import pytest
from db_fixture import AL_PHA, BE_TA, GAM_MA, small_db
from permission import PermissionException, get_role, get_staff, require


def test_unknown_user_capabilities(small_db):
    assert get_staff(small_db, 1) is None
    with pytest.raises(PermissionException):
        require(small_db, 1, 'view')


def test_unknown_role_capabilities(small_db):
    with pytest.raises(PermissionException):
        require(small_db, AL_PHA, 'missing')


def test_error_message(small_db):
    with pytest.raises(PermissionException, match='^Permission exception:.*missing.*'):
        require(small_db, AL_PHA, 'missing')


@pytest.mark.parametrize('cap', ('add', 'delete', 'invalidate', 'view'))
def test_admin_capabilities_allowed(small_db, cap):
    assert get_role(small_db, AL_PHA) == 'admin'
    require(small_db, AL_PHA, cap)


@pytest.mark.parametrize('cap', ['add', 'invalidate', 'view'])
def test_user_capabilities_allowed(small_db, cap):
    assert get_role(small_db, BE_TA) == 'user'
    require(small_db, BE_TA, cap)


def test_user_capabilities_disallowed(small_db):
    assert get_role(small_db, BE_TA) == 'user'
    with pytest.raises(PermissionException):
        require(small_db, BE_TA, 'delete')


@pytest.mark.parametrize('cap, expected', [('add', False), ('delete', False), ('invalidate', False), ('view', True)])
def test_viewer_capabilities(small_db, cap, expected):
    assert get_role(small_db, GAM_MA) == 'viewer'
    if expected:
        require(small_db, GAM_MA, cap)
    else:
        with pytest.raises(PermissionException):
            require(small_db, GAM_MA, cap)
