from app.auth.routes import router as auth_routes
from app.core import all_models
from app.invite.routes import router as invite_routes
from app.organization.routes import router as organization_routes
from app.organization_user.routes import router as organization_user_routes
from app.role_management.role.routes import router as role_routes
from app.role_management.system.system_permission.routes import (
    router as system_permission_routes,
)
from app.user.routes import router as user_routes

routers = [
    auth_routes,
    user_routes,
    organization_routes,
    invite_routes,
    role_routes,
    system_permission_routes,
    organization_user_routes,
]
