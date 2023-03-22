import java.util.*;

public class RemoveDuplicates {
    public static void main(String[] args) {
        // Create a vector of integers
        Vector<Integer> numbers = new Vector<Integer>();

        // Add some integers to the vector
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(2);
        numbers.add(4);
        numbers.add(5);
        numbers.add(3);
        numbers.add(5);
        numbers.add(5);
        numbers.add(5);

        // Print out the original vector
        System.out.println("Original vector: " + numbers);

        // Create a new vector to store the unique elements
        Vector<Integer> uniqueNumbers = new Vector<Integer>();

        // Loop through the original vector and add unique elements to the new vector
        for (int number : numbers) {
            if (!uniqueNumbers.contains(number)) {
                uniqueNumbers.add(number);
            }
        }

        // Print out the new vector with duplicates removed
        System.out.println("Vector with duplicates removed: " + uniqueNumbers);
    }
}
