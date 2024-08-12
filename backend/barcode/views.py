from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import os
from dotenv import load_dotenv
import numpy as np
from io import BytesIO
from PIL import Image
from pyzbar import pyzbar
from .models import Product
from links.views import google_search_and_store
import requests
from ultralytics import YOLO


load_dotenv()
# Get the API URL from the environment
API_URL = os.getenv('API_URL')

@csrf_exempt
def decode_barcode(request):
    if request.method == 'POST':
        try:
            uploaded_image = request.FILES.get('image')

            # Read the uploaded image
            image_data = uploaded_image.read()
            image_np_array = np.frombuffer(image_data, dtype=np.uint8)
            img = cv2.imdecode(image_np_array, cv2.IMREAD_UNCHANGED)

            # Decode barcodes
            barcodes = pyzbar.decode(img)
            print(barcodes)
            # Assuming you want details for the first barcode found
            if barcodes:
                barcode_data = barcodes[0].data.decode("utf-8")
                product_name = get_product_details(barcode_data)
                Product.objects.create(name=product_name)

                print(f'Product name is: {product_name}')
                google_search_and_store(product_name)
                # print(f'search_results are.... {search_results}')
                return JsonResponse({'productName': product_name})
            else:
                # If no barcode detected, perform object detection
                objects_detected = detect_objects(img)
                print(f'Product name is: {objects_detected}')
                if objects_detected:
                    Product.objects.create(name=objects_detected)
                    google_search_and_store(objects_detected)
                    print(f'objects_detected: {objects_detected}')
                    return JsonResponse({'objectsDetected': objects_detected})
                else:
                    return JsonResponse({'error': 'No barcode or objects found in the image'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def detect_objects(image_path):
    try:
        # Determine the absolute path to the current script
        current_script_path = os.path.abspath(__file__)
        print(f"Current script path: {current_script_path}")

        # Determine the project root path based on the current script path
        # Move up two levels to get to the 'backend' directory
        project_root_path = os.path.abspath(os.path.join(current_script_path, '../..'))
        print(f"Project root path: {project_root_path}")

        # Determine the path to the YOLO model file
        model_path = os.path.join(project_root_path, 'best.pt')
        print(f"YOLO model path: {model_path}")

        print("Loading YOLO model...")
        yolo_model = YOLO(model_path)
        
        print("YOLO model loaded successfully.")

        print("Performing object detection...")
        results = yolo_model.predict(image_path, verbose=False)[0]
        names = yolo_model.names

        # Get the first detected object name
        object_detected = names[int(results.boxes.cls[0])]

        print("Object Detected:", object_detected)
        return object_detected
    except Exception as e:
        print("Error in detect_objects:", str(e))
        return None


def get_product_details(barcode):
    api_url = f'{API_URL}{barcode}.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        product_details = response.json().get('product', {})
        product_name = product_details.get('product_name', 'Product Name Not Found')
        return product_name
    else:
        return 'Error fetching product details'


