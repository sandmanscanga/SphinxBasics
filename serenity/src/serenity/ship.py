"""
Module grouping actions that can be performed with Firefly.

Summary:
    This module contains functions that can be used to perform
    actions with a Firefly and its crew. The functions are simple
    and are intended to demonstrate how to document functions in a
    Python package using Sphinx and ReadTheDocs.

Functions:
    change_pilot: Changes the pilot on a Firefly instance to the
    given value.

Example:
    The following example demonstrates how to use the functions in
    this module:

    >>> from serenity.ship import Firefly
    >>> firefly = Firefly()
    >>> serenity.actions.change_pilot(firefly, "Malcolm Reynolds")
    >>> print(firefly.pilot)
    Malcolm Reynolds

"""


class Firefly:
    """
    Class representing the Firefly ship from the TV show Firefly.

    Summary:
        This class represents the ship which might be considered a
        main character. The ship has a number of passengers and a
        direction. The ship also has a pilot who can change the
        direction of the ship. The ship can also perform a "crazy
        Ivan" maneuver to change direction by 180 degrees.

    Attributes:
        passengers (int): Number of passengers aboard
        direction (int): Direction the ship is facing in degrees
        pilot (str): Name of the pilot

    Example:
        The following example demonstrates how to use the class:

        >>> from serenity.ship import Firefly
        >>> firefly = Firefly()
        >>> firefly.passengers
        3
        >>> firefly.direction
        0
        >>> firefly.pilot
        'Wash'

    """

    def __init__(self, passengers: int = 3) -> None:
        """
        Initialize a Firefly object.

        Summary:
            This method initializes a Firefly object with a number of
            passengers. The default number of passengers is 3. The
            ship is facing in the 0 degree direction by default and
            the pilot is Wash. The ship is ready to fly.

        Args:
            passengers (int): Number of passengers aboard

        """

        self.passengers = passengers
        self.direction = 0
        self.pilot = "Wash"

    def crazy_ivan(self) -> int:
        """
        Changes direction by 180 degrees.

        Summary:
            This method changes the direction of the ship by 180
            degrees. This is a maneuver that is known as a "crazy
            Ivan" and is used to quickly change direction.

        Returns:
            int: New direction

        Example:
            The following example demonstrates how to use the method:

            >>> from serenity.ship import Firefly
            >>> firefly = Firefly()
            >>> firefly.crazy_ivan()
            180

        """

        self.direction = (self.direction + 180) % 360

        return self.direction
