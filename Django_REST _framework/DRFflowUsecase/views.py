# Django REST Framework API view that returns all Walk records as JSON
# Create class-based API view. APIView is DRF's base class for handling HTTP requests.
class WalkListView(APIView):
            def get(self, request):  # Hhndle HTTP GET requests (example: GET /api/walks/)
                        #ask database 2 retrieve Walk objects:
                        walks = Walk.objects.all() 
                        # Equivalent SQL: SELECT * FROM walk;
# *Then Convert Django model objects into Python data that can be rendered as JSON:
                        serializer = WalkSerializer(walks, many=True) # many=True: walks is a queryset containing multiple records
                        # *Example data:
                        # [
                        # Walk(id=1, title="Morning Walk"),
                        #Walk(id=2, title="Evening Walk")
                        # ]
                        return Response(serializer.data)
                 
                            
                    
# bad example - do not emplement - 200 lines of business logic, do nor doit (-:
class ListingView(APIView):
    def post(self, request):
            
# good example - emplement this way:
class ListingView(APIView):
    def post(self, request):
        listing = create_listing(request.data)
        return Response(...)


#  my view, ddo not use it it is just an example:

class tstList(generics.ListCreateAPIView):
    queryset = tst.objects.all()
    serializer_class = tstSerializer
    filter_backends = [DjangoFilterBackend]

