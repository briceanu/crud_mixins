"""
URL configuration for crud_mixins project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from crud.views import BookView,BookViewUpdate,BookViewMixin, RemoveBook, RemoveBookWithQueryParams
from crud.views import BookDelete,BookViewList,SignUp,SignIn
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book',BookView.as_view(),name='book'),
    path('bookupdate',BookViewUpdate.as_view(),name='bookupdate'),
    path('books/<uuid:pk>', BookView.as_view(), name='book-detail'),
    path('books/', BookView.as_view(), name='book-detail'),
    # path('book/update/<uuid:book_id>',BookViewMixin.as_view(),name='book-update'),
    path('book/update/',BookViewMixin.as_view(),name='book-update'),
    path('removebook/<uuid:book_id>',RemoveBook.as_view(),name='remove-book'),
    path('removebook',RemoveBookWithQueryParams.as_view(),name='remove-book'),
    # path('deletebook/<uuid:book_id>',BookDelete.as_view(),name='delelte-book'),
    path('deletebook',BookDelete.as_view(),name='delelte-book'),
    path('listbooks',BookViewList.as_view(),name='list-books'),
    path('signup',SignUp.as_view(),name='signup'),
    path('signin',SignIn.as_view(),name='sigin')



]


