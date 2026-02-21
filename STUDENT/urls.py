from .views.books_views import Booksview
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books',Booksview)
urlpatterns  = router.urls