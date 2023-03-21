from rest_framework import generics
from .models import Book, User, Order
from .serializers import BookSerializer, UserSerializer, OrderSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class AddToCart(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put(self, request, pk):
        order = Order.objects.filter(user=request.user).first()
        if order is None:
            order = Order.objects.create(user=request.user)
        book = Book.objects.get(pk=pk)
        order.books.add(book)
        order.total += book.price
        order.save()
        return Response(OrderSerializer(order).data)

class RemoveFromCart(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put(self, request, pk):
        order = Order.objects.filter(user=request.user).first()
        if order is None:
            return Response({'error': 'No order found for this user.'})
        book = Book.objects.get(pk=pk)
        order.books.remove(book)
        order.total -= book.price
        order.save()
        return Response(OrderSerializer(order).data)

class PlaceOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request):
        order = Order.objects.filter(user=request.user).first()
        if order is None or not order.books.exists():
            return Response({'error': 'No items in cart.'})
        order.save()
        return Response(OrderSerializer(order).data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
