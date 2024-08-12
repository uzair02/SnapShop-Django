from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from reviewmark.models import ProductReview
from .serializers import WebStoreRatingSerializer
from .models import WebStoreRating
from .models import WebStore
from django.shortcuts import get_object_or_404
from django.db.models import Avg, F, Func


@api_view(['POST'])
def submit_rating(request):
    serializer = WebStoreRatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_webstore_names(request):
    webstore_names = WebStore.objects.values_list('webstore_name', flat=True).distinct()
    print(webstore_names)
    return Response(webstore_names)

class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'

@api_view(['GET'])
def get_webstore_ratings(request):
    ratings = WebStoreRating.objects.values('webstore').annotate(averageRating=Round(Avg('rating')))
    return Response(ratings)

@api_view(['GET'])
def get_product_details(request):

    product_ids_string = request.GET.get('productIds')

    if not product_ids_string:
        return Response({'error': 'Missing productIds parameter'}, status=400)

    try:
        product_ids = [int(id) for id in product_ids_string.split(',')]
    except ValueError:
        return Response({'error': 'Invalid product ID format'}, status=400)

    # Filter WebStore objects based on IDs
    webstores = WebStore.objects.filter(pk__in=product_ids)

    # Check if any products were found
    if not webstores.exists():
        return Response({'error': 'No products found with provided IDs'}, status=404)

    # Serialize data (modify as needed)
    serialized_data = [
        {'id': webstore.id, 'title': webstore.title, 'link': webstore.link, 'price': webstore.price} for webstore in webstores
    ]

    return Response(serialized_data)




def recommend_products(request):
    # Calculate average ratings for each webstore
    webstore_ratings = WebStoreRating.objects.values('webstore').annotate(avg_rating=Avg('rating'))
    
    # Find the maximum average rating
    max_avg_rating = max(webstore_ratings, key=lambda x: x['avg_rating'])['avg_rating']
    
    # Find all webstores with the maximum average rating
    max_avg_rating_stores = [rating['webstore'] for rating in webstore_ratings if rating['avg_rating'] == max_avg_rating]
    
    # Fetch unique webstores with the maximum average rating
    unique_webstores = WebStore.objects.filter(webstore_name__in=max_avg_rating_stores).distinct()
    
    # Create a dictionary to store ratings for each product
    product_ratings = {review.product_id: review.rating for review in ProductReview.objects.filter(product_id__in=unique_webstores.values('id'))}
    
    # Prepare data including ratings
    data = []
    for store in unique_webstores:
        rating = product_ratings.get(store.id, None)
        data.append({
            'title': store.title,
            'link': store.link,
            'price': store.price,
            'rating': rating
        })

    if data:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'No recommendations available'}, status=404)




   























# import traceback
# import pandas as pd
# from django.db.models import Avg
# from sklearn.model_selection import train_test_split
# from sklearn.metrics.pairwise import cosine_similarity

# # Assuming you have a model named WebStoreRating with fields: user, webstore, rating

# def recommend_products(request):
#     try:
#         # Fetch all user ratings
#         user_ratings = WebStoreRating.objects.all()

#         # Extract relevant information from WebStoreRating objects
#         ratings_data = [
#             {
#                 'user': rating.user,
#                 'webstore': rating.webstore,
#                 'rating': rating.rating
#             }
#             for rating in user_ratings
#         ]

#         # Create DataFrame from the extracted data
#         user_ratings_df = pd.DataFrame(ratings_data)
#         print(user_ratings_df)
#         # Split data into train and test sets
#         train_data, test_data = train_test_split(user_ratings_df, test_size=0.2)

#         # Create user-item matrix (pivot table)
#         user_item_matrix = train_data.pivot_table(index='user', columns='webstore', values='rating')

#         # Fill missing values with 0 (assuming no rating means no interaction)
#         user_item_matrix = user_item_matrix.fillna(0)

#         # Compute similarity matrix (e.g., cosine similarity)
#         similarity_matrix = cosine_similarity(user_item_matrix, user_item_matrix)

#         # Print shapes of matrices for debugging
#         print("User-item matrix shape:", user_item_matrix.shape)
#         print("Similarity matrix shape:", similarity_matrix.shape)

#         # Predict ratings for missing entries (user-webstore pairs with no rating)
#         predicted_ratings = user_item_matrix.values.dot(similarity_matrix) / similarity_matrix.sum(axis=1)

#         # Convert predicted ratings array to DataFrame
#         predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns)

#         # Get unrated webstores for each user
#         unrated_webstores = user_item_matrix[user_item_matrix == 0]

#         # Get top N recommended webstores for each user
#         top_n_recommendations = {}
#         for user_id, unrated in unrated_webstores.iterrows():
#             top_n_recommendations[user_id] = predicted_ratings_df.loc[user_id].nlargest(10).index.tolist()

#         # Convert recommendations to JSON format
#         recommendations_json = {}
#         for user_id, recommendations in top_n_recommendations.items():
#             recommendations_json[user_id] = [{
#                 'title': WebStore.objects.get(webstore_name=webstore_name).title,
#                 'link': WebStore.objects.get(webstore_name=webstore_name).link,
#                 'rating': predicted_ratings_df.loc[user_id, webstore_name]
#             } for webstore_name in recommendations]

#         return JsonResponse(recommendations_json, safe=False)

#     except Exception as e:
#         traceback.print_exc()
#         return JsonResponse({'error': str(e)}, status=500)
