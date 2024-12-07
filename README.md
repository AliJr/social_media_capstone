
# Social Media API


This project is a RESTful API for a basic social media platform, built using Django and Django Rest Framework (DRF). The API allows users to create, read, update, and delete posts, follow other users, and view a personalized feed of posts from users they follow. The goal is to provide the backend for a social media application with essential features like user authentication, post management, and social interactions.

# Features

* User Authentication: Register and login users securely using JWT or session-based authentication.
* Post Management: Users can create, read, update, and delete posts. Posts can contain text and media.
* Follow System: Users can follow and unfollow other users, and see posts from those users in their feed.
* Personalized Feed: A feed of posts displayed for a user, based on the users they follow.
* Optional Features (Future Expansion):
Likes: Users can like posts.
Comments: Users can comment on posts.

# Project Structure
social_media_api/              
├── core/                  
│   ├── migrations/        
│   ├── __init__.py
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py          
│   ├── views.py           
│   ├── urls.py            
│   └── tests.py           
├── social_media_api/                 
│   ├── __init__.py           
│   ├── settings.py        
│   ├── urls.py            
│   ├── wsgi.py            
│   └── asgi.py            
├── manage.py              
├── .gitignore             
├── README.md                    
