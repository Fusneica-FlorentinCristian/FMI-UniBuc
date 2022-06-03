package Miscellaneous;

import Products_Services.Product;
import java.util.Objects;

import java.util.List;

public class Event implements Comparable<Event> {

    private Location location;
    private List<Product> products;
    private String event_name;

    public Event(Location location, List<Product> products, String event_name) {
        this.location = location;
        this.products = products;
        this.event_name = event_name;
    }

    public Event(Event event) {
        this.location = event.location;
        this.products = event.products;
        this.event_name = event.event_name;
    }

    @Override
    public String toString() {
        return "Event{Location: " + location +
                "\nProducts: " + products +
                "\nEvent name: " + event_name
                + "}\n";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Event event = (Event) o;
        return (location.getStreet_name().equals(event.location.getStreet_name()) && event_name.equals(event.event_name));
    }

    @Override
    public int compareTo(Event o) {
        return this.event_name.compareTo(o.getEvent_name());
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void setProducts(List<Product> products) {
        this.products = products;
    }

    public String getEvent_name() {
        return event_name;
    }

    public void setEvent_name(String event_name) {
        this.event_name = event_name;
    }
}
