import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Example2Test {

    @Test
    void test_rS() {
        String a = "abcdefg";
        String b = Example2.rS(a);
        System.out.println(a);
        System.out.println(b);
        assertEquals("gfedcba", b);
    }
}