from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS so your React app (localhost:5173) can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---
class Order(BaseModel):
    name: str
    email: str
    address: str

# --- Updated Database with Valid Shopsy Assets ---


# 1. Main Products Section
PRODUCTS_DATA = [
    {"id": 1, "img": "../../public/assets/women/women.png", "title": "Women Ethnic", "rating": 5.0, "color": "white", "aosDelay": "0"},
    {"id": 2, "img": "../../public/assets/women/women2.jpg", "title": "Women western", "rating": 4.5, "color": "Red", "aosDelay": "200"},
    {"id": 3, "img": "../../public/assets/women/women3.jpg", "title": "Goggles", "rating": 4.7, "color": "brown", "aosDelay": "400"},
    {"id": 4, "img": "../../public/assets/women/women4.jpg", "title": "Printed T-Shirt", "rating": 4.4, "color": "Yellow", "aosDelay": "600"},
    {"id": 5, "img": "../../public/assets/women/women2.jpg", "title": "Fashion T-Shirt", "rating": 4.5, "color": "Pink", "aosDelay": "800"},
]

# 2. Top Products (Best Products) Section
TOP_PRODUCTS_DATA = [
    {"id": 1, "img": "../../public/assets/shirt/shirt.png", "title": "Casual Wear", "description": "High-quality casual wear for daily comfort and style."},
    {"id": 2, "img": "../../public/assets/shirt/shirt2.png", "title": "Printed shirt", "description": "Trendsetting printed shirts for a modern, sharp look."},
    {"id": 3, "img": "../../public/assets/shirt/shirt3.png", "title": "Women shirt", "description": "Elegant women's shirts designed for formal and casual events."},
]

# 3. Testimonials Section
TESTIMONIALS_DATA = [
    {"id": 1, "name": "Victor", "text": "The quality of the ethnic wear is top-notch. Highly recommended!", "img": "https://picsum.photos/id/10/200/200"},
    {"id": 2, "name": "Satya Nadella", "text": "Fast delivery and easy payment methods. Great experience.", "img": "https://picsum.photos/id/22/200/200"},
    {"id": 3, "name": "Virat Kohli", "text": "The printed shirts have a perfect fit. Definitely shopping again.", "img": "https://picsum.photos/id/34/200/200"},
    {"id": 4, "name": "Sachin Tendulkar", "text": "Excellent collection and very responsive customer support.", "img": "https://picsum.photos/id/45/200/200"},
]

# --- API Endpoints ---
@app.get("/api/products")
async def get_products():
    return PRODUCTS_DATA

@app.get("/api/top-products")
async def get_top_products():
    return TOP_PRODUCTS_DATA

@app.get("/api/testimonials")
async def get_testimonials():
    return TESTIMONIALS_DATA

@app.post("/api/order")
async def place_order(order: Order):
    # This is where you'd save to a database
    print(f"Order Received: {order.name} ({order.email}) at {order.address}")
    return {"status": "success", "message": f"Thanks {order.name}, your order is placed!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)