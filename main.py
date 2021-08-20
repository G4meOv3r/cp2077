from Core.Console.Console import Console
from Core.Console.Colors import Colors
from Core.Console.Effects import Effects
from Core.Console.Text import Text

def main(): 
    Console().message(Text("<red>red</red> <i>italic</i> <b>bold</b>"))

if __name__ == "__main__":
    main()
