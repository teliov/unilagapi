## UNILAG API

This is web app simply scrapes the [unilag website](http://new.unilag.edu.ng) for news and stores quick details (slug, link, title, etc) about the news in a database. This is done via the cron script. Ideally should be run every hour

It provides endpoints for retrieving the saved news items

This is part of a series of learning excercises ultimately targeted at building a front-end web app with vue.js

The `.env.sample` file containts the keys for the .env file. To run this ensure that the proper values are supplied