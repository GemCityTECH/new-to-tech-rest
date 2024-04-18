from fastapi import FastAPI, HTTPException, status
from schema.character import Character
from schema.skills import Skill

app = FastAPI()

characters: list[Character] = []
characters.append(Character(name="Hiromatsu", family="Toda", skills=[Skill.sword, Skill.guile]))
characters.append(Character(name="John", family="Blackthorne", skills=[Skill.cannon, Skill.vulgarity]))

@app.get("/")
async def root():
    return "The root endpoint of a service (/) is often used as a health check to determine whether the service is working or not."

@app.get(
    "/characters",
    response_model=list[Character],
)
async def get_characters():
    return characters

@app.get(
    "/characters/{family}",
)
async def get_characters_in_family(family: str) -> list[Character]:
    ret = next((character for character in characters if character.family == family), None)
    if not ret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{family}'s dishonor has erased them from history."
        )
    return ret

@app.post(
    "/characters",
    status_code=status.HTTP_201_CREATED,
)
async def create_character(character: Character) -> Character:
    characters.append(character)
    return character

@app.put(
    "/characters/{family}/{name}",
)
async def update_character(character: Character, family: str, name: str) -> Character:
    character_to_update = next((character for character in characters if character.family == family and character.name == name), None)
    if character_to_update:
        character_to_update.family = character.family
        character_to_update.name = character.name
        character_to_update.skills = character.skills
    else:
        character_to_update = character
        characters.append(character_to_update)
    return character_to_update

@app.delete(
    "/characters/{family}/{name}",
)
async def delete_character(family: str, name: str) -> Character | None:
    character_to_delete = next((character for character in characters if character.family == family and character.name == name), None)
    if character_to_delete:
        characters.remove(character_to_delete)
    return character_to_delete
