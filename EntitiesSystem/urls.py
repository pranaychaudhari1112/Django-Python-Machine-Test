from django.contrib import admin
from django.urls import path
from EntitiesSystem_APP.views import ClientList, ClientDetail, ProjectList, ProjectListForUser
from rest_framework.authtoken.views import obtain_auth_token  # Import this for token generation

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/clients/', ClientList.as_view(), name='client-list'),
    path('api/clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('api/clients/<int:client_id>/projects/', ProjectList.as_view(), name='project-list'),
    path('api/projects/', ProjectListForUser.as_view(), name='project-list-user'),
    # API routes
    #path('api/clients/', ClientView.as_view(), name='client-list'),  # This should match your '/api/clients/' endpoint
    # path('api/clients/<int:pk>/', ClientView.as_view(), name='client-detail'),
    # path('api/projects/', ProjectView.as_view(), name='project-list'),
    
    # Add this route for token authentication
    path('api/token/', obtain_auth_token, name='api_token'),  # Token URL for authentication
]
