## Story Time Backend

### ERD Diagram
[erd](https://i.imgur.com/t2G7ndp.jpeg)

### Backend routes

```python
# Index and post request
path('stories/', Stories.as_view(), name='stories'),
# Show, Delete and Update request
path('stories/<int:pk>', StoryDetails.as_view(), name='story_details'),
# Index and Post for chapters request
path('chapters/', Chapters.as_view(), name='chapters'),
# Show, Delete and Update Request for chapters
path('chapters/<int:pk>', ChapterDetails.as_view(), name='chapters'),
# Sign up request post
path('sign-up/', SignUp.as_view(), name='sign-up'),
# Sign in request get
path('sign-in/', SignIn.as_view(), name='sign-in'),
# sign out request delete
path('sign-out/', SignOut.as_view(), name='sign-out'),
# change password request update
path('change-pw/', ChangePassword.as_view(), name='change-pw')
```

### Installation instructions
1. Run git init
2. install pipenv
3. run pipenv shell
4. run pipenv install django-rest-auth django-cors-headers python-dotenv dj-database-url
5. run psql -U postgres -f settings.sql
