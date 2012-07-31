regression-memcache-stat
========================

Applying statistical regression on the memcache stats to predict the expiry time as per request.

Calculating the expiry time for memcache request using regression.

If the hit percentage is what you are after to achieve and

    hit = function( timeperiod, advance_period ), then

    hit  = lambda timeperiod, adv : CONST+T_COEF*timeperiod + A_COEF*adv

The multiple regression provides a statistical point of view for calculating the unknwon co-efficients in the above equation. The statistical regression uses the historical data of the system and facilitates the equation above.
