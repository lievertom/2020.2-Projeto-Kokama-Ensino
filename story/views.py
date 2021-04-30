from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

SERVER_ERROR = 'Erro interno do servidor'

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('-id')
    serializer_class = StorySerializer

    def create(self, request, *args, **kwargs):
        has_portuguese = request.POST.get('title_portuguese') and request.POST.get('text_portuguese')
        has_kokama = request.POST.get('title_kokama') and request.POST.get('text_kokama')

        if has_portuguese or has_kokama:
            try:
                Story.objects.create(
                    title_portuguese=request.POST.get('title_portuguese'),
                    text_portuguese=request.POST.get('text_portuguese'),
                    title_kokama=request.POST.get('title_kokama'),
                    text_kokama=request.POST.get('text_kokama')
                )
            except Exception:
                return Response(HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(HTTP_200_OK) 
        else:
            return Response(HTTP_400_BAD_REQUEST) 

    def update(self, request, *args, **kwargs):
        has_portuguese = request.data.get('title_portuguese') and request.data.get('text_portuguese')
        has_kokama = request.data.get('title_kokama') and request.data.get('text_kokama')

        if has_portuguese or has_kokama:
            story = self.get_object()
            try:
                story.title_portuguese = request.data.get('title_portuguese')
                story.text_portuguese = request.data.get('text_portuguese')
                story.title_kokama = request.data.get('title_kokama')
                story.text_kokama = request.data.get('text_kokama')
                story.save()
            except Exception:
                return Response(HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(HTTP_200_OK) 
        else:
            return Response(HTTP_400_BAD_REQUEST) 
