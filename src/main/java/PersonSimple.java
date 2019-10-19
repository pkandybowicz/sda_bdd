class PersonSimple {
    private final String givenName;
    private final String surname;

    PersonSimple(String givenName, String surname) {
        this.givenName = givenName;
        this.surname = surname;
    }

    String getDisplayName() {
        return surname + ", " + givenName;
    }

}
