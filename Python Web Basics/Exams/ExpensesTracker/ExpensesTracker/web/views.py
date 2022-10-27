from django.shortcuts import render, redirect

from ExpensesTracker.web.models import Profile, Expense
from ExpensesTracker.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, ExpenseCreateForm, ExpenseEditForm, ExpenseDeleteForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_left_money():
    total_money = get_profile().budget

    for expense in Expense.objects.all():
        total_money -= expense.price

    return total_money


def home(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    left_money = get_left_money()

    context = {
        'expenses': Expense.objects.all(),
        'profile': profile,
        'left_money': left_money,
    }

    return render(request, 'core/home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = ExpenseCreateForm()
    else:
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'expenses/expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        form = ExpenseEditForm(instance=expense)
    else:
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expenses/expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseDeleteForm(instance=expense)
    else:
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            expense.delete()
            return redirect('home')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expenses/expense-delete.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'left_money': get_left_money()
    }

    return render(request, 'profiles/profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            expenses = Expense.objects.all()
            expenses.delete()
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)
