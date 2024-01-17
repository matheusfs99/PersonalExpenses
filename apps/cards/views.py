from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForms


def list_cards(request):
    queryset = Card.objects.all()
    context = {"cards": queryset}
    return render(request, "list-cards.html", context)


def create_card(request):
    form = CardForms(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("cards:list_cards")
    return render(request, "create-card.html", context)


def update_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    form = CardForms(request.POST or None, instance=card)
    context = {"form": form}
    if request.method == "POST":
        form.save()
        return redirect("cards:list_cards")
    return render(request, "update-card.html", context)
