import argparse

def load(filepath:str):
    try:
        """Loads data from filepath to the database"""
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except Exception as e:
        print(f"File not found: {e}")

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

    globals()[args.subcommand](args.filepath)

if __name__ == "__main__":
    main()
