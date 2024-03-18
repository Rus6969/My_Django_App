from django.urls import path
from.import views
# urlpatterns = [

#     path("<int:month>",views.monthly_challenge_byNumber),
#     path("<str:month>",views.monthly_challenge)

# ]

# path name to URL for constructing paths 
urlpatterns = [

    path("<int:month>",views.monthly_challenge_byNumber),
    # we gave name here to our path "name = month-challege " to implement redirection in views 
    path("<str:month>",views.monthly_challenge,name="month-challenge")

]