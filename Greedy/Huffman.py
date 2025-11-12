import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman(freq):
    heap = []

    for ch, fr in freq.items():
        heapq.heappush(heap, Node(ch, fr))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]
    codes = dict()

    def generate(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code
            return

        generate(node.left, code + "0")
        generate(node.right, code + "1")

    generate(root, "")
    return codes

freq = {'a' : 5, 'b' : 9, 'c' : 12, 'd' : 13, 'e' : 16, 'f' : 45}
codes = huffman(freq)

for ch in codes:
    print(ch, codes[ch])

