from django.shortcuts import render, redirect

from GamesPlay.web.models import Profile, Game
from GamesPlay.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, GameCreateForm, GameEditForm, \
    GameDeleteForm


def check_profile_exists():
    try:
        Profile.objects.get()
        return True
    except Profile.DoesNotExist:
        return False


def get_user():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_average_rating():
    games = Game.objects.all()

    if not games:
        return 0.0

    total_rating = 0
    games_count = Game.objects.count()

    for game in games:
        total_rating += game.rating

    return total_rating / games_count


def home(request):
    context = {
        'hide_nav_links': True if not check_profile_exists() else False,
    }

    return render(request, 'core/home-page.html', context)


def dashboard(request):
    context = {
        'games': Game.objects.all(),
    }
    return render(request, 'core/dashboard.html', context)


def game_create(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'games/create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'games/details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'games/edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        game.delete()
        return redirect('dashboard')

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'games/delete-game.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'hide_nav_links': True if not check_profile_exists() else False,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    context = {
        'profile': get_user(),
        'games_count': Game.objects.count(),
        'average_rating': get_average_rating(),
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_user()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_user()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
