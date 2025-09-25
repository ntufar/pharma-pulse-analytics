from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from .middleware.auth_middleware import AuthMiddleware
from .middleware.logging_middleware import LoggingMiddleware
from .api import customers, products, sales_transactions, users

app = FastAPI()

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Add authentication middleware
app.add_middleware(AuthMiddleware)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # React frontend default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(customers.router, prefix="/api")
app.include_router(products.router, prefix="/api")
app.include_router(sales_transactions.router, prefix="/api")
app.include_router(users.router, prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to PharmaPulse Analytics API"}
