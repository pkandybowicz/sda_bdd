import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PersonTest2 {

    Person person;

    @BeforeEach
    void setUp() {
        person = new Person("Anna", "Kowalska");
    }

    @Test
    void testGetDisplayName() {
//        Person person = new Person("Anna", "Kowalska");
        String personName = person.getDisplayName();
        assertEquals("Kowalska, Anna", personName);
    }

    @Test
    void testSetDefaultAge() {
//        Person person = new Person("Jan", "Kowalski");
        int personAge = person.getAge();
        assertEquals(18, personAge);
    }

    @Test
    void testSetAge() {
//        Person person = new Person("Jan", "Nowak");
        person.setAge(49);
        assertEquals(49, person.getAge());
    }

    @Test
    void testSetAgeWithYearInput() {
//        Person person = new Person("Ola", "Zima");
        person.setAge(1987);
        assertEquals(32, person.getAge());
    }


    @Test
    void setJobToRandomOne() {
//        Person person = new Person("Marcin", "Brzozka");
        person.setJobToRandomOne();
        List<String> jobs = Arrays.asList("Developer", "Tester", "Budowlaniec", "Sprzątaczka", "Premier");
        assertTrue(jobs.contains(person.getJob()));
    }
}