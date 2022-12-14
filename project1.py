from random import randint
import click
from typing import List

class Pizza:
    """ This class represents different types of pizza with specific name, size and list of ingredients """

    def __init__(self, name: str, size: str, ingredients: List[str]):
        self.name = name
        self.size = size
        self.ingredients = ingredients
        valid = {'L', 'XL'}
        if size not in valid:
            raise ValueError('size not available')

    def dict(self) -> dict[str]:
        """
        This method returns the name and ingredients of some pizza in the form of a dictionary
        arguments: no arguments
        return: dict
        """
        recipe = dict()
        recipe[self.name] = ",".join(self.ingredients)
        return recipe

    def __eq__(self, other):
        """
        This method checks the size equality of different pizzas
        """
        return self.size == other.size


Margherita = Pizza('Margherita', 'L', ['tomato sauce', 'mozzarella', 'tomatoes'])
Pepperoni = Pizza('Pepperoni', 'XL', ['tomato sauce', 'mozzarella', 'pepperoni'])
Hawaiian = Pizza('Hawaiian', 'L', ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'])


def menuu():
    """
        This function returns the existing menu
        Arguments: no arguments
    """
    print(f'- {Pepperoni.name} 🍕: {" ".join(list(Pepperoni.dict().values()))} \n'
          f'- {Margherita.name} 🧀: {" ".join(list(Margherita.dict().values()))} \n'
          f'- {Hawaiian.name} 🍍: {" ".join(list(Hawaiian.dict().values()))}')


def log(string):
    def decorator(func):
        def wrapper(arg):
            return string.format(randint(1, 5))

        return wrapper

    return decorator


@log('🧑‍🍳 Приготовили за {}с!')
def bake(pizza):
    pass


@log('🛵 Доставили за {}с!')
def deliveryy(pizza):
    pass


@log('🏠 Забрали за {}с!')
def pickup(pizza):
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(bake(pizza))
    if delivery:
        print(deliveryy(pizza))


@cli.command()
def menu():
    """Выводит меню"""
    menuu()


if __name__ == '__main__':
    cli()