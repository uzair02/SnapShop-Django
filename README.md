Here's an updated README with the additional instructions for running both the backend and frontend:

---

# Final Year Project (FYP) - Product Search and Recommendation System

## Overview
This repository contains the code for my Final Year Project (FYP), **SnapShop** — a comprehensive product search and recommendation system. This project enables users to search for products using three methods:
1. **Text Search**
2. **Barcode Search**
3. **Image Search**

The image search feature is powered by a custom-trained YOLOv8 model, with all aspects managed by me, including data gathering, cleaning, annotation, and model training.

## Features

### Search Options
- **Text Search**: Search for products using text input.
- **Barcode Search**: Look up products by scanning barcodes.
- **Image Search**: Leverages a YOLOv8 model to recognize products from images, with the full data preparation and model training pipeline handled in-house.

### Price Scraping
- **Scrapy**: Used for scraping product prices across various sources.
- **Selenium**: Integrated with Scrapy for JavaScript-driven pages and dynamic content scraping.

### Additional Features
- **Profile Customization**: Users can manage their profiles, including:
  - A **recommendation system**
  - **Wishlist** management
  - **Product and store reviews**

## Project Structure
- **Frontend**: Built with React, located in the `frontend` folder.
- **Backend**: Built with Django, located in the `backend` folder.

## User Experience
Users can choose their preferred search method (text, barcode, or image) to locate a product. The system then displays results with prices from different sources. Users have options to manage their profiles, wishlist, review products, and stores, or proceed with purchasing.

---

## How to Run the Project

### Backend (Django)

1. **Navigate to the backend folder**:
   ```bash
   cd SnapShop-Django/backend
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Django server**:
   ```bash
   python manage.py runserver
   ```

### Frontend (React)

1. **Navigate to the frontend folder**:
   ```bash
   cd SnapShop-Django/frontend
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Start the React development server**:
   ```bash
   npm start
   ```

---

**Project developed by Chemsa Technologies**
