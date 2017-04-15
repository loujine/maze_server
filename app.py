import os
from flask import Flask, Response, request, abort
from resources import CellResource, ExitResource, RootResource

app = Flask(__name__)

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
    return resp

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
