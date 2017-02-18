"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='assembly_plant',
                    processed_cargos_and_output_ratios=[('VPTS', 4), ('VBOD', 4)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['VEHI'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='141',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'assembly_plant': 56}),
                    remove_cost_multiplier='0',
                    name='string(STR_IND_ASSEMBLY_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HEAVY_INDUSTRY))',
                    fund_cost_multiplier='145',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='assembly_plant_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'assembly_plant_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'assembly_plant_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_1',
    sprites = [(10, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_2',
    sprites = [(80, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_3',
    sprites = [(150, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_4',
    sprites = [(220, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_5',
    sprites = [(290, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_6',
    sprites = [(360, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_7',
    sprites = [(430, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_8',
    sprites = [(500, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_9 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_9',
    sprites = [(570, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_10 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_10',
    sprites = [(640, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_11 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_11',
    sprites = [(710, 10, 64, 80, -31, -49)],
    zextent = 32
)
spriteset_12 = industry.add_spriteset(
    id = 'assembly_plant_spriteset_12',
    sprites = [(640, 100, 64, 80, -31, -49)],
    zextent = 32
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 13,
    yoffset= 0,
    zoffset= 73,
)

industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_rear_assembly_hall_windows',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_rear_assembly_hall_doors',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_central_assembly_hall',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_front_assembly_hall_windows',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_front_assembly_hall_doors',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_goods_in_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_offices',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_tyres',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_vehicles_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_vehicles_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_11],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'assembly_plant_spritelayout_vehicles_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_12],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'assembly_plant_industry_layout_1',
    layout = [(0, 0, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_rear_assembly_hall_windows'),
              (0, 1, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_central_assembly_hall'),
              (0, 2, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_front_assembly_hall_doors'),
              (0, 3, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_1'),
              (1, 0, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_rear_assembly_hall_windows'),
              (1, 1, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_central_assembly_hall'),
              (1, 2, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_front_assembly_hall_windows'),
              (1, 3, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_2'),
              (2, 0, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_rear_assembly_hall_windows'),
              (2, 1, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_central_assembly_hall'),
              (2, 2, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_front_assembly_hall_doors'),
              (2, 3, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_1'),
              (3, 0, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_offices'),
              (3, 1, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_offices'),
              (3, 2, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_tyres'),
              (3, 3, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_2'),
              (4, 0, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_goods_in_1'),
              (4, 1, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_tyres'),
              (4, 2, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_3'),
              (4, 3, 'assembly_plant_tile_1', 'assembly_plant_spritelayout_vehicles_3'),
    ]
)