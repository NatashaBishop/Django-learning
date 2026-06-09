Convert Django model objects into Python data that can be rendered as JSON (continue from file views.py).

    serializer = WalkSerializer(walks, many=True)
Example data:

    [
      Walk(id=1, title="Morning Walk"),
      Walk(id=2, title="Evening Walk")
  ]
  
  becomes:
  
    [
        {"id": 1, "title": "Morning Walk"},
        {"id": 2, "title": "Evening Walk"}
    ]
