import java.util.Arrays;
import java.util.List;
import java.util.Random;

class Person {
    private final String givenName;
    private final String surname;
    private int age;
    private String job;

    Person(String givenName, String surname) {
        this.givenName = givenName;
        this.surname = surname;
        this.age = 18;
    }

    String getDisplayName() {
        return surname + ", " + givenName;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int i) {
        if (i > 1900) {
            this.age = 2019 - i;
        } else {
            this.age = i;
        }
    }

    public void setJobToRandomOne(){
        List<String> jobs = Arrays.asList("Developer", "Tester", "Budowlaniec", "Sprzątaczka", "Premier");
        Random r = new Random();
        int randomInt = r.nextInt(jobs.size());
        this.job = jobs.get(randomInt);
    }

    public String getJob() {
        return job;
    }
}
