from django.urls import path

from books_api.views import ListBooksView, DetailBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all"),
    path('books/<int:pk>/', DetailBookView.as_view(), name="books-all"),
]
