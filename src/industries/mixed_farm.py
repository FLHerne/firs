from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='mixed_farm',
                                  prod_cargo_types=['LVST', 'FICR'],
                                  prob_in_game='3',
                                  prob_random='11',
                                  prod_multiplier='[13, 14]',
                                  map_colour='85',
                                  spec_flags='bitmask(IND_FLAG_PLANT_FIELDS_PERIODICALLY, IND_FLAG_PLANT_FIELDS_WHEN_BUILT)',
                                  # mixed farm doesn't cluster, by design - no industry location checks needed
                                  prospect_chance='0.75',
                                  name='string(STR_IND_MIXEDFARM)',
                                  extra_text_fund='string(STR_FUND_MIXED_FARM)',
                                  nearby_station_name='string(STR_STATION_BARNS)',
                                  fund_cost_multiplier='49')

industry.economy_variations['EXTREME'].enabled = True
# definitely not in Arctic Basic, farm has been added and removed more than once from that economy :P
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['MAIZ', 'LVST']
industry.economy_variations['MISTAH_KURTZ'].prob_random = '14'
industry.economy_variations['MISTAH_KURTZ'].prod_multiplier = '[14, 13]'

industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].name = 'string(STR_IND_BASICFARM)'
industry.economy_variations['STEELTOWN'].prod_cargo_types = ['FOOD']

industry.add_tile(id='mixed_farm_tile_1',
                  location_checks=TileLocationChecks(disallow_steep_slopes=True,
                                                     disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='empty'
)
sprite_ground_mud = industry.add_sprite(
    sprite_number='GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_1_ground = industry.add_spriteset(
    sprites=[(10, 70, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -21)],
)
spriteset_2_ground = industry.add_spriteset(
    sprites=[(80, 70, 64, 52, -31, -21)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_3_ground = industry.add_spriteset(
    sprites=[(150, 70, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_4_ground = industry.add_spriteset(
    sprites=[(220, 70, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 52, -31, -21)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 52, -31, -21)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id='mixed_farm_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_1_ground,
    building_sprites=[spriteset_1],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_2_ground,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_3',
    ground_sprite=sprite_ground_mud,
    ground_overlay=spriteset_3_ground,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_4_ground,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_7',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='mixed_farm_spritelayout_8',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    terrain_aware_ground=True
)

industry.add_industry_layout(
    id='mixed_farm_industry_layout_1',
    layout=[(0, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_8'),
            (0, 3, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_3'),
            (1, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_2'),
            (2, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_1'),
            (2, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_5'),
            (2, 3, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_7'),
            (3, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_6'),
            (3, 3, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_4'),
            ]
)
industry.add_industry_layout(
    id='mixed_farm_industry_layout_2',
    layout=[(0, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_4'),
            (0, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_7'),
            (0, 3, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_6'),
            (1, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_5'),
            (1, 3, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_1'),
            (2, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_8'),
            (2, 1, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_3'),
            (2, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_2'),
            ]
)
industry.add_industry_layout(
    id='mixed_farm_industry_layout_3',
    layout=[(0, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_8'),
            (0, 1, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_1'),
            (0, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_5'),
            (1, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_2'),
            (1, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_3'),
            (2, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_7'),
            (3, 0, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_4'),
            (3, 2, 'mixed_farm_tile_1', 'mixed_farm_spritelayout_6'),
            ]
)
