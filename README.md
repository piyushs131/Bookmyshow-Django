# 🎬 BookMyShow Clone 🎟️

A fully functional Django-based clone of BookMyShow — India's top platform for booking movie and event tickets. This project includes authentication, movie/event listings, booking, seat selection, reviews, and admin management (excluding payment gateway).

---

## 🚀 Features

* 🔐 User registration and login
* 🎥 Movie listings with poster, trailer, and schedule
* 🎫 Seat selection for movie shows
* 📆 Event listings and booking
* 📜 Booking history per user
* 📝 User reviews on movies and events
* 🛠 Admin panel to manage all data
* 🖼 Media file handling for posters and thumbnails
* 📱 Fully responsive frontend using Django templates

---

## Installation Steps

1. Clone the Repository
   ````sh
    git clone https://github.com/yourusername/bookmyshow-clone.git
    cd bookmyshow-clone

2. Create and Activate Virtual Environment
   ````sh
    git clone https://github.com/yourusername/bookmyshow-clone.git
    cd bookmyshow-clone

3. 📄 Install Requirements
   ````sh
    pip install -r requirements.txt

4. Install Requirements
   - Create .env file in root
   ````sh
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

5. 🛠 Apply Migrations
    ````sh
    python manage.py makemigrations
    python manage.py migrate

6. 👤 Create Superuser
    ````sh
    python manage.py createsuperuser

7. 🏁 Run the Server
    ````sh
    python manage.py runserver

-- Visit in browser: http://127.0.0.1:8000


 ## 👤 User Roles
    - Anonymous User — Can browse movies/events, register, and login
    - Authenticated User — Can book tickets, leave reviews, and view bookings
    - Admin User — Full control over movies, events, seats, and user management



 ## Folder-wise Description

  * 📁 users/

  - Handles registration, login, logout, and user profiles
  - Templates: users/templates/users/

  * 📁 movies/

  -  Manages movies, trailers, posters, and schedules
  -  Admin can add/edit/delete movies

  * 📁 events/

  - Handles non-movie events (comedy, music, theatre, etc.)
  - Linked with bookings and reviews

  * 📁 bookings/

  - Ticket booking system
  - Includes show timing, seat booking, and user history

  * 📁 seats/

  - Seat layout and availability per show
  - Dynamically updates per movie/event

  *  📁 reviews/

  - User reviews for movies and events
  - Tied to registered users and admin moderation
