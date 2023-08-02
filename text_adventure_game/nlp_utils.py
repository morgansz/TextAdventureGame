"""
nlp_utils.py

This file contains utility functions for natural language processing.

"""

from typing import List
import random


def generate_text(choices: List[str]) -> str:
    """
    Generate descriptive text based on the given choices.

    Args:
        choices (List[str]): A list of choices made by the player.

    Returns:
        str: The generated descriptive text.

    """
    template = "在%s里,%s的时候,%s。" 

    location = choices[0]
    action1 = choices[1]
    action2 = choices[2]
    
    text = template % (location, action1, action2)
    
    # 增加一定的随机性
    actions = ["突然","接着","就在这时"]
    text = text % (random.choice(actions))
    
    return text



   
def adapt_storyline(storyline: str, input: str) -> str:
    """
    Adapt the storyline based on the player's input.

    Args:
        storyline (str): The current storyline.
        input (str): The player's input.

    Returns:
        str: The adapted storyline.

    """
    # 检查输入指令
    command = input.split()[0]
    
    if command == "go":
        # 获取前往的方向 
        direction = input.split()[1]
        if direction == "south":
            storyline = "场景切换到了森林"
        elif direction == "north": 
            storyline = "场景切换到了雪山"
            
    elif command == "get":
        # 获取拾取的物品
        item = input.split()[1]
        storyline += f" 玩家拾取到了{item}"
        
    return storyline
