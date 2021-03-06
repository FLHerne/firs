from cargo import Cargo

cargo = Cargo(
    id="wood",
    type_name="TTD_STR_CARGO_PLURAL_WOOD",
    unit_name="TTD_STR_CARGO_SINGULAR_WOOD",
    type_abbreviation="TTD_STR_ABBREV_WOOD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="WOOD",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_WOOD",
    penalty_lowerbound="24",
    single_penalty_length="255",
    price_factor=97,
    capacity_multiplier="1",
    icon_indices=(8, 0),
)
