from .models import Book
from .bookserializer import BookSerializer
from rest_framework.generics import GenericAPIView ,ListCreateAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound ,AuthenticationFailed
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .user_serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import authenticate





class BookView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # using the  get_object function to get the book
    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            return Response({"error":'no book id found'},status=status.HTTP_400_BAD_REQUEST)
        try:
            return Book.objects.filter(book_id__gte=book_id)
        except Book.DoesNotExist:
            return Response({"error": 'book not found'}, status=status.HTTP_404_NOT_FOUND)




    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)







class BookViewUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        
        if not book_id:
            raise NotFound(detail="book_id query parameter is required")

        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail=f"No book with id {book_id} found")


    def patch(self, request, *args, **kwargs):
        book_id = request.query_params.get('book_id')
        book_name = request.data.get('book_name')
        
        if not book_id or not book_name:
            return Response({"error": "book_id or book_name not provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Call the get_object method to retrieve the book
        book = self.get_object()

        try:
            book.name = book_name
            book.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Use the update method from UpdateModelMixin
        return self.update(request,partial=True, *args, **kwargs)





class BookViewMixin(GenericAPIView,UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = 'book_id'

    """
    the get_object function is used for passing the 
     book_id as a query paramater
     this updateModelMixin comes with a security issue because
     a threat actor can update other fields apart from the one that 
     was intended to be modified
    """
     
    
    def get_object(self):
        
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            raise serializers.ValidationError('book_id not provided')
        return Book.objects.get(book_id=book_id)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class RemoveBook(DestroyModelMixin,GenericAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializer
    lookup_field = 'book_id'
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    


 
class RemoveBookWithQueryParams(DestroyModelMixin,GenericAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializer
    

    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            raise NotFound(detail="book_id query parameter is required")
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise NotFound(f'book with id {book_id} not found')




    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)   


# class BookDelete(GenericAPIView,DestroyModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'book_id'


#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)


# removing a instance using query paramaters

class BookDelete(GenericAPIView,DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = 'book_id'
    def get_object(self):
        book_id = self.request.query_params.get('book_id')
        if not book_id:
            raise NotFound(detail="book_id not provided") 
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            raise NotFound(f'book with id {book_id} not found')

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class BookViewList(GenericAPIView,ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes= [IsAuthenticated]


    # using the  get_object function to get the book

    # get_object
    # get_queryset

    """
    
        get_object return a single instance of a class one object
        get_queryset returns more than one instance of a class 
        more than one object

    """

    def get_queryset(self):
        year_of_publish = self.request.query_params.get('year_of_publish')
        if not year_of_publish:
            raise NotFound(detail="book_id not provided") 

        return Book.objects.filter(year_of_publish__gte=year_of_publish)


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    



class SignUp(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class SignIn(GenericAPIView,CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self,request,*args,**kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        if not username or not password:
            raise NotFound(detail='username or password not provided')

        authenticate_user = authenticate(username=username,password=password)
        if not authenticate_user:
            raise AuthenticationFailed(detail='Incorrect authentication credentials.')

        refresh_token = RefreshToken.for_user(authenticate_user)
        access_token = refresh_token.access_token

        return Response({
                "access":str(access_token),
                "refresh":str(refresh_token)},status=status.HTTP_200_OK)
    
         