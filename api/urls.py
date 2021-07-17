from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.story_views import Stories, StoryDetails
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.chapter_views import Chapters, ChapterDetails

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('stories/', Stories.as_view(), name='stories'),
    path('stories/<int:pk>', StoryDetails.as_view(), name='story_details'),
    path('chapters/', Chapters.as_view(), name='chapters'),
    path('chapters/<int:pk>', ChapterDetails.as_view(), name='chapters'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
