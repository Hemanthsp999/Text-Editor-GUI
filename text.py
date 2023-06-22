import tkinter as tk


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TextEditorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create a linked list to store the text
        self.head = None
        self.tail = None
        self.cursor = None

        # Create the text input field
        self.text_input = tk.Text(self.root)
        self.text_input.pack()

        # Bind key events to their respective functions
        self.text_input.bind('<Key>', self.handle_keypress)
        self.text_input.bind('<Left>', self.move_cursor_left)
        self.text_input.bind('<Right>', self.move_cursor_right)
        self.text_input.bind('<BackSpace>', self.delete_character)

    def handle_keypress(self, event):
        # Insert the typed character at the cursor position
        character = event.char
        self.insert_character(character)

    def insert_character(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node
        else:
            if self.cursor is None:
                self.tail.next = new_node
                self.tail = new_node
                self.cursor = new_node
            else:
                new_node.next = self.cursor.next
                self.cursor.next = new_node
                self.cursor = new_node

    def delete_character(self, event):
        if self.cursor is None:
            return

        if self.cursor == self.head:
            self.head = self.head.next
            self.cursor = self.head
        else:
            temp = self.cursor
            prev_node = self.get_previous_node()
            prev_node.next = self.cursor.next
            self.cursor = prev_node
            if temp == self.tail:
                self.tail = self.cursor

    def move_cursor_left(self, event):
        if self.cursor is None:
            return
        current = self.head
        while current.next != self.cursor:
            current = current.next
        self.cursor = current

    def move_cursor_right(self, event):
        if self.cursor is not None:
            self.cursor = self.cursor.next

    def get_previous_node(self):
        current = self.head
        while current.next != self.cursor:
            current = current.next
        return current

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditorGUI(root)
    editor.run()
