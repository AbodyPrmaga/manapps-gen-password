import click
import random
import string

@click.command()
@click.option('--length', default=12, help='Length of the password')
@click.option('--symbols/--no-symbols', default=True, help='Include symbols like @$!?')
@click.option('--digits/--no-digits', default=True, help='Include digits (0-9)')
@click.option('--upper/--no-upper', default=True, help='Include uppercase letters (A-Z)')
@click.option('--lower/--no-lower', default=True, help='Include lowercase letters (a-z)')
def generate_password(length, symbols, digits, upper, lower):
    """🔐 CLI tool to generate a strong random password."""

    chars = ''
    if symbols:
        chars += string.punctuation
    if digits:
        chars += string.digits
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase

    if not chars:
        click.echo("❌ You must enable at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    click.secho(f"\nGenerated Password:\n{password}\n", fg='green')
    click.secho("Made with ❤️  by Abdelrahman || Telegram : @AbodeDev", fg='red')


if __name__ == '__main__':
    generate_password()
