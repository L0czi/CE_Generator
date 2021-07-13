import argparse
import utilities as util


def get_parser():
    # create the top-level parser'
    parser = argparse.ArgumentParser(
        prog="main.py", usage="%(prog)s [add or display or generate]"
    )

    # create sub-parser
    sub_parsers = parser.add_subparsers(dest="command")

    # create the parser for the "add" sub-command
    parser_add = sub_parsers.add_parser(
        "add", usage="main.py add", help="Add radiator to database"
    )

    # create the parser for the "display" sub-command
    parser_display = sub_parsers.add_parser(
        "display", usage="main.py display", help="Display radiators stored in database"
    )
    # create the parse for the "generate" sub-command
    parser_generate = sub_parsers.add_parser(
        "generate",
        usage="main.py generate [-o or --option]",
        help="Generate CE Declaration for choosen radiators",
    )
    parser_generate.add_argument(
        "-l",
        "--language",
        metavar="",
        type=str,
        choices=["EN", "DE", "FR", "IT", "PL"],
        default="EN",
        help="choose declaration language: ['EN','DE','FR','IT','PL']",
    )

    group_parser_generate = parser_generate.add_mutually_exclusive_group()
    group_parser_generate.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="generate CE Declarations for all radiator from database",
    )
    group_parser_generate.add_argument(
        "-c",
        "--cp",
        metavar="",
        type=int,
        help="generate CE Declarations for radiators by given CP number",
    )
    group_parser_generate.add_argument(
        "-f",
        "--family",
        metavar="",
        type=str,
        help="generate CE Declarations for radiators by given family name",
    )
    group_parser_generate.add_argument(
        "-m",
        "--model",
        metavar="",
        type=str,
        help="generate CE Declarations for chosen model",
    )

    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args["command"] == "add":

        data_from_csv = util.read_data_from_csv("example_temporary.csv")
        rad_from_csv = data_from_csv[1:]

        data_from_db = util.read_data_from_db()
        rad_from_db = [rad[0] for rad in data_from_db]

        input_data = util.compare_data(rad_from_csv, rad_from_db)
        util.store_data_in_db(input_data)

    if args["command"] == "display":

        data_from_db = util.read_data_from_db()
        rad_from_db = [(rad[0], rad[1], rad[2], rad[3]) for rad in data_from_db]

        for i, rad in enumerate(rad_from_db, start=1):
            print(i, rad)

    if args["command"] == "generate":

        if (
            args["all"] == False
            and args["cp"] == None
            and args["family"] == None
            and args["model"] == None
        ):
            print("Choose one of the options!!!\n")

        if args["all"] == True:

            query = "SELECT * from CE_radiators"

            rad_from_db = util.read_data_from_db(query)
            util.generate_CE(rad_from_db, args["language"])

        if args["cp"] != None:

            query = "SELECT * from CE_radiators WHERE cp=:cp "
            value = {}
            value["cp"] = args["cp"]

            rad_from_db = util.read_data_from_db(query, value)
            util.generate_CE(rad_from_db, args["language"])

        if args["family"] != None:

            query = "SELECT * from CE_radiators WHERE Family=:family"
            value = {}
            value["family"] = args["family"]

            rad_from_db = util.read_data_from_db(query, value)
            util.generate_CE(rad_from_db, args["language"])

        if args["model"] != None:

            query = "SELECT * from CE_radiators WHERE Name=:model"
            value = {}
            value["model"] = args["model"]

            rad_from_db = util.read_data_from_db(query, value)
            util.generate_CE(rad_from_db, args["language"])

    if args["command"] == None:
        print("Please choose a command or use -h for help")


if __name__ == "__main__":
    command_line_runner()
