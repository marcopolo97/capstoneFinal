# Welcome to Marcus' Personal Restaurant!

Please pardon the UI. It is currently under construction :hammer:

## Project 

This is a Udacity Capstone Project for the Full Stack NanoDegree Course. This is site is about a new restaurant called Marcus' Personal Restaurant. On this site, users will be able to see what entrees the restaurant serves as well as drinks.

## Live Deployment

Check out the running site on [Heroku](https://udacity-food-capstone.herokuapp.com)

## API Documentation

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable

### Endpoints

#### GET /entrees

General:

- Returns a list of all the available entrees 

Sample: 

```
curl https://udacity-food-capstone.herokuapp.com/entrees

```

Output

```html

<p>Entrees Are Here!</p>

<ul class="items">

	<li>
		<p>Steak</p>
		<p>Broccoli</p>
		<p>Rice</p>
		<p>$25.50</p>
	</li>
	<br>

	<li>
		<p>Chicken</p>
		<p>Salad</p>
		<p>Mac and Cheese</p>
		<p>$5.50</p>
	</li>
	<br>

	<li>
		<p>Lamb</p>
		<p>Salad</p>
		<p>Green Beans</p>
		<p>$10.25</p>
	</li>
	<br>
</ul>

```
#### GET /drinks

General:

- Returns a list of all the available drinks 

Sample: 

```
curl https://udacity-food-capstone.herokuapp.com/drinks

```

Output

```html

<p>Here are the drinks we offer!</p>

<ul class="items">

	<li>
		<p>Drink: Vanilla Milkshake</p>
		<p>Price: $1.50</p>
	</li>
	<br>

	<li>
		<p>Drink: Water</p>
		<p>Price: $0.00</p>
	</li>
	<br>

	<li>
		<p>Drink: Soda</p>
		<p>Price: $1.00</p>
	</li>
	<br>

	<li>
		<p>Drink: Oreo Milkshake</p>
		<p>Price: $2.00</p>
	</li>
	<br>

	<li>
		<p>Drink: MnM Milkshake</p>
		<p>Price: $2.00</p>
	</li>
	<br>

</ul>

```

#### POST /entrees

General:

- Adds a entree to the database. The entree must have a meat, side_1, side_2, and price
- Returns the data passed to create a entree

Sample: 

```sh
curl -X POST -H "Content-Type: application/json" -d '{"meal": "Ham", "side_1": "Broccoli", "side_2": "Mashed Potatoes", "price":"$10.98"}' https://udacity-food-capstone.herokuapp.com/entrees

```

Output:

```json

{
    "meat": "Turkey",
    "price": "$9.80",
    "side_1": "Mashed Potatoes",
    "side_2": "Green Beans",
    "success": true
}

```

#### PATCH /entrees/{entree_id}

General:

- Updates a entree if it's in the database. The entree must have a meat, side_1, side_2, and price
- Returns the data passed to create a entree

Sample: 

```sh
curl -X POST -H "Content-Type: application/json" -d '{"meal": "Ham", "side_1": "Broccoli", "side_2": "Mashed Potatoes", "price":"$10.98"}' https://udacity-food-capstone.herokuapp.com/entrees/2

```

Output:

```json

{
    "meat": "Turkey",
    "price": "$20.10",
    "side_1": "Mashed Potatoes",
    "side_2": "Black Beans",
    "success": true
}

```

#### DELETE /entrees/{entree_id}

General:

- Deletes a entree if it's in the database 
- Returns the deleted entree id

Sample: 

```sh
curl -X DELETE -H "Content-Type: application/json" https://udacity-food-capstone.herokuapp.com/entrees/2

```

Output:

```json

{
    "delete": 7,
    "success": true
}

```

## Getting Started

### Installing Dependencies 

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup

This project uses the Heroku Database **only** to store data.

If you would like to create a Heroku Database, check out their [docs](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python)!

You can also set up a database locally.

### Authetication

This site uses [AUTH0](https://auth0.com/docs/) to reach the endpoints mentioned above. Within Auth0, there are two roles:
 

#### Customer

- Has access to get the entrees and drinks ONLY

#### Owner

- Has access to get the entrees and drinks
- Has access to create a new entree 
- Has access to update an entree
- Has access to delete an entree 


If a user with the role, Customer, tries to post a entree, update an entree, or delete an entree, they will be given an 403 error.

To test out the different roles in a tool like **Postman**, you can copy the below JWT tokens.

Customer JWT:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRvazdyRW5DSC1SRWJTanNqemNrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi10NmZwY3E1Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0ZjVlNDVmZTM5YmIwMDY5MWNlM2QzIiwiYXVkIjoiZm9vZCIsImlhdCI6MTYzMjU5MzQ0MywiZXhwIjoxNjMyNjAwNjQzLCJhenAiOiJWN1loT0plUEhtVGk3VWl0SkJyVVFjRmNKY1d1MzRpdyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcyIsImdldDplbnRyZWVzIl19.O6ob9Edpraj7XPIyanfLeVvdsVKOMJ5XkPIHJ7nwF_qdrAi7pwmQ5MZkwnM83Xw_iNJroBejG2Ik8BU_Pkw7WeAwmdDpX6UzyJCVjpgpkZnk-1yr5DaH0BXIh0QsDyX7X9aq7sClYQ8-JvE8msyLbpWkroPChvzXTvleHElRKYEGEKet3FntzuOFPTHMTlAyjMUg5yFP5T2_01EbhMqmP0PQBY53cAB8P01r4dldUie0PGYkQo5KOvPDTqPp_ebE1NywdYKkx1A1kciublIcWIP03FITILo8BuNvZL7hRppZ6WmBjxb04TLCE7VskY8eRMLi94bfbJMklE-bw1DR8w


Owner JWT 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRvazdyRW5DSC1SRWJTanNqemNrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi10NmZwY3E1Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NzM4YjQ0NDY3MmMwMDY5NGQwM2I3IiwiYXVkIjoiZm9vZCIsImlhdCI6MTYzMjYwMDkzOCwiZXhwIjoxNjMyNjA4MTM4LCJhenAiOiJWN1loT0plUEhtVGk3VWl0SkJyVVFjRmNKY1d1MzRpdyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmVudHJlZXMiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmVudHJlZXMiLCJwYXRjaDplbnRyZWVzIiwicG9zdDplbnRyZWVzIl19.UJKLu4iSG7t8xftJLRGYodGInl_CXJM_xtmoW0AXoGnE68n1IS673ulhC7bqKISPBFcBHeZFzr2jX9j-PqSjRzjaAXNI2JyAIxmavXEOCexO4sGQN-2SVrPo_GcNSzNSDTB8xCcedFBpgsgIkO82zX7e-b0aVW-SrcbpfZ2jYPXi3Gv8JR3vaHBcfhRJ-lxSpoQSN7lv6NyP66HOskqLgZMTnY7Aslcci1SDWCr3VXcrD7q5JA3PDsJx6GF6wSJsD-VeBL2lpcyhZzFOxfh4mgBXIJDkZgV8uR9x1-LlQXXlAs2wOGQi_3eOlgSaDA-44Y0vLxVgh3-7YrZO5NUy6g

[Login](https://dev-t6fpcq56.us.auth0.com/authorize?audience=food&response_type=token&client_id=V7YhOJePHmTi7UitJBrUQcFcJcWu34iw&redirect_uri=https://udacity-food-capstone.herokuapp.com) to the site to get a token.


## Running the App

If you have set up your database locally, you can run the following command:

```sh

flask run --reload

```

If you would like to, however, run your app in Heroku, you can do so as I did.

Check out their docs to learn how to deploy!


Note: You may need to run the following command for your environment variables

```sh

source setup.sh

```



