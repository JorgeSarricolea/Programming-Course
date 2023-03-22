/* Create a program that takes in a vector of integers and checks if it is a palindrome. A vector is a palindrome if it reads the same forwards and backwards. 
The program should print out whether or not the vector is a palindrome. */

import java.util.*;

public class PalindromeVector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the vector: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the vector: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        boolean isPalindrome = true;
        for (int i = 0; i < n/2; i++) {
            if (arr[i] != arr[n-1-i]) {
                isPalindrome = false;
                break;
            }
        }
        if (isPalindrome) {
            System.out.println("The vector is a palindrome");
        } else {
            System.out.println("The vector is not a palindrome");
        }
        sc.close();
    }
}
