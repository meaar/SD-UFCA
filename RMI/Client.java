import java.rmi.Naming;

public class Client {

    private static Message message = null;
    private static HostAddress hostAddress = null;
    private static DateTime dateTime = null;

    public static void main(String[] args) {
        try {
            message = (Message) Naming.lookup("rmi://localhost:11099/RMIMessage");
            message.addMessage("Mensagem");
            System.out.println(message.getMessage());
            hostAddress = (HostAddress) Naming.lookup("rmi://localhost:11099/RMIHostAddress");
            System.out.println(hostAddress.getHostAddress());
            dateTime = (DateTime) Naming.lookup("rmi://localhost:11099/RMIDateTime");
            System.out.println(dateTime.getDateTime());
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }

}