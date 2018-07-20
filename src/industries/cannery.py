from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='cannery',
                             processed_cargos_and_output_ratios=[('BEAN', 6), ('FRUT', 6)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['FOOD'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='181',
                             name='TTD_STR_INDUSTRY_NAME_FOOD_PROCESSING_PLANT',
                             nearby_station_name='string(STR_STATION_FOOD_CORPORATION)',
                             fund_cost_multiplier='65')

industry.economy_variations['EXTREME'].enabled = True
industry.economy_variations['EXTREME'].processed_cargos_and_output_ratios = [('STEL', 2), ('FRUT', 4), ('ENUM', 2)]
industry.economy_variations['EXTREME'].prod_cargo_types = ['FOOD']

industry.add_tile(id='cannery_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 87, -31, -56)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 87, -31, -56)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 87, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 87, -31, -56)],
)

industry.add_spritelayout(
    id='cannery_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id='cannery_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cannery_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cannery_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='cannery_industry_layout_1',
    layout=[(0, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (0, 1, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (0, 2, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (1, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 1, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 2, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (2, 0, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (2, 1, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (2, 2, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (3, 0, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (3, 1, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (3, 2, 'cannery_tile_1', 'cannery_spritelayout_4'),
            ]
)
industry.add_industry_layout(
    id='cannery_industry_layout_2',
    layout=[(0, 0, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (0, 1, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (0, 2, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (0, 3, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (1, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 1, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (1, 2, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 3, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (2, 0, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (2, 1, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (2, 2, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (3, 0, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (3, 1, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (3, 2, 'cannery_tile_1', 'cannery_spritelayout_1')
            ]
)
industry.add_industry_layout(
    id='cannery_industry_layout_3',
    layout=[(0, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (0, 1, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (0, 2, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (0, 3, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (1, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 1, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (1, 2, 'cannery_tile_1', 'cannery_spritelayout_2'),
            (1, 3, 'cannery_tile_1', 'cannery_spritelayout_3'),
            (2, 0, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (2, 1, 'cannery_tile_1', 'cannery_spritelayout_1'),
            (2, 2, 'cannery_tile_1', 'cannery_spritelayout_4'),
            (2, 3, 'cannery_tile_1', 'cannery_spritelayout_4'),
            ]
)
