from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from language.models import Language, Framework

# Les sérialiseurs définissent la représentation de l'API.
# Creation de  classe serializer pour faire la conversion entre model et json
# ici la classe ModelSerializer permet de mapper un model en json
class LangSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Language # ca prend le model a mapper
        fields = '__all__' # tous les donnes du models comvernees
        
class FrameSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Framework
        fields = '__all__'

# Par la suite il faut creer les vues qui vont recevoir les differents call API et 
# qui vont les traiter en utilisants les serializer creer en haut