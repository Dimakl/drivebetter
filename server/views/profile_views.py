from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from server.models import ProfileData
from server.serializers import ProfileDataSerializer
from django import forms


class ProfileDataForm(forms.Form):
    uuid = forms.CharField(max_length=100)
    name = forms.CharField(max_length=256)
    gender = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')))
    city = forms.CharField(max_length=256)
    birth_date = forms.CharField(max_length=100)
    licence = forms.CharField(max_length=100)
    licence_received = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=256)


class ProfileDataView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        form = ProfileDataForm(request.data)
        if form.is_valid():
            serializer = ProfileDataSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                # Create a new user directly from the request data
                user = ProfileData.objects.create_user(
                    **serializer.validated_data
                )
                return Response({}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        user = request.user  # Retrieve the current authenticated user
        if user.is_anonymous:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Get the fields to update from the request data
        data = {
            'gender': request.data.get('gender'),
            'city': request.data.get('city'),
            'birth_date': request.data.get('birth_date'),
            'licence': request.data.get('licence'),
            'licence_received': request.data.get('licence_received'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
        }

        # Exclude None values from the data dictionary
        data = {k: v for k, v in data.items() if v is not None}

        serializer = ProfileDataSerializer(user, data=data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
