/**
 * Created by admin on 13/10/15.
 */

public class Dollar extends Money{

    public Dollar(int amount, String currency) {
        this.amount   = amount;
    public Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
        this.currency = currency;
    }

    }
}
