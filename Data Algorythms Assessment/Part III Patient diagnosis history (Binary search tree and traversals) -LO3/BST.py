import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def find_min(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.key

    def find_max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.key

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_recursive(node.right, min_larger_node.key)
        return node

    def _min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return max(self._height(node.left), self._height(node.right)) + 1

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

    def level_order(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def visualize(self):
        if self.root is None:
            print("Tree is empty")
            return
        
        graph = nx.DiGraph()
        self._build_graph(self.root, graph)
        pos = self._get_positions(self.root, x=0, y=0, level=0, pos={}, width=2)
        
        plt.figure(figsize=(8, 6))
        nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, edge_color="gray")
        plt.title("Binary Search Tree Visualization")
        plt.show()

    def _build_graph(self, node, graph):
        if node is None:
            return
        if node.left:
            graph.add_edge(node.key, node.left.key)
            self._build_graph(node.left, graph)
        if node.right:
            graph.add_edge(node.key, node.right.key)
            self._build_graph(node.right, graph)

    def _get_positions(self, node, x, y, level, pos, width):
        if node is not None:
            pos[node.key] = (x, -y)
            offset = width / (2 ** (level + 1))
            self._get_positions(node.left, x - offset, y + 1, level + 1, pos, width)
            self._get_positions(node.right, x + offset, y + 1, level + 1, pos, width)
        return pos
    
    # TRAVERSALS VISUALIZATION
    # THIS CODE AFTER RAN SHOWS EACH NODE STEP FOR EVERY TRAVERSAL METHOD SEPERATELY

    def visualize_traversal(self, traversal):
        if self.root is None:
            print("Tree is empty")
            return

        graph = nx.DiGraph()
        self._build_graph(self.root, graph)
        pos = self._get_positions(self.root, x=0, y=0, level=0, pos={}, width=2)

        plt.ion()  # interactive mode ON
        fig, ax = plt.subplots(figsize=(8, 6))

        for i, node_key in enumerate(traversal):
            ax.clear()
            node_colors = ['red' if node == node_key else 'lightblue' for node in graph.nodes()]
            nx.draw(graph, pos, with_labels=True, node_size=1500,
                    node_color=node_colors, font_size=12, edge_color='gray', ax=ax)
            ax.set_title(f"Traversal Step {i+1}: Visiting Node {node_key}")
            plt.pause(1)  

        plt.ioff()  
        plt.show()

# RANDOM TEST
# Insert 10 random patient IDs between 1 and 100
import random

bst = BST()
patients = random.sample(range(1, 100), 10)
for p in patients:
    bst.insert(p)

print("Patient IDs inserted:", patients)
print("Inorder traversal:", bst.inorder())
print("Preorder traversal:", bst.preorder())
print("Postorder traversal:", bst.postorder())
print("Level-order traversal:", bst.level_order())


bst.visualize()
bst.visualize_traversal(bst.inorder())
bst.visualize_traversal(bst.preorder())
bst.visualize_traversal(bst.postorder())
bst.visualize_traversal(bst.level_order())