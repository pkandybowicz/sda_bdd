public class Example2 {

    static String rS(String input){

        char[] temparray = input.toCharArray();
        int left, right=0;
        right = temparray.length-1;

        for (left=0; left < right ; left++ ,right--)
        {
            // Swap values of left and right
            char temp = temparray[left];
            temparray[left] = temparray[right];
            temparray[right]=temp;
        }
        return new String(temparray);

    }
}
