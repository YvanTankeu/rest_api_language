from django.shortcuts import render

from rest_framework import viewsets
from language.models import Framework, Language
from language.serializer import LangSerializer, FrameSerializer

def lang(request):
    return render(request, 'language/lang.html')

def frame(request):
    return render(request, 'language/frame.html')

def lang_frame(request):
    return render(request, 'language/lang_frame.html')

# Creation de la classe LangViewSet qui heritera de la classe ModelViewSet
class LangViewSet(viewsets.ModelViewSet):
    #   Point de terminaison de l'API qui permet de visualiser
    queryset = Language.objects.all() # on indique les donnees 
    serializer_class = LangSerializer

class FrameViewSet(viewsets.ModelViewSet):
    #   Point de terminaison de l'API qui permet de visualiser
    queryset = Framework.objects.all() # on indique les donnees 
    serializer_class = FrameSerializer
    
# Il faut definir les urls qui permettront d'acceder aux endpoints de nos API