/**
 * Created by admin on 19/10/15.
 */
interface Expression {

    Money reduce(Bank bank, String to);

    Expression plus(Expression addend);
}
