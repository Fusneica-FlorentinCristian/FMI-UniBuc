package Services;

public class ServiceService
{
    String nume;

    private ServiceService(){}

    private static final class SingletonHolder{
        private static final ServiceService instance = new ServiceService();
    }

    public static final ServiceService getInstance(){
        return SingletonHolder.instance;
    }

    public String ceva(String altcv)
    {
        return altcv;
    }


}