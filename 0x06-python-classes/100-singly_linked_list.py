#!/usr/bin/python3
"""Singly Linked Lists module.
This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.
"""


class Node:
    """This class allows you to create and manipulate Node objects."""

    def __init__(self, data, next_node=None):
        """Initialize a new Square
        Args:
            data (int): data for node
            next_node(Node): pointer to None or Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """method that prints the entire list in stdout,
            one node number by line."""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)
