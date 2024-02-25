import java.rmi.Naming;

public class CurrencyConverterClient {

    private static CurrencyConverter currencyConverter = null;

    public static void main(String[] args) {
        try {
            currencyConverter = (CurrencyConverter) Naming.lookup("rmi://127.0.0.1:11099/RMICurrencyConverter");
            System.out.println(String.format("%.2f",currencyConverter.convertEuroToReal(1)));
            System.out.println(String.format("%.2f",currencyConverter.convertRealToEuro(1)));
            System.out.println(String.format("%.2f",currencyConverter.convertDolarToReal(1)));
            System.out.println(String.format("%.2f",currencyConverter.convertRealToDolar(1)));
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}