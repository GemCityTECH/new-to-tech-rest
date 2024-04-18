from schema.skills import Skill

from pydantic import BaseModel

class Character(BaseModel):
    name: str
    family: str
    skills: list[Skill] = []

    # Attack another character
        # for skill:
            # attack each of defender's skills
    # Return:
        # Win, loss, or tie
        # 'combat log'

    # Defend from another character