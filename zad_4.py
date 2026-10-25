import argparse

import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: str | None,
        address_2: str | None,
        address_3: str | None,
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: float | None,
        latitude: float | None,
        phone: str | None,
        website_url: str | None,
        state: str,
        street: str | None,
    ) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (f"{self.name} ({self.brewery_type})\n"
                f"  adres: {self.street}, {self.postal_code} {self.city}, "
                f"{self.state_province}, {self.country}\n"
                f"  tel: {self.phone}, www: {self.website_url}")


def get_breweries(city: str | None = None) -> list[Brewery]:
    params = {"per_page": 20}
    if city:
        params["by_city"] = city
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return [Brewery(**item) for item in data]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="pobierz browary tylko z tego miasta")
    args = parser.parse_args()

    breweries = get_breweries(args.city)
    for brewery in breweries:
        print(brewery)
        print()
