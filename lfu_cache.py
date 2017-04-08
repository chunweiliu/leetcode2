"""Least Frequently Used (LFU) cache

    http://dhruvbird.com/lfu.pdf
    * Double linked-list
        - Good to delete someone in the middle
    * Hash table
        - Good to find anyone in the list

    * Evicts the key with least access (both in put and set) frequency
    * LRU evicts the key that is not recently used

    LFUCache cache = new LFUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.get(3);       // returns 3.
    cache.put(4, 4);    // evicts key 1.
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4

Time: 
    - get O(1)
    - put O(1)

Space: O(n)
"""
class FreqNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.items = set()
        self.prev = prev if prev else self
        self.next = next if next else self

        # self.head = None
        # self.tail = None


class LFUItem:
    def __init__(self, key, data, parent, prev=None, next=None):
        self.key = key

        # In our setting this will be the value
        self.data = data

        # parent points to the frequency node
        self.parent = parent

        # self.prev = prev if prev else self 
        # self.next = next if next else self


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.bykey = {}
        self.freq_head = FreqNode()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.bykey.get(key)

        if not node:
            return

        self.update_freq(node)
        return node.data

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if len(self.bykey) == self.capacity:
        #     # Delete the last node
        #     last = self.get_lfu_item()
        #     delete_node(last)

        # Add the node
        node = self.bykey.get(key)

        if not node:
            # Add new key, value
            freq = self.freq_head.next

            if freq.value != 1:
                freq = FreqNode(1, self.freq_head, freq)

            freq.items.add(key)
            self.bykey[key] = LFUItem(key, value, freq)
        else:
            # Update exist
            freq = self.node.parent
            self.bykey[key] = LFUItem(key, value, freq.value + 1)
            self.update_freq(node)

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def update_freq(self, node):
        freq = node.parent
        next_freq = freq.next

        if next_freq is self.freq_head or \
           (next_freq and next_freq.value != freq.value + 1):
            next_freq = FreqNode(freq.value + 1, freq, next_freq)

        next_freq.items.add(node.key)
        node.parent = next_freq

        freq.items.remove(node.key)
        if len(freq.items) == 0:
            self.delete_node(freq)

    # def get_lfu_item(self):
    #     if len(self.bykey) == 0:
    #         return
    #     return self.freq_head.next.tail

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)