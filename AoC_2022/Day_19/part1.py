# ------------------------------------------------------------------------------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ------------------------------------------------------------------------------

from re import compile

BLUEPRINT_REGEX = compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian.")

class Blueprint:
    def __init__(self, id_, ore_robot_cost, clay_robot_cost, obsidian_robot_cost_ore, obsidian_robot_cost_clay, geode_robot_cost_ore, geode_robot_cost_obsidian):
        self.id = id_
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost_ore = obsidian_robot_cost_ore
        self.obsidian_robot_cost_clay = obsidian_robot_cost_clay
        self.geode_robot_cost_ore = geode_robot_cost_ore
        self.geode_robot_cost_obsidian = geode_robot_cost_obsidian
        self.total_cost = ore_robot_cost + clay_robot_cost + obsidian_robot_cost_ore + obsidian_robot_cost_clay + geode_robot_cost_ore + geode_robot_cost_obsidian

    def calculate_max_geodes(self, minutes=24):
        raise NotImplementedError("Blueprint.calculate_max_geodes() is not implemented yet.")
        ore, clay, obsidian, geode = 0, 0, 0, 0
        for _ in range(minutes):
            pass
        return geode

    def calculate_quality_level(self, minutes=24):
        return self.id * self.calculate_max_geodes(minutes)

def main(d: list, bar):
    blueprints = []
    for line in d:
        match = BLUEPRINT_REGEX.match(line)
        if match:
            blueprints.append(Blueprint(*map(int, match.groups())))
        else:
            raise ValueError("Invalid Blueprint")

    quality_levels = [blueprint.calculate_quality_level() for blueprint in blueprints]
    return sum(quality_levels)
