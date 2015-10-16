/**
 * Created by admin on 14/10/15.
 */

public abstract class Money {

    protected int amount;
    protected String currency;

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && object.getClass().equals(money.getClass());
    }

    static Money dollar(int amount) {
        return new Dollar(amount, "USD");
    }

    static Money franc(int amount) {
        return new Franc(amount, "CHF");
    }

    abstract Money times(int amount);

    public String currency() {
        return currency;
    }
}
