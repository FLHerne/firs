from economy import Economy

economy = Economy(
    id="STEELTOWN",
    numeric_id=5,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acid",
        "mail",
        "alloy_steel",
        "aluminium",
        "vehicles",  # no goods?
        "carbon_black",
        "carbon_steel",
        "cast_iron",
        "cement",
        "chlorine",
        "food",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "electrical_parts",
        "engineering_supplies",
        "farm_supplies",
        "ferrochrome",
        "glass",
        "iron_ore",
        "limestone",
        "lye",
        "manganese",
        "oxygen",
        "paints_and_coatings",
        "pig_iron",
        "pipe",
        "plastics",
        "quicklime",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
        "stainless_steel",
        "steel_sections",
        "steel_sheet",
        "steel_wire_rod",
        "sulphur",
        "tyres",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "zinc",
        "potash",
    ],
)
