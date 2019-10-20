import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Stepdefs {

    int[] arr;
    String stringReverse;
    Person person;

    @Given("Input array is: {int},{int},{int},{int},{int}")
    public void input_array_is(int one, int two, int three, int four, int five) {
        // Write code here that turns the phrase above into concrete actions
        arr = new int[]{one, two, three, four, five};
        System.out.println(arr);
    }

    @When("Array is bubble sorted")
    public void array_is_bubble_sorted() {
        Example1.bS(arr);
    }

    @Then("Array is: {int},{int},{int},{int},{int}")
    public void array_is(int one, int two, int three, int four, int five) {
        // Write code here that turns the phrase above into concrete actions
        int[] arr_excpected = new int[]{one, two, three, four, five};
        assertArrayEquals(arr_excpected, arr);
    }

    @Given("Input string {string}")
    public void input_string(String string) {
        stringReverse = string;
    }

    @When("String is reversed")
    public void string_is_reversed() {
        stringReverse = Example2.rS(stringReverse);
    }

    @Then("Then output string is {string}")
    public void then_output_string_is(String string) {
        assertEquals(string, stringReverse);
    }

    @When("new person with name {string} and surname {string} is created")
    public void new_person_with_name_and_surname_is_created(String firstName, String lastName) {
        person = new Person(firstName, lastName);
    }

    @Then("Person name is displayed as {string}")
    public void person_name_is_displayed_as(String expectedFullName) {
        assertEquals(expectedFullName, person.getDisplayName());
    }

}