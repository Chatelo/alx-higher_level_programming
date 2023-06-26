import sys

def safe_print_integer_err(value):
    """Print an integer safely and return True if successful, False otherwise."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

