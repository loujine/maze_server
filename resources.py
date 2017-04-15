from flask import abort
from representor import Representor
from representor.contrib.browser import BrowserAdapter
from representor.contrib.maze_xml import MazeXMLAdapter
from representor.wrappers import FlaskAPIResource
import maze

Representor.adapters.add(BrowserAdapter)
Representor.adapters.add(MazeXMLAdapter)

class MazeResource(FlaskAPIResource):

    def maze_resource(self, type_of):
        """
        Sets up a Representor for the resource
        """
        resource = Representor()
        resource.meta.attributes.add("title", "Hypermedia Maze")
        if type_of == "cell":
            resource.attributes.add("Room:", self.cell_num)
            resource.attributes.add("Direction:", maze.labels[self.direction])
        if type_of == "item":
            resource.attributes.add("Choose your way", "")
        resource.meta.attributes.add("type", type_of)
        return resource

class RootResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='item')
        resource.links.add(rel='start', href=maze.link_to_cell(0, 'north'), label="Start")
        return resource

class ExitResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='completed')
        resource.attributes.add('Congratulations!', 'You exited the maze')
        resource.links.add(rel='start', href=maze.link_to_cell(0, 'north'), label="Restart")
        return resource

class CellResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='cell')
        if not maze.has_cell(self.cell_num):
            abort(404)
        links = maze.get_links_for_cell(self.cell_num)
        for rel, link in links.iteritems():
            resource.links.add(rel=rel, href=link, label=maze.labels[rel])
        directions = maze.directions[self.direction]
        doors = [directions[0] in links,
                 directions[1] in links or 'exit' in links,
                 directions[2] in links]
        resource.img = map(lambda x: "" if x else "no", doors)
        return resource
