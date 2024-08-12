
####### GOOGLE SEARCH API #######

# For Django Endpoint Communication
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Depnedencies for seaerching links
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import F, Q

from pro_scrape.models import ScrapedData
from .models import SearchResult  
import re
import os
from dotenv import load_dotenv
from webstore.models import WebStore
import requests
import subprocess
import threading
from urllib.parse import urlparse 

# Load environment variables from .env file
load_dotenv() 

# Create event and lock for synchronization
scrapy_lock = threading.Lock()
scrapy_completed = threading.Event()

def google_search_and_store(query):
    API_KEY = os.getenv('GOOGLE_API_KEY')
    SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

    if not API_KEY or not SEARCH_ENGINE_ID:
        return HttpResponse("API key or search engine ID is not set in the environment variables.")

    search_query_pk = f"{query} buy OR shop OR store OR online OR ecommerce site:pk"
    num_results_pk = 9

    endpoint = "https://www.googleapis.com/customsearch/v1"

    SearchResult.objects.all().delete()
    ScrapedData.objects.all().delete()

    params_pk = {
        'q': search_query_pk,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'num': num_results_pk,
    }

    response_pk = requests.get(endpoint, params=params_pk)
    
    if response_pk.status_code != 200:
        return HttpResponse(f"Error in .pk search: {response_pk.status_code} - {response_pk.text}")

    # Get .pk links
    data_pk = response_pk.json()
    for item in data_pk.get('items', []):
            link = item.get('link', '')
            description = item.get('title', '') 
            print(f"Description: {description}, Link: {link}")
            # Extract store name from the link
            store_name = extract_store_name(link)

            # Create WebStore instance
            WebStore.objects.create(title=description, link=link, webstore_name=store_name)
            SearchResult.objects.create(description=description, link=link)

    # Second search for .com
    search_query_com = f"{query} buy OR shop OR store OR online OR ecommerce site:com"
    num_results_com = 3

    params_com = {
        'q': search_query_com,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'num': num_results_com,
    }

    response_com = requests.get(endpoint, params=params_com)

    if response_com.status_code != 200:
        return HttpResponse(f"Error in .com search: {response_com.status_code} - {response_com.text}")

    # Get .com links
    data_com = response_com.json()
    for item in data_com.get('items', []):
            link = item.get('link', '')
            description = item.get('title', '') 
            print(f"Description: {description}, Link: {link}")
            # Extract store name from the link
            store_name = extract_store_name(link)

            # Create WebStore instance
            WebStore.objects.create(title=description, link=link, webstore_name=store_name)
            SearchResult.objects.create(description=description, link=link)
            
    return HttpResponse("Search and store complete")

def extract_store_name(link):
    # Regular expression to match store name
    match = re.search(r'(?:https?://(?:www\.)?)?([a-zA-Z0-9-]+)\.(?:com\.pk|com|pk)/', link)
    if match:
        return match.group(1).capitalize()  # Capitalize store name
    else:
        return None

    

def run_scrapy_project(links):
    # Determine the absolute path to the current script
    current_script_path = os.path.abspath(__file__)
    print(f"Current script path: {current_script_path}")
    
    # Determine the project root path based on the current script path
    project_root_path = os.path.abspath(os.path.join(current_script_path, '../..'))
    print(f"Project root path: {project_root_path}")
    
    # Determine the path to the scrapy project folder
    scrapy_project_path = os.path.join(project_root_path, 'selenium_backend')
    print(f"Scrapy project path: {scrapy_project_path}")

    formatted_links = []
    for link in links:
        # Check if the link already has a scheme
        if not urlparse(link).scheme:
            # Prepend 'http://' as default scheme
            link = 'https://' + link
        formatted_links.append(link)
    
    command = f"cd {scrapy_project_path} && scrapy crawl product -a urls={','.join(formatted_links)}"
    subprocess.run(command, shell=True, check=True)


@api_view(['POST'])
def search_and_store(request):
    if request.method == 'POST':
        data = request.POST
        query = data.get('query', '')

        
        google_search_and_store(query)
        print(SearchResult.objects.all().values_list("link", flat=True))
        run_scrapy_project(SearchResult.objects.all().values_list("link", flat=True))

        update_webstore_with_prices()

        # Set event to signal completion of Scrapy command
        with scrapy_lock:
            scrapy_completed.set()
        
        print(f"Received data from frontend: {data}")

        return Response({'status': 'success'})
    else:
        return Response({'status': 'error', 'message': 'Invalid request method'})


def update_webstore_with_prices():
    # Iterate through ScrapedData objects
    for scraped_data in ScrapedData.objects.all():
        # Get corresponding WebStore object with matching link
        webstore_obj = WebStore.objects.filter(link=scraped_data.link).first()
        if webstore_obj:
            # Update WebStore object with scraped price
            webstore_obj.price = scraped_data.price
            webstore_obj.save()

@api_view(['GET'])
def get_products(request):
    threshold_time = timezone.now() - timezone.timedelta(hours=2.5)
    old_results = SearchResult.objects.filter(timestamp__lt=threshold_time)
    old_results.delete()
    
    products = SearchResult.objects.all().values('id', 'description', 'link')
    return Response(list(products))


@api_view(['GET'])
def get_scraped_products(request):
    # Calculate the threshold time
    threshold_time = timezone.now() - timezone.timedelta(hours=2.5)
    
    # Delete old results
    old_results = ScrapedData.objects.filter(timestamp__lt=threshold_time)
    old_results.delete()

    # Fetch records where price is neither "Price Not Found" nor an empty string
    scraped_products = ScrapedData.objects.exclude(Q(price="Price Not Found") | Q(price="")).values('title', 'price', 'link')

    # Return the response
    return Response(list(scraped_products))



