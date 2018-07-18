from economy import Economy
economy = Economy(id = "EXTREME",
                  numeric_id = 2,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'ammonia',
                            'bauxite',
                            'goods',
                            'building_materials',
                            'canned_food',
                            'chlorine',
                            'clay',
                            'coal',
                            'coffee',
                            'cotton',
                            'dairy_products',
                            'engineering_supplies',
                            'ethylene',
                            'farm_supplies',
                            'flour',
                            'fruits',
                            'furniture',
                            'grain',
                            'iron_ore',
                            'livestock',
                            'limestone',
                            'lumber',
                            'lye',
                            'meat',
                            'milk',
                            'oil',
                            'paper',
                            'petrol',
                            'phosphate',
                            'plastic',
                            'potash',
                            'potatos',
                            'recyclables',
                            'salt',
                            'sand',
                            'scrap_metal',
                            'soda_ash',
                            'steel',
                            'sugar',
                            'sugar_beet',
                            'textiles',
                            'wood',
                            'wool'])
