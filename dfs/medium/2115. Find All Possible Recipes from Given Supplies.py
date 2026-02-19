from typing import Dict, List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplySet = set(supplies)
        req: Dict[str, List[str]] = dict(zip(recipes, ingredients))

        state: Dict[str, int] = {}  # 0 unvisited, 1 visiting, 2 done
        memo: Dict[str, bool] = {}  # recipe -> can make?

        def can_make(food: str):
            # supplies
            if food in supplySet:                    
                return True

            # not a recipe, can't be made
            if food not in req:
                return False

            # possible recipe case
            if state.get(food, 0) == 2:
                return memo[food]

            # cycle detection
            if state.get(food, 0) == 1:
                return False

            state[food] = 1

            possible = True
            for ing in req[food]:
                if not can_make(ing):
                    possible = False
                    break

            state[food] = 2
            memo[food] = possible

            if possible:
                supplySet.add(food)

            return possible

        return [r for r in recipes if can_make(r)]