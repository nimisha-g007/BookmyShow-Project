CINEBOOK - DJANGO MOVIE AND EVENTS WEBSITE

This is a student project inspired by the layout and colour palette of online movie/event ticket websites. It is not affiliated with BookMyShow.

RUN ON MAC:
1. Extract this ZIP.
2. Open the extracted BookMyShow_Django_Complete folder in VS Code.
3. Open Terminal > New Terminal.
4. Run:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver
5. Open http://127.0.0.1:8000/
6. Admin: http://127.0.0.1:8000/admin/

ADD MOVIES AND EVENTS:
Log in to Django Admin. Add Movie and Event records. Paste direct image URLs into poster_url or image_url. Movie and event cards will then appear on Home, Movies and Events pages.

PAGES:
Home /, Movies /movies/, Events /events/, About /about/, Login /login/, Sign Up /signup/.
Movie and event cards open their own detail pages.

NOTE:
This project includes movie/event listing and Django user registration/login. It does not include payment processing, cinema seat selection, ticket inventory, OTP, or a live external movie catalogue.


HOME PAGE UPDATE
----------------
The homepage now has Recommended Movies, a dark Premieres section, and Live Events.
The navbar includes Home, Movies, Streams, and Events on every page.

To add the sample movie and event records, run this from the folder containing manage.py:
    python3 manage.py migrate
    python3 manage.py add_sample_data

The sample poster and event images are loaded from external image URLs, so an internet connection is needed for those images to appear.
