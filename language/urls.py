from rest_framework import routers
from language.views import LangViewSet, FrameViewSet

router = routers.DefaultRouter()
router.register('languages', LangViewSet) #Enregistre la route
router.register('frameworks', FrameViewSet)

#Par la suite importer nos urls dans le url root se trouvant dans le meme dossier que settings.py