import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Example2Test {

    @Test
    void test_rS() {
        String a = "abcdefg";
        String b = Example2.rS(a);
        assertEquals("gfedcba", b, "Our string is not reversed, Input was: " + a + " expected: gfedcb, but was: "+ b);
    }
}