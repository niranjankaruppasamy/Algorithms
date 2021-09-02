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
        ll.insertAtBeginning(10);
        ll.insertAtBeginning(20);
        ll.insertAtBeginning(30);
        ll.insertAtEnd(40);
        ll.printList();
    }
}
