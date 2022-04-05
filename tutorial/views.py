from itertools import count

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import filters
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .serializer import CRUDTutorialSerializer, TutorialListSerializer, VideoSerializer, TutorialUpdateSerializer
from .models import Tutorial


class CRUDTutorialAPiView(APIView):
    """ admin can create video tutorials"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'content_type__content')

    def get_queryset(self, uuid):
        if uuid is None:
            qs = Tutorial.objects.all()
        if uuid:
            qs = Tutorial.objects.filter(uuid=uuid)
        content = self.request.query_params.get('content')
        if content is not None:
            qs = qs.filter(content_type_id=content)

        video_id = self.request.query_params.get('video')
        if video_id is not None:
            qs = qs.filter(videos=video_id)

        video_title = self.request.query_params.get('video_title')
        if video_title is not None:
            qs = qs.filter(videos__title=video_title)

        video_title = self.request.query_params.get('title')
        if video_title is not None:
            qs = qs.filter(videos__title__icontains=video_title)

        tutorial_title = self.request.query_params.get('search')
        if tutorial_title is not None:
            qs = qs.filter(title__icontains=tutorial_title)
        return qs

    def post(self, request):
        serializer = CRUDTutorialSerializer(data=self.request.data)
        if serializer.is_valid():
            tutorial = serializer.save()
            return Response({
                "Message": "Success", "status": "CREATED",
                'data': TutorialListSerializer(tutorial).data,
            },)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, uuid=None):
        qs = self.get_queryset(uuid)
        serializer = TutorialListSerializer(qs, many=True)
        return Response({"count": len(qs), "Message": "Success", "data": serializer.data})

    def put(self, request, uuid=None):
        if uuid:
            qs = Tutorial.objects.get(uuid=uuid)
            serializer = TutorialUpdateSerializer(qs, data=self.request.data)
            if serializer.is_valid():
                tutorial = serializer.save()
                return Response({
                    "Message": "Success", "status": "UPDATED",
                    'data': TutorialListSerializer(tutorial).data,
                }, )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




