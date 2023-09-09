import os
import sys
from typing import List

from actions import io

import cowsay


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    name, age = os.environ["INPUT_NAME"], os.environ["INPUT_AGE"]
    message = cowsay.get_output_string("cow", f"Hello {name}. I know you are {age}!")

    io.write_to_output({"message": message})


if __name__ == "__main__":
    main(sys.argv)

