## How to run
- Before running you need to install the dependencies, using `pip install -r requirements.txt`.
- After that, run `python main.py` on terminal and the API will be turned on.
# Routes
## /create [POST]
This one creates a **task** and saves it on database.
- You need to pass a body like that:
```js
{
  "title": "do a readme", // the title for the task
  "description": "i am already doing it" // the description for the task
}
```
## /edit [PATCH]
It updates a **task** that was created before.
- Body:
```js
{
  "id": 1, // the id for the task, it must be an integer
  "title": "i need to do readme?", // the new title for the task
  "description": "yes i need" // the new description for the task
}
```
- The **title** and **description** are both optional, but you need to pass atleast one in the body.
## /tasks [GET] | [POST]
This one gets all the tasks or filtered tasks.
### GET
If you pass **get** method it will return an array with all the tasks in database.
### POST
This one with **post** method returns an array with filtered tasks in database with body filters.
- Body:
```js
{
  "id": 2, // searchs tasks for its id, must be integer
  "title": "readme", // searchs tasks for its title, must be string
  "completed": false // searchs tasks if its completed or not, must be boolean
}
```
- All options are optional, but you need to pass atleast one.
## /complete/:id [GET]
This one marks a task with **completed**, use **get** method.<br>
`/complete/1`<br>
Now `completed` will be **True**
```js
{ "completed": True }
```
## /delete/:id [DELETE]
Removes a task from database permanently, use **delete** method.<br>
`/delete/3`
- Now task with id **3** no longer exists.
