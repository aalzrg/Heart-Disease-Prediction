# cli/banner.py

from rich.console import Console
from rich.text import Text

console = Console()

BANNER = r"""
      *****       *****
    *********   *********
   *********** ***********
   ************************
    **********************
     ********************
       ****************
         ************
           ********
             ****
              **
.------------------------------------------------------------.
|                                                            |
|                Heart Disease Detection                     |
|                          CLI Tool                          |
|                                                            |
'------------------------------------------------------------'
"""

def show_banner():
    """Prints the ASCII banner with colors"""
    console.print(BANNER, style="bold red")
