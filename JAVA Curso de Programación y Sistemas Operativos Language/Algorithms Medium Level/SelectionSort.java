import java.util.Random;

public class SelectionSort {
    public static void main(String[] args) {
      int n = 10; // number of integers to generate and sort
    int[] arr = new int[n];
    Random rand = new Random();

      // generate random integers between 1 and 100 and store them in the array
    for (int i = 0; i < n; i++) {
    arr[i] = rand.nextInt(100) + 1;
    }

      // print the unsorted array
    System.out.println("Unsorted Array:");
    for (int i = 0; i < n; i++) {
    System.out.print(arr[i] + " ");
    }
    System.out.println();

      // sort the array using selection sort
    for (int i = 0; i < n - 1; i++) {
    int minIdx = i;
    for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
    }
         // swap arr[i] with arr[minIdx]
    int temp = arr[i];
    arr[i] = arr[minIdx];
    arr[minIdx] = temp;
    }

      // print the sorted array
    System.out.println("Sorted Array:");
    for (int i = 0; i < n; i++) {
    System.out.print(arr[i] + " ");
    }
    System.out.println();
    }
}
