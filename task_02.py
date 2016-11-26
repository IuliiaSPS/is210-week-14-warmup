#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """Function to generate dictionary of combined data.

    Args:
        shoplist(dict): Dictionary of item and it quantity.

    Returns:
        dict: new dictionary keyed by the name of the fruit with the total cost
        per-item reflected.

    Examples:

        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1
        })
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: FRUIT.get(key) * value for key, value in shoplist.iteritems()
            if FRUIT.get(key)}


def get_total_cost(shoplist):
    """Function does some math.

    Args:
        shoplist(dict): Dictionary of item and it quantity.

    Returns
        float: Sums the values of the resultant dictionary together.

    Examples:

        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return float(sum(value for key, value in get_cost_per_item(shoplist)
                     .iteritems()))
