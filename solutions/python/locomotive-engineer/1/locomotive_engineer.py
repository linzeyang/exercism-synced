"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids: int) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_ids)


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return each_wagons_id[2:3] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]


def add_missing_stops(routing: dict, **kwargs: str) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    routing["stops"] = [stop for number, stop in sorted(kwargs.items(), key=lambda item: item[0])]

    return routing


def extend_route_information(route: dict[str, str], more_route_information: dict[str, str]) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return route | more_route_information


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    wagons_rows[1][0], wagons_rows[0][1] = wagons_rows[0][1], wagons_rows[1][0]
    wagons_rows[2][0], wagons_rows[0][2] = wagons_rows[0][2], wagons_rows[2][0]
    wagons_rows[1][2], wagons_rows[2][1] = wagons_rows[2][1], wagons_rows[1][2]

    return wagons_rows
