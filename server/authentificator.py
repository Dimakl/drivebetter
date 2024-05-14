from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            print(user.password)
            if user.password == password:
            # if user.check_password(password): TODO: bugged or what?
                return user
        except User.DoesNotExist:
            return None