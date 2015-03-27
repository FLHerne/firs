"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='nitrate_mine',
                    accept_cargo_types=['ENSP'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FMSP', 'NITR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[15, 17]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='164',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    min_cargo_distr='5',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_NITRATE_MINE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='180',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='nitrate_mine_tile')

spriteset_ground = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_ground',
    type = 'empty'
)
"""
sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)
"""
spriteset_ground_overlay = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_ground_overlay',
    type = 'empty'
)

spriteset_1 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_1',
    sprites = [(10, 10, 64, 110, -31, -70)],
    zextent = 128
)
spriteset_2 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_2',
    sprites = [(80, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_4',
    sprites = [(220, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_5',
    sprites = [(290, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_6',
    sprites = [(360, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_7',
    sprites = [(430, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_8',
    sprites = [(500, 10, 64, 64, -31, -31)],
    zextent = 32
)
spriteset_9 = industry.add_spriteset(
    id = 'nitrate_mine_spriteset_9',
    sprites = [(570, 10, 64, 64, -31, -31)],
    zextent = 32
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 8,
    yoffset= 2,
    zoffset= 70,
)

industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_chimney',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_large_shed',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_conveyors',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_processor',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_raised_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_raised_shed',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_machinery',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_hut',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'nitrate_mine_spritelayout_empty',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'nitrate_mine_industry_layout_1',
    layout = [(0, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_chimney'),
              (0, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_raised_shed'),
              (0, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_hut'),
              (1, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_raised_tanks'),
              (1, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_raised_tanks'),
              (1, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_empty'),
              (2, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_processor'),
              (2, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_processor'),
              (2, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_empty'),
              (3, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_conveyors'),
              (3, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_conveyors'),
              (3, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_empty'),
              (4, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_large_shed'),
              (4, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_large_shed'),
              (4, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_machinery'),
    ]
)
industry.add_industry_layout(
    id = 'nitrate_mine_industry_layout_2',
    layout = [(0, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_raised_tanks'),
              (0, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_processor'),
              (0, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_processor'),
              (0, 3, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_raised_shed'),
              (1, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_chimney'),
              (1, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_conveyors'),
              (1, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_conveyors'),
              (1, 3, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_empty'),
              (2, 0, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_machinery'),
              (2, 1, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_large_shed'),
              (2, 2, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_large_shed'),
              (2, 3, 'nitrate_mine_tile', 'nitrate_mine_spritelayout_hut'),
    ]
)