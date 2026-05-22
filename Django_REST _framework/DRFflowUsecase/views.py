
        class WalkListView(APIView):
            def get(self, request):
                walks = Walk.objects.all()
                serializer = WalkSerializer(walks, many=True)
                return Response(serializer.data)
