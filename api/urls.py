from django.urls import path , include
from book.views import CategoryViewSet , AuthorViewSet, BookViewSet, BookImageViewSet, ReviewViewSet
from order.views import BorrowBookViewSet , BorrowViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('categories', CategoryViewSet, basename='categories')
router.register('author', AuthorViewSet)
router.register('borrows', BorrowViewSet, basename='borrows')


book_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_router.register('images', BookImageViewSet, basename='book-image')
book_router.register('reviews', ReviewViewSet, basename='book-review')


borrow_router = routers.NestedDefaultRouter(
    router, 'borrows', lookup='borrow')
borrow_router.register('books', BorrowBookViewSet, basename='borrow-books')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(borrow_router.urls)),
    path('', include(book_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
