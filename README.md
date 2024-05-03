# product_inventory

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:ApoorvaJu08/product_inventory.git
   cd product_inventory

2. Build and run the docker containers
    docker-compose up --build

3. Visit http://localhost:8000 in your browser to access the API.

## API Endpoints

# Create Product
POST /api/products/create/

# Update Product
PUT /api/products/{id}/update/

# Delete Product
DELETE /api/products/{id}/delete/

# List Products
GET /api/products/

# View Product Details
GET /api/products/{id}/

# Adjust Stock
PATCH /api/products/{id}/adjust-stock/
