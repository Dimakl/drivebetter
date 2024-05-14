from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django import forms
from rest_framework import status

from server.models import ProfileData

from server.authentificator import EmailAuthBackend


class LoginView(APIView):
    permission_classes = [AllowAny]

    class LoginForm(forms.Form):
        email = forms.EmailField()
        password = forms.CharField(max_length=256)

    def post(self, request):
        form = self.LoginForm(request.data)
        if not form.is_valid():
            errors = dict(form.errors.items())
            return Response({'error': 'Validation error', 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            # User exists with the provided credentials
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)