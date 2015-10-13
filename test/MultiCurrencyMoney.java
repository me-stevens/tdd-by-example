/**
 * Created by admin on 13/10/15.
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MultiCurrencyMoney {

    @Test
    public void multiplication() {
        Dollar five = new Dollar(5);
        five.times(2);
        assertEquals(10, five.amount);
    }
}
