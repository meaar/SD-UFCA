import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CurrencyConverterServer extends UnicastRemoteObject implements CurrencyConverter {

    final float EURTOBRL = 5.41f;
    final float BRLTOEUR = 0.18f;
    final float USDTOBRL = 5.00f;
    final float BRLTOUSD = 0.20f;

    protected CurrencyConverterServer() throws RemoteException {
        super();
    }

    @Override
    public float convertEuroToReal(float euro) throws RemoteException {
        return euro*EURTOBRL;
    }

    @Override
    public float convertRealToEuro(float real) throws RemoteException {
        return real*BRLTOEUR;
    }

    @Override
    public float convertDolarToReal(float dolar) throws RemoteException {
       return dolar*USDTOBRL;
    }

    @Override
    public float convertRealToDolar(float real) throws RemoteException {
        return real*BRLTOUSD;
    }

    public static void main(String[] args) {
        try {
            CurrencyConverterServer server = new CurrencyConverterServer();
            System.out.println("Currency Converter is running...");
            Naming.rebind("rmi://localhost:11099/RMICurrencyConverter", server);
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}