/**
 * Created by admin on 13/10/15.
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class MultiCurrencyMoney {

    @Test
    public void multiplication() {
        Dollar five    = new Dollar(5);
        Dollar product = five.times(2);
        assertEquals(10, product.amount);

        product = five.times(3);
        assertEquals(15, product.amount);
    }

    @Test
    public void equality() {
        assertTrue(new Dollar(5).equals(new Dollar(5)));
    }
}
