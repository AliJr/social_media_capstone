from rest_framework.permissions import BasePermission

# Custom permission for user actions
# List: Staff only can view the list of users
# Create: Anyone can create a user
# Retrieve: User can view own data or staff can view any user
# Update, Partial update: User can update own data or staff can update any user
# Destroy: staff can delete any user



class UserPermission(BasePermission):

    def has_permission(self, request, view):
        # Check if the action is 'list' and allow only staff to access
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        # Check if the action is 'create' and allow anyone to create a user
        elif view.action == 'create':
            return True
        # Allow actions 'retrieve', 'update', 'partial_update', 'destroy' for authenticated users
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the action is 'retrieve' and allow the user to access their own data or staff to access any user
        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        # Allow 'update' and 'partial_update' if the user is updating their own data or staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        # Allow 'destroy' if the user is deleting their own data or staff
        elif view.action == 'destroy':
            return obj == request.user or request.user.is_staff
        else:
            return False
