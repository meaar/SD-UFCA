import java.rmi.*;

public interface Message extends Remote {

    public void addMessage(String message) throws RemoteException;
    public String getMessage() throws RemoteException;
    
}
