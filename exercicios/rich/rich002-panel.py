from rich import print
from rich.panel import Panel

box = Panel("[white]Hello World![/]\n[blue]Isso é um panel de exemplo[/]", title="Title", style="blue")

print(box)