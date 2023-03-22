/* Program to calculate the sum of the first n integer numbers. */

import java.util.Scanner;

public class SumOfNIntegers {
    public static void main(String[] args) {
        int n, sum = 0;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a positive integer: ");
        n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            sum += i;
        }

        System.out.println("The sum of the first " + n + " integers is " + sum);

        scanner.close();
    }
}