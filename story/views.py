from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def destroy(self, request, *args, **kwargs):
        try:
            story = self.get_object()
            story.delete()
        except:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def add_story(request, id):
    story = Story.objects.none()
    # Edit
    if id:
        story = Story.objects.get(id=id) # Conferir se existe (try)
        if story.title != request.POST.get('title') or Story.objects.filter(title=request.POST.get('title')).first():
            return Response(
                {'error': 'Narrativa já cadastrada.'},
                status=HTTP_400_BAD_REQUEST,
            )

        story.delete()

    story, created = Story.objects.get_or_create(
        title=request.POST.get('title'),
    )
    if not created:
        return Response(
            {'error': 'Narrativa já cadastrada.'},
            status=HTTP_400_BAD_REQUEST,
        )
    story.save()

    return Response(status=HTTP_200_OK)
