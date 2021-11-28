[![DOI](https://zenodo.org/badge/77233450.svg)](https://zenodo.org/badge/latestdoi/77233450)

# Paris Multilayer Transport Network

This repository contains the multimodal transportation network of [Ile-de-France](https://en.wikipedia.org/wiki/%C3%8Ele-de-France),  it's modelled by graph layers corresponding each to a different transportation mode, interconnected together into a multilayer graph. The graph of the transport networks is provided under various format: graphml, gml, edge and vertex files format. The network is composed of three layers: the road network, [the train network](https://en.wikipedia.org/wiki/R%C3%A9seau_Express_R%C3%A9gional) is a hybrid commuter rapid transit system in France serving Paris and its suburbs and the [subway network](https://en.wikipedia.org/wiki/Paris_M%C3%A9tro). To build this graph, multiple geospatial datasets, namely the road network from the [French National Geographic Institute (IGN)](http://www.ign.fr/) and the rail transport network (train and metro) from [OpenStreetMap (OSM)](https://www.openstreetmap.org/#map=5/51.500/-0.100) were aggregated. Each node in the graph is either a road intersection, a rail station or a metro station. A key feature of the proposed multimodal transportation network is its modelling of transitions between different transport modes during a given trip. Cross-layer transition modelling is ensured by adding cross-layer edge between layers.

### Summary table
|         | #Node  | #Edge  | Reference |
|---------|-------:|-------:|:---------:|
| Subway  | 303    | 356    | OSM       |
| Train   | 241    | 244    | OSM       |
| Road    | 14798  | 22276  | IGN       |


Please reference the following papers when using with this data:

_F. Asgari , A. Sultan , H. Xiong , V. Gauthier, , M. A. El-Yacoubi_, "**[CT-Mapper: Mapping sparse multimodal cellular trajectories using a multilayer transportation network](http://dx.doi.org/10.1016/j.comcom.2016.04.014)**", in Computer Communications SI on Mobile Traffic Analytics, vol. 95, 2016. DOI: [10.1016/j.comcom.2016.04.014](http://dx.doi.org/10.1016/j.comcom.2016.04.014)

## Vertices and edges properties
### Vertices properties
#### Lat, Lon
The latitude and the longitude formated to the standard coordinate system [WSG 84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84).

#### Layer
This filed could only takes four following values

1. road
2. train
3. metro

### Edges properties
#### Name
The name could be:

1. road name
2. Subway line name
3. Train line name

#### Direction
This filed could only takes two followings values:

1. TwoWay
2. OneWay

#### Layer
This filed could only takes four following values

1. road
2. train
3. metro
4. crosslayer
