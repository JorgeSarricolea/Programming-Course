/* Find the maximum value in a vector. */

import java.util.Vector;

public class VectorMaxValue {
    public static void main(String[] args) {
        Vector<Integer> vector = new Vector<Integer>();
        vector.add(10);
        vector.add(20);
        vector.add(30);
        vector.add(40);
        vector.add(50);

        int max = vector.get(0);

        for (int i = 1; i < vector.size(); i++) {
            if (vector.get(i) > max) {
                max = vector.get(i);
            }
        }

        System.out.println("Maximum value in the vector: " + max);
    }
}
