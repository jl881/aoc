public class SinglyLinkedList {
    public Node head;
    public Node tail;

    // remove and return head
    public Node popFirst() {
        Node temp = head;
        this.head = head.next;
        return temp;
    }

    //append to end
    public void append(int data) {
        Node newNode = new Node(data,null);
        append(newNode);
    }

    public void append(Node node) {
        if (this.head != null) {
            node.next = null;
            this.tail.next = node;
        } else {
            this.head = node;
        }
        this.tail = node;
    }

    //insert three values after a particular value
    public void insertThree(Node left, Node[] values) {
        Node one = values[0];
        Node three = values[2];

        Node right = left.next;
        left.next = one;
        three.next = right;
        if (right == null) {
            this.tail = three;
        }
    }
}