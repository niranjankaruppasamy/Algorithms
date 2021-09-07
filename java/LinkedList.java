class Node {
    public int data;
    public Node next = null;

    public Node(int val) {
        data = val;
    }

    public Node(int val, Node nextNode) {
        data = val;
        next = nextNode;
    }
}

class SinglyLinkedList {
    Node head = null;

    public void insertAtBeginning(int val) {
        if (this.head == null) {
            this.head = new Node(val);
        } else {
            Node node = new Node(val, this.head);
            this.head = node;
        }
    }

    public void insertAtEnd(int val) {
        Node curr = this.head;
        while (curr != null) {
            if (curr.next == null) {
                curr.next = new Node(val);
                break;
            }
            curr = curr.next;
        }
    }

    public int getLength() {
        int length = 0;
        Node node = this.head;
        while (node != null) {
            length += 1;
            node = node.next;
        }
        return length;
    }

    public void insertAtIndex(int val, int index) {
        int totalLength = getLength();
        if (index > totalLength) {
            throw new IndexOutOfBoundsException("Invalid index");
        }
        if (index == 0) {
            insertAtBeginning(val);
            return;
        }
        if (index == totalLength) {
            insertAtEnd(val);
            return;
        }
        int counter = 1;
        Node node = this.head.next;
        while (node != null) {
            if (counter == index - 1) {
                node.next = new Node(val, node.next);
                break;
            }
            node = node.next;
            ++counter;
        }
    }


    public void printList() {
        Node currentNode = this.head;
        String res = "";
        while (currentNode != null) {
            res = res + String.valueOf(currentNode.data) + "-->";
            currentNode = currentNode.next;
        }
        System.out.println(res);
    }
}

public class LinkedList {
    public static void main(String[] args) {
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.insertAtBeginning(30);
        ll.insertAtBeginning(20);
        ll.insertAtBeginning(10);
        ll.insertAtEnd(40);
        ll.insertAtIndex(50, 4);
        ll.insertAtIndex(45, 4);
        ll.printList();
    }
}
