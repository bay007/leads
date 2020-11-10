from rest_framework.exceptions import APIException


class RoleNotInitialized(APIException):
    status_code = 500
    default_detail = 'Rol for queue messages can´t be initialized.'
    default_code = 'rol_uninitialized'
