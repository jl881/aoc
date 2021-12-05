import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day23 {

    private static final int numOfCups = 1000000;
    private static final int iterations = 10000000;

    private SinglyLinkedList linkedList = new SinglyLinkedList();
    private List<Node> lookup = new ArrayList<>();


    public void prepare() {
        int[] input = {1, 6, 7, 2, 4, 8, 3, 5, 9};
        Node[] temp = new Node[input.length + 1];
        for (int i = 1; i < input.length + 1; i++) {
            Node newNode = new Node(input[i-1]);
            linkedList.append(newNode);
            temp[input[i-1]] = newNode;
        }
        lookup.addAll(Arrays.asList(temp));
        for (int i = input.length + 1; i < numOfCups + 1; i++) {
            Node newNode = new Node(i);
            linkedList.append(newNode);
            lookup.add(newNode);
        }
    }

    public void play() {
        for (int i = 0; i < iterations; i++) {
            Node first = linkedList.popFirst();
            Node[] nextThree = new Node[3];
            for (int j = 0; j< 3; j++) {
                nextThree[j] = linkedList.popFirst();
            }
            int destValue = (first.data == 1) ? numOfCups : (first.data -1);
            while (destValue == nextThree[0].data || destValue == nextThree[1].data || destValue == nextThree[2].data) {
                destValue = (destValue == 1) ? numOfCups : (destValue -1);
            }

            Node destNode = lookup.get(destValue);
            linkedList.insertThree(destNode, nextThree);
            linkedList.append(first);
        }

        Node node1 = lookup.get(1);
        Node neighbour1 = (node1.next == null) ? linkedList.head : node1.next;
        Node neighbour2 = (neighbour1.next == null) ? linkedList.head : neighbour1.next;
        long n1 = neighbour1.data;
        long n2 = neighbour2.data;
        long product = n1*n2;
        System.out.println(product);

    }

    public static void main(String[] args) {
        Day23 day23 = new Day23();
        day23.prepare();
        day23.play();
    }
}
