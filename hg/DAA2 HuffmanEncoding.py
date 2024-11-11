class Node:
    def __init__(self, left=None, right=None, value=None, frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency

    def children(self):
        return (self.left, self.right)


class Huffman_Encoding:
    def __init__(self, string):
        self.q = []
        self.string = string
        self.encoding = {}

    def char_frequency(self):
        count = {}
        for char in self.string:
            if char not in count:
                count[char] = 0
            count[char] += 1

        for char, value in count.items():
            node = Node(value=char, frequency=value)
            self.q.append(node)
        self.q.sort(key=lambda x: x.frequency)

    def build_tree(self):
        while len(self.q) > 1:
            n1 = self.q.pop(0)
            n2 = self.q.pop(0)
            node = Node(left=n1, right=n2, frequency=n1.frequency + n2.frequency)
            self.q.append(node)
            self.q.sort(key=lambda x: x.frequency)
            # Print the frequency of the newly created internal node
            print("Created internal node with frequency:", node.frequency)

    def helper(self, node: Node, binary_str=""):
        if isinstance(node.value, str):  # Leaf node
            self.encoding[node.value] = binary_str
            return
        l, r = node.children()
        self.helper(node.left, binary_str + "0")
        self.helper(node.right, binary_str + "1")

    def huffman_encoding(self):
        root = self.q[0]
        self.helper(root, "")

    def print_encoding(self):
        print(' Char | Huffman code ')
        for char, binary in self.encoding.items():
            print(" %-4r |%12s" % (char, binary))

    def encode(self):
        self.char_frequency()
        self.build_tree()
        self.huffman_encoding()
        self.print_encoding()


string = input("Enter string to be encoded: ")
# string = 'AAAAAAABBCCCCCCDDDEEEEEEEEE'
encode = Huffman_Encoding(string)
encode.encode()


"""
1. Node Class
The Node class represents each node in the Huffman Tree, which can be either:

A leaf node (contains a character and its frequency).
An internal node (formed by merging two nodes with the smallest frequencies).
Attributes:

left and right: References to the left and right child nodes.
value: Stores the character (only for leaf nodes).
frequency: Stores the frequency of the character (or combined frequency for internal nodes).
Methods:

children(): Returns the left and right children, useful for tree traversal.
2. Huffman_Encoding Class
This class is where the Huffman encoding process takes place. It builds a tree based on character frequencies and then generates the binary codes.

Key Attributes:
self.q: A list to hold nodes, acting as a priority queue (sorted by frequency).
self.string: The input string to be encoded.
self.encoding: A dictionary where each character’s Huffman code will be stored.
Key Methods:
char_frequency(self)
This method calculates the frequency of each character in self.string:

A dictionary count is used to store each character's frequency.
For each unique character, a Node is created with its frequency and appended to self.q.
self.q is then sorted by frequency, preparing it for the tree-building process.
build_tree(self)
This method builds the Huffman Tree by repeatedly combining the two nodes with the smallest frequencies:

While self.q has more than one node:
The two nodes with the smallest frequencies (n1 and n2) are popped from self.q.
A new internal Node is created with n1 and n2 as its left and right children.
The frequency of this internal node is the sum of n1 and n2's frequencies.
The new internal node is appended to self.q, which is then re-sorted by frequency.
The line print("Created internal node with frequency:", node.frequency) prints each intermediate frequency, showing the internal node creation process.
helper(self, node, binary_str="")
This recursive helper function assigns binary codes to each character by traversing the Huffman Tree:

If the node is a leaf (has a character in node.value), it adds an entry to self.encoding with the character and binary_str.
For each internal node:
It recursively calls itself with the left child and binary_str + "0", indicating a "0" in the binary code.
Similarly, it calls itself with the right child and binary_str + "1", indicating a "1".
This generates unique binary codes based on the path from the root to each leaf.

huffman_encoding(self)
This method initiates the encoding by calling helper() on the root node, which is now the only element in self.q after building the tree.

print_encoding(self)
This method displays the character and its corresponding Huffman code, stored in self.encoding, in a formatted table.

encode(self)
This method is the main function to execute the Huffman encoding process:

Calls char_frequency() to compute character frequencies.
Calls build_tree() to build the Huffman Tree.
Calls huffman_encoding() to generate the Huffman codes.
Calls print_encoding() to display the final codes.
"""
