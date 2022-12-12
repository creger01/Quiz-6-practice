class Ambulance:
    """A medical car that helps people.
    attributees: priority, speed, capacity."""

myHelp = Ambulance()

myHelp.priority = 1
myHelp.speed = 120
myHelp.capacity = 2


def formula(amber):
    x = -10*(1-amber.priority)
    y = 2.37*(amber.speed/10)**3.98
    z = 30*(amber.capacity + 1.2)
    controlled_velocity = x + y + z
    print(controlled_velocity)

formula(myHelp)
