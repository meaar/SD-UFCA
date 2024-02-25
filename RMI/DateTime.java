import java.rmi.*;

public interface DateTime extends Remote{

    public String getDateTime() throws RemoteException;

}
