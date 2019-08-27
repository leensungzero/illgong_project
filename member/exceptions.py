from rest_framework.exceptions import APIException


class EmailValidationException(APIException):
    status_code = 400
    default_detail = {
        'success': False,
        'data': {
            'message': '이메일 형식에 맞지 않습니다.'
        }
    }
    default_code = 'email_validate_error'
