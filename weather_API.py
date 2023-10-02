import click
import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        return None


def find_weather_data_by_datetime(data, dt):
    for item in data:
        if item["dt_txt"] == dt:
            return item
    return None


@click.command()
def main():
    weather_data = get_weather_data()
    if not weather_data:
        click.echo("Failed to retrieve weather data from the API.")
        return

    while True:
        click.echo("\nOptions:")
        click.echo("1. Get Temperature")
        click.echo("2. Get Wind Speed")
        click.echo("3. Get Pressure")
        click.echo("0. Exit")

        option = click.prompt("Enter your choice", type=int)

        if option == 0:
            break
        elif option in [1, 2, 3]:
            dt = click.prompt("Enter date and time (YYYY-MM-DD HH:MM:SS)", type=str)
            weather_info = find_weather_data_by_datetime(weather_data, dt)
            if weather_info:
                if option == 1:
                    click.echo(click.style(f"\n==> Temperature: {weather_info['main']['temp']} K", fg='green') )
                elif option == 2:
                    click.echo(click.style(f"\n==> Wind Speed: {weather_info['wind']['speed']} ",fg='green') )
                elif option == 3:
                    click.echo(click.style(f"\nPressure: {weather_info['main']['pressure']} ", fg='green') )
            else:
                click.echo(click.style("\nData not found for the specified date and time.", fg='red'))
        else:
            click.echo(click.style("Invalid option. Please choose a valid option (0-3).",fg='red'))


if __name__ == "__main__":
    main()
