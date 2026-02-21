from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated , IsAdminUser


from ..serializers.books_serializers import BooksSerializer
from ..models import Books
from ..permissions.books_permissions import IsAdminOrReadOnly

class Booksview(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filterset_fields = ['auther']
    search_fields = ['title']
    
    permission_classes = [IsAdminOrReadOnly]











#from rest_framework import status

# @api_view(['GET','DELETE','PUT','POST'])
# def books_detail_api(request,id):

#     book = get_object_or_404(Books,id=id)
#     if request.method == 'GET':
#         #books = Books.objects.all()
#         serializer = BooksSerializer(book)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = BooksSerializer(book,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data
#             )
        
#         else :
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#                 )
        
#     if request.method == 'POST':
#         serializer = BooksSerializer(data=request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
    
#         else :
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#                  )
    
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    