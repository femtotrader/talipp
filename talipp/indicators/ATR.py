from typing import List, Any

from talipp.indicators.Indicator import Indicator, InputModifierType
from talipp.indicators.TrueRange import TrueRange
from talipp.input import SamplingPeriodType
from talipp.ohlcv import OHLCV
from talipp.ma import MAType, MAFactory


class ATR(Indicator):
    """Average True Range

    Input type: [OHLCV][talipp.ohlcv.OHLCV]

    Output type: `float`

    Args:
        period: Period.
        input_values: List of input values.
        input_indicator: Input indicator.
        input_modifier: Input modifier.
        input_sampling: Input sampling type.
    """    
    def __init__(self, period: int,
                 input_values: List[OHLCV] = None,
                 input_indicator: Indicator = None,
                 input_modifier: InputModifierType = None,
                 ma_type: MAType = MAType.WilderMA,
                 input_sampling: SamplingPeriodType = None):
        super(ATR, self).__init__(input_modifier=input_modifier,
                                  input_sampling=input_sampling)

        self.period = period

        self._tr = TrueRange()
        self.add_sub_indicator(self._tr)

        self._ma_tr = MAFactory.get_ma(ma_type, period, input_indicator=self._tr)

        self.initialize(input_values, input_indicator)

    def _calculate_new_value(self) -> Any:
        return self._ma_tr.output_values[-1]
