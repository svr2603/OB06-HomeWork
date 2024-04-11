import random
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return self.health > 0


class PlayerHero(Hero):
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")


class ComputerHero(Hero):
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")


class Game:
    def __init__(self, player_name):
        self.player = PlayerHero(player_name)
        self.computer = ComputerHero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break


# Пример использования:
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()
