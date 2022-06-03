package Miscellaneous;

import Products_Services.*;
import Sellers_Clients.Client;

import java.util.Objects;


public class Transaction implements Comparable<Transaction>{
    private Client client;
    private float price;
    private Product product;

    public Transaction(Client client, float price, Product product) {
        this.client = client;
        this.price = price;
        this.product = product;
    }

    public Transaction(Transaction transaction) {
        this.client = transaction.client;
        this.price = transaction.price;
        this.product = transaction.product;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    @Override
    public String toString() {
        return "Client: " + client + " Price: " + price + " " + product + "\n";
    }

    @Override
    public int compareTo(Transaction o) {
        return  Float.compare(this.getPrice(), o.getPrice());
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Transaction t = (Transaction) o;
        return Objects.equals(t.client, this.client) && Objects.equals(t.product, this.product);

    }
}
