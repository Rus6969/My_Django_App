from django.urls import path
from.import views
# urlpatterns = [

#     path("<int:month>",views.monthly_challenge_byNumber),
#     path("<str:month>",views.monthly_challenge)

# ]

# path name to URL for constructing paths 
urlpatterns = [
    # this empty path is created to create URL for /challenges
    path("",views.index),
    path("<int:month>",views.monthly_challenge_by_number),
    # we gave name here to our path "name = month-challege " to implement redirection in views 
    path("<str:month>",views.monthly_challenge,name="month-challenge")

]