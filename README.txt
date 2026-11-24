# BookMyShow – Movie and Events Website

## 1. Project Title

**BookMyShow – Django Movie and Events Website**

BookMyShow is a web-based movie and events discovery platform developed using Django. It is inspired by the layout and functionality of online movie and event ticketing platforms.

This is an academic project and is not affiliated with the official BookMyShow company.

## 2. Project Objective

The objective of this project is to develop a user-friendly website where users can explore movies, discover upcoming events, view detailed information, and create or access their accounts.

The project demonstrates the implementation of Django, database management, user authentication, dynamic web pages, HTML templates, and CSS styling.

## 3. Features

### Home Page
- Navigation bar with links to different sections.
- Recommended Movies section.
- Movie posters and details.
- Premieres section.
- Live Events section.
- Responsive and visually appealing layout.

### Movies Page
- Displays available movies dynamically from the database.
- Shows movie posters and information.
- Allows users to open individual movie detail pages.

### Movie Detail Page
- Displays detailed information about a selected movie.
- Shows movie title, genre, language, duration, rating, release date, and description.

### Events Page
- Displays available events dynamically from the database.
- Shows event images, categories, locations, dates, and prices.
- Allows users to open individual event detail pages.

### Event Detail Page
- Displays detailed information about a selected event.
- Includes event title, category, city, venue, date, price, and description.

### About Page
- Provides information about the BookMyShow project.

### Login Page
- Allows registered users to log in.
- Uses Django authentication.

### Sign Up Page
- Allows new users to create an account.
- Uses Django's built-in user authentication system.

### Logout
- Allows logged-in users to securely log out.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML | Web page structure |
| CSS | Styling and layout |
| SQLite3 | Database management |
| Django Authentication | Login and registration |
| Git and GitHub | Version control and project hosting |

## 5. Project Structure

```text
BookMyShow_Django_Complete/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── website/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── add_sample_data.py
│   ├── static/
│   │   └── website/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── website/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── movies.html
│   │       ├── movie_detail.html
│   │       ├── events.html
│   │       ├── event_detail.html
│   │       ├── about.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. Installation and Setup Instructions

Follow these steps to run the project on a local computer.

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/nimisha-g007/BookmyShow-Project.git
```

### Step 2: Open the Project Folder

```bash
cd BookmyShow-Project
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Create the Database and Apply Migrations

```bash
python3 manage.py migrate
```

The project uses SQLite3. The database file (`db.sqlite3`) is created automatically when migrations are applied.

The migration files are included in the GitHub repository, so there is no need to upload the existing local database file.

### Step 7: Add Sample Movies and Events

Run the following command to populate the database with sample records:

```bash
python3 manage.py add_sample_data
```

Alternatively, movies and events can be added through the Django Admin panel.

### Step 8: Create an Administrator Account (Optional)

```bash
python3 manage.py createsuperuser
```

Follow the instructions in the terminal to create an administrator account.

### Step 9: Start the Development Server

```bash
python3 manage.py runserver
```

### Step 10: Open the Website

Open the following address in your browser:

http://127.0.0.1:8000/

## 7. Page URLs

The following pages are available after starting the Django development server.

| Page | URL |
|---|---|
| Home | http://127.0.0.1:8000/ |
| Movies | http://127.0.0.1:8000/movies/ |
| Events | http://127.0.0.1:8000/events/ |
| About | http://127.0.0.1:8000/about/ |
| Login | http://127.0.0.1:8000/login/ |
| Sign Up | http://127.0.0.1:8000/signup/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

Individual movie and event detail pages are opened by selecting their respective cards.

## 8. Database and Migrations

The project uses SQLite3 as its database.

Two main application models are implemented:

**Movie Model**
- Title
- Genre
- Language
- Duration
- Release Date
- Rating
- Poster URL
- Description

**Event Model**
- Title
- Category
- City
- Venue
- Event Date
- Price
- Image URL
- Description

Django migration files are included in the `website/migrations/` folder.

The existing `db.sqlite3` file is not included in the GitHub repository. Each user can create their own database by running:

```bash
python3 manage.py migrate
```

To populate the database with sample movies and events:

```bash
python3 manage.py add_sample_data
```

The project uses Django's built-in authentication tables for user registration and login.


## 11. Security and Configuration

- Secret keys and private credentials should not be uploaded to GitHub.
- The virtual environment is excluded from version control.
- The local SQLite database file is excluded from version control.
- Temporary Python files and local environment files are excluded using `.gitignore`.
- Migration files are included in the repository.
- Each user should create their own local virtual environment and install dependencies using `requirements.txt`.

## 12. Project Limitations

This project focuses on movie and event discovery, dynamic listings, detail pages, and user authentication.

It does not currently implement actual ticket payment processing, cinema seat selection, ticket inventory management, OTP verification, or a live external movie catalogue.

## 13. GitHub Repository

**Project Repository:**

https://github.com/nimisha-g007/BookmyShow-Project

---

**Project Name:** BookMyShow – Movie and Events Website  
**Framework:** Django  
**Database:** SQLite3  
**Repository:** GitHub
