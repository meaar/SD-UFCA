import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.net.InetAddress;

public class HostAddressServer extends UnicastRemoteObject implements HostAddress {


    protected HostAddressServer() throws RemoteException {
        super();
    }

    @Override
    public String getHostAddress() throws RemoteException {
        try {
            InetAddress localHost = InetAddress.getLocalHost();
            return localHost.getHostAddress();
        } catch (Exception e) {
            return "InetAddress Error: "+e;
        }
    }
    
}
