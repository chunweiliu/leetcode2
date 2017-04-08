"""Given tickets in [from, to] format, find the valid itinerary

    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

    * Is cycle OK?
      - Yes!
      - Cannot use a typical topological sort, but the idea is similar
      - Just remeber traverse larger lexicon order first

      0 ->- 1 ->- 2 ->- 3
              ->- a

    - Eulerian path
      - DFS given the available tickets
      - When we stock in some place, finish that route and add the final airport to the order
      - Back to the previous airport and see if we can go to another routes

Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return tickets

        from_to = defaultdict(list)

        # Make sure the order in list is reverse
        # {'JFK': 'SFO', 'ATL'}
        for a, b in sorted(tickets, reverse=True):
            from_to[a].append(b)

        def visit(airport):
            # While we have tickets from this airport to other, go through all of them
            while from_to[airport]:
                visit(from_to[airport].pop())
            order.append(airport)

        order = []
        visit('JFK')
        return order[::-1]
