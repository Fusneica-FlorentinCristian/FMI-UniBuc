package Products_Services;

import Miscellaneous.Event;
import Miscellaneous.Transaction;
import Sellers_Clients.Seller;

import java.util.Objects;

public class Product implements Comparable<Product>{
    private String name;
    private float starting_price;
    private int quantity;
    private Seller seller;

    public Product(String name, float starting_price, int quantity, Seller seller) {
        this.name = name;
        this.starting_price = starting_price;
        this.quantity = quantity;
        this.seller = seller;
    }

    public Product(Product product) {
        this.name = product.name;
        this.starting_price = product.starting_price;
        this.quantity = product.quantity;
        this.seller = product.seller;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float getStarting_price() {
        return starting_price;
    }

    public void setStarting_price(float starting_price) {
        this.starting_price = starting_price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Seller getSeller() {
        return seller;
    }

    public void setSeller(Seller seller) {
        this.seller = seller;
    }

    private boolean inStock(){
        return quantity > 0;
    }

    float showQuantity(){
        if(inStock()){
            return quantity;
        }
        else
            return 0;
    }

    @Override
    public String toString() {
        return "Product{name: " + name +
                " Quatity: " + quantity +
                " Starting price: " + starting_price +
                " \n" + seller
                + "}\n";
    }

    @Override
    public int compareTo(Product o) {
        return this.name.compareTo(o.getName());
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product p = (Product) o;
        return Objects.equals(p.name, this.name) && Objects.equals(p.starting_price, this.starting_price) &&
                Objects.equals(p.seller, this.seller);

    }
}
