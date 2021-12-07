import json 
import csv
import networkx as nx
import os, sys

def test(nodefile,edgefile,jsonfile ):
    """ from "data/ETL.ipynb"

    Create 2 random/binomial/Erdős-Rényi graph and a unified fully connected graph.

    Parameters
        - int n : number of nodes in
        - int k : edge creation coefficient

    Return
        - Graph G :
        - Graph g1 :
        - Graph g2 :

    """

    # open json file
    with open(jsonfile, 'r') as jsfile:
        # open csv file
        with open(nodefile, 'w+') as nodefiled:
            # open csv file
            with open(edgefile, 'w+') as edgefiled:
                
                # write the data in csv
                node = csv.writer(nodefiled)
                edge = csv.writer(edgefiled)
      
                
                # write the data in csv
                node.writerow(["# NodeID", "Lat", " Lon", "Layer"])
                edge.writerow(["# EdgeID", "Source NodeID", "Target NodeID", "Direction", "Layer"])
            
                
                for line in jsfile:
                    
                    # load line 
                    print(line)
                    jsentry = json.loads(line)
                    
                    
                    if jsentry['properties']['type'] == "node":
                        node.writerow([
                                jsentry['_id']['$oid'], 
                                jsentry['geometry']['coordinates'][0], 
                                jsentry['geometry']['coordinates'][1], 
                                jsentry['properties']['layer']])
                        
                    if jsentry['properties']['type'] == "edge":
                        if jsentry['properties']['name'].startswith("54"):
                            jsentry['properties']['name'] = "None"
                        if 'direction' in jsentry['properties']:
                            if jsentry['properties']['direction'] == "Double sens":
                                direction = "TwoWay"
                            elif (jsentry['properties']['direction'] == "Sens inverse" 
                                  or jsentry['properties']['direction'] == "Sens unique"):
                                direction = "OneWay"

                            edge.writerow([
                                jsentry['properties']['mongo_org_id'],
                                jsentry['properties']['mongo_dest_id'],
                                jsentry['_id']['$oid'], 
                                direction,
                                jsentry['properties']['layer'], 
                                jsentry['properties']['name']])
                        
                        else:
                            edge.writerow([
                                jsentry['properties']['mongo_org_id'],
                                jsentry['properties']['mongo_dest_id'],
                                jsentry['_id']['$oid'],
                                "TwoWay",
                                jsentry['properties']['layer'], 
                                jsentry['properties']['name']])
    return node, edge                  


def nodeSetting(G, layer=1):
    """ Generate (x,y,z) coordinates, Node ID and Attribute Setting for cascade methods

    (x,y) coordinates follow the networkx spring layout.
    z coordinates(Layer) is given as a parameter 'layer'
    Save (x,y,z) coordinates as an attribute of node named '3D_pos'
    This information is used for drawing interdependent graph

    Parameters
    ----------
    G : Network Graph
    layer : Layer of this graph
    
    """
    # Node Attribute '3D_pos' added
    G = nx.DiGraph()

    with open(nodefile, 'r') as node:
        reader = csv.reader(node)
        next(reader)
        for row in reader:
            lat = row[1]
            lon = row[2]
            ntype = row[3]
            G.add_node(row[0], lat=lat, lon=lon, type=ntype)

    with open(edgefile, 'r') as node:
        reader = csv.reader(node)
        next(reader)
        for row in reader:
            G.add_edge(row[1], row[2], type=row[4], name=row[5])
            if row[3] == 'TwoWay':
                G.add_edge(row[2], row[1], type=row[4], name=row[5])

    nx.write_graphml(G, graphmlfile)
    nx.write_graphml(G, gmlfile)

def Paris_NodeSetting (G,df_vertex,Layer_num=1):

    attrs = {}
    _ = {}
    for data in df_vertex.values:
        _ = {}
        _['Lat'] = data[1]
        _['Lon'] = data[2]
        _['Layer'] = Layer_num
        _['3D_pos'] = np.array([_['Lat'],_['Lon'],Layer_num])
        attrs[data[0]] = _
    nx.set_node_attributes(G,attrs)

    return G

def ParisTranspNetwork (vertex_csv, edge_csv, LayerName):
    df_vertex = pd.read_csv(vertex_csv)
    df_edge = pd.read_csv(edge_csv)

    transp_vertex = df_vertex['Layer']==LayerName
    transp_edge = df_edge['Layer']==LayerName

    df_vertex_transp = df_vertex[transp_vertex]
    df_edge_transp = df_edge[transp_edge]

    G = nx.from_pandas_edgelist(df_edge_transp, '# Source NodeID','Target NodeID',['Layer','name'])
    
    return G, df_vertex_transp, df_edge_transp
