from UM.View.Renderer import Renderer
from UM.Scene.SceneNode import SceneNode
from UM.Application import Application
from UM.Resources import Resources
from UM.Mesh.MeshData import MeshData
from UM.Mesh.MeshBuilder import MeshBuilder
from UM.Math.Vector import Vector
from UM.Math.Color import Color

import numpy

class BuildVolume(SceneNode):
    VolumeOutlineColor = Color(140, 170, 240, 255)

    def __init__(self, parent = None):
        super().__init__(parent)

        self._width = 0
        self._height = 0
        self._depth = 0

        self._material = None

        self._grid_mesh = None
        self._grid_material = None

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def setDepth(self, depth):
        self._depth = depth

    def render(self, renderer):
        if not self.getMeshData():
            return True

        if not self._material:
            self._material = renderer.createMaterial(
                Resources.getPath(Resources.ShadersLocation, 'basic.vert'),
                Resources.getPath(Resources.ShadersLocation, 'vertexcolor.frag')
            )
            self._grid_material = renderer.createMaterial(
                Resources.getPath(Resources.ShadersLocation, 'basic.vert'),
                Resources.getPath(Resources.ShadersLocation, 'grid.frag')
            )
            self._grid_material.setUniformValue('u_gridColor0', Color(255, 255, 255, 255))
            self._grid_material.setUniformValue('u_gridColor1', Color(140, 170, 240, 255))

        renderer.queueNode(self, material = self._material, mode = Renderer.RenderLines)
        renderer.queueNode(self, mesh = self._grid_mesh, material = self._grid_material)
        return True

    def rebuild(self):
        if self._width == 0 or self._height == 0 or self._depth == 0:
            return

        minW = -self._width / 2
        maxW = self._width / 2
        minH = 0.0
        maxH = self._height
        minD = -self._depth / 2
        maxD = self._depth / 2

        mb = MeshBuilder()

        mb.addLine(Vector(minW, minH, minD), Vector(maxW, minH, minD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(minW, minH, minD), Vector(minW, maxH, minD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(minW, maxH, minD), Vector(maxW, maxH, minD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(maxW, minH, minD), Vector(maxW, maxH, minD), color = self.VolumeOutlineColor)

        mb.addLine(Vector(minW, minH, maxD), Vector(maxW, minH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(minW, minH, maxD), Vector(minW, maxH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(minW, maxH, maxD), Vector(maxW, maxH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(maxW, minH, maxD), Vector(maxW, maxH, maxD), color = self.VolumeOutlineColor)

        mb.addLine(Vector(minW, minH, minD), Vector(minW, minH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(maxW, minH, minD), Vector(maxW, minH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(minW, maxH, minD), Vector(minW, maxH, maxD), color = self.VolumeOutlineColor)
        mb.addLine(Vector(maxW, maxH, minD), Vector(maxW, maxH, maxD), color = self.VolumeOutlineColor)

        self.setMeshData(mb.getData())

        mb = MeshBuilder()
        mb.addQuad(
            Vector(minW, minH, maxD),
            Vector(maxW, minH, maxD),
            Vector(maxW, minH, minD),
            Vector(minW, minH, minD)
        )
        self._grid_mesh = mb.getData()
        for n in range(0, 6):
            v = self._grid_mesh.getVertex(n)
            self._grid_mesh.setVertexUVCoordinates(n, v[0], v[2])
