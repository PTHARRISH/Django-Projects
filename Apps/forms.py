from django import forms

#  Form is a subclass of the forms module, which is part of the Django web framework. 
# Form provides a way to create and validate HTML forms in a web application. 
# A Form object can have one or more fields, each of which corresponds to an HTML input element. 
# The fields can have various types, such as CharField, EmailField, BooleanField, etc. 
# A Form object can also have methods to handle the form submission, such as clean, save, is_valid, etc.
class feedback(forms.Form):
    title=forms.CharField(label='Title',max_length=50)
    subject=forms.CharField(label='Subject Description',max_length=250)