import itertools


class Effect:
    def __init__(self, influence, is_instant=True, turns=None):
        if is_instant and turns:
            raise ValueError("Instant effects cannot have a number of turns.")

        if not is_instant and not turns:
            raise ValueError("Non-instant effects must have an associated number of turns.")

        self.influence = influence
        self.is_instant = is_instant
        self.turns = turns


class ActiveEffect:
    @staticmethod
    def init(spell):
        spell_effect = spell.effect

        if spell_effect.is_instant:
            raise ValueError("You cannot create an active effect when using a spell with an instant effect.")

        return ActiveEffect(spell.name, spell_effect.influence, spell_effect.turns)

    def __init__(self, spell_name, influence, remaining_turns):
        self.spell_name = spell_name
        self.influence = influence
        self.remaining_turns = remaining_turns


class Spell:
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect


class Strategy:
    def __init__(self, spells):
        self.spells = spells

    def __str__(self):
        return map(lambda spell: spell.name, self.spells).__str__()

    def total_mana_cost(self):
        return sum([spell.cost for spell in self.spells])


class Player:
    def __init__(self, hp, mana, armor=0):
        self.hp = hp
        self.mana = mana
        self.armor = armor


class Boss:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage


def update_active_effects(active_effects):
    result = []

    for active_effect in active_effects:
        if active_effect.remaining_turns > 1:
            active_effect.remaining_turns -= 1
            result.append(active_effect)

    return result


def print_status(player, boss):
    pass
    # print "Player has", player.hp, "hit points,", player.mana, "mana"
    # print "Boss has", boss.hp, "hit points"


SPELLS = [
    Spell("Shield", 113, Effect(lambda player, boss: (Player(player.hp, player.mana, player.armor + 7), boss), is_instant=False, turns=6)),
    Spell("Poison", 173, Effect(lambda player, boss: (player, Boss(boss.hp - 3, boss.damage)), is_instant=False, turns=6)),
    Spell("Recharge", 229, Effect(lambda player, boss: (Player(player.hp, player.mana + 101, player.armor), boss), is_instant=False, turns=5)),
    Spell("Magic Missile", 53, Effect(lambda player, boss: (player, Boss(boss.hp - 4, boss.damage)))),
    Spell("Drain", 73, Effect(lambda player, boss: (Player(player.hp + 2, player.mana, armor=player.armor), Boss(boss.hp - 2, boss.damage)))),
]


if __name__ == "__main__":
    best_viable_strategy_cost = None

    max_strategy_length = 11
    strategy_length = 1

    while strategy_length <= max_strategy_length:

        total_number_of_turns = 2 * strategy_length

        strategies = map(lambda spells: Strategy(spells), itertools.product(SPELLS, repeat=strategy_length))

        for strategy in strategies:
            # print "\n----------------- NEW STRATEGY, length", strategy_length, "-----------------"

            if best_viable_strategy_cost and strategy.total_mana_cost() >= best_viable_strategy_cost:
                # We already have a viable strategy at least as cheap as this candidate.
                break

            for spell in SPELLS:
                if not spell.effect.is_instant:
                    cooldown_period = spell.effect.turns

                    spell_indices = [index for index, strategy_spell in enumerate(strategy.spells) if strategy_spell == spell]
                    spell_index_spacings = [spell_indices[i+1] - spell_indices[i] for i in range(len(spell_indices) - 1)]

                    if len(spell_index_spacings) > 0 and min(spell_index_spacings) < cooldown_period:
                        # Not a valid strategy; casting spells while effects are still active.
                        break

            player = Player(50, 500)
            boss = Boss(58, 9)

            active_effects = []

            turn_number = 1
            while turn_number <= total_number_of_turns:
                if turn_number % 2 == 1:
                    # print "\n-- Player turn --"
                    print_status(player, boss)

                    for effect in active_effects:
                        # print "Applying effect", effect.spell_name
                        (updated_player, updated_boss) = effect.influence(player, boss)
                        player = updated_player
                        boss = updated_boss

                    print_status(player, boss)

                    if boss.hp <= 0:
                        # print "Player wins!"
                        best_viable_strategy_cost = min(strategy.total_mana_cost(), best_viable_strategy_cost) if best_viable_strategy_cost else strategy.total_mana_cost()
                        break

                    active_effects = update_active_effects(active_effects)

                    spell_to_cast = strategy.spells[(turn_number + 1)/2 - 1]

                    if spell_to_cast.cost > player.mana:
                        # print "Player cannot afford to cast", spell_to_cast.name, "; not a viable strategy"
                        break

                    # print "Player casts", spell_to_cast.name
                    player = Player(player.hp, player.mana - spell_to_cast.cost, player.armor)

                    if spell_to_cast.effect.is_instant:
                        (updated_player, updated_boss) = spell_to_cast.effect.influence(player, boss)
                        player = updated_player
                        boss = updated_boss

                    if not spell_to_cast.effect.is_instant:
                        active_effects.append(ActiveEffect.init(spell_to_cast))

                    print_status(player, boss)

                    if boss.hp <= 0:
                        # print "Player wins!"
                        best_viable_strategy_cost = min(strategy.total_mana_cost(), best_viable_strategy_cost) if best_viable_strategy_cost else strategy.total_mana_cost()
                        break
                else:
                    # print "\n-- Boss turn --"
                    print_status(player, boss)

                    for effect in active_effects:
                        # print "Applying effect", effect.spell_name
                        (updated_player, updated_boss) = effect.influence(player, boss)
                        player = updated_player
                        boss = updated_boss

                    print_status(player, boss)

                    if boss.hp <= 0:
                        # print "Player wins!"
                        best_viable_strategy_cost = min(strategy.total_mana_cost(), best_viable_strategy_cost) if best_viable_strategy_cost else strategy.total_mana_cost()
                        break

                    active_effects = update_active_effects(active_effects)

                    boss_damage = max(boss.damage - player.armor, 1)
                    # print "Boss attacks for", boss_damage, "damage"
                    player.hp -= boss_damage

                    print_status(player, boss)

                    if player.hp <= 0:
                        # Not a viable strategy - we lost!
                        # print "Player loses!"
                        break

                turn_number += 1

            # If we reach here without _someone_ dying, the strategy is not viable.

        strategy_length += 1

    print best_viable_strategy_cost if best_viable_strategy_cost else "No viable strategies"
