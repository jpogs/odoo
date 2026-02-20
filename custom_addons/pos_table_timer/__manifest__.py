{
    "name": "POS Table Timer",
    "version": "1.0",
    "depends": ["point_of_sale", "pos_restaurant"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_table_timer/static/src/js/table_timer.js",
            "pos_table_timer/static/src/xml/table_timer.xml",
        ],
    },
    "installable": True,
}
