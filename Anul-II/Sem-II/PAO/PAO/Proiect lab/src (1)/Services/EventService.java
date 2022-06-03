package Services;

import Miscellaneous.Event;
import Miscellaneous.Transaction;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class EventService {
    private List<Event> eventList;

    private static EventService instance = null;

    public EventService() {
        eventList = new ArrayList<>();
    }

    public static EventService getInstance() {
        if(instance == null) {
            instance = new EventService();
        }
        return instance;
    }

    public void addEvent(Event event) {
        eventList.add(new Event(event));
    }

    public void showAllEvents() {
        for(Event event : eventList) {
            System.out.println(event);
        }
    }

    public void sortEvents() {
        Collections.sort(eventList);
    }

    public void removeEvent(Event e) {
        eventList.remove(e);
    }
}
