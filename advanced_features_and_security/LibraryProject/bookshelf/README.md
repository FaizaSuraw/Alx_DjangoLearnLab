# Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: all permissions

## Usage
Permissions are enforced in views using `@permission_required`. Example:

```python
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    ...
