import java.util.Scanner;

public class AverageCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count;

        System.out.print("Enter the number of values: ");
        count = scanner.nextInt();

        int sum = 0;
        for (int i = 1; i <= count; i++) {
            System.out.print("Enter number " + i + ": ");
            sum += scanner.nextInt();
        }

        double average = (double) sum / count;
        System.out.println("The average is: " + average);
    }
}
