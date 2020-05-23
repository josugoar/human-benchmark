import random
from functools import singledispatch
from typing import Any, Iterable, Optional, Tuple, Set, Union


class Edge:
    """Link between two vertices
    """

    def __init__(self, source_vertex: "Vertex", target_vertex: "Vertex", directed: bool = False, weight: float = 0.) -> None:
        """Create edge

        Arguments:
            source_vertex {Vertex}
            target_vertex {Vertex}

        Keyword Arguments:
            directed {bool} -- (default: {True})
            weight {float} -- (default: {0.})
        """
        assert source_vertex and target_vertex, "Vertices must not be None..."
        self.source_vertex = source_vertex
        self.target_vertex = target_vertex
        self.__directed = directed
        self.set_weight(weight)

    def vertex_from(self, source_vertex: "Vertex") -> Optional["Vertex"]:
        """Return target vertex linked from source vertex by edge

        Arguments:
            source_vertex {Vertex}

        Returns:
            Optional[Vertex]
        """
        if source_vertex is self.source_vertex:
            return self.target_vertex
        elif source_vertex is self.target_vertex and not self.__directed:
            return self.source_vertex

    def is_directed(self) -> bool:
        """Return if edge is directed

        Returns:
            bool
        """
        return self.__directed

    def get_weight(self) -> float:
        """Return weight of edge

        Returns:
            float
        """
        return self.__weight

    def set_weight(self, weight: float) -> None:
        """Set weight of edge

        Arguments:
            weight {float}
        """
        self.__weight = weight

    def __contains__(self, vertex: "Vertex") -> bool:
        """Return if vertex is linked by edge

        Arguments:
            vertex {Vertex} -- Vertex to evaluate

        Returns:
            bool
        """
        return vertex in tuple(self.source_vertex, self.target_vertex)

    def __str__(self) -> str:
        """Return edge attribute summary

        Returns:
            str
        """
        return f"Edge (source_vertex: [{self.source_vertex}], target_vertex: [{self.target_vertex}], directed: [{self.__directed}], weight: [{self.__weight}])"


class Vertex:
    """Intersection point of a graph
    """

    def __init__(self, value: Optional[Any] = None) -> None:
        """Create vertex

        Keyword Arguments:
            value {Optional[Any]} -- (default: {None})
        """
        self.__edges = set()
        self.set_value(value)

    def add_edge(self, edge: "Edge") -> None:
        """Add edge to vertex

        Arguments:
            edge {Edge}

        Raises:
            AssertionError: if not edge.vertex_from(self)
        """
        vertex_from = edge.vertex_from(self)
        assert vertex_from, "Edge must be connected from vertex..."
        self.__edges.add(edge)
        if not edge.is_directed():
            vertex_from.__edges.add(edge)

    def remove_edge(self, edge: "Edge") -> None:
        """Remove edge from vertex

        Arguments:
            edge {Edge}
        """
        self.__edges.remove(edge)
        edge.vertex_from(self).__edges.remove_edge(edge)

    def get_edges(self) -> Set["Vertex"]:
        """Return edge set

        Returns:
            Set[Vertex]
        """
        return self.__edges

    def get_value(self) -> Optional[Any]:
        """Return value of vertex

        Returns:
            Optional[Any]
        """
        return self.__value

    def set_value(self, value: Optional[Any]) -> None:
        """Set value of vertex

        Arguments:
            value {[type]}
        """
        self.__value = value

    def __contains__(self, edge: "Edge") -> bool:
        """Return if edge is contained in vertex

        Arguments:
            edge {Edge} -- Edge to evaluate

        Returns:
            bool
        """
        return edge in self.__edges

    def __iter__(self) -> Iterable:
        """Return iterable of edges in vertex

        Returns:
            Iterable
        """
        return iter(self.__edges)

    def __str__(self) -> str:
        """Return vertex attribute summary

        Returns:
            str
        """
        return f"Vertex (edge_count: [{len(self.__edges)}], value: [{self.__value}])"


class Graph:
    """Mathematical representation of a network which describes the relationship between lines and points
    """

    def __init__(self, root: Optional["Vertex"] = None) -> None:
        """Create graph

        Keyword Arguments:
            root {Optional[Vertex]} -- (default: {None})
        """
        self.__edges = set()
        self.__vertices = set()
        if root:
            self.add_vertex(root)
        self.set_root(root)

    def add_edge(self, edge: "Edge") -> None:
        """Add edge to graph

        Arguments:
            edge {Edge}

        Raises:
            AssertionError: if not (edge.source_vertex in self and edge.target_vertex in self)
        """
        assert edge.source_vertex in self and edge.target_vertex in self, "Vertices connected by edge must belong to graph..."
        edge.source_vertex.add_edge(edge)
        self.__edges.add(edge)

    def add_vertex(self, vertex: "Vertex") -> None:
        """Add vertex to graph

        Arguments:
            vertex {Vertex}

        Raises:
            AssertionError: if edge.traverse(vertex) not in self
        """
        for edge in vertex:
            assert edge.vertex_from(vertex) in self, "Vertices connected by edge from vertex must belong to graph..."
        self.__vertices.add(vertex)

    # TODO: Fix
    def remove_edge(self, edge: "Edge") -> None:
        """Remove vertex from graph

        Arguments:
            edge {edge}
        """
        if edge in self:
            edge.source_vertex.remove_edge(edge)
        self.__edges.remove(edge)

    def remove_vertex(self, vertex: "Vertex") -> None:
        """Remove vertex from graph

        Arguments:
            vertex {Vertex}
        """
        if vertex in self:
            for edge in vertex:
                edge.vertex_from(vertex).remove_edge(edge)
        self.__vertices.remove(vertex)

    def set_root(self, root: Optional["Vertex"]) -> None:
        """Set vertex root of graph

        Arguments:
            root {Optional[Vertex]}

        Raises:
            AssertionError: if root not in self
        """
        if root:
            assert root in self, "Vertex root must belong to graph..."
        self.__root = root

    # TODO: Fix
    @singledispatch
    def __contains__(self, edge: "Edge") -> bool:
        """Return if edge is contained in graph

        Arguments:
            edge {Edge} -- Edge to evaluate

        Returns:
            bool
        """
        return True

    @__contains__.register
    def __contains__(self, vertex: "Vertex") -> bool:
        """Return if vertex is contained in graph

        Arguments:
            vertex {Vertex} -- Vertex to evaluate

        Returns:
            bool
        """
        return vertex in self.__vertices

    def __iter__(self) -> Iterable:
        return iter(self.__vertices)

    def __str__(self) -> str:
        return f"Graph (vertex_count: [{len(self.__vertices)}])"


# ============================ Test ============================
G = Graph()
V = [Vertex(i) for i in range(5)]
E = [Edge(random.choice(V), random.choice(V), directed=False)
     for i in range(5)]
for v in V:
    G.add_vertex(v)
for e in E:
    G.add_edge(e)

for e in E:
    print(e)
for v in G:
    print(v)
