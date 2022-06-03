package Sellers_Clients;

import Miscellaneous.Transaction;
import Products_Services.Product;

import java.time.LocalDate;
import java.util.Objects;
import java.util.List;

public class Client extends Person{
    List <Transaction> transactions;
    LocalDate registrationDate;

    public Client (String firstName, String lastName, LocalDate birthday) {
        super(firstName, lastName, birthday);
        this.registrationDate = LocalDate.now();
    }

    public Client (String firstName, String lastName, LocalDate birthday, LocalDate registrationDate) {
        super(firstName, lastName, birthday);
        this.registrationDate = registrationDate;
    }

    public Client(Client client) {
        super(client);
        this.transactions = client.transactions;
        this.registrationDate = client.registrationDate;
    }

    @Override
    public String toString() {
        return "Client{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", birthday=" + birthday +
                ", registrationDate=" + registrationDate +
                "}\n";
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
