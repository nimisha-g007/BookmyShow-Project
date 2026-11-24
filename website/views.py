

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import Movie, Event


# ---------------- HOME PAGE ----------------

def home(request):
    movies = Movie.objects.all().order_by('-release_date')[:8]

    premieres = Movie.objects.all().order_by('-release_date')[:5]

    events = Event.objects.all().order_by('event_date')[:5]

    music_events = Event.objects.filter(
        Q(category__icontains='music') |
        Q(category__icontains='concert') |
        Q(title__icontains='music') |
        Q(title__icontains='concert') |
        Q(title__icontains='festival') |
        Q(title__icontains='DJ')
    ).order_by('event_date')[:5]

    context = {
        'movies': movies,
        'premieres': premieres,
        'events': events,
        'music_events': music_events,
    }

    return render(request, 'website/home.html', context)


# ---------------- MOVIES PAGE ----------------

def movies(request):
    search = request.GET.get('search', '')

    all_movies = Movie.objects.all()

    if search:
        all_movies = all_movies.filter(
            Q(title__icontains=search) |
            Q(genre__icontains=search) |
            Q(language__icontains=search)
        )

    context = {
        'movies': all_movies.order_by('-release_date'),
        'search': search,
    }

    return render(request, 'website/movies.html', context)


# ---------------- MOVIE DETAIL PAGE ----------------

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    return render(
        request,
        'website/movie_detail.html',
        {'movie': movie}
    )


# ---------------- EVENTS PAGE ----------------

def events(request):
    search = request.GET.get('search', '').strip()

    all_events = Event.objects.all()

    if search:
        category = search.lower()

        if category in ['comedy']:
            all_events = all_events.filter(
                Q(category__icontains='comedy') |
                Q(title__icontains='comedy')
            )

        elif category in ['amusement park', 'fun & amusement', 'amusement']:
            all_events = all_events.filter(
                Q(category__icontains='amusement') |
                Q(category__icontains='fun') |
                Q(title__icontains='amusement') |
                Q(title__icontains='fun')
            )

        elif category in ['theatre', 'theater']:
            all_events = all_events.filter(
                Q(category__icontains='theatre') |
                Q(category__icontains='theater') |
                Q(title__icontains='theatre') |
                Q(title__icontains='theater')
            )

        elif category in ['music', 'concert']:
            all_events = all_events.filter(
                Q(category__icontains='music') |
                Q(category__icontains='concert') |
                Q(title__icontains='music') |
                Q(title__icontains='concert')
            )

        elif category in ['workshops', 'workshop']:
            all_events = all_events.filter(
                Q(category__icontains='workshop') |
                Q(title__icontains='workshop')
            )

        else:
            all_events = all_events.filter(
                Q(title__icontains=search) |
                Q(category__icontains=search) |
                Q(city__icontains=search)
            )

    # Show maximum 4 events for the selected category
    all_events = all_events.order_by('event_date')[:4]

    context = {
        'events': all_events,
        'search': search,
    }

    return render(request, 'website/events.html', context)


# ---------------- EVENT DETAIL PAGE ----------------

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(
        request,
        'website/event_detail.html',
        {'event': event}
    )


# ---------------- ABOUT PAGE ----------------

def about(request):
    return render(request, 'website/about.html')


# ---------------- SIGN UP ----------------

def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not email or not password or not confirm_password:
            messages.error(request, 'Please fill in all fields.')

        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')

        else:
            try:
                validate_password(password)

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                login(request, user)

                messages.success(request, 'Account created successfully!')

                return redirect('home')

            except ValidationError as error:
                for message in error.messages:
                    messages.error(request, message)

    return render(request, 'website/signup.html')


# ---------------- LOGIN ----------------

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            messages.success(request, 'Logged in successfully!')

            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'website/login.html')


# ---------------- LOGOUT ----------------

def logout_view(request):

    logout(request)

    messages.success(request, 'You have been logged out.')

    return redirect('home')

