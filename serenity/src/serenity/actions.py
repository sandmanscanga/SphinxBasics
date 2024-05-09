"""Module grouping actions that can be performed with Firefly.

This module contains functions that can be used to perform actions
with a Firefly and its crew. The functions are simple and are
intended to demonstrate how to document functions in a Python
package using Sphinx and ReadTheDocs.

Functions:
    change_pilot: Changes the pilot on a Firefly instance to the
    given value.

Example:
    The following example demonstrates how to use the functions in
    this module:

    >>> from serenity.ship import Firefly
    >>> from serenity.actions import change_pilot
    >>> firefly = Firefly()
    >>> change_pilot(firefly, "Malcolm Reynolds")
    >>> print(firefly.pilot)
    Malcolm Reynolds

"""

from serenity.ship import Firefly


def change_pilot(firefly: Firefly, pilot: str) -> None:
    """Changes the pilot on a Firefly instance to the given value.

    This function changes the pilot on a Firefly instance to the
    given value. The function takes a Firefly instance and a string
    with the new pilot's name as arguments. The function then sets
    the pilot attribute of the Firefly instance to the given value.

    Args:
        firefly (Firefly): The Firefly instance who's pilot
        attribute is to be changed.
        pilot (str): The new pilot's name.

    Example:
        The following example demonstrates how to use the function:

        >>> from serenity.ship import Firefly
        >>> from serenity.actions import change_pilot
        >>> firefly = Firefly()
        >>> change_pilot(firefly, "Malcolm Reynolds")
        >>> print(firefly.pilot)
        Malcolm Reynolds

    """

    # This is a silly example that should be a method on the object
    firefly.pilot = pilot
