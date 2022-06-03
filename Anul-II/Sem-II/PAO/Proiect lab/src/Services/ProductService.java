package Services;

import Miscellaneous.Transaction;
import Products_Services.Product;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class ProductService
{
    private List<Product> productList;

    private static ProductService instance = null;

    private ProductService() {
        productList = new ArrayList<>();
    }

    public static ProductService getInstance() {
        if(instance == null) {
            instance = new ProductService();
        }
        return instance;
    }

    public void addProduct(Product product) {
        productList.add(new Product(product));
    }

    public void showAllProducts() {
        for(Product product : productList) {
            System.out.println(product);
        }
    }

    public void sortProducts() {
        Collections.sort(productList);
    }

    public void removeProduct(Product p) {
        productList.remove(p);
    }
}