/**
 * Created by admin on 14/10/15.
 */

public class Franc extends Money {

    public Franc(int amount, String currency) {
        this.amount   = amount;
        this.currency = currency;
    }

    public Money times(int multiplier) {
        return new Franc(amount * multiplier);
    }

    public String currency() {
        return currency;
    }
}