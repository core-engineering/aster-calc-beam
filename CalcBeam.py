# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/media/Calculs/aster-calc-beam')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(2000, 0, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Compound_1 = geompy.MakeCompound([Line_1])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Compound_1, geompy.ShapeType["VERTEX"])
HEB360 = geompy.CreateGroup(Compound_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(HEB360, [2])
Fixed = geompy.CreateGroup(Compound_1, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Fixed, [3])
Force = geompy.CreateGroup(Compound_1, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Force, [4])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Compound_1, 'Compound_1' )
geompy.addToStudyInFather( Compound_1, HEB360, 'HEB360' )
geompy.addToStudyInFather( Compound_1, Fixed, 'Fixed' )
geompy.addToStudyInFather( Compound_1, Force, 'Force' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Compound_1)
Regular_1D = Mesh_1.Segment()
Max_Size_1 = Regular_1D.MaxSize(20)
isDone = Mesh_1.Compute()
HEB360_1 = Mesh_1.GroupOnGeom(HEB360,'HEB360',SMESH.EDGE)
Fixed_1 = Mesh_1.GroupOnGeom(Fixed,'Fixed',SMESH.NODE)
HEB360_2 = Mesh_1.GroupOnGeom(HEB360,'HEB360',SMESH.NODE)
Force_1 = Mesh_1.GroupOnGeom(Force,'Force',SMESH.NODE)
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/media/Calculs/aster-calc-beam/CalcBeam.med', 1, SMESH.MED_V2_2, 1, Mesh_1, 0, [], 'ev' )
except:
  print 'ExportPartToMED() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Max_Size_1, 'Max Size_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(HEB360_1, 'HEB360')
smesh.SetName(HEB360_2, 'HEB360')
smesh.SetName(Force_1, 'Force')
smesh.SetName(Fixed_1, 'Fixed')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
