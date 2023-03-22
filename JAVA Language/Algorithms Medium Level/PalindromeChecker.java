import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        if (isPalindrome(input)) {
            System.out.println("The input string is a palindrome.");
        } else {
            System.out.println("The input string is not a palindrome.");
        }
        sc.close();
    }

    public static boolean isPalindrome(String str) {
        str = str.replaceAll("\\W", "").toLowerCase(); // remove non-word characters and convert to lowercase
        StringBuilder reversedStr = new StringBuilder(str).reverse(); // reverse the string
        return str.equals(reversedStr.toString()); // compare the original and reversed string
    }
}
