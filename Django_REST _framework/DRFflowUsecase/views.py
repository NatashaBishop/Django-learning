# Django REST Framework API view that returns all Walk records as JSON
        class WalkListView(APIView):
            def get(self, request):
                walks = Walk.objects.all()
                serializer = WalkSerializer(walks, many=True)
                return Response(serializer.data)
                    
# bad example - do not emplement - 200 lines of business logic, do nor doit (-:
class ListingView(APIView):
    def post(self, request):
            
# good example - emplement this way:
class ListingView(APIView):
    def post(self, request):
        listing = create_listing(request.data)
        return Response(...)
