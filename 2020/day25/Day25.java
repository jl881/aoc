

public class Day25 {

    public void calculate() {
        long door_pk = 18356117;
        long card_pk = 5909654;
//        long door_pk = 17807724;
//        long card_pk = 5764801;
        long card_loop_size = find_loop_size(card_pk);
        System.out.println(card_loop_size);
        long encryption = power(door_pk, card_loop_size);
        System.out.println(encryption);
    }


    public long power(long base, long exponent) {
        long value = 1;
        for (int i = 0; i< exponent; i++) {
            value = (value*base)%20201227;
        }
        return value;
    }

    public long find_loop_size(long pk) {
        long try_size = 0;
        long value = 1;
        while (value != pk) {
            value = (value*7)%20201227;
            try_size += 1;
        }
        return try_size;

    }

    public static void main(String[] args) {
        Day25 day25 = new Day25();
        day25.calculate();
    }
}
