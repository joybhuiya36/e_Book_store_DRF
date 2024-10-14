from django.urls import path
from .views import RegisterView, LoginView, CreateBookView, BookListView

urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('books/create/', CreateBookView.as_view(), name='create_book'),
    path('books/', BookListView.as_view(), name='list_books'),
]
