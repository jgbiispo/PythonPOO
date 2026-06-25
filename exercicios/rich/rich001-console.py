from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "bold magenta",
    "warning": "bold yellow",
    "error": "bold red",
})

console = Console(theme=custom_theme).print

console("Print Informativo", style="info")
console("Print de Aviso", style="warning")
console("Print de Erro", style="error")