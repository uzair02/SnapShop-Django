from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Wishlist, ProductReview
from rest_framework.permissions import IsAuthenticated
from .serializers import WishlistSerializer, ProductReviewSerializer
from .models import Wishlist, ProductReview
from django.http import JsonResponse, HttpResponse
from .serializers import WishlistSerializer, ProductReviewSerializer
import json
from webstore.models import WebStore
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def add_to_wishlist(request):
    print('Request Data:', request.data)

    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("ok")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_from_wishlist(request, product_id):
    try:
        # Find all wishlist items with the given product ID
        wishlist_items = Wishlist.objects.filter(product=product_id)
        
        # Delete all found wishlist items
        wishlist_items.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except Wishlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_wishlist(request):
    wishlist_items = Wishlist.objects.filter()
    serializer = WishlistSerializer(wishlist_items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submit_product_review(request):
    print(request.data)
    serializer = ProductReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def get_wishlist_items(request):
    try:
        user_id = request.GET.get('userId')
        if user_id is None:
            return HttpResponse(json.dumps({'error': 'User ID is required'}), content_type="application/json", status=400)
        
        wishlist_items = Wishlist.objects.filter(user=user_id)
        serializer = WishlistSerializer(wishlist_items, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type="application/json", status=200)
    except Exception as e:
        print("Error fetching wishlist items:", e)
        return HttpResponse(json.dumps({'error': 'Internal Server Error'}), content_type="application/json", status=500)

def get_user_reviews(request):
    try:
        user_id = request.GET.get('userId')
        if user_id is None:
            return HttpResponse(json.dumps({'error': 'User ID is required'}), content_type="application/json", status=400)

        user_reviews = ProductReview.objects.filter(user=user_id)
        serializer = ProductReviewSerializer(user_reviews, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type="application/json", status=200)
    except Exception as e:
        print("Error fetching user reviews:", e)
        return HttpResponse(json.dumps({'error': 'Internal Server Error'}), content_type="application/json", status=500)

@api_view(['DELETE'])
def delete_review(request, review_id):
    try:
        review = ProductReview.objects.get(product=review_id)
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully'}, status=200)
    except ProductReview.DoesNotExist:
        return JsonResponse({'error': 'Review not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


