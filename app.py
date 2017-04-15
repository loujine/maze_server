import os
from flask import Flask, Response, request, abort, url_for, redirect
from resources import CellResource, ExitResource, RootResource

import maze


app = Flask(__name__, static_url_path='')

# Route and views

@app.route('/', methods=["GET"])
def root():
    return RootResource().response_for(request)

@app.route('/cells/999/<direction>', methods=["GET"])
def exit(direction='north'):
    return ExitResource().response_for(request)

@app.route('/cells/<int:cell_num>/<direction>', methods=["GET"])
def cell(cell_num, direction):
    resource = CellResource()
    resource.cell_num = cell_num
    resource.direction = direction
    resp = resource.response_for(request)
    links = maze.get_links_for_cell(resource.cell_num)
    resp.headers.add_header('Link',
                            u', '.join('<%s>; rel="%s"' % (v,k)
                                       for (k,v) in links.items()))
    return resp

@app.route('/static/<image>', methods=["GET"])
def media(image):
    return redirect(url_for('static', filename=image))


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
