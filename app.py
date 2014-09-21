import os
from flask import Flask, Response, request, abort
from hypermedia_resource import HypermediaResource
from hypermedia_resource.contrib.browser import BrowserAdapter
from hypermedia_resource.wrappers import HypermediaResponse, ResponseBuilder
import maze

app = Flask(__name__)
HypermediaResource.adapters.add(BrowserAdapter)

# Helper functions for the views

def maze_resource(type_of):
    """
    Sets up a HypermediaResource for the resource
    """
    resource = HypermediaResource()
    resource.meta.attributes.add("title", "Hypermedia Maze")
    resource.meta.attributes.add("type", type_of)
    return resource

def maze_response(resource):
    """
    Build a HypermediaResponse
    """
    response_builder = ResponseBuilder("application/vnd.amundsen.maze+xml")
    response = response_builder.build(resource, request.headers.get("Accept"))
    return Response(response.body, mimetype=response.media_type)

# Route and views

@app.route('/', methods=["GET"])
def root():
    """
    Root resource
    """
    resource = maze_resource(type_of='item')
    resource.links.add(rel='start', href=maze.link_to_cell(0), label="Start")
    return maze_response(resource)

@app.route('/cells/999', methods=["GET"])
def exit():
    """
    Exit resource
    """
    resource = maze_resource(type_of='completed')
    resource.links.add(rel='start', href=maze.link_to_cell(0), label="Start")
    return maze_response(resource)

@app.route('/cells/<cell_num>', methods=["GET"])
def cell(cell_num):
    """
    Cell resource
    """
    resource = maze_resource(type_of='cell')
    if not maze.has_cell(cell_num):
        abort(404)
    links = maze.get_links_for_cell(int(cell_num))
    for rel, link in links.iteritems():
        resource.links.add(rel=rel, href=link, label=maze.labels[rel])
    return maze_response(resource)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
