## UNILAG API

This is web app simply scrapes the [unilag website](http://new.unilag.edu.ng) for news and stores quick details (slug, link, title, etc) about the news in a database. This is done via the cron script. Ideally should be run every hour

It provides endpoints for retrieving the saved news items

This is part of a series of learning excercises ultimately targeted at building a front-end web app with vue.js

The `.env.sample` file containts the keys for the .env file. To run this ensure that the proper values are supplied

### Run Instructions

Best to run this in a virtual environment, so if virtualenv is not installed already:
```bash
sudo apt-get install python-virtualenv
```

In the app directory setup and activate the virtualenv
```bash
virtualenv unilagapi
source unilagapi/bin/activate
```

Then install the dependencies
```bash
pip install -r requirements.txt
```


Run the initial migration (very crude stuff, calling it migrations is a lool event)
```bash
python migrate.py
```

Populate the database via the cron script
```bash
python cron.py
```

And start the gunicorn server (remebeer to make sure all the entries in the `.env` file have been filled out)
```bash
./unilagapi/bin/gunicorn -c gunicorn_config.py wsgi
```

That's all

