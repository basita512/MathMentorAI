"""Semantic memory using knowledge graph for concept dependencies."""
import networkx as nx
from typing import List, Dict, Set, Optional
import json
from pathlib import Path

from src.utils.logger import get_logger

logger = get_logger()

class SemanticMemory:
    """
    Knowledge graph-based semantic memory.
    
    Tracks:
    - Concept dependencies (calculus requires algebra)
    - Related topics (integration ↔ differentiation)
    - Prerequisite chains for learning paths
    """
    
    def __init__(self, persist_path: str = "data/semantic_memory.json"):
        """Initialize knowledge graph."""
        self.graph = nx.DiGraph()
        self.persist_path = Path(persist_path)
        
        # Load existing graph if available
        if self.persist_path.exists():
            self.load()
        else:
            self._initialize_base_graph()
    
    def _initialize_base_graph(self):
        """Create base concept graph for JEE math."""
        # Core concepts
        concepts = {
            "arithmetic": {"level": 1, "category": "foundation"},
            "algebra": {"level": 2, "category": "foundation"},
            "trigonometry": {"level": 2, "category": "foundation"},
            "geometry": {"level": 2, "category": "foundation"},
            "coordinate_geometry": {"level": 2, "category": "foundation"},
            "calculus": {"level": 3, "category": "advanced"},
            "probability": {"level": 3, "category": "advanced"},
            "statistics": {"level": 3, "category": "advanced"},
            "linear_algebra": {"level": 3, "category": "advanced"},
            "vectors": {"level": 3, "category": "advanced"},
            "3d_geometry": {"level": 3, "category": "advanced"},
        }
        
        # Add nodes
        for concept, attrs in concepts.items():
            self.graph.add_node(concept, **attrs)
        
        # Add prerequisite edges
        prerequisite_edges = [
            ("arithmetic", "algebra"),
            ("algebra", "calculus"),
            ("algebra", "linear_algebra"),
            ("trigonometry", "calculus"),
            ("arithmetic", "probability"),
            ("probability", "statistics"),
            ("algebra", "coordinate_geometry"),
            ("coordinate_geometry", "vectors"),
            ("geometry", "coordinate_geometry"),
            ("geometry", "3d_geometry"),
            ("vectors", "3d_geometry"),
        ]
        
        for prereq, concept in prerequisite_edges:
            self.graph.add_edge(prereq, concept, relation="prerequisite")
        
        # Add related edges
        related_edges = [
            ("calculus", "geometry", "application"),
            ("probability", "calculus", "related"),
            ("vectors", "linear_algebra", "related"),
            ("coordinate_geometry", "3d_geometry", "extension"),
            ("statistics", "probability", "application"),
        ]
        
        for c1, c2, rel in related_edges:
            self.graph.add_edge(c1, c2, relation=rel)
        
        logger.info(f"Initialized knowledge graph with {len(self.graph.nodes)} concepts")
    
    def add_concept(self, concept: str, level: int, category: str, prerequisites: List[str] = None):
        """Add a new concept to the graph."""
        self.graph.add_node(concept, level=level, category=category)
        
        if prerequisites:
            for prereq in prerequisites:
                if prereq in self.graph:
                    self.graph.add_edge(prereq, concept, relation="prerequisite")
        
        logger.info(f"Added concept: {concept}")
    
    def get_prerequisites(self, concept: str) -> List[str]:
        """Get all prerequisites for a concept."""
        if concept not in self.graph:
            return []
        
        # Get all ancestors (transitive prerequisites)
        prerequisites = list(nx.ancestors(self.graph, concept))
        return prerequisites
    
    def get_related_concepts(self, concept: str, max_distance: int = 2) -> List[Dict]:
        """
        Find related concepts within a certain graph distance.
        
        Returns:
            List of {concept, distance, relation_path}
        """
        if concept not in self.graph:
            return []
        
        related = []
        
        # BFS to find nearby concepts
        for node in self.graph.nodes():
            if node == concept:
                continue
            
            try:
                # Check shortest path
                path = nx.shortest_path(self.graph.to_undirected(), concept, node)
                distance = len(path) - 1
                
                if distance <= max_distance:
                    related.append({
                        "concept": node,
                        "distance": distance,
                        "path": path
                    })
            except nx.NetworkXNoPath:
                continue
        
        return sorted(related, key=lambda x: x["distance"])
    
    def suggest_learning_path(self, target_concept: str) -> List[str]:
        """Suggest an ordered learning path to reach target concept."""
        if target_concept not in self.graph:
            return []
        
        prerequisites = self.get_prerequisites(target_concept)
        
        # Filter for prerequisite edges only to avoid cycles from 'related' edges
        prereq_graph = nx.DiGraph()
        prereq_graph.add_nodes_from(prerequisites + [target_concept])
        
        for u, v, data in self.graph.edges(prerequisites + [target_concept], data=True):
            if data.get("relation") == "prerequisite":
                if u in prereq_graph and v in prereq_graph:
                    prereq_graph.add_edge(u, v)
        
        try:
            learning_path = list(nx.topological_sort(prereq_graph))
            return learning_path
        except (nx.NetworkXError, nx.NetworkXUnfeasible):
            logger.warning(f"Cycle detected or error in learning path for {target_concept}")
            return prerequisites + [target_concept]
    
    def save(self):
        """Persist graph to disk."""
        data = {
            "nodes": [
                {"id": node, **self.graph.nodes[node]}
                for node in self.graph.nodes()
            ],
            "edges": [
                {"source": u, "target": v, **self.graph.edges[u, v]}
                for u, v in self.graph.edges()
            ]
        }
        
        self.persist_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.persist_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved semantic memory to {self.persist_path}")
    
    def load(self):
        """Load graph from disk."""
        with open(self.persist_path, 'r') as f:
            data = json.load(f)
        
        # Rebuild graph
        self.graph = nx.DiGraph()
        
        for node in data["nodes"]:
            node_id = node.pop("id")
            self.graph.add_node(node_id, **node)
        
        for edge in data["edges"]:
            source = edge.pop("source")
            target = edge.pop("target")
            self.graph.add_edge(source, target, **edge)
        
        logger.info(f"Loaded semantic memory with {len(self.graph.nodes)} concepts")
    
    def get_concept_info(self, concept: str) -> Optional[Dict]:
        """Get full information about a concept."""
        if concept not in self.graph:
            return None
        
        return {
            "concept": concept,
            **self.graph.nodes[concept],
            "prerequisites": self.get_prerequisites(concept),
            "related": [r["concept"] for r in self.get_related_concepts(concept)],
            "learning_path": self.suggest_learning_path(concept)
        }
    
    def get_graph_stats(self) -> Dict:
        """Get statistics about the knowledge graph."""
        return {
            "total_concepts": len(self.graph.nodes),
            "total_relationships": len(self.graph.edges),
            "foundation_concepts": len([n for n, d in self.graph.nodes(data=True) if d.get("category") == "foundation"]),
            "advanced_concepts": len([n for n, d in self.graph.nodes(data=True) if d.get("category") == "advanced"]),
            "max_depth": max(d.get("level", 1) for n, d in self.graph.nodes(data=True)) if self.graph.nodes else 0
        }

# Global instance
semantic_memory = SemanticMemory()
