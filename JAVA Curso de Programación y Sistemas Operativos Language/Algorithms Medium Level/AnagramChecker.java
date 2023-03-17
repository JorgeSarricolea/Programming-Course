import java.util.Arrays;
import java.util.Scanner;

public class AnagramChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the first string: ");
        String str1 = sc.nextLine();
        System.out.print("Enter the second string: ");
        String str2 = sc.nextLine();
        sc.close();

        if (isAnagram(str1, str2)) {
            System.out.println("The strings are anagrams");
        } else {
            System.out.println("The strings are not anagrams");
        }
    }

    public static boolean isAnagram(String str1, String str2) {
        char[] charArray1 = str1.replaceAll("[\\s]", "").toCharArray();
        char[] charArray2 = str2.replaceAll("[\\s]", "").toCharArray();

        if (charArray1.length != charArray2.length) {
            return false;
        }

        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        return Arrays.equals(charArray1, charArray2);
    }
}