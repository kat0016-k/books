# books
 Assignment

This schema defines three models: Book, User, and Order. Book contains information about each book, including the title, author, description, and price. User contains information about each user, including their name and email. Order contains information about each order, including the user who placed the order, the books in the order, the date the order was placed, and the total cost of the order.

This API defines several endpoints for interacting with the database schema. BookList returns a list of all books, while BookDetail returns the details of a particular book by its ID. AddToCart adds a book to the shopping cart for the currently authenticated user, while RemoveFromCart removes a book from the shopping cart. PlaceOrder places an order for the currently authenticated user

In serializer.py, we define serializers for the Book, User, and Order models. Each serializer specifies which fields to include in the response.

In urls.py, we define the endpoints for each API view. We also include endpoints for obtaining and refreshing JSON Web Tokens (JWTs) using Django REST framework's built-in views TokenObtainPairView and TokenRefreshView. These JWTs are used for authentication and authorization in our API.