from django.shortcuts import render


def about(request):
    """View-функция для ренедринга страницы с общей информации о Блогикуме."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """View-функция для ренедринга страницы правил Блогикума."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
