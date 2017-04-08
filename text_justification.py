"""Text justification

    << ["This", "is", "an", "example", "of", "text", "justification."]

    => [
         "This    is    an",
         "example  of text",
         "justification.  "
       ]
       
    Round robin the white spaces.
    - The last line only append white space.
       
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        lines = []
        words_in_line = []
        num_chars = 0

        for word in words:
            # num_chars + num_spaces + the current word exceed max width, create a new line
            if num_chars + len(words_in_line) + len(word) > maxWidth:
                num_spaces = len(words_in_line) - 1 or 1

                # Seperate the remain spaces behind different words in line
                for i in range(maxWidth - num_chars):
                    words_in_line[i % num_spaces] += ' '

                lines.append(''.join(words_in_line))

                words_in_line = []
                num_chars = 0

            words_in_line.append(word)
            num_chars += len(word)

        # If the current line remain
        lines.append(' '.join(words_in_line).ljust(maxWidth))

        return lines