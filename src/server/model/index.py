from collections import defaultdict
from typing import Any, Dict, Iterable, Set, Tuple, Union


class Graph:
    """Mathematical representation of a network which describes the relationship between lines and points
    """

    def __init__(self, **kwargs: Any):
        """Create a new graph

        Keyword Arguments:
            **kwargs {Any} -- Graph data to be assigned
        """
        self.graph = dict(kwargs)
        self.__adj = defaultdict(dict)
        self.__vertices = defaultdict(dict)

    @property
    def name(self) -> str:
        """String identifier of graph

        Returns:
            str -- String identifier of graph, defaulted to an empty string
        """
        return self.graph.get("name", "")

    @name.setter
    def name(self, name: str):
        """Set the string identifier of graph

        Arguments:
            name {str} -- New string identifier of graph
        """
        self.graph["name"] = name

    # TODO: Fix

    @property
    def directed(self) -> bool:
        """Directed value of graph

        Returns:
            bool -- True if the directed value of graph is truthy, False otherwise
        """
        return bool(self.graph.get("directed", True))

    @directed.setter
    def directed(self, directed: bool) -> None:
        """Set the directed value of graph

        Arguments:
            directed {bool} -- New directed value of graph
        """
        self.graph["directed"] = directed

    def add_edge(self, u: Any, v: Any, **kwargs: Any) -> None:
        """Add edge to graph

        Arguments:
            u, v {Any} -- Vertices to be connected by edge

        Keyword Arguments:
            **kwargs {Any} -- Edge data to be assigned
        """
        ...

    def add_edges_from(self, iter: Iterable[Union[Tuple[Any, Any]], Tuple[Any, Any, Any]], **kwargs: Any):
        """Add edges to graph

        Arguments:
            iter {Iterable[Union[Tuple[Any, Any]], Tuple[Any, Any, Any]]} -- Edges and edge data to be added

        Keyword Arguments:
            **kwargs {Any} -- Edge data to be assigned
        """
        ...

    def add_vertex(self, v: Any, **kwargs: Any) -> None:
        """Add vertex to graph

        Arguments:
            v {Any} -- Vertex to be added

        Keyword Arguments:
            **kwargs {Any} -- Edge data to be assigned
        """
        self.__adj[v]
        self.__vertices[v].update(kwargs)

    def add_vertices_from(self, iter: Iterable[Union[Any], Tuple[Any, Any]], **kwargs: Any):
        """Add vertices to graph

        Arguments:
            iter {Iterable[Union[Any], Tuple[Any, Any]]} -- Vertices and vertex data to be added

        Keyword Arguments:
            **kwargs {Any} -- Vertex data to be assigned
        """
        ...

    def degree_of(self, v: Any) -> int:
        """Return the number of vertices connected from source vertex

        Arguments:
            vertex {Any} -- Source vertex to be evaluated

        Returns:
            int -- Degree of source vertex
        """
        ...

    def edges_of(self, vertex: Any) -> Set[Any]:
        ...

    def get_all_edges(self, u: Any, v: Any) -> Set[Any]:
        ...

    def get_edges(self, u: Any, v: Any) -> Any:
        ...

    def is_adjacent(self, u: Any, v: Any) -> bool:
        """Return if v is connected from u

        Arguments:
            u {Any} -- Source vertex to be evaluated
            v {Any} -- Target vertex to be evaluated

        Returns:
            bool -- True if v is connected from u, False otherwise
        """
        ...

    def __contains__(self, v: Any) -> bool:
        """Return whether graph contains vertex

        Arguments:
            vertex {Any} -- Vertex to be evaluated

        Returns:
            bool -- True if graph contains edge, False otherwise
        """
        return v in self.__adj

    def __getitem__(self, v: Any) -> Dict[Any]:
        """Return the edge target vertex mapping from source vertex

        Arguments:
            v {Any} -- Source vertex to be evaluated

        Returns:
            Dict[Any] -- Edge target vertex mapping from source vertex
        """
        return self.__adj[v]

    def __setitem__(self, v, **kwargs):
        ...
