# Todo List Web Application

## Version 1.0 Features
- Multiple users should be able to use this web-app.
- A user is able to create, view, edit, or delete a task.
- A user can mark a task complete.

## Starting the application locally

- Clone this Repo
- Install the [Yarn Package Manager](https://classic.yarnpkg.com/en/docs/install/#mac-stable)
- Install the [Vue CLI](https://cli.vuejs.org/guide/installation.html)
- navigate to frontend dir `cd frontend`
- Run `yarn install` 
- Run `yarn serve` 

## The Stack

### Frontend 
The frontend is built with the vue javascript framework.
[Vue]("https://vuejs.org/") is a progressive javascript framework that is based 
on compontents. Components are a grouping of HTML, CSS, and JS.
Vue is also fully supported and maintained by the open source community, not
tied to a single organization. In order to build, lint, and serve 
the frontend we will be utilizing the [yarn package manager](
https://yarnpkg.com/)

#### Authentication Hack
Authentication is handled via a few hardcoded mock accounts.
although this is obviously not a production implementation, this allows
the showcasing of passing an user id as a authorized user cookie, to access
specific tasks based on the user on the backend. 
Given more time, I would utilize an /login endpoint that interacts with the backend
database and ensure https through the call flow. 


### Backend 
The backend is a cloud hosted node red rest api. Node red is a low code IOT platform
built on top of node js and express. **This endpoint has been decomissioned**

| Method     |      Pattern          |  Action | 
|:----------:|:---------------------:|:-------:|
| GET        |  /task                | Retrieve all tasks |
| POST       |  /task                | Create a task |
| PUT        |  /task/{id}           | Update task with id = {id} |
| DELETE     |  /task/{id}           | Delete task with id = {id} |

### Persistence

Persistence is managed via a cloud hosted mysql database. Below is the minimal schema to 
showcase a relationship between users and tasks for a todo-list.
**This endpoint has been decomissioned**

```mysql
CREATE TABLE users (
  user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
  task_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT FALSE,
  user_id INTEGER NOT NULL REFERENCES users
);

```

- Example Insert Statement
```mysql
INSERT INTO tasks (title, user_id) VALUES ('{{taskTitle}}', {{userID}})
```
- Example Update Statement
```mysql
UPDATE tasks SET title = '{{taskTitle}}', completed = {{taskCompleted}} WHERE task_id = {{taskID}}
```
- Example Delete Statement
```mysql
DELETE FROM tasks WHERE task_id={{taskID}}
```
- Example Retrieve Statement
```mysql
SELECT * FROM tasks JOIN users USING ( user_id ) WHERE user_id=2;
```
