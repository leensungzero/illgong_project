from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from member.models.user_profile import UserProfile
from member.serializers import (
    UserProfileSerializer,
)
from member.exceptions import (
    EmailValidationException,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view(['GET'])
def email_validate(request):
    email = request.GET.get('email')

    try:
        validate_email(email)
    except ValidationError:
        raise EmailValidationException
    else:
        return Response({
            'success': True,
            'data': {
                'message': '사용 가능한 이메일',
            }
        })
