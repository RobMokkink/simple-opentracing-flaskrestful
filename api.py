from flask import Flask, Response, request
from flask_restful import Resource, Api
from jaeger_client import Config
from flask_opentracing import FlaskTracer
import opentracing
import requests


# Constants
todos = {}

def init_tracer(service):
  config = Config(
      config={
          'sampler': {'type': 'const', 'param': 1}
      },
      service_name=service)
  return config.initialize_tracer()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class TodoSimple(Resource):

    def get(self, todo_id):
        with tracer.start_span('get-todo', child_of=parent_span) as span:
            span.set_tag("get_todo",todo_id) 
            return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        with tracer.start_span('put-todo', child_of=parent_span) as span:
            span.set_tag("put_todo",todo_id) 
            todos[todo_id] = request.form['data']
            span.set_tag("put_todo_data",request.form['data']) 
            return {todo_id: todos[todo_id]}

if __name__ == '__main__':

    # Create flask instance
    app = Flask(__name__)

    # Create Restful instance
    api = Api(app)

    # Set the opentracing configuration
    tracer = init_tracer('hello-world')

    # Add the tracer to the app
    flask_tracer = FlaskTracer(tracer, True, app)

    # Create parent span
    parent_span = flask_tracer.get_span()

    # Add default route to HelloWorld
    api.add_resource(HelloWorld, '/')

    # Add route /todo to TodoSimple
    api.add_resource(TodoSimple, '/todo/<string:todo_id>')

    # Start the flask app
    app.run(debug=False,host='0.0.0.0')
