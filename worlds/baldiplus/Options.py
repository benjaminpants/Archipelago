from dataclasses import dataclass

from Options import PerGameCommonOptions, DeathLink


class BaldiPlusDeathLink(DeathLink):
    """
    When you die, everyone dies. The reverse is also true, even if you have the apple (by default)
    """

@dataclass
class BaldiPlusOptions(PerGameCommonOptions):
    death_link: BaldiPlusDeathLink