package test;

public class Quick_Sort {
	 
    public static void main(String[] args) {
        
        int[] arr = { 10, 50, 80, 90, 70 };
        
        quick_Sort(arr, 0, arr.length - 1);
        output(arr);
    }
 
    private static void quick_Sort(int[] arr, int start, int end) {
        
        int left = start;
        int right = end;
        /*pivot을 중앙 값으로 셋팅*/
        int pivot = arr[(left + right) / 2];
 
        do {
            while (arr[left] < pivot) {
                left++;
            }
            while (arr[right] > pivot) {
                right--;
            }
 
            if (left <= right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
 
        } while (left <= right);
        
        output(arr);
        System.out.println("\n");
 
        if (start < right) {
            quick_Sort(arr, start, right);
 
        }
        if (end > left) {
            quick_Sort(arr, left, end);
        }
    }
 
    private static void output(int[] arr) {
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}

