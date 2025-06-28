import typer

app = typer.Typer(help="CLI-интерфейс проекта vkx2008")

@app.command()
def hello(name: str = "мир"):
    """
    Приветствие пользователя.
    """
    typer.echo(f"Привет, {name}!")

@app.command()
def add(x: int, y: int):
    """
    Складывает два числа.
    """
    result = x + y
    typer.echo(f"{x} + {y} = {result}")

if __name__ == "__main__":
    app()
