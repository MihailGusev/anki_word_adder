"""anki_word_adder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import MainPageView, GuidePageView, VersionsPageView, GetWordDataView, FeedbackView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('anki_word_adder.apps.accounts.urls')),

    path('', MainPageView.as_view(), name='main'),

    path('guide/', GuidePageView.as_view(), name='guide'),

    path('versions/', VersionsPageView.as_view(), name='versions'),

    path('word-data/<str:word>', GetWordDataView.as_view(), name='word_data'),

    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
