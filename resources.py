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
        resource.meta.attributes.add("type", type_of)
        return resource

class RootResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='item')
        resource.links.add(rel='start', href=maze.link_to_cell(0), label="Start")
        return resource

class ExitResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='completed')
        resource.links.add(rel='start', href=maze.link_to_cell(0), label="Start")
        return resource

class CellResource(MazeResource):

    def read(self, request):
        resource = self.maze_resource(type_of='cell')
        if not maze.has_cell(self.cell_num):
            abort(404)
        links = maze.get_links_for_cell(self.cell_num)
        for rel, link in links.iteritems():
            resource.links.add(rel=rel, href=link, label=maze.labels[rel])
        return resource
