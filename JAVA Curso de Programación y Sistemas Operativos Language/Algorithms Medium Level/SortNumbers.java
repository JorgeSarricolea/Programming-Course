import java.util.*;

public class SortNumbers {

    public static void main(String[] args) {
        // Prompt the user to enter a list of numbers
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a list of integers separated by commas: ");
        String input = scanner.nextLine();

        // Convert the input string to an array of integers
        String[] stringArray = input.split(",");
        int[] numbers = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {
            numbers[i] = Integer.parseInt(stringArray[i].trim());
        }

        // Sort the array of integers
        Arrays.sort(numbers);

        // Print the sorted list of integers
        System.out.print("Sorted list of integers: ");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
    }
}
