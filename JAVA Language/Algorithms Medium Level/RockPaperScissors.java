import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] choices = {"rock", "paper", "scissors"};

        System.out.println("Welcome to Rock, Paper, Scissors!");

        while (true) {
            System.out.print("Enter your choice (rock, paper, or scissors): ");
            String userChoice = sc.nextLine().toLowerCase();

            // Check if user's choice is valid
            if (!isValidChoice(userChoice)) {
                System.out.println("Invalid choice. Please enter rock, paper, or scissors.");
                continue;
            }

            // Generate a random choice for the computer
            String computerChoice = choices[(int) (Math.random() * choices.length)];

            // Print the choices
            System.out.println("You chose " + userChoice + ".");
            System.out.println("The computer chose " + computerChoice + ".");

            // Determine the winner
            int result = getResult(userChoice, computerChoice);
            if (result == 0) {
                System.out.println("It's a tie!");
            } else if (result == 1) {
                System.out.println("You win!");
            } else {
                System.out.println("The computer wins!");
            }

            // Ask if the user wants to play again
            System.out.print("Do you want to play again? (y/n): ");
            String playAgain = sc.nextLine().toLowerCase();
            if (!playAgain.equals("y")) {
                break;
            }
        }
    }

    // Check if a choice is valid
    public static boolean isValidChoice(String choice) {
        return choice.equals("rock") || choice.equals("paper") || choice.equals("scissors");
    }

    // Determine the winner
    public static int getResult(String userChoice, String computerChoice) {
        if (userChoice.equals(computerChoice)) {
            return 0; // Tie
        } else if (userChoice.equals("rock")) {
            return computerChoice.equals("scissors") ? 1 : -1; // User wins if computer chose scissors, otherwise computer wins
        } else if (userChoice.equals("paper")) {
            return computerChoice.equals("rock") ? 1 : -1; // User wins if computer chose rock, otherwise computer wins
        } else {
            return computerChoice.equals("paper") ? 1 : -1; // User wins if computer chose paper, otherwise computer wins
        }
    }
}
