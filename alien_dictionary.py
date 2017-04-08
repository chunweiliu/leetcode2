"""Find the order of an alien dictionary (Topological sort)

    << [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]

    => "wertf"

    In a Directed Acyclic Graph (DAG), any valid path that connects all nodes is
    a topological sort.

    1) Build the graph
    2) Find the path

Time: O(v + e)
Space: O(v + e)
"""
from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def has_cycle(s, visit, finish):
            if s in visit:
                return True

            # Don't repeat on finish node. Note that not return True either
            # because this is not a cycle.
            if s in finish:
                return False

            visit.add(s)

            for t in edges[s]:
                if has_cycle(t, visit, finish):
                    return True

            visit.remove(s)
            finish.add(s)            
            order.append(s)
            return False

        nodes = set()
        for word in words:
            for char in word:
                nodes.add(char)

        edges = defaultdict(list)
        for pair in zip(words, words[1:]):
            for s, t in zip(*pair):
                if s != t:
                    edges[s].append(t)
                    
                    # Break because we only need one order pair
                    break
                    
            # '' empty char should have higher order. 
            # Dictionary like ['wrtkj', 'wrt'] validates this assumption
            if s == t and len(pair[0]) > len(pair[1]):
                return ''

        order = []
        visit = set()
        finish = set()
        for node in nodes:
            if has_cycle(node, visit, finish):
                return ''
        return ''.join(order[::-1])

    
    def alienOrderInOut(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        order = []

        # Build the graph
        indegree = defaultdict(set)
        outdegree = defaultdict(set)

        # zip => [('wrt', 'wrf'), ('wrf', 'er'), ('er', 'ett'), ('ett', 'rftt')]
        for pair in zip(words, words[1:]):
            # zip => char comparison
            for s, t in zip(*pair):
                if s != t:
                    indegree[t].add(s)
                    outdegree[s].add(t)
                    
                    # We can only add one order for a pair
                    break
                    
            # '' empty char should have higher order. 
            # Dictionary like ['wrtkj', 'wrt'] validates this assumption
            if s == t and len(pair[0]) > len(pair[1]):
                return ''

        # Bug: If a node has no outdegree, it would not be considered.
        # outdegree_only = set(outdegree) - set(indegree)

        all_chars = {c for word in words for c in word}

        outdegree_only = all_chars - set(indegree)
        while outdegree_only:
            s = outdegree_only.pop()
            order += s

            # Take out any indegree contributed by this node
            for t in outdegree[s]:
                indegree[t].discard(s)
                if not indegree[t]:
                    outdegree_only.add(t)
                    del indegree[t]

        if set(order) == all_chars:
            return ''.join(order)
        return ''
