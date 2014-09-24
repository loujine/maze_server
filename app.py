import os
from flask import Flask, Response, request, abort
from resources import CellResource, ExitResource, RootResource

app = Flask(__name__)

# Route and views

@app.route('/', methods=["GET"])
def root():
    return RootResource().response_for(request)

@app.route('/cells/999', methods=["GET"])
def exit():
    return ExitResource().response_for(request)

@app.route('/cells/<int:cell_num>', methods=["GET"])
def cell(cell_num):
    resource = CellResource()
    resource.cell_num = cell_num
    return resource.response_for(request)

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
