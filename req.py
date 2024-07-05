import requests

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzU0MDY2LCJpYXQiOjE3MTk3NTM0NjYsImp0aSI6IjJmNzM0NmIxZGE4YzQ5MWU4NzIwODg3ZTMzNGEwMzBmIiwidXNlcl9pZCI6Nn0.K5OexpQ9or-DZ_l72eUeOJFGoRJRu1WVa9B9TId9W70"}
url = 'http://6a9b-46-39-54-218.ngrok-free.app/api/Protected/'
s = requests.get(url=url, headers=headers)
print(s.content)
