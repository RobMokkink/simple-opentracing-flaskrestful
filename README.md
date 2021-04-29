# simple-opentracing-flaskrestful
This is a very simple example of a flask-restful app with opentracing.
It is just for demo/testing, the code is not optimal

# Podman
I done this with podman and not with docker!

# Start the containers
start the jaeger container as described in https://opentracing.io/guides/python/quickstart/, be sure to add ```--network=host```
build and start the flask container, be sure to add ```--network=host```

# Testing
Do some curl, like ```curl localhost:5000/todo/todo1 -d "data=Rember the milk" -X PUT``` and ```curl localhost:5000/todo/todo1```
Check the output in jaeger
