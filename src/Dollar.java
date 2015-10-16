/**
 * Created by admin on 13/10/15.
 */

public class Dollar extends Money{

    private String currency;

    public Dollar(int amount) {
        this.amount   = amount;
        this.currency = "USD";
    }

    public Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    public String currency() {
        return currency;
    }
}
