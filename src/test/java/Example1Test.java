import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class Example1Test {

    @org.junit.jupiter.api.Test
    void test_bS() {
        int[] a = new int[]{1, 5, 2, 7, 9, 1, 7, 8, 1, 1, 5, 9, 0};
        int[] b = new int[]{0, 1, 1, 1, 1, 2, 5, 5, 7, 7, 8, 9, 0};
        Example1.bS(a);
        assertArrayEquals(a, b);
    }


}