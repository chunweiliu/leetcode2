"""Find the longest absoluted file path given a string representation of files

    << "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

    >> "dir/subdir2/subsubdir2/file2.ext"
    => 32

    - Not a graph problem (cannot do it in O(n))
    - Use number of \t to determine the structure
    - Use a dict to store the {length: string} hash

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        root_path_length = {0: 0}

        # str.split('\n')
        for line in input.splitlines():
            # Take off all leading chars that in '\t'
            name = line.lstrip('\t')

            # len('\t') = 1 in coding, also, it will be transform to '/'
            num_tabs = len(line) - len(name)

            # If it is a file
            if '.' in name:
                max_length = max(max_length, root_path_length[num_tabs] + len(name))

            # Else it is a dir. We don't preserve every root_path_length.
            # It will be overide next time for the next subfolder in the same depth.
            else:
                root_path_length[num_tabs + 1] = root_path_length[num_tabs] + len(name) + 1  # 1 for '/'

        return max_length

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print Solution().lengthLongestPath(input)
