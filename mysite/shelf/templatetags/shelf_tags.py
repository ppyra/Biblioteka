from django.template import Library

register = Library()

@register.filter(name='pub_date')
def pub_date(date):
    return date.year

@register.inclusion_tag('tags/show_editions.html') #nazwa pliku szablonu, który ma być wyrenderowany
def show_editions(obj): #tag pobiera taki obiekt
    return {'editions': obj.editions.all()} # swraca słownik, gdzie w kluczu editions bedzie przypisany queryset