# DRF supports multiple auth methods:

# Token Authentication
# Session Authentication
# JWT (via external libraries)
from rest_framework.permissions import IsAuthenticated

class SecureView(APIView):
    permission_classes = [IsAuthenticated]
