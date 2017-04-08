class Solution(object):
    def __init__(self):
        self.triangle = []
        self.triangle.append([1])
        self.triangle.append([1, 1])

    def generate(self, num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]

        Example:
        i
        0          1
        1        1   1
        2      1   2   1
        3    1   3   3   1

           j 0   1   2   3
        """
        while len(self.triangle) < num_rows:
            last_row = self.triangle[-1]
            self.triangle.append(
                [1] + \
                [last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)] + \
                [1])
        return self.triangle[:num_rows]
