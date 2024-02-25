import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;

public class MessageServer extends UnicastRemoteObject implements Message {

    private ArrayList<String> messages = new ArrayList<String>();

    protected MessageServer() throws RemoteException {
        super();
    }

    @Override
    public void addMessage(String message) throws RemoteException {
        this.messages.add(message);
    }

    @Override
    public String getMessage() throws RemoteException {
        return this.messages.toString();
    }
    
}
