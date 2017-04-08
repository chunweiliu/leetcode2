"""Paint the houses with min cost, such that no two adjacent houses have the same color.

DP
    0 1 1 1 colors
    1 0 1 1
    1 1 0 1
    
Time: O(nk)

- Preserve the entire cost for every colors
Space: O(k)

- Only store the cost for the minimum and the second minimum colors 
Space: O(1)
"""

class Solution(object):
    def minCostII(self, costs):
        if not costs or not costs[0]:
            return 0
            
        min_spend = costs[0]
        for cost_for_colors in costs[1:]:

            spent = min_spend[:]
            for i, cost in enumerate(cost_for_colors):
                
                # spent[:i] + spent[i+1:] is empty when only one cost_for_colors,
                # but if that is a cast, we cannot paint anyway.
                min_spend[i] = cost + min(spent[:i] + spent[i + 1:])

        return min(min_spend)


    def minCostIIConstSpace(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        # Color for min cost
        # Why use a list? We need to preserve the previous when updating the current
        color = [-1, -1]

        first = [0, 0]
        second = [0, 0]

        prev, curr = 0, 1
        for i, colors in enumerate(costs):
            first[curr] = second[curr] = 0x7FFFFFFF
            
            # To test color j, we have choose j
            for j, cost in enumerate(colors):
                accumulated = cost
                accumulated += first[prev] if color[prev] != j else second[prev]

                # Update the first and second minimum
                if accumulated < first[curr]:
                    first[curr], second[curr] = accumulated, first[curr]
                    color[curr] = j
                elif accumulated < second[curr]:
                    second[curr] = accumulated

            # Reuse this two variables
            curr, prev = prev, curr

        # After the swap in the last step, prev is the actual current we want.
        return first[prev]
