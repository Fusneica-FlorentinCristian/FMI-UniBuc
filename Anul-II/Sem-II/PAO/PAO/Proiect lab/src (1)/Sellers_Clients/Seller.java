package Sellers_Clients;

import Miscellaneous.Transaction;
import java.time.LocalDate;
import java.util.Objects;
import java.util.List;

public class Seller extends Person{
    List <Transaction> transactions;
    LocalDate registrationDate;

    public Seller (String firstName, String lastName, LocalDate birthday) {
        super(firstName, lastName, birthday);
        this.registrationDate = LocalDate.now();
    }

    public Seller (String firstName, String lastName, LocalDate birthday, LocalDate registrationDate) {
        super(firstName, lastName, birthday);
        this.registrationDate = registrationDate;
    }

    public Seller(Seller client) {
        super(client);
        this.transactions = client.transactions;
        this.registrationDate = client.registrationDate;
    }

    @Override
    public String toString() {
        return "Seller{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", birthday=" + birthday +
                ", registrationDate=" + registrationDate +
                "}\n";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Seller client = (Seller) o;
        return Objects.equals(firstName, client.firstName) && Objects.equals(lastName, client.lastName) && Objects.equals(birthday, client.birthday) && Objects.equals(registrationDate, client.registrationDate);
    }

    public List<Transaction> getTransactions() {
        return transactions;
    }

    public void setTransactions(List<Transaction> transactions) {
        this.transactions = transactions;
    }

    public LocalDate getRegistrationDate() {
        return registrationDate;
    }

    public void setRegistrationDate(LocalDate registrationDate) {
        this.registrationDate = registrationDate;
    }


}
