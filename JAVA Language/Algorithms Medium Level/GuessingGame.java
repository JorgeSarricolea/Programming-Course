import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int generatedNumber = random.nextInt(100) + 1; // Generate a random number between 1 and 100
        int attemptsLeft = 10;

        System.out.println("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.");

        while (attemptsLeft > 0) {
            System.out.print("Guess #" + (11 - attemptsLeft) + ": ");
            int guess = scanner.nextInt();

            if (guess == generatedNumber) {
                System.out.println("Congratulations! You guessed the number in " + (11 - attemptsLeft) + " attempts.");
                return;
            } else if (guess < generatedNumber) {
                System.out.println("Your guess is too low.");
            } else {
                System.out.println("Your guess is too high.");
            }

            attemptsLeft--;
        }
        System.out.println("Sorry, you didn't guess the number. The number was " + generatedNumber + ".");
        scanner.close();
    }
}

