"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='sheep_farm')

industry.add_tile(id='sheep_farm_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'sheep_farm_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'sheep_farm_spriteset_1',
    sprites = [(10, 10, 64, 80, -31, -49)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'sheep_farm_spriteset_2',
    sprites = [(80, 10, 64, 80, -31, -49)],
    zextent = 48
)

industry.add_spritelayout(
    id = 'sheep_farm_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['se','sw']
)
industry.add_spritelayout(
    id = 'sheep_farm_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['se','sw']
)
industry.add_industry_layout(
    id = 'sheep_farm_industry_layout',
    default_spritelayout = 'sheep_farm_spritelayout_1',
    layout = [(0, 0, 'sheep_farm_tile', 'sheep_farm_spritelayout_2'),
              (1, 0, 'sheep_farm_tile', 'sheep_farm_spritelayout_1'),
    ]
)

# Templating
industry.render_and_save_pnml()
