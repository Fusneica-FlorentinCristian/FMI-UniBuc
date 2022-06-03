import Products_Services.*;
import Sellers_Clients.*;
import Miscellaneous.*;
import Services.EventService;
import Services.ProductService;
import Services.TransactionService;

import java.time.LocalDate;
import java.util.ArrayList;

import static java.time.LocalDate.now;

public class Main {
    public static void main(String [] args)
    {
        Location l1 = new Location("Banu Manta 16", 12, "Romania", "Bucuresti", "Bucuresti");
        Location l2 = new Location("Banu Manta 1321", 12, "Romania", "Bucuresti", "Bucuresti");
        Location l3 = new Location("1233Banu Manta 16", 12, "Romania", "Bucuresti", "Bucuresti");

        Seller s1 =  new Seller("Andrei", "Andrei1", now());
        Seller s2 =  new Seller("Andrei", "Andrei2", now());
        Seller s3 =  new Seller("Andrei", "Andrei3", now());

        Product p1 = new Product("product1", 10, 10, s1);
        Product p2 = new Product("product3", 30, 30, s2);
        Product p3 = new Product("product2", 20, 20, s3);

        ProductService ps = ProductService.getInstance();
        ps.addProduct(p1);
        ps.addProduct(p2);
        ps.addProduct(p3);
        ps.showAllProducts();
        ps.removeProduct(p1);
        ps.sortProducts();
        ps.showAllProducts();

        Client c1 = new Client("Client1", "Client1", now());
        Client c2 = new Client("Client3", "Client3", now());;
        Client c3 = new Client("Client2", "Client2", now());;

        TransactionService ts = TransactionService.getInstance();
        ts.addTransaction(new Transaction(c1, 10, p1));
        ts.addTransaction(new Transaction(c2, 30, p2));
        ts.addTransaction(new Transaction(c3, 20, p3));
        ts.showAllTransactions();
        ts.removeTransaction(new Transaction(c2, 30, p2));
        ts.sortTransaction();
        ts.showAllTransactions();

        ArrayList<Product> products = new ArrayList<Product>();
        products.add(p1);
        products.add(p2);

        ArrayList<Product> products2 = new ArrayList<Product>();
        products2.add(p3);
        products2.add(p1);


        EventService es = new EventService();
        es.addEvent(new Event(l1,products,"Licitatie Bucuresti"));
        es.addEvent(new Event(l2,products2,"2Licitatie Bucuresti"));

        es.removeEvent(new Event(l2,products2,"2Licitatie Bucuresti"));
        es.showAllEvents();
        es.sortEvents();
        es.showAllEvents();


    }
}
