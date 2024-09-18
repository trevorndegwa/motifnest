# MotifNest

MotifNest is a social platform where users can share and showcase their unique motifs, images, and posts. The web application is built using Flask and SQLAlchemy, offering features like user authentication, profile management, post creation with image uploads, and a comment system.

# Deployed Application

You can access the live version of the application here: [MotifNest](https://trevorndegwa96.pythonanywhere.com/home).

## LinkedIn

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/trevor-ndegwa-794246194/).

## Technologies Used

- **Flask**: Python-based web framework for the backend.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite**: Database used for development.
- **Flask-WTF**: Form handling.
- **Flask-Login**: User session management.
- **Jinja2**: Template engine for rendering HTML.
- **PythonAnywhere**: Deployment platform.
- **HTML/CSS**: For the frontend and static content.

## Features

- **User Registration and Authentication**: Users can sign up, log in, and manage their accounts.
- **Profile Management**: Users can upload profile pictures and update their personal information.
- **Post Creation**: Users can create posts that include images and text, and display them in the feed.
- **Comment System**: Users can comment on posts.
- **CRUD Operations**: Users can Create, Read, Update, and Delete their posts.
- **Pagination**: Proper pagination to handle large amounts of posts.
- **Deployment**: The app is deployed on PythonAnywhere.

## Project Structure

1. **Initial Setup**: Setting up the Flask environment and the basic project structure.
2. **Templates Creation**: Building reusable HTML templates using Jinja2.
3. **Form Handling**: Managing user input with Flask-WTF.
4. **Database Integration**: Using SQLAlchemy ORM to interact with the SQLite database.
5. **Project Organization**: Structuring the project in a modular way.
6. **User Authentication**: Implementing secure login and registration using Flask-Login.
7. **Profile Management**: Allowing users to manage their profiles, including profile picture uploads.
8. **CRUD Operations**: Providing users the ability to create, edit, and delete posts.
9. **Pagination**: Implementing pagination to manage the display of posts effectively.
10. **Deployment**: Deploying the application on PythonAnywhere.

## Challenges Faced

- **Database Conflicts**: Encountered merge conflicts in `site.db` during Git operations, which were resolved by re-migrating the database.
- **User Authentication**: Managing proper session handling and user permissions for secure access to posts.
- **CRUD Operations**: Ensuring proper deletion of posts and comments without leaving database inconsistencies.

## Future Fixes and Improvements

- **Search Functionality**: Adding the ability for users to search posts by keywords.
- **Image Optimization**: Compressing uploaded images to reduce storage requirements.
- **Enhanced Commenting System**: Adding nested comments for better discussion threads.
- **Real-Time Updates**: Implementing real-time features for post and comment updates.
- **Improved Error Handling**: Enhancing the robustness of the app by implementing more detailed error messages and logging.
- **Payment Integration**: MPESA API will be utilised for facilitating transactions between clients and designers.

## How to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/trevorndegwa/motifnest.git
    cd motifnest
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Initialize the database:
    ```bash
    flask db upgrade
    ```

4. Run the application:
    ```bash
    flask run
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
