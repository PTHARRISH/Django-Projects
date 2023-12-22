# Create urls.py file in Apps
# import path, import views file in Apps
from django.urls import path
from . import views

# add urlpatterns
urlpatterns=[
     path('',views.myfunctioncall,name='myfunctioncall'),
     # pass parameters and add two numbers
     path('add/<int:a>/<int:b>',views.add,name='add'),
     # pass str and int parameter print in json response
     path('name/<str:name>',views.printname,name='printname'),
     # pass parameter and display name and age stored in mydictionary print in json response
     path('intro/<str:name>/<int:age>',views.intro,name='intro'),
     # First HTML Page create navigation bar 
     path('first/',views.firstpage,name='first'),
     # second HTML page and extends details from first html page
     path('second/',views.secondpage,name='second'),
     # create dictionary and display in templates
     path('third/',views.thirdpage,name='third'),
     # create fruit list convert dictionary and display in templates
     path('fruits/',views.fruits,name='fruits'),
     # If else part print num1 or num2 Greater
     path('num/<int:num1>/<int:num2>',views.num,name='num'),
     # print Image and css stye in static files
     path('image/<str:image>',views.myimage,name='myimage'),
     # create form and enter the data
     path('myforms/',views.myforms,name='myforms'),
     # get the data from the form.html and display in the submitform json responses
     path('submit/',views.submitform,name='submitform'),
     # create forms.py file and add fields.
     path('forms/',views.forms,name="forms"),
     # create an login form and add the alert validation and display message
     path('alert/',views.forms_alert,name="forms_alert"),
]