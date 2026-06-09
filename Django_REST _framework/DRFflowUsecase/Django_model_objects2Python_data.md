Convert Django model objects into Python data that can be rendered as JSON (continue from file views.py).

    serializer = WalkSerializer(walks, many=True)
Example data:

    </> Python
    [
      Walk(id=1, title="Morning Walk"),
      Walk(id=2, title="Evening Walk")
    ]
  
  becomes:
  
    </> Python
    [
        {"id": 1, "title": "Morning Walk"},
        {"id": 2, "title": "Evening Walk"}
    ]

Return the serialized data as a JSON HTTP response: return Response(serializer.data)  
Example response:
        
    </> JSON
    [
        {
            "id": 1,
            "title": "Morning Walk"
        },
        {
            "id": 2,
            "title": "Evening Walk"
        }
    ]
