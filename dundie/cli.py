import argparse
from dundie.core import load # noqa


# I implemented this like a little monkey, so deal with it.
def main():
    # print("Executing entrypoint for dundie...")

    # create a object parser from ArgumentParser
    parser = argparse.ArgumentParser(
        prog="dundie",
        description="Dundler Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious.",
    )
    parser.add_argument(
        # Add first positional argument
        "subcommand",
        type=str,
        help="The Subcommand to run",
        choices=("load", "show", "send"),
        # default="help"# help how defalt
    )

    parser.add_argument(
        # Add second positional argument
        "filepath",
        type=str,
        help="File path to load",
    )

    args = parser.parse_args()

    print(globals()[args.subcommand](args.filepath))
