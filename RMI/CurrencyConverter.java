import java.rmi.*;

public interface CurrencyConverter extends Remote {
    
    public float convertEuroToReal(float euro) throws RemoteException;
    public float convertRealToEuro(float real) throws RemoteException;
    public float convertDolarToReal(float dolar) throws RemoteException;
    public float convertRealToDolar(float real) throws RemoteException;

}