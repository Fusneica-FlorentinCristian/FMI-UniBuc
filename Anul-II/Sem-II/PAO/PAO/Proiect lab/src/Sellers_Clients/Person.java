package Sellers_Clients;

import java.time.LocalDate;
import java.util.Objects;

public class Person implements Comparable<Person>{
    protected String firstName;
    protected String lastName;
    protected LocalDate birthday;

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public Person(String firstName, String lastName, LocalDate birthday) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthday = birthday;
    }

    public Person (Person person) {
        this.firstName = person.getFirstName();
        this.lastName = person.getLastName();
        this.birthday = person.getBirthday();
    }

    @Override
    public String toString() {
        return "Person{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", birthday=" + birthday +
                "}\n";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return Objects.equals(firstName, person.firstName) && Objects.equals(lastName, person.lastName) && Objects.equals(birthday, person.birthday);
    }

    @Override
    public int compareTo(Person person) {
        if(this.lastName.equals(person.getLastName())) {
            if (this.firstName.equals(person.getFirstName())) {
                return this.birthday.compareTo(person.getBirthday());
            } else {
                return this.firstName.compareTo(person.getFirstName());
            }
        } else {
            return this.lastName.compareTo(person.getLastName());
        }
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public LocalDate getBirthday() {
        return birthday;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }
}
