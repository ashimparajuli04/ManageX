from app.auth.routes import router as auth_routes
from app.user.routes import router as user_routes

routers = [
    auth_routes,
    user_routes,
]
