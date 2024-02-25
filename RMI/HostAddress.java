import java.rmi.*;

public interface HostAddress extends Remote {

    public String getHostAddress() throws RemoteException;

}
