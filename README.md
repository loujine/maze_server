Hypermedia Maze Server
----------------------

This is an example project to show a server using the [HypermediaResource Python library](https://github.com/the-hypermedia-project/hypermedia-resource-python). It uses the `HypermediaResource` class to represent resources, and it uses the `HypermediaResponse` class to create responses based on content negotiation.

## Overview

The Hypermedia Resource library is used to support several different media types. It also includes a browser adapter that provides a simple HTML representation for the API, making it accessible in the browser. This method allows you to specify the hypermedia elements in general way, separate from hypermedia formats. Once the `resource` has been populated with the data, it can then be translated to any supported format.

The Hypermedia Resource library also provides a resource builder, which allows content negotiation to decide to which format the resource should be translated. This allows you as a developer to provide an `Accept` header and a resource to the response builder, and it will respond with the appropriate representation.

## Install

```script
pip install -r requirements.txt
```

## Run Server

The server will run at localhost on port 5000.

```script
python app.py
```

## Heroku

For pushing to Heroku, you need an environment variable set for the base IRI. Change the variable below to match your app. Important: leave off the trailing slash.

```script
heroku config:add BASE_IRI=http://maze-server.herokuapp.com
```