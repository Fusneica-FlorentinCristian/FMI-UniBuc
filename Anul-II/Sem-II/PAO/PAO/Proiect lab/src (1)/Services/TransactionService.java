package Services;

import Miscellaneous.Transaction;
import Products_Services.Product;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TransactionService
{
    private List<Transaction> transactionList;

    private static TransactionService instance = null;

    private TransactionService() {
        transactionList = new ArrayList<>();
    }

    public static TransactionService getInstance() {
        if(instance == null) {
            instance = new TransactionService();
        }
        return instance;
    }

    public void addTransaction(Transaction transaction) {
        transactionList.add(new Transaction(transaction));
    }

    public void showAllTransactions() {
        for(Transaction transaction : transactionList) {
            System.out.println(transaction);
        }
    }

    public void sortTransaction() {
        Collections.sort(transactionList);
    }

    public void removeTransaction(Transaction t) {
        transactionList.remove(t);
    }
}