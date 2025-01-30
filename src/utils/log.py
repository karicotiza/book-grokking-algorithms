"""Print debug function.

I made this for:
* Print what is going on inside of algorithm.
"""


def log(msg: str, *, verbose: bool) -> None:
    """Log any string to console.

    Why use "verbose" - I suppose that every debug version of algorithm will
    log function inside it, but it would be inconvenient to get all the logs
    for all the algorithms at once, so if you need debug for any algorithm call
    you will add verbose=True to that call.

    Args:
        msg (str): any string
        verbose (bool): if True print, otherwise do nothing.

    """
    if verbose:
        print(msg)  # noqa: T201
