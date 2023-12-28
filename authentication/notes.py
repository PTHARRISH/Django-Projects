# create two folders : front, backend
# create virtual environment: py -m venv (venv name)
# move to backend : cd backend
# activate virtual env : venv/scripts/activate
# install django : pip install django
# install djangorestframework : pip install djangorestframework

# create a django project : django-admin startproject (projectname .)
# create a django app : python manage.py startapp (app name), django-admin startapp (appname)
# setup settings.py -> INSTALLED_APPS = [ 'rest_framework',   'appname']
# open crud -> urls.py file ->
# from django.urls import path,include
# urlpatterns=[path('', include('app.urls'))]

# create urls.py file inside app
# type inside urls.py -> from django.urls import path, urlpatterns=[ ]
# add views inside urls.py -> from . import views
# import http inside views.py -> from django.http import HttpResponse,JsonResponse
# create a function 
# and make migrations -> python manage.py makemigrations (No changes detected)
# and migrate -> python manage.py migrate
# to run server -> python manage.py runserver





# crete an react app 
# install node js and react extansion in vscode
# type to install npm globally -> npm install -g npm
# create a react app -> npx create-react-app (app name)



# Now we need two connect React and django
# so we need to install package - corsheaders (pip install django-cors-headers)
# It is used for communication between two different domains like react and django 
# these two run different localhost 3000 and 8000
# setup settings.py -> INSTALLED_APPS = [ 'corsheaders']
# add middleware in settings.py -> MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware",] on top
# type after middleware -> CORS_ALLOWED_ORIGINS = [ "http://localhost:3000",]




# Install React Router Dom
# It is used to help us to navigate across pages using various functions
# It is used to implement dynamic routing in a web app. 
# It allows you to display pages and allow users to navigate them.
# change directory to app folder -> cd frontapp
# To install react router dom -> npm i react-router-dom 
# open index.js file and import browser routers
# import browser routers -> import {BrowserRouter as Router} from 'react-router-dom'
# Browser Router is React’s router implementation for HTML5 browsers.
# They direct traffic functions on the internet and essentially make frontend pathways to different pages within an app or website, without redirecting (refreshing) the page.


# Create a component folder inside src folder and create home.js file
# Type inside home.js rafce -> react arrow function export component will be created 
# now create about,create page -> about.js,create.js inside component folder
# open app.js and remove inside div contents
# To display different pages we create based on the urls
# Inside app.js import for routing ->import { Routes, Route } from 'react-router-dom'; 
# and import all files inside components folder 
# import Home from './components/Home';
# import About from './components/About';
# import Create from './components/Create';
# inside div app class we routes the paths. 
# Routes have more than one Route. The route contains path and elements
# paths represents urlpaths and elements represent imported components
    # <div className="App">
    #   <Routes>
    #     <Route path='' element={<Home/>}/>
    #     <Route path='/about' element={<About/>}/>
    #     <Route path='/create' element={<Create/>}/>
    #   </Routes>
     
    # </div>
# Now we Route each pages individually inside a Routes tag 
# react will see and rendered the elements inside the route tag


# now run react -> npm start
# http://localhost:3000/ -> display home page and display Home
# http://localhost:3000/about -> display about page and display About
# http://localhost:3000/create -> display Create page and display Create
# 
# here we add 