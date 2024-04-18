from abc import abstractmethod
from enum import Enum
from typing import Tuple

class SkillType(str, Enum):
    tea = "Tea"
    cannon = "Cannon"
    sword = "Sword"
    guile = "Guile"
    vulgarity = "Vulgarity"

class Skill:
    type: SkillType

    @abstractmethod
    def defend_from(self, attacker_skill: SkillType) -> Tuple[bool, str]:
        return [False, "Not yet implemented"]

class TeaSkill(Skill):
    type = SkillType.tea

    def defend_from(self, attacker_skill: SkillType) -> Tuple[bool, str]:
        match attacker_skill:
            case SkillType.cannon:
                return [True, "Tea douses gunpowder. The cannon can't fire!"]
            case SkillType.guile:
                return [True, "Guile does not work in the Willow World."]
            case SkillType.sword:
                return [False, "Sword cuts through tea."]
            case SkillType.vulgarity:
                return [False, "Another fine pour."]


# Tea beats Cannon and Guile
# Cannon beats Sword and Vulgarity
# Sword beats Tea and Guile
# Guile beats Cannon and Vulgarity
# Vulgarity beats Tea and Sword