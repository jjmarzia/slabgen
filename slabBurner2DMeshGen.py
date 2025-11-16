# this simple python script is used to generate a 2D hex mesh for the specified slab burner geometry
import math
import sys

import gmsh
import argparse


# function to convert the specified locations to gMsh points
def convert_to_point(locations):
    if type(locations) is list:
        points = []
        for location in locations:
            points.append(gmsh.model.geo.add_point(location[0], location[1], 0.0))
        return points
    else:
        return gmsh.model.geo.add_point(locations[0], locations[1], 0.0)


# the sideList is a list of sides
def define_boundary(sides, name, boundary_list):
    line_ids = []
    # march over and add each side
    for side in sides:
        line_ids.append(gmsh.model.geo.add_bspline(side))

    # define the boundary condition for this
    tag_id = gmsh.model.geo.addPhysicalGroup(1, line_ids)
    gmsh.model.setPhysicalName(1, tag_id, name)

    if boundary_list is not None:
        boundary_list.extend(line_ids)


# Initialize gmsh:
gmsh.initialize()

# define the experimental chamber points
lowerLeft = convert_to_point((0.0, 0.0))
upperLeft = convert_to_point((0.0, 0.025))
lowerRight = convert_to_point((0.1, 0.0))
upperRight = convert_to_point((0.1, 0.025))

# define a list of points for the slab burner, starting with the left most point
import numpy as np

slabBoundaryLocations = [
(0.014000, 0.0000000000000000),
(0.014500, 0.0004545454545455),
(0.015000, 0.0009090909090909),
(0.015500, 0.0013636363636364),
(0.016000, 0.0018181818181818),
(0.016500, 0.0022727272727273),
(0.017000, 0.0027272727272727),
(0.017500, 0.0031818181818182),
(0.018000, 0.0036363636363636),
(0.018500, 0.0040909090909091),
(0.019000, 0.0045454545454545),
(0.019500, 0.0050000000000000),
(0.020000, 0.0054545454545455),
(0.020500, 0.0059090909090909),
(0.021000, 0.0063636363636364),
(0.021500, 0.0068181818181818),
(0.022000, 0.0072727272727273),
(0.022500, 0.0077272727272727),
(0.023000, 0.0081818181818182),
(0.023500, 0.0086363636363636),
(0.024000, 0.0090909090909091),
(0.024500, 0.0095454545454545),
(0.025000, 0.0100000000000000),
(0.025500, 0.01),
(0.026000, 0.01),
(0.026500, 0.01),
(0.027000, 0.01),
(0.027500, 0.01),
(0.028000, 0.01),
(0.028500, 0.01),
(0.029000, 0.01),
(0.029500, 0.01),
(0.030000, 0.01),
(0.030500, 0.01),
(0.031000, 0.01),
(0.031500, 0.01),
(0.032000, 0.01),
(0.032500, 0.01),
(0.033000, 0.01),
(0.033500, 0.01),
(0.034000, 0.01),
(0.034500, 0.01),
(0.035000, 0.01),
(0.035500, 0.01),
(0.036000, 0.01),
(0.036500, 0.01),
(0.037000, 0.01),
(0.037500, 0.01),
(0.038000, 0.01),
(0.038500, 0.01),
(0.039000, 0.01),
(0.039500, 0.01),
(0.040000, 0.01),
(0.040500, 0.01),
(0.041000, 0.01),
(0.041500, 0.01),
(0.042000, 0.01),
(0.042500, 0.01),
(0.043000, 0.01),
(0.043500, 0.01),
(0.044000, 0.01),
(0.044500, 0.01),
(0.045000, 0.01),
(0.045500, 0.01),
(0.046000, 0.01),
(0.046500, 0.01),
(0.047000, 0.01),
(0.047500, 0.01),
(0.048000, 0.01),
(0.048500, 0.01),
(0.049000, 0.01),
(0.049500, 0.01),
(0.050000, 0.01),
(0.050500, 0.01),
(0.051000, 0.01),
(0.051500, 0.01),
(0.052000, 0.01),
(0.052500, 0.01),
(0.053000, 0.01),
(0.053500, 0.01),
(0.054000, 0.01),
(0.054500, 0.01),
(0.055000, 0.01),
(0.055500, 0.01),
(0.056000, 0.01),
(0.056500, 0.01),
(0.057000, 0.01),
(0.057500, 0.01),
(0.058000, 0.01),
(0.058500, 0.01),
(0.059000, 0.01),
(0.059500, 0.01),
(0.060000, 0.01),
(0.060500, 0.01),
(0.061000, 0.01),
(0.061500, 0.01),
(0.062000, 0.01),
(0.062500, 0.01),
(0.063000, 0.01),
(0.063500, 0.01),
(0.064000, 0.01),
(0.064500, 0.01),
(0.065000, 0.01),
(0.065500, 0.01),
(0.066000, 0.01),
(0.066500, 0.01),
(0.067000, 0.01),
(0.067500, 0.01),
(0.068000, 0.01),
(0.068500, 0.01),
(0.069000, 0.01),
(0.069500, 0.01),
(0.07, 0.010000),
(0.07, 0.009500),
(0.07, 0.009000),
(0.07, 0.008500),
(0.07, 0.008000),
(0.07, 0.007500),
(0.07, 0.007000),
(0.07, 0.006500),
(0.07, 0.006000),
(0.07, 0.005500),
(0.07, 0.005000),
(0.07, 0.004500),
(0.07, 0.004000),
(0.07, 0.003500),
(0.07, 0.003000),
(0.07, 0.002500),
(0.07, 0.002000),
(0.07, 0.001500),
(0.07, 0.001000),
(0.07, 0.000500),
(0.07, 0.000000)
]

