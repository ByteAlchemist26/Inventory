from django.urls import path     #imports Django's built-in path() function
from . import views              #imports the views.py file from the current directory (your app)
                            #so you can connect URLS to the view functions defined there

urlpatterns = [
    path('', views.medicine_list, name = 'medicine_list'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('info/<int:product_id>', views.medicine_info, name='medicine_info'),
    path("update_stock/<int:product_id>/", views.update_stock, name="update_stock"),
    # '' -> An empty string means this the root URL of your app
    # views.medicine_list -> Connets URL to the medicine_list function
                             # in your views.py
    # name = 'medicine_list'-> Gives URL pattern a name, which is useful in templates
]
# This list of URL pattern for the app
# Django reads this to know which views to call for which URL paths