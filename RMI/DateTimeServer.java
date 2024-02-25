import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeServer extends UnicastRemoteObject implements DateTime {


    protected DateTimeServer() throws RemoteException {
        super();
    }

    @Override
    public String getDateTime() throws RemoteException {
        LocalDateTime myDateObj = LocalDateTime.now();
        DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        return myDateObj.format(myFormatObj);
    }
    
}
