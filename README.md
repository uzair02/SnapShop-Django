# Final Year Project (FYP) - Product Search and Recommendation System

## Overview

This repository contains the code for my Final Year Project (FYP), which includes a comprehensive product search and recommendation system. The project allows users to search for products using three different options:

1. **Search by Text**
2. **Search by Barcode**
3. **Search by Image**

The search by image functionality is powered by a custom-trained YOLOv8 model. I have personally handled every aspect of this process, including data gathering, data cleaning, image annotation, and training the YOLO model.

## Features

### Search Options
- **Text Search**: Allows users to search for products using text input.
- **Barcode Search**: Enables product search by scanning barcodes.
- **Image Search**: Utilizes a YOLOv8 model to identify products from images. This includes:
  - Data Gathering
  - Data Cleaning
  - Image Annotation
  - Training the YOLOv8 Model

### Price Scraping
- **Scrapy**: Used and refined for scraping product prices from various sources.
- **Selenium**: Integrated with Scrapy for loading JavaScript content and scraping dynamic web pages.

### Additional Features
- **Custom Profile Settings**: Users can customize their profiles, including:
  - Recommendation System
  - Adding to Wishlist
  - Reviewing Products and Stores

## Project Structure

- **Frontend**: Built with React, located in the `frontend` folder of this repository.
- **Backend**: Built with Django, located in the `backend` folder of this repository.

## User Experience

When a customer wants to buy a product, they can use any of the search options provided (text, barcode, or image). The system then displays links with prices scraped from various sources. Users can further customize their profile, add products to their wishlist, review products, and stores, or proceed to purchase the product for convenience.





Project developed by **'Chemsa Devs'**
