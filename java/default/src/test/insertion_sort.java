package test;

public class insertion_sort {
	public void insertionSort(int[] data) {
		int len = data.length;
		int min, temp;
		for (int i = 0; i < len; i ++) {
			min = i;
			for (int j = i; j < len; j ++) {
				if (data[min] > data[j])
					min = j;
			}
			
			temp = data[i];
			data[i] = data[min];
			data[min] = temp;
		}
		
	}
	
	public static void main(String[] args) {
		int[] test = {66,10,1,99,5};
		insertion_sort selection = new insertion_sort();
		selection.insertionSort(test);
		
		for (int e: test) {
			System.out.print(e + " ");
		}
		
		
		
	}
}
