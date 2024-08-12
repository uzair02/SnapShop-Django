from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from api.models import User
import json
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Profile  # Assuming Profile is in the same directory


@api_view(['GET'])
def get_user_info(request):  # Use user_id as a parameter
    try:
        user_id = request.GET.get('userId')
        user = get_object_or_404(User, id=user_id)
        profile = Profile.objects.get(user=user)

        data = {
            'full_name': profile.full_name,
            'username': user.username,
            'email': user.email,
            'bio': profile.bio,
            'verified': profile.verified,
            # Add other relevant user data you want to include
        }

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        print("Error fetching user info:", e)
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



@api_view(['POST'])
def update_profile(request):
    if request.method == 'POST':
        user_id = request.data.get('user_id') 
        full_name = request.data.get('fullName')
        bio = request.data.get('bio')

        user = get_object_or_404(User, id=user_id)

        profile = user.profile

        if full_name:
            profile.full_name = full_name
        if bio:
            profile.bio = bio

        profile.save()  # Save the profile

        return JsonResponse({'message': 'Profile updated successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)