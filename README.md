
# Social Media API


This project is a RESTful API for a basic social media platform, built using Django and Django Rest Framework (DRF). The API allows users to create, read, update, and delete posts, follow other users. The goal is to provide the backend for a social media application with essential features like user authentication, post management, and social interactions.

# Features

* User Authentication: Register and login users securely using JWT or session-based authentication.
* Post Management: Users can create, read, update, and delete posts. Posts can contain text and media.
* Follow System: Users can follow and unfollow other users, and see posts from those users in their feed.
* Optional Features (Future Expansion):
Likes: Users can like posts.
Comments: Users can comment on posts.

# Project Structure
|   manage.py
|   requirments.txt
+---api
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   permissions.py
|   |   serializers.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|           
+---core
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---images
|   |           
|   +---static
|   |   +---css
|   |   |       styles.css
|   |   |       
|   |   \---js
|   |           scripts.js
|   |           
|   +---templates
|       \---core
|               base.html
|               home.html
|               login.html
|               register.html
|               reset_password.html     
+---posts
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   serializers.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py     
+---social_media_api
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py    
\---userProfile
    |   admin.py
    |   apps.py
    |   models.py
    |   tests.py
    |   views.py
    |   __init__.py
            
