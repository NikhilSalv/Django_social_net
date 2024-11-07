## Social Media App

This is a simple Django-based social media platform that allows users to upload posts, follow others, like posts, and customize their profiles. The app includes functionalities for user authentication (sign up, sign in, logout), profile management, posting, and interacting with other users' content.

## Features

> - User Authentication:
> - Sign up
> - Sign in
> - Logout
> - Post Management:
> - - Upload posts with images and captions
> - Like or unlike posts
> - Profile Management:
> - - Edit user profile (image, bio, and location)
> - View other users' profiles
> - Follow and unfollow users
> - Feed:
> - - View posts from followed users

## Prerequisites

- Before you begin, ensure that you have met the following requirements:

      Python 3.x
      Django 3.x or higher
      A database (SQLite, PostgreSQL, etc.)
      Pillow library for image handling
      Git

## Installation

- **Clone the repository:**


`git clone https://github.com/yourusername/social-media-app.git`

`cd social-media-app`

- **Set up a virtual environment and install dependencies:**

`python -m venv venv`

`source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'`

`pip install -r requirements.txt`

- **Apply database migrations:**

`python manage.py migrate`

- **Create a superuser to manage the application:**

`python manage.py createsuperuser`

- **Run the development server:**

`python manage.py runserver`

- **Open the app in your browser at http://127.0.0.1:8000.**

## File Structure

    social-media-app/
    │
    ├── app/
    │   ├── migrations/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │       └── index.html
    ├── manage.py
    ├── requirements.txt
    └── settings.py

## App Functionality

**1. Sign Up**
-  Users can sign up by providing a username, email, password, and a password confirmation. Passwords are validated for strength.

**2. Sign In**
- After signing up, users can log in using their credentials. If credentials are incorrect, an error message is displayed.

**3. Feed**
- Users will see posts from people they follow. Each post includes a caption and an image.

**4. Like a Post**
- Users can like or unlike posts. Likes are stored in the LikedPost model.

**5. Follow/Unfollow**
- Users can follow or unfollow others. The FollowCount model keeps track of the relationships between users.

**6. User Profile**
- Users can view their own profile and the profiles of others. They can edit their bio, profile image, and location.

**7. Settings**
- Users can update their profile image, bio, and location in the settings page.


## Models

**Profile**
- Represents a user's profile.

- > user: Foreign key to the User model.
- > id_user: User ID (primary key).
- > bio: User's bio text.
- > profile_img: Profile image (uploaded to profile_images folder).
- > location: User's location.

**Post**

- Represents a post made by a user.

- > id: Unique identifier (UUID).
- > user: Username of the user who made the post.
- > image: Image uploaded with the post.
- > caption: Caption for the post.
- > created_at: Timestamp when the post was created.
- > no_of_likes: Number of likes on the post.

**LikedPost**

- Tracks which users have liked which posts.

- > post_id: ID of the post.
- > username: Username of the user who liked the post.

**FollowCount**

- Tracks the following relationships between users.

- > follower: Username of the follower.
- > user: Username of the user being followed.

**Templates**

- > index.html: Displays the feed of posts.
- > profile.html: Displays a user's profile, posts, and follow/unfollow button.
- > settings.html: Allows users to update their profile details.

## Development

**If you'd like to contribute to the project:**

- > **Fork the repository.**
- > **Create a new branch (git checkout -b feature/your-feature).**
- > **Make your changes.**
- > **Commit your changes (git commit -am 'Add your feature').**
- > **Push to the branch (git push origin feature/your-feature).**
- > **Open a pull request.**
