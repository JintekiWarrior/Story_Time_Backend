## Story Time Backend
Backend for the client. This repo containes two models, one is the model that
allows the user to create a story by adding a title. The other allows the user
to add chapters with a name and a body. There is a one to many relationship in
which the user can add as many chapters to one story. All the data and routes
are handled in this repo as well.

### Repos
[Server Repo](https://github.com/JintekiWarrior/Story_Time_Backend)
[Deployed Server](https://story-time-backend-app.herokuapp.com)
[Client Repo](https://github.com/JintekiWarrior/Story_Time_Frontend)
[Deployed Client](https://jintekiwarrior.github.io/Story_Time_Frontend)

### ERD Diagram
[erd](https://i.imgur.com/t2G7ndp.jpeg)

### Technologies
React, Javascript, HTML, CSS, Django, Python, Postgres

### Unsolved Issues
- Other users cannot see your created stories
- User's cannot add to others stories
- User's cannot comment or like other's stories

### Strategy
Used the github khanban board to plan the project. After a todo tab was done it
was moved to the completed pile. Any issues ran into were googled to find the
answer. If too much time was bieng spent on the issue, a project issue tab
was opened and an instructor would guide me to the right answer.


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
