import enum
import itertools


class Loadout:
    def __init__(self, weapon, armor_component, rings):
        self.weapon = weapon
        self.armor_component = armor_component
        self.rings = rings

    def __str__(self):
        armor_string = self.armor_component.name if self.armor_component else "No armor"
        rings_string = map(lambda ring: ring.__str__(), self.rings).__str__() if self.rings else "No rings"

        return self.weapon.name + ", " + armor_string + ", " + rings_string


    def total_damage(self):
        # Armor never does damage.
        rings_damage = sum([r.damage for r in self.rings]) if self.rings else 0
        return self.weapon.damage + rings_damage

    def total_armor(self):
        # Weapons never provide armor.
        armor_component_armor = self.armor_component.armor if self.armor_component else 0
        rings_armor = sum([r.armor for r in self.rings]) if self.rings else 0
        return armor_component_armor + rings_armor

    def total_cost(self):
        armor_cost = self.armor_component.cost if self.armor_component else 0
        rings_cost = sum([r.cost for r in self.rings]) if self.rings else 0
        return self.weapon.cost + armor_cost + rings_cost


class LoadoutItem:
    def __init__(self, name, item_type, cost, damage, armor):
        self.name = name
        self.item_type = item_type
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return self.name


class LoadoutItemType(enum.Enum):
    Weapon = 0
    Armor = 1
    Ring = 2


class Combatant:
    @staticmethod
    def initialize_with_hp_and_loadout(hp, loadout):
        return Combatant(hp, loadout.total_damage(), loadout.total_armor())

    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def defeats(self, combatant):
        remaining_player_hp = self.hp
        remaining_opponent_hp = combatant.hp

        player_inflicted_damage_per_turn = max(self.damage - combatant.armor, 1)
        opponent_inflicted_damage_per_turn = max(combatant.damage - self.armor, 1)

        while True:
            remaining_opponent_hp -= player_inflicted_damage_per_turn

            if remaining_opponent_hp <= 0:
                return True

            remaining_player_hp -= opponent_inflicted_damage_per_turn

            if remaining_player_hp <= 0:
                return False


PART_1_BOSS = Combatant(104, 8, 1)


SHOP_ITEMS = {
    LoadoutItem("Dagger",      LoadoutItemType.Weapon,  8, 4, 0),
    LoadoutItem("Shortsword",  LoadoutItemType.Weapon, 10, 5, 0),
    LoadoutItem("Warhammer",   LoadoutItemType.Weapon, 25, 6, 0),
    LoadoutItem("Longsword",   LoadoutItemType.Weapon, 40, 7, 0),
    LoadoutItem("Greataxe",    LoadoutItemType.Weapon, 74, 8, 0),
    LoadoutItem("Leather",     LoadoutItemType.Armor,  13, 0, 1),
    LoadoutItem("Chainmail",   LoadoutItemType.Armor,  31, 0, 2),
    LoadoutItem("Splintmail",  LoadoutItemType.Armor,  53, 0, 3),
    LoadoutItem("Bandedmail",  LoadoutItemType.Armor,  75, 0, 4),
    LoadoutItem("Platemail",   LoadoutItemType.Armor, 102, 0, 5),
    LoadoutItem("Damage + 1",  LoadoutItemType.Ring,   25, 1, 0),
    LoadoutItem("Damage + 2",  LoadoutItemType.Ring,   50, 2, 0),
    LoadoutItem("Damage + 3",  LoadoutItemType.Ring,  100, 3, 0),
    LoadoutItem("Defense + 1", LoadoutItemType.Ring,   20, 0, 1),
    LoadoutItem("Defense + 2", LoadoutItemType.Ring,   40, 0, 2),
    LoadoutItem("Defense + 3", LoadoutItemType.Ring,   80, 0, 3),
}


if __name__ == "__main__":
    weapon_options = [loadout_item for loadout_item in SHOP_ITEMS if loadout_item.item_type == LoadoutItemType.Weapon]

    armor = [loadout_item for loadout_item in SHOP_ITEMS if loadout_item.item_type == LoadoutItemType.Armor]
    armor_options = set(armor)
    armor_options.add(None)

    rings = [loadout_item for loadout_item in SHOP_ITEMS if loadout_item.item_type == LoadoutItemType.Ring]
    ring_options = set()
    ring_options.update(itertools.combinations(rings, 2))
    ring_options.update(itertools.combinations(rings, 1))
    ring_options.add(None)

    # print [weapon_option.name for weapon_option in weapon_options]
    # print [armor_option.name if armor_option else "None" for armor_option in armor_options]
    # print [map(lambda x: x.name, ring_option) if ring_option else "None" for ring_option in ring_options]

    loadouts_to_check = [Loadout(p[0], p[1], p[2])
                         for p in list(itertools.product(weapon_options, armor_options, ring_options))]

    # A crude upper bound on the cheapest viable loadout.
    minimum_cost_of_successful_loadout = sum(loadout_item.cost for loadout_item in SHOP_ITEMS)

    for player_loadout in loadouts_to_check:
        print "Testing loadout:", player_loadout

        player = Combatant.initialize_with_hp_and_loadout(100, player_loadout)

        if player.defeats(PART_1_BOSS):
            minimum_cost_of_successful_loadout = min(minimum_cost_of_successful_loadout, player_loadout.total_cost())

    print minimum_cost_of_successful_loadout
