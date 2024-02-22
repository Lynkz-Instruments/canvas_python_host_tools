#!/usr/bin/env python3

import argparse
import logging
import sys
import os
sys.path.append('./common_lib/libraries')
import discovery


def main(upload: str, repl: str = ""):
    boards = discovery.get_connected_boards()
    if len(boards) == 0:
        logging.error("No boards found")
        exit(1)

    # check if upload is a file or directory
    files = []
    if os.path.isfile(upload):
        files.append(upload)
    elif os.path.isdir(upload):
        # get all files in directory and append them to the directory
        files.extend(f"{upload}/{f}" for f in os.listdir(upload))
    else:
        logging.error(f"Error!  {upload} is not a file or directory.")
        exit(1)

    choice = 0
    if len(boards) > 1:
        print("Which board do you want to upload to?")
        for i, board in enumerate(boards):
            print(f"{i}: {board.id} {board.ports}")
        choice = int(input("Enter the number of the board: "))
    board = boards[choice]
    board.open_ports()
    board.close_repl_uart()
    board.open_raw_repl_uart()
    for file in files:
        logging.info(f"Uploading {file}")
        # strip path from file name
        file_name = file.split("/")[-1]
        board.upload_py_file(file, file_name)
    print("Done")
    board.close_raw_repl_uart()
    board.close_ports()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="File Uploader",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Tool to upload files onto a MicroPython board.",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable verbose debug messages"
    )
    parser.add_argument("-u", "--upload", required=True,
                        help="upload a file or all files in directory")
    # TODO: Implement option to specify board by com port
    # parser.add_argument(
    #     "-r", "--repl", help="The REPL com port to use for file upload"
    # )

    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO
    )
    args, unknown = parser.parse_known_args()
    if args.debug:
        logging.info("Debugging mode enabled")
        logging.getLogger().setLevel(logging.DEBUG)

    main(args.upload)
