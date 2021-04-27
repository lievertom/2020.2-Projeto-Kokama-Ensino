from .models import Story
from .serializers import StorySerializer
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from decouple import config
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)


UNAUTHORIZED_ERROR = 'Você não tem autorização'

@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def authenticate(request):
    user_ip = request.META['REMOTE_ADDR']
    if user_ip in config('ALLOWED_IP_LIST'):
        return Response(HTTP_200_OK)
    else:
        return Response(status=HTTP_401_UNAUTHORIZED)


class StoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Story.objects.all().order_by('-id')
    serializer_class = StorySerializer

    def create(self, request, *args, **kwargs):
        if authenticate(request).status_code != HTTP_200_OK:
            return HttpResponse(
                UNAUTHORIZED_ERROR,
                status=HTTP_403_FORBIDDEN,
            )
        try:
            Story.objects.create(
                title=request.data['title'],
                text=request.data['text']
            )   
        except Exception:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        if authenticate(request).status_code != HTTP_200_OK:
            return HttpResponse(
                UNAUTHORIZED_ERROR,
                status=HTTP_403_FORBIDDEN,
            )
        try:
            story = self.get_object()
            story.title = request.data['title']
            story.text = request.data['text']
            story.save()
        except Exception:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        if authenticate(request).status_code != HTTP_200_OK:
            return HttpResponse(
                UNAUTHORIZED_ERROR,
                status=HTTP_403_FORBIDDEN,
            )
        try:
            story = self.get_object()
            story.delete()
        except Exception:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=HTTP_204_NO_CONTENT)
