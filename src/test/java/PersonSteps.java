import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import static org.junit.jupiter.api.Assertions.*;

public class PersonSteps {

    PersonSimple person;

    @Given("New person with first name {string} and last name {string} is created")
    public void new_person_with_first_name_and_last_name_is_created(String firstname, String lastname) {
        person = new PersonSimple(firstname, lastname);
    }

    @Then("Then this person name is displayed as {string}")
    public void then_this_person_name_is_displayed_as(String expectedName) {
        // Write code here that turns the phrase above into concrete actions
        assertEquals(expectedName, person.getDisplayName());
    }
}
