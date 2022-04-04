from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import CRUDUserProfileSerializer, UserLoginSerializer
from .models import UserProfile, User


class UserLogin(APIView):
    def post(self, request):
        # import ipdb;
        # ipdb.set_trace()
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data
            try:
                user = UserProfile.objects.get(email=email['email'])
                Token.objects.all().delete()
                token = Token.objects.create(user=user.user)
                if user:
                    return Response({"Message": "Successfully Logged in", "status": status.HTTP_200_OK,
                                     "token": token.key, "data": serializer.data})
                else:
                    return Response({"Message": "This User email does not exist", 'status': 'ERROR',
                                     'code': 910, })
            except:
                return Response({"Message": "This User email does not exist", 'status': 'ERROR',
                                 'code': 910, })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
