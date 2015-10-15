/**
 * Created by admin on 14/10/15.
 */

public class Money {

    protected int amount;

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && object.getClass().equals(money.getClass());
    }
}