# convert the locations to points
slabBoundary = convert_to_point(slabBoundaryLocations)

# define the chamber boundary with associated names, define the nodes in a counterclockwise order
boundary_ids = []
define_boundary([[upperLeft, lowerLeft]], "inlet", boundary_ids)
define_boundary([[upperRight, lowerRight]], "outlet", boundary_ids)
define_boundary([
    [upperRight, upperLeft],
    [lowerLeft, slabBoundary[0]],
    [slabBoundary[-1], lowerRight]
], "wall", boundary_ids)
define_boundary([slabBoundary], "slab", boundary_ids)

# define the curve and resulting plane
curve_id = gmsh.model.geo.add_curve_loop(boundary_ids, reorient=True)
surface_id = gmsh.model.geo.add_plane_surface([curve_id])
gmsh.model.setPhysicalName(2, gmsh.model.geo.addPhysicalGroup(2, [surface_id]), "main")

# Create the relevant Gmsh data structures from Gmsh model.
gmsh.model.geo.synchronize()

# set the default properties to generate quad mesh
gmsh.option.setNumber("Mesh.Algorithm", 11)  # 11: Quasi-structured Quad
gmsh.option.setNumber("Mesh.Algorithm3D", 1)  # 1: Delaunay
gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 3)  # 3: blossom full-quad

# gmsh.option.setNumber("Mesh.MeshSizeMin", 0.0005)
# gmsh.option.setNumber("Mesh.MeshSizeMax", 0.0008)  # with the other options this results in about 0.6 mm element size


gmsh.option.setNumber("Mesh.MeshSizeMin", 0.0005)
gmsh.option.setNumber("Mesh.MeshSizeMax", 0.0008)  # with the other options this results in about 0.6 mm element size

gmsh.option.setNumber("Mesh.SubdivisionAlgorithm", 1)  # 1: all quadrangles
gmsh.option.setNumber("Mesh.RecombineAll", 1)  # true

# set the options to prevent gmsh from adding too many elements to each geometry line
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.Smoothing", 10)

# generate the mesh
gmsh.model.mesh.setRecombine(2, surface_id)
gmsh.model.mesh.generate(2)

# parse input arguments
parser = argparse.ArgumentParser(
    description='Generates 2D slabBurner Hex Mesh')
parser.add_argument('--preview', dest='preview', action='store_true',
                    help='If true, preview mesh instead of saving', default=False)
parser.add_argument('--summary', dest='summary', action='store_true',
                    help='If true, computes the element summary', default=False)
args = parser.parse_args()

if args.summary:
    # print a summary of mesh information
    elements = gmsh.model.mesh.getElements(2)
    print(f'Number Elements: {len(elements[1][0])}')
    minDistance = 1E30
    maxDistance = 0
    for ele_tag in elements[1][0]:
        element = gmsh.model.mesh.getElement(ele_tag)
        node_ids = element[1]
        number_nodes = len(node_ids)
        for n in range(number_nodes):
            node_n = gmsh.model.mesh.get_node(node_ids[n])[0]
            for nn in range(n + 1, number_nodes):
                node_nn = gmsh.model.mesh.get_node(node_ids[nn])[0]
                distance = math.sqrt(
                    (node_n[0] - node_nn[0]) ** 2 + (node_n[1] - node_nn[1]) ** 2 + (node_n[2] - node_nn[2]) ** 2)
                minDistance = min(minDistance, distance)
                maxDistance = max(maxDistance, distance)
    print(f'Min/Max Distance: {minDistance}/{maxDistance}')

if args.preview:
    # Creates  graphical user interface
    if 'close' not in sys.argv:
        gmsh.fltk.run()
else:
    # # Write mesh data:
    gmsh.write("/Users/jjmarzia/Desktop/ablate2/python/slabBurner2DMesh.msh")

# It finalizes the Gmsh API
gmsh.finalize()
