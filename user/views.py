from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import CRUDUserProfileSerializer, UserLoginSerializer
from .models import UserProfile, User


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class CRUDUserProfileAPIView(APIView):
    """ create new user profile"""

    def post(self, request):
        serializer = CRUDUserProfileSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "data": serializer.data, })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        qs = UserProfile.objects.all()
        serializer = CRUDUserProfileSerializer(qs, many=True)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data, })
