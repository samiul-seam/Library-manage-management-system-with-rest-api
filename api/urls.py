from django.urls import path , include
from book.views import CategoryViewSet , AuthorViewSet, BookViewSet
from order.views import BorrowBookViewSet , BorrowViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('author', AuthorViewSet)
router.register('books', BookViewSet, basename='books')
router.register('borrows', BorrowViewSet, basename='borrows')


borrow_router = routers.NestedDefaultRouter(
    router, 'borrows', lookup='borrow')
borrow_router.register('books', BorrowBookViewSet, basename='borrow-books')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(borrow_router.urls))
]
