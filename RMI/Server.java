import java.rmi.Naming;

public class Server {
     public static void main(String[] args) {
        try {
            MessageServer messageServer = new MessageServer();
            HostAddressServer hostAddressServer = new HostAddressServer();
            DateTimeServer dateTimeServer = new DateTimeServer();
            System.out.println("Server is running...");
            Naming.rebind("rmi://localhost:11099/RMIMessage", messageServer);
            Naming.rebind("rmi://localhost:11099/RMIHostAddress", hostAddressServer);
            Naming.rebind("rmi://localhost:11099/RMIDateTime", dateTimeServer);
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
