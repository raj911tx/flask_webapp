# flask_webapp
A Blogging Webapplication Using Flask deployed using kubernetes

First activate the python virtual environment using
```
source venv/Scripts/activate
```
To install the dependencies run
```
pip install -e
```

To initilize the database
```
flask init-db
```

To run the web application
```
export FLASK_APP=blogy
export FLASK_ENV=development
flask run
```

![](https://github.com/raj911tx/flask_webapp/blob/master/feed.PNG)
![](https://github.com/raj911tx/flask_webapp/blob/master/post.PNG)
