# Pokemon Red map data keyed by mapIdDecimal
# Usage: maps[0]  ->  PALLET_TOWN data
# References -> https://github.com/pret/pokered and https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/ROM_map

maps = {
  "0": {
    "mapIdHex": "0x00",
    "mapIdDecimal": 0,
    "mapName": "PALLET_TOWN",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 5,
        "y": 5,
        "targetMap": "REDS_HOUSE_1F",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 5,
        "targetMap": "BLUES_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 11,
        "targetMap": "OAKS_LAB",
        "targetWarpId": 2
      }
    ],
    "bg_events": [
      {
        "x": 13,
        "y": 13,
        "description": "TEXT_PALLETTOWN_OAKSLAB_SIGN"
      },
      {
        "x": 7,
        "y": 9,
        "description": "TEXT_PALLETTOWN_SIGN"
      },
      {
        "x": 3,
        "y": 5,
        "description": "TEXT_PALLETTOWN_PLAYERSHOUSE_SIGN"
      },
      {
        "x": 11,
        "y": 5,
        "description": "TEXT_PALLETTOWN_RIVALSHOUSE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 5,
        "name": "TEXT_PALLETTOWN_OAK"
      },
      {
        "x": 3,
        "y": 8,
        "name": "TEXT_PALLETTOWN_GIRL"
      },
      {
        "x": 11,
        "y": 14,
        "name": "TEXT_PALLETTOWN_FISHER"
      }
    ]
  },
  "1": {
    "mapIdHex": "0x01",
    "mapIdDecimal": 1,
    "mapName": "VIRIDIAN_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 23,
        "y": 25,
        "targetMap": "VIRIDIAN_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 29,
        "y": 19,
        "targetMap": "VIRIDIAN_MART",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 15,
        "targetMap": "VIRIDIAN_SCHOOL_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 9,
        "targetMap": "VIRIDIAN_NICKNAME_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 32,
        "y": 7,
        "targetMap": "VIRIDIAN_GYM",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 17,
        "y": 17,
        "description": "TEXT_VIRIDIANCITY_SIGN"
      },
      {
        "x": 19,
        "y": 1,
        "description": "TEXT_VIRIDIANCITY_TRAINER_TIPS1"
      },
      {
        "x": 21,
        "y": 29,
        "description": "TEXT_VIRIDIANCITY_TRAINER_TIPS2"
      },
      {
        "x": 30,
        "y": 19,
        "description": "TEXT_VIRIDIANCITY_MART_SIGN"
      },
      {
        "x": 24,
        "y": 25,
        "description": "TEXT_VIRIDIANCITY_POKECENTER_SIGN"
      },
      {
        "x": 27,
        "y": 7,
        "description": "TEXT_VIRIDIANCITY_GYM_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 13,
        "y": 20,
        "name": "TEXT_VIRIDIANCITY_YOUNGSTER1"
      },
      {
        "x": 30,
        "y": 8,
        "name": "TEXT_VIRIDIANCITY_GAMBLER1"
      },
      {
        "x": 30,
        "y": 25,
        "name": "TEXT_VIRIDIANCITY_YOUNGSTER2"
      },
      {
        "x": 17,
        "y": 9,
        "name": "TEXT_VIRIDIANCITY_GIRL"
      },
      {
        "x": 18,
        "y": 9,
        "name": "TEXT_VIRIDIANCITY_OLD_MAN_SLEEPY"
      },
      {
        "x": 6,
        "y": 23,
        "name": "TEXT_VIRIDIANCITY_FISHER"
      },
      {
        "x": 17,
        "y": 5,
        "name": "TEXT_VIRIDIANCITY_OLD_MAN"
      }
    ]
  },
  "2": {
    "mapIdHex": "0x02",
    "mapIdDecimal": 2,
    "mapName": "PEWTER_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 14,
        "y": 7,
        "targetMap": "MUSEUM_1F",
        "targetWarpId": 1
      },
      {
        "x": 19,
        "y": 5,
        "targetMap": "MUSEUM_1F",
        "targetWarpId": 3
      },
      {
        "x": 16,
        "y": 17,
        "targetMap": "PEWTER_GYM",
        "targetWarpId": 1
      },
      {
        "x": 29,
        "y": 13,
        "targetMap": "PEWTER_NIDORAN_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 17,
        "targetMap": "PEWTER_MART",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 29,
        "targetMap": "PEWTER_SPEECH_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 25,
        "targetMap": "PEWTER_POKECENTER",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 19,
        "y": 29,
        "description": "TEXT_PEWTERCITY_TRAINER_TIPS"
      },
      {
        "x": 33,
        "y": 19,
        "description": "TEXT_PEWTERCITY_POLICE_NOTICE_SIGN"
      },
      {
        "x": 24,
        "y": 17,
        "description": "TEXT_PEWTERCITY_MART_SIGN"
      },
      {
        "x": 14,
        "y": 25,
        "description": "TEXT_PEWTERCITY_POKECENTER_SIGN"
      },
      {
        "x": 15,
        "y": 9,
        "description": "TEXT_PEWTERCITY_MUSEUM_SIGN"
      },
      {
        "x": 11,
        "y": 17,
        "description": "TEXT_PEWTERCITY_GYM_SIGN"
      },
      {
        "x": 25,
        "y": 23,
        "description": "TEXT_PEWTERCITY_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 15,
        "name": "TEXT_PEWTERCITY_COOLTRAINER_F"
      },
      {
        "x": 17,
        "y": 25,
        "name": "TEXT_PEWTERCITY_COOLTRAINER_M"
      },
      {
        "x": 27,
        "y": 17,
        "name": "TEXT_PEWTERCITY_SUPER_NERD1"
      },
      {
        "x": 26,
        "y": 25,
        "name": "TEXT_PEWTERCITY_SUPER_NERD2"
      },
      {
        "x": 35,
        "y": 16,
        "name": "TEXT_PEWTERCITY_YOUNGSTER"
      }
    ]
  },
  "3": {
    "mapIdHex": "0x03",
    "mapIdDecimal": 3,
    "mapName": "CERULEAN_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 27,
        "y": 11,
        "targetMap": "CERULEAN_TRASHED_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 15,
        "targetMap": "CERULEAN_TRADE_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 19,
        "y": 17,
        "targetMap": "CERULEAN_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 30,
        "y": 19,
        "targetMap": "CERULEAN_GYM",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 25,
        "targetMap": "BIKE_SHOP",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 25,
        "targetMap": "CERULEAN_MART",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 11,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 1
      },
      {
        "x": 27,
        "y": 9,
        "targetMap": "CERULEAN_TRASHED_HOUSE",
        "targetWarpId": 3
      },
      {
        "x": 9,
        "y": 11,
        "targetMap": "CERULEAN_BADGE_HOUSE",
        "targetWarpId": 2
      },
      {
        "x": 9,
        "y": 9,
        "targetMap": "CERULEAN_BADGE_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 23,
        "y": 19,
        "description": "TEXT_CERULEANCITY_SIGN"
      },
      {
        "x": 17,
        "y": 29,
        "description": "TEXT_CERULEANCITY_TRAINER_TIPS"
      },
      {
        "x": 26,
        "y": 25,
        "description": "TEXT_CERULEANCITY_MART_SIGN"
      },
      {
        "x": 20,
        "y": 17,
        "description": "TEXT_CERULEANCITY_POKECENTER_SIGN"
      },
      {
        "x": 11,
        "y": 25,
        "description": "TEXT_CERULEANCITY_BIKESHOP_SIGN"
      },
      {
        "x": 27,
        "y": 21,
        "description": "TEXT_CERULEANCITY_GYM_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 20,
        "y": 2,
        "name": "TEXT_CERULEANCITY_RIVAL"
      },
      {
        "x": 30,
        "y": 8,
        "name": "TEXT_CERULEANCITY_ROCKET"
      },
      {
        "x": 31,
        "y": 20,
        "name": "TEXT_CERULEANCITY_COOLTRAINER_M"
      },
      {
        "x": 15,
        "y": 18,
        "name": "TEXT_CERULEANCITY_SUPER_NERD1"
      },
      {
        "x": 9,
        "y": 21,
        "name": "TEXT_CERULEANCITY_SUPER_NERD2"
      },
      {
        "x": 28,
        "y": 12,
        "name": "TEXT_CERULEANCITY_GUARD1"
      },
      {
        "x": 29,
        "y": 26,
        "name": "TEXT_CERULEANCITY_COOLTRAINER_F1"
      },
      {
        "x": 28,
        "y": 26,
        "name": "TEXT_CERULEANCITY_SLOWBRO"
      },
      {
        "x": 9,
        "y": 27,
        "name": "TEXT_CERULEANCITY_COOLTRAINER_F2"
      },
      {
        "x": 4,
        "y": 12,
        "name": "TEXT_CERULEANCITY_SUPER_NERD3"
      },
      {
        "x": 27,
        "y": 12,
        "name": "TEXT_CERULEANCITY_GUARD2"
      }
    ]
  },
  "4": {
    "mapIdHex": "0x04",
    "mapIdDecimal": 4,
    "mapName": "LAVENDER_TOWN",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 5,
        "targetMap": "LAVENDER_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 14,
        "y": 5,
        "targetMap": "POKEMON_TOWER_1F",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 9,
        "targetMap": "MR_FUJIS_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 15,
        "y": 13,
        "targetMap": "LAVENDER_MART",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 13,
        "targetMap": "LAVENDER_CUBONE_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 13,
        "targetMap": "NAME_RATERS_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 11,
        "y": 9,
        "description": "TEXT_LAVENDERTOWN_SIGN"
      },
      {
        "x": 9,
        "y": 3,
        "description": "TEXT_LAVENDERTOWN_SILPH_SCOPE_SIGN"
      },
      {
        "x": 16,
        "y": 13,
        "description": "TEXT_LAVENDERTOWN_MART_SIGN"
      },
      {
        "x": 4,
        "y": 5,
        "description": "TEXT_LAVENDERTOWN_POKECENTER_SIGN"
      },
      {
        "x": 5,
        "y": 9,
        "description": "TEXT_LAVENDERTOWN_POKEMON_HOUSE_SIGN"
      },
      {
        "x": 17,
        "y": 7,
        "description": "TEXT_LAVENDERTOWN_POKEMON_TOWER_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 15,
        "y": 9,
        "name": "TEXT_LAVENDERTOWN_LITTLE_GIRL"
      },
      {
        "x": 9,
        "y": 10,
        "name": "TEXT_LAVENDERTOWN_COOLTRAINER_M"
      },
      {
        "x": 8,
        "y": 7,
        "name": "TEXT_LAVENDERTOWN_SUPER_NERD"
      }
    ]
  },
  "5": {
    "mapIdHex": "0x05",
    "mapIdDecimal": 5,
    "mapName": "VERMILION_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 11,
        "y": 3,
        "targetMap": "VERMILION_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 9,
        "y": 13,
        "targetMap": "POKEMON_FAN_CLUB",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 13,
        "targetMap": "VERMILION_MART",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 19,
        "targetMap": "VERMILION_GYM",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 19,
        "targetMap": "VERMILION_PIDGEY_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 31,
        "targetMap": "VERMILION_DOCK",
        "targetWarpId": 1
      },
      {
        "x": 19,
        "y": 31,
        "targetMap": "VERMILION_DOCK",
        "targetWarpId": 1
      },
      {
        "x": 15,
        "y": 13,
        "targetMap": "VERMILION_TRADE_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 3,
        "targetMap": "VERMILION_OLD_ROD_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 27,
        "y": 3,
        "description": "TEXT_VERMILIONCITY_SIGN"
      },
      {
        "x": 37,
        "y": 13,
        "description": "TEXT_VERMILIONCITY_NOTICE_SIGN"
      },
      {
        "x": 24,
        "y": 13,
        "description": "TEXT_VERMILIONCITY_MART_SIGN"
      },
      {
        "x": 12,
        "y": 3,
        "description": "TEXT_VERMILIONCITY_POKECENTER_SIGN"
      },
      {
        "x": 7,
        "y": 13,
        "description": "TEXT_VERMILIONCITY_POKEMON_FAN_CLUB_SIGN"
      },
      {
        "x": 7,
        "y": 19,
        "description": "TEXT_VERMILIONCITY_GYM_SIGN"
      },
      {
        "x": 29,
        "y": 15,
        "description": "TEXT_VERMILIONCITY_HARBOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 19,
        "y": 7,
        "name": "TEXT_VERMILIONCITY_BEAUTY"
      },
      {
        "x": 14,
        "y": 6,
        "name": "TEXT_VERMILIONCITY_GAMBLER1"
      },
      {
        "x": 19,
        "y": 30,
        "name": "TEXT_VERMILIONCITY_SAILOR1"
      },
      {
        "x": 30,
        "y": 7,
        "name": "TEXT_VERMILIONCITY_GAMBLER2"
      },
      {
        "x": 29,
        "y": 9,
        "name": "TEXT_VERMILIONCITY_MACHOP"
      },
      {
        "x": 25,
        "y": 27,
        "name": "TEXT_VERMILIONCITY_SAILOR2"
      }
    ]
  },
  "6": {
    "mapIdHex": "0x06",
    "mapIdDecimal": 6,
    "mapName": "CELADON_CITY",
    "width": 25,
    "height": 18,
    "warps": [
      {
        "x": 8,
        "y": 13,
        "targetMap": "CELADON_MART_1F",
        "targetWarpId": 1
      },
      {
        "x": 10,
        "y": 13,
        "targetMap": "CELADON_MART_1F",
        "targetWarpId": 3
      },
      {
        "x": 24,
        "y": 9,
        "targetMap": "CELADON_MANSION_1F",
        "targetWarpId": 1
      },
      {
        "x": 24,
        "y": 3,
        "targetMap": "CELADON_MANSION_1F",
        "targetWarpId": 3
      },
      {
        "x": 25,
        "y": 3,
        "targetMap": "CELADON_MANSION_1F",
        "targetWarpId": 3
      },
      {
        "x": 41,
        "y": 9,
        "targetMap": "CELADON_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 27,
        "targetMap": "CELADON_GYM",
        "targetWarpId": 1
      },
      {
        "x": 28,
        "y": 19,
        "targetMap": "GAME_CORNER",
        "targetWarpId": 1
      },
      {
        "x": 39,
        "y": 19,
        "targetMap": "CELADON_MART_5F",
        "targetWarpId": 1
      },
      {
        "x": 33,
        "y": 19,
        "targetMap": "GAME_CORNER_PRIZE_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 31,
        "y": 27,
        "targetMap": "CELADON_DINER",
        "targetWarpId": 1
      },
      {
        "x": 35,
        "y": 27,
        "targetMap": "CELADON_CHIEF_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 43,
        "y": 27,
        "targetMap": "CELADON_HOTEL",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 27,
        "y": 15,
        "description": "TEXT_CELADONCITY_TRAINER_TIPS1"
      },
      {
        "x": 19,
        "y": 15,
        "description": "TEXT_CELADONCITY_SIGN"
      },
      {
        "x": 42,
        "y": 9,
        "description": "TEXT_CELADONCITY_POKECENTER_SIGN"
      },
      {
        "x": 13,
        "y": 29,
        "description": "TEXT_CELADONCITY_GYM_SIGN"
      },
      {
        "x": 21,
        "y": 9,
        "description": "TEXT_CELADONCITY_MANSION_SIGN"
      },
      {
        "x": 12,
        "y": 13,
        "description": "TEXT_CELADONCITY_DEPTSTORE_SIGN"
      },
      {
        "x": 39,
        "y": 21,
        "description": "TEXT_CELADONCITY_TRAINER_TIPS2"
      },
      {
        "x": 33,
        "y": 21,
        "description": "TEXT_CELADONCITY_PRIZEEXCHANGE_SIGN"
      },
      {
        "x": 27,
        "y": 21,
        "description": "TEXT_CELADONCITY_GAMECORNER_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 17,
        "name": "TEXT_CELADONCITY_LITTLE_GIRL"
      },
      {
        "x": 11,
        "y": 28,
        "name": "TEXT_CELADONCITY_GRAMPS1"
      },
      {
        "x": 14,
        "y": 19,
        "name": "TEXT_CELADONCITY_GIRL"
      },
      {
        "x": 25,
        "y": 22,
        "name": "TEXT_CELADONCITY_GRAMPS2"
      },
      {
        "x": 22,
        "y": 16,
        "name": "TEXT_CELADONCITY_GRAMPS3"
      },
      {
        "x": 32,
        "y": 12,
        "name": "TEXT_CELADONCITY_FISHER"
      },
      {
        "x": 30,
        "y": 12,
        "name": "TEXT_CELADONCITY_POLIWRATH"
      },
      {
        "x": 32,
        "y": 29,
        "name": "TEXT_CELADONCITY_ROCKET1"
      },
      {
        "x": 42,
        "y": 14,
        "name": "TEXT_CELADONCITY_ROCKET2"
      }
    ]
  },
  "7": {
    "mapIdHex": "0x07",
    "mapIdDecimal": 7,
    "mapName": "FUCHSIA_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 5,
        "y": 13,
        "targetMap": "FUCHSIA_MART",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 27,
        "targetMap": "FUCHSIA_BILLS_GRANDPAS_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 19,
        "y": 27,
        "targetMap": "FUCHSIA_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 27,
        "y": 27,
        "targetMap": "WARDENS_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 3,
        "targetMap": "SAFARI_ZONE_GATE",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 27,
        "targetMap": "FUCHSIA_GYM",
        "targetWarpId": 1
      },
      {
        "x": 22,
        "y": 13,
        "targetMap": "FUCHSIA_MEETING_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 31,
        "y": 27,
        "targetMap": "FUCHSIA_GOOD_ROD_HOUSE",
        "targetWarpId": 2
      },
      {
        "x": 31,
        "y": 24,
        "targetMap": "FUCHSIA_GOOD_ROD_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 15,
        "y": 23,
        "description": "TEXT_FUCHSIACITY_SIGN1"
      },
      {
        "x": 25,
        "y": 15,
        "description": "TEXT_FUCHSIACITY_SIGN2"
      },
      {
        "x": 17,
        "y": 5,
        "description": "TEXT_FUCHSIACITY_SAFARI_GAME_SIGN"
      },
      {
        "x": 6,
        "y": 13,
        "description": "TEXT_FUCHSIACITY_MART_SIGN"
      },
      {
        "x": 20,
        "y": 27,
        "description": "TEXT_FUCHSIACITY_POKECENTER_SIGN"
      },
      {
        "x": 27,
        "y": 29,
        "description": "TEXT_FUCHSIACITY_WARDENS_HOME_SIGN"
      },
      {
        "x": 21,
        "y": 15,
        "description": "TEXT_FUCHSIACITY_SAFARI_ZONE_SIGN"
      },
      {
        "x": 5,
        "y": 29,
        "description": "TEXT_FUCHSIACITY_GYM_SIGN"
      },
      {
        "x": 33,
        "y": 7,
        "description": "TEXT_FUCHSIACITY_CHANSEY_SIGN"
      },
      {
        "x": 27,
        "y": 7,
        "description": "TEXT_FUCHSIACITY_VOLTORB_SIGN"
      },
      {
        "x": 13,
        "y": 7,
        "description": "TEXT_FUCHSIACITY_KANGASKHAN_SIGN"
      },
      {
        "x": 31,
        "y": 13,
        "description": "TEXT_FUCHSIACITY_SLOWPOKE_SIGN"
      },
      {
        "x": 13,
        "y": 15,
        "description": "TEXT_FUCHSIACITY_LAPRAS_SIGN"
      },
      {
        "x": 7,
        "y": 7,
        "description": "TEXT_FUCHSIACITY_FOSSIL_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 12,
        "name": "TEXT_FUCHSIACITY_YOUNGSTER1"
      },
      {
        "x": 28,
        "y": 17,
        "name": "TEXT_FUCHSIACITY_GAMBLER"
      },
      {
        "x": 30,
        "y": 14,
        "name": "TEXT_FUCHSIACITY_ERIK"
      },
      {
        "x": 24,
        "y": 8,
        "name": "TEXT_FUCHSIACITY_YOUNGSTER2"
      },
      {
        "x": 31,
        "y": 5,
        "name": "TEXT_FUCHSIACITY_CHANSEY"
      },
      {
        "x": 25,
        "y": 6,
        "name": "TEXT_FUCHSIACITY_VOLTORB"
      },
      {
        "x": 12,
        "y": 6,
        "name": "TEXT_FUCHSIACITY_KANGASKHAN"
      },
      {
        "x": 30,
        "y": 12,
        "name": "TEXT_FUCHSIACITY_SLOWPOKE"
      },
      {
        "x": 8,
        "y": 17,
        "name": "TEXT_FUCHSIACITY_LAPRAS"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_FUCHSIACITY_FOSSIL"
      }
    ]
  },
  "8": {
    "mapIdHex": "0x08",
    "mapIdDecimal": 8,
    "mapName": "CINNABAR_ISLAND",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 6,
        "y": 3,
        "targetMap": "POKEMON_MANSION_1F",
        "targetWarpId": 2
      },
      {
        "x": 18,
        "y": 3,
        "targetMap": "CINNABAR_GYM",
        "targetWarpId": 1
      },
      {
        "x": 6,
        "y": 9,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 11,
        "targetMap": "CINNABAR_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 15,
        "y": 11,
        "targetMap": "CINNABAR_MART",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 9,
        "y": 5,
        "description": "TEXT_CINNABARISLAND_SIGN"
      },
      {
        "x": 16,
        "y": 11,
        "description": "TEXT_CINNABARISLAND_MART_SIGN"
      },
      {
        "x": 12,
        "y": 11,
        "description": "TEXT_CINNABARISLAND_POKECENTER_SIGN"
      },
      {
        "x": 9,
        "y": 11,
        "description": "TEXT_CINNABARISLAND_POKEMONLAB_SIGN"
      },
      {
        "x": 13,
        "y": 3,
        "description": "TEXT_CINNABARISLAND_GYM_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 5,
        "name": "TEXT_CINNABARISLAND_GIRL"
      },
      {
        "x": 14,
        "y": 6,
        "name": "TEXT_CINNABARISLAND_GAMBLER"
      }
    ]
  },
  "9": {
    "mapIdHex": "0x09",
    "mapIdDecimal": 9,
    "mapName": "INDIGO_PLATEAU",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 9,
        "y": 5,
        "targetMap": "INDIGO_PLATEAU_LOBBY",
        "targetWarpId": 1
      },
      {
        "x": 10,
        "y": 5,
        "targetMap": "INDIGO_PLATEAU_LOBBY",
        "targetWarpId": 1
      }
    ]
  },
  "10": {
    "mapIdHex": "0x0A",
    "mapIdDecimal": 10,
    "mapName": "SAFFRON_CITY",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 7,
        "y": 5,
        "targetMap": "COPYCATS_HOUSE_1F",
        "targetWarpId": 1
      },
      {
        "x": 26,
        "y": 3,
        "targetMap": "FIGHTING_DOJO",
        "targetWarpId": 1
      },
      {
        "x": 34,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 11,
        "targetMap": "SAFFRON_PIDGEY_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 11,
        "targetMap": "SAFFRON_MART",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 21,
        "targetMap": "SILPH_CO_1F",
        "targetWarpId": 1
      },
      {
        "x": 9,
        "y": 29,
        "targetMap": "SAFFRON_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 29,
        "y": 29,
        "targetMap": "MR_PSYCHICS_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 17,
        "y": 5,
        "description": "TEXT_SAFFRONCITY_SIGN"
      },
      {
        "x": 27,
        "y": 5,
        "description": "TEXT_SAFFRONCITY_FIGHTING_DOJO_SIGN"
      },
      {
        "x": 35,
        "y": 5,
        "description": "TEXT_SAFFRONCITY_GYM_SIGN"
      },
      {
        "x": 26,
        "y": 11,
        "description": "TEXT_SAFFRONCITY_MART_SIGN"
      },
      {
        "x": 39,
        "y": 19,
        "description": "TEXT_SAFFRONCITY_TRAINER_TIPS1"
      },
      {
        "x": 5,
        "y": 21,
        "description": "TEXT_SAFFRONCITY_TRAINER_TIPS2"
      },
      {
        "x": 15,
        "y": 21,
        "description": "TEXT_SAFFRONCITY_SILPH_CO_SIGN"
      },
      {
        "x": 10,
        "y": 29,
        "description": "TEXT_SAFFRONCITY_POKECENTER_SIGN"
      },
      {
        "x": 27,
        "y": 29,
        "description": "TEXT_SAFFRONCITY_MR_PSYCHICS_HOUSE_SIGN"
      },
      {
        "x": 1,
        "y": 19,
        "description": "TEXT_SAFFRONCITY_SILPH_CO_LATEST_PRODUCT_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 6,
        "name": "TEXT_SAFFRONCITY_ROCKET1"
      },
      {
        "x": 20,
        "y": 8,
        "name": "TEXT_SAFFRONCITY_ROCKET2"
      },
      {
        "x": 34,
        "y": 4,
        "name": "TEXT_SAFFRONCITY_ROCKET3"
      },
      {
        "x": 13,
        "y": 12,
        "name": "TEXT_SAFFRONCITY_ROCKET4"
      },
      {
        "x": 11,
        "y": 25,
        "name": "TEXT_SAFFRONCITY_ROCKET5"
      },
      {
        "x": 32,
        "y": 13,
        "name": "TEXT_SAFFRONCITY_ROCKET6"
      },
      {
        "x": 18,
        "y": 30,
        "name": "TEXT_SAFFRONCITY_ROCKET7"
      },
      {
        "x": 8,
        "y": 14,
        "name": "TEXT_SAFFRONCITY_SCIENTIST"
      },
      {
        "x": 23,
        "y": 23,
        "name": "TEXT_SAFFRONCITY_SILPH_WORKER_M"
      },
      {
        "x": 17,
        "y": 30,
        "name": "TEXT_SAFFRONCITY_SILPH_WORKER_F"
      },
      {
        "x": 30,
        "y": 12,
        "name": "TEXT_SAFFRONCITY_GENTLEMAN"
      },
      {
        "x": 31,
        "y": 12,
        "name": "TEXT_SAFFRONCITY_PIDGEOT"
      },
      {
        "x": 18,
        "y": 8,
        "name": "TEXT_SAFFRONCITY_ROCKER"
      },
      {
        "x": 18,
        "y": 22,
        "name": "TEXT_SAFFRONCITY_ROCKET8"
      },
      {
        "x": 19,
        "y": 22,
        "name": "TEXT_SAFFRONCITY_ROCKET9"
      }
    ]
  },
  "11": {
    "mapIdHex": "0x0B",
    "mapIdDecimal": 11,
    "mapName": "UNUSED_MAP_0B",
    "width": 0,
    "height": 0
  },
  "12": {
    "mapIdHex": "0x0C",
    "mapIdDecimal": 12,
    "mapName": "ROUTE_1",
    "width": 10,
    "height": 18,
    "warps": [],
    "bg_events": [
      {
        "x": 9,
        "y": 27,
        "description": "TEXT_ROUTE1_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 24,
        "name": "TEXT_ROUTE1_YOUNGSTER1"
      },
      {
        "x": 15,
        "y": 13,
        "name": "TEXT_ROUTE1_YOUNGSTER2"
      }
    ]
  },
  "13": {
    "mapIdHex": "0x0D",
    "mapIdDecimal": 13,
    "mapName": "ROUTE_2",
    "width": 10,
    "height": 36,
    "warps": [
      {
        "x": 12,
        "y": 9,
        "targetMap": "DIGLETTS_CAVE_ROUTE_2",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 11,
        "targetMap": "VIRIDIAN_FOREST_NORTH_GATE",
        "targetWarpId": 2
      },
      {
        "x": 15,
        "y": 19,
        "targetMap": "ROUTE_2_TRADE_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 35,
        "targetMap": "ROUTE_2_GATE",
        "targetWarpId": 2
      },
      {
        "x": 15,
        "y": 39,
        "targetMap": "ROUTE_2_GATE",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 43,
        "targetMap": "VIRIDIAN_FOREST_SOUTH_GATE",
        "targetWarpId": 3
      }
    ],
    "bg_events": [
      {
        "x": 5,
        "y": 65,
        "description": "TEXT_ROUTE2_SIGN"
      },
      {
        "x": 11,
        "y": 11,
        "description": "TEXT_ROUTE2_DIGLETTS_CAVE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 13,
        "y": 54,
        "name": "TEXT_ROUTE2_MOON_STONE"
      },
      {
        "x": 13,
        "y": 45,
        "name": "TEXT_ROUTE2_HP_UP"
      }
    ]
  },
  "14": {
    "mapIdHex": "0x0E",
    "mapIdDecimal": 14,
    "mapName": "ROUTE_3",
    "width": 35,
    "height": 9,
    "warps": [],
    "bg_events": [
      {
        "x": 59,
        "y": 9,
        "description": "TEXT_ROUTE3_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 57,
        "y": 11,
        "name": "TEXT_ROUTE3_SUPER_NERD"
      },
      {
        "x": 10,
        "y": 6,
        "name": "TEXT_ROUTE3_YOUNGSTER1"
      },
      {
        "x": 14,
        "y": 4,
        "name": "TEXT_ROUTE3_YOUNGSTER2"
      },
      {
        "x": 16,
        "y": 9,
        "name": "TEXT_ROUTE3_COOLTRAINER_F1"
      },
      {
        "x": 19,
        "y": 5,
        "name": "TEXT_ROUTE3_YOUNGSTER3"
      },
      {
        "x": 23,
        "y": 4,
        "name": "TEXT_ROUTE3_COOLTRAINER_F2"
      },
      {
        "x": 22,
        "y": 9,
        "name": "TEXT_ROUTE3_YOUNGSTER4"
      },
      {
        "x": 24,
        "y": 6,
        "name": "TEXT_ROUTE3_YOUNGSTER5"
      },
      {
        "x": 33,
        "y": 10,
        "name": "TEXT_ROUTE3_COOLTRAINER_F3"
      }
    ]
  },
  "15": {
    "mapIdHex": "0x0F",
    "mapIdDecimal": 15,
    "mapName": "ROUTE_4",
    "width": 45,
    "height": 9,
    "warps": [
      {
        "x": 11,
        "y": 5,
        "targetMap": "MT_MOON_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 5,
        "targetMap": "MT_MOON_1F",
        "targetWarpId": 1
      },
      {
        "x": 24,
        "y": 5,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 8
      }
    ],
    "bg_events": [
      {
        "x": 12,
        "y": 5,
        "description": "TEXT_ROUTE4_POKECENTER_SIGN"
      },
      {
        "x": 17,
        "y": 7,
        "description": "TEXT_ROUTE4_MT_MOON_SIGN"
      },
      {
        "x": 27,
        "y": 7,
        "description": "TEXT_ROUTE4_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 9,
        "y": 8,
        "name": "TEXT_ROUTE4_COOLTRAINER_F1"
      },
      {
        "x": 63,
        "y": 3,
        "name": "TEXT_ROUTE4_COOLTRAINER_F2"
      },
      {
        "x": 57,
        "y": 3,
        "name": "TEXT_ROUTE4_TM_WHIRLWIND"
      }
    ]
  },
  "16": {
    "mapIdHex": "0x10",
    "mapIdDecimal": 16,
    "mapName": "ROUTE_5",
    "width": 10,
    "height": 18,
    "warps": [
      {
        "x": 10,
        "y": 29,
        "targetMap": "ROUTE_5_GATE",
        "targetWarpId": 4
      },
      {
        "x": 9,
        "y": 29,
        "targetMap": "ROUTE_5_GATE",
        "targetWarpId": 3
      },
      {
        "x": 10,
        "y": 33,
        "targetMap": "ROUTE_5_GATE",
        "targetWarpId": 1
      },
      {
        "x": 17,
        "y": 27,
        "targetMap": "UNDERGROUND_PATH_ROUTE_5",
        "targetWarpId": 1
      },
      {
        "x": 10,
        "y": 21,
        "targetMap": "DAYCARE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 17,
        "y": 29,
        "description": "TEXT_ROUTE5_UNDERGROUND_PATH_SIGN"
      }
    ]
  },
  "17": {
    "mapIdHex": "0x11",
    "mapIdDecimal": 17,
    "mapName": "ROUTE_6",
    "width": 10,
    "height": 18,
    "warps": [
      {
        "x": 9,
        "y": 1,
        "targetMap": "ROUTE_6_GATE",
        "targetWarpId": 3
      },
      {
        "x": 10,
        "y": 1,
        "targetMap": "ROUTE_6_GATE",
        "targetWarpId": 3
      },
      {
        "x": 10,
        "y": 7,
        "targetMap": "ROUTE_6_GATE",
        "targetWarpId": 1
      },
      {
        "x": 17,
        "y": 13,
        "targetMap": "UNDERGROUND_PATH_ROUTE_6",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 19,
        "y": 15,
        "description": "TEXT_ROUTE6_UNDERGROUND_PATH_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 21,
        "name": "TEXT_ROUTE6_COOLTRAINER_M1"
      },
      {
        "x": 11,
        "y": 21,
        "name": "TEXT_ROUTE6_COOLTRAINER_F1"
      },
      {
        "x": 0,
        "y": 15,
        "name": "TEXT_ROUTE6_YOUNGSTER1"
      },
      {
        "x": 11,
        "y": 31,
        "name": "TEXT_ROUTE6_COOLTRAINER_M2"
      },
      {
        "x": 11,
        "y": 30,
        "name": "TEXT_ROUTE6_COOLTRAINER_F2"
      },
      {
        "x": 19,
        "y": 26,
        "name": "TEXT_ROUTE6_YOUNGSTER2"
      }
    ]
  },
  "18": {
    "mapIdHex": "0x12",
    "mapIdDecimal": 18,
    "mapName": "ROUTE_7",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 18,
        "y": 9,
        "targetMap": "ROUTE_7_GATE",
        "targetWarpId": 3
      },
      {
        "x": 18,
        "y": 10,
        "targetMap": "ROUTE_7_GATE",
        "targetWarpId": 4
      },
      {
        "x": 11,
        "y": 9,
        "targetMap": "ROUTE_7_GATE",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 10,
        "targetMap": "ROUTE_7_GATE",
        "targetWarpId": 2
      },
      {
        "x": 5,
        "y": 13,
        "targetMap": "UNDERGROUND_PATH_ROUTE_7",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 13,
        "description": "TEXT_ROUTE7_UNDERGROUND_PATH_SIGN"
      }
    ]
  },
  "19": {
    "mapIdHex": "0x13",
    "mapIdDecimal": 19,
    "mapName": "ROUTE_8",
    "width": 30,
    "height": 9,
    "warps": [
      {
        "x": 1,
        "y": 9,
        "targetMap": "ROUTE_8_GATE",
        "targetWarpId": 1
      },
      {
        "x": 1,
        "y": 10,
        "targetMap": "ROUTE_8_GATE",
        "targetWarpId": 2
      },
      {
        "x": 8,
        "y": 9,
        "targetMap": "ROUTE_8_GATE",
        "targetWarpId": 3
      },
      {
        "x": 8,
        "y": 10,
        "targetMap": "ROUTE_8_GATE",
        "targetWarpId": 4
      },
      {
        "x": 13,
        "y": 3,
        "targetMap": "UNDERGROUND_PATH_ROUTE_8",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 17,
        "y": 3,
        "description": "TEXT_ROUTE8_UNDERGROUND_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 5,
        "name": "TEXT_ROUTE8_SUPER_NERD1"
      },
      {
        "x": 13,
        "y": 9,
        "name": "TEXT_ROUTE8_GAMBLER1"
      },
      {
        "x": 42,
        "y": 6,
        "name": "TEXT_ROUTE8_SUPER_NERD2"
      },
      {
        "x": 26,
        "y": 3,
        "name": "TEXT_ROUTE8_COOLTRAINER_F1"
      },
      {
        "x": 26,
        "y": 4,
        "name": "TEXT_ROUTE8_SUPER_NERD3"
      },
      {
        "x": 26,
        "y": 5,
        "name": "TEXT_ROUTE8_COOLTRAINER_F2"
      },
      {
        "x": 26,
        "y": 6,
        "name": "TEXT_ROUTE8_COOLTRAINER_F3"
      },
      {
        "x": 46,
        "y": 13,
        "name": "TEXT_ROUTE8_GAMBLER2"
      },
      {
        "x": 51,
        "y": 12,
        "name": "TEXT_ROUTE8_COOLTRAINER_F4"
      }
    ]
  },
  "20": {
    "mapIdHex": "0x14",
    "mapIdDecimal": 20,
    "mapName": "ROUTE_9",
    "width": 30,
    "height": 9,
    "warps": [],
    "bg_events": [
      {
        "x": 25,
        "y": 7,
        "description": "TEXT_ROUTE9_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 13,
        "y": 10,
        "name": "TEXT_ROUTE9_COOLTRAINER_F1"
      },
      {
        "x": 24,
        "y": 7,
        "name": "TEXT_ROUTE9_COOLTRAINER_M1"
      },
      {
        "x": 31,
        "y": 7,
        "name": "TEXT_ROUTE9_COOLTRAINER_M2"
      },
      {
        "x": 48,
        "y": 8,
        "name": "TEXT_ROUTE9_COOLTRAINER_F2"
      },
      {
        "x": 16,
        "y": 15,
        "name": "TEXT_ROUTE9_HIKER1"
      },
      {
        "x": 43,
        "y": 3,
        "name": "TEXT_ROUTE9_HIKER2"
      },
      {
        "x": 22,
        "y": 2,
        "name": "TEXT_ROUTE9_YOUNGSTER1"
      },
      {
        "x": 45,
        "y": 15,
        "name": "TEXT_ROUTE9_HIKER3"
      },
      {
        "x": 40,
        "y": 8,
        "name": "TEXT_ROUTE9_YOUNGSTER2"
      },
      {
        "x": 10,
        "y": 15,
        "name": "TEXT_ROUTE9_TM_TELEPORT"
      }
    ]
  },
  "21": {
    "mapIdHex": "0x15",
    "mapIdDecimal": 21,
    "mapName": "ROUTE_10",
    "width": 10,
    "height": 36,
    "warps": [
      {
        "x": 11,
        "y": 19,
        "targetMap": "ROCK_TUNNEL_POKECENTER",
        "targetWarpId": 1
      },
      {
        "x": 8,
        "y": 17,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 1
      },
      {
        "x": 8,
        "y": 53,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 3
      },
      {
        "x": 6,
        "y": 39,
        "targetMap": "POWER_PLANT",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 7,
        "y": 19,
        "description": "TEXT_ROUTE10_ROCKTUNNEL_NORTH_SIGN"
      },
      {
        "x": 12,
        "y": 19,
        "description": "TEXT_ROUTE10_POKECENTER_SIGN"
      },
      {
        "x": 9,
        "y": 55,
        "description": "TEXT_ROUTE10_ROCKTUNNEL_SOUTH_SIGN"
      },
      {
        "x": 5,
        "y": 41,
        "description": "TEXT_ROUTE10_POWERPLANT_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 44,
        "name": "TEXT_ROUTE10_SUPER_NERD1"
      },
      {
        "x": 3,
        "y": 57,
        "name": "TEXT_ROUTE10_HIKER1"
      },
      {
        "x": 14,
        "y": 64,
        "name": "TEXT_ROUTE10_SUPER_NERD2"
      },
      {
        "x": 7,
        "y": 25,
        "name": "TEXT_ROUTE10_COOLTRAINER_F1"
      },
      {
        "x": 3,
        "y": 61,
        "name": "TEXT_ROUTE10_HIKER2"
      },
      {
        "x": 7,
        "y": 54,
        "name": "TEXT_ROUTE10_COOLTRAINER_F2"
      }
    ]
  },
  "22": {
    "mapIdHex": "0x16",
    "mapIdDecimal": 22,
    "mapName": "ROUTE_11",
    "width": 30,
    "height": 9,
    "warps": [
      {
        "x": 49,
        "y": 8,
        "targetMap": "ROUTE_11_GATE_1F",
        "targetWarpId": 1
      },
      {
        "x": 49,
        "y": 9,
        "targetMap": "ROUTE_11_GATE_1F",
        "targetWarpId": 2
      },
      {
        "x": 58,
        "y": 8,
        "targetMap": "ROUTE_11_GATE_1F",
        "targetWarpId": 3
      },
      {
        "x": 58,
        "y": 9,
        "targetMap": "ROUTE_11_GATE_1F",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 5,
        "targetMap": "DIGLETTS_CAVE_ROUTE_11",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 5,
        "description": "TEXT_ROUTE11_DIGLETTSCAVE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 14,
        "name": "TEXT_ROUTE11_GAMBLER1"
      },
      {
        "x": 26,
        "y": 9,
        "name": "TEXT_ROUTE11_GAMBLER2"
      },
      {
        "x": 13,
        "y": 5,
        "name": "TEXT_ROUTE11_YOUNGSTER1"
      },
      {
        "x": 36,
        "y": 11,
        "name": "TEXT_ROUTE11_SUPER_NERD1"
      },
      {
        "x": 22,
        "y": 4,
        "name": "TEXT_ROUTE11_YOUNGSTER2"
      },
      {
        "x": 45,
        "y": 7,
        "name": "TEXT_ROUTE11_GAMBLER3"
      },
      {
        "x": 33,
        "y": 3,
        "name": "TEXT_ROUTE11_GAMBLER4"
      },
      {
        "x": 43,
        "y": 5,
        "name": "TEXT_ROUTE11_YOUNGSTER3"
      },
      {
        "x": 45,
        "y": 16,
        "name": "TEXT_ROUTE11_SUPER_NERD2"
      },
      {
        "x": 22,
        "y": 12,
        "name": "TEXT_ROUTE11_YOUNGSTER4"
      }
    ]
  },
  "23": {
    "mapIdHex": "0x17",
    "mapIdDecimal": 23,
    "mapName": "ROUTE_12",
    "width": 10,
    "height": 54,
    "warps": [
      {
        "x": 10,
        "y": 15,
        "targetMap": "ROUTE_12_GATE_1F",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 15,
        "targetMap": "ROUTE_12_GATE_1F",
        "targetWarpId": 2
      },
      {
        "x": 10,
        "y": 21,
        "targetMap": "ROUTE_12_GATE_1F",
        "targetWarpId": 3
      },
      {
        "x": 11,
        "y": 77,
        "targetMap": "ROUTE_12_SUPER_ROD_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 13,
        "y": 13,
        "description": "TEXT_ROUTE12_SIGN"
      },
      {
        "x": 11,
        "y": 63,
        "description": "TEXT_ROUTE12_SPORT_FISHING_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 62,
        "name": "TEXT_ROUTE12_SNORLAX"
      },
      {
        "x": 14,
        "y": 31,
        "name": "TEXT_ROUTE12_FISHER1"
      },
      {
        "x": 5,
        "y": 39,
        "name": "TEXT_ROUTE12_FISHER2"
      },
      {
        "x": 11,
        "y": 92,
        "name": "TEXT_ROUTE12_COOLTRAINER_M"
      },
      {
        "x": 14,
        "y": 76,
        "name": "TEXT_ROUTE12_SUPER_NERD"
      },
      {
        "x": 12,
        "y": 40,
        "name": "TEXT_ROUTE12_FISHER3"
      },
      {
        "x": 9,
        "y": 52,
        "name": "TEXT_ROUTE12_FISHER4"
      },
      {
        "x": 6,
        "y": 87,
        "name": "TEXT_ROUTE12_FISHER5"
      },
      {
        "x": 14,
        "y": 35,
        "name": "TEXT_ROUTE12_TM_PAY_DAY"
      },
      {
        "x": 5,
        "y": 89,
        "name": "TEXT_ROUTE12_IRON"
      }
    ]
  },
  "24": {
    "mapIdHex": "0x18",
    "mapIdDecimal": 24,
    "mapName": "ROUTE_13",
    "width": 30,
    "height": 9,
    "warps": [],
    "bg_events": [
      {
        "x": 15,
        "y": 13,
        "description": "TEXT_ROUTE13_TRAINER_TIPS1"
      },
      {
        "x": 33,
        "y": 5,
        "description": "TEXT_ROUTE13_TRAINER_TIPS2"
      },
      {
        "x": 31,
        "y": 11,
        "description": "TEXT_ROUTE13_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 49,
        "y": 10,
        "name": "TEXT_ROUTE13_COOLTRAINER_M1"
      },
      {
        "x": 48,
        "y": 10,
        "name": "TEXT_ROUTE13_COOLTRAINER_F1"
      },
      {
        "x": 27,
        "y": 9,
        "name": "TEXT_ROUTE13_COOLTRAINER_F2"
      },
      {
        "x": 23,
        "y": 10,
        "name": "TEXT_ROUTE13_COOLTRAINER_F3"
      },
      {
        "x": 50,
        "y": 5,
        "name": "TEXT_ROUTE13_COOLTRAINER_F4"
      },
      {
        "x": 12,
        "y": 4,
        "name": "TEXT_ROUTE13_COOLTRAINER_M2"
      },
      {
        "x": 33,
        "y": 6,
        "name": "TEXT_ROUTE13_BEAUTY1"
      },
      {
        "x": 32,
        "y": 6,
        "name": "TEXT_ROUTE13_BEAUTY2"
      },
      {
        "x": 10,
        "y": 7,
        "name": "TEXT_ROUTE13_BIKER"
      },
      {
        "x": 7,
        "y": 13,
        "name": "TEXT_ROUTE13_COOLTRAINER_M3"
      }
    ]
  },
  "25": {
    "mapIdHex": "0x19",
    "mapIdDecimal": 25,
    "mapName": "ROUTE_14",
    "width": 10,
    "height": 27,
    "warps": [],
    "bg_events": [
      {
        "x": 17,
        "y": 13,
        "description": "TEXT_ROUTE14_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 4,
        "name": "TEXT_ROUTE14_COOLTRAINER_M1"
      },
      {
        "x": 15,
        "y": 6,
        "name": "TEXT_ROUTE14_COOLTRAINER_M2"
      },
      {
        "x": 12,
        "y": 11,
        "name": "TEXT_ROUTE14_COOLTRAINER_M3"
      },
      {
        "x": 14,
        "y": 15,
        "name": "TEXT_ROUTE14_COOLTRAINER_M4"
      },
      {
        "x": 15,
        "y": 31,
        "name": "TEXT_ROUTE14_COOLTRAINER_M5"
      },
      {
        "x": 6,
        "y": 49,
        "name": "TEXT_ROUTE14_COOLTRAINER_M6"
      },
      {
        "x": 5,
        "y": 39,
        "name": "TEXT_ROUTE14_BIKER1"
      },
      {
        "x": 4,
        "y": 30,
        "name": "TEXT_ROUTE14_BIKER2"
      },
      {
        "x": 15,
        "y": 30,
        "name": "TEXT_ROUTE14_BIKER3"
      },
      {
        "x": 4,
        "y": 31,
        "name": "TEXT_ROUTE14_BIKER4"
      }
    ]
  },
  "26": {
    "mapIdHex": "0x1A",
    "mapIdDecimal": 26,
    "mapName": "ROUTE_15",
    "width": 30,
    "height": 9,
    "warps": [
      {
        "x": 7,
        "y": 8,
        "targetMap": "ROUTE_15_GATE_1F",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 9,
        "targetMap": "ROUTE_15_GATE_1F",
        "targetWarpId": 2
      },
      {
        "x": 14,
        "y": 8,
        "targetMap": "ROUTE_15_GATE_1F",
        "targetWarpId": 3
      },
      {
        "x": 14,
        "y": 9,
        "targetMap": "ROUTE_15_GATE_1F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 39,
        "y": 9,
        "description": "TEXT_ROUTE15_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 41,
        "y": 11,
        "name": "TEXT_ROUTE15_COOLTRAINER_F1"
      },
      {
        "x": 53,
        "y": 10,
        "name": "TEXT_ROUTE15_COOLTRAINER_F2"
      },
      {
        "x": 31,
        "y": 13,
        "name": "TEXT_ROUTE15_COOLTRAINER_M1"
      },
      {
        "x": 35,
        "y": 13,
        "name": "TEXT_ROUTE15_COOLTRAINER_M2"
      },
      {
        "x": 53,
        "y": 11,
        "name": "TEXT_ROUTE15_BEAUTY1"
      },
      {
        "x": 41,
        "y": 10,
        "name": "TEXT_ROUTE15_BEAUTY2"
      },
      {
        "x": 48,
        "y": 10,
        "name": "TEXT_ROUTE15_BIKER1"
      },
      {
        "x": 46,
        "y": 10,
        "name": "TEXT_ROUTE15_BIKER2"
      },
      {
        "x": 37,
        "y": 5,
        "name": "TEXT_ROUTE15_COOLTRAINER_F3"
      },
      {
        "x": 18,
        "y": 13,
        "name": "TEXT_ROUTE15_COOLTRAINER_F4"
      },
      {
        "x": 18,
        "y": 5,
        "name": "TEXT_ROUTE15_TM_RAGE"
      }
    ]
  },
  "27": {
    "mapIdHex": "0x1B",
    "mapIdDecimal": 27,
    "mapName": "ROUTE_16",
    "width": 20,
    "height": 9,
    "warps": [
      {
        "x": 17,
        "y": 10,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 1
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 2
      },
      {
        "x": 24,
        "y": 10,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 3
      },
      {
        "x": 24,
        "y": 11,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 4
      },
      {
        "x": 17,
        "y": 4,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 5
      },
      {
        "x": 17,
        "y": 5,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 6
      },
      {
        "x": 24,
        "y": 4,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 7
      },
      {
        "x": 24,
        "y": 5,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 8
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "ROUTE_16_FLY_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 27,
        "y": 11,
        "description": "TEXT_ROUTE16_CYCLING_ROAD_SIGN"
      },
      {
        "x": 5,
        "y": 17,
        "description": "TEXT_ROUTE16_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 17,
        "y": 12,
        "name": "TEXT_ROUTE16_BIKER1"
      },
      {
        "x": 14,
        "y": 13,
        "name": "TEXT_ROUTE16_BIKER2"
      },
      {
        "x": 11,
        "y": 12,
        "name": "TEXT_ROUTE16_BIKER3"
      },
      {
        "x": 9,
        "y": 11,
        "name": "TEXT_ROUTE16_BIKER4"
      },
      {
        "x": 6,
        "y": 10,
        "name": "TEXT_ROUTE16_BIKER5"
      },
      {
        "x": 3,
        "y": 12,
        "name": "TEXT_ROUTE16_BIKER6"
      },
      {
        "x": 26,
        "y": 10,
        "name": "TEXT_ROUTE16_SNORLAX"
      }
    ]
  },
  "28": {
    "mapIdHex": "0x1C",
    "mapIdDecimal": 28,
    "mapName": "ROUTE_17",
    "width": 10,
    "height": 72,
    "warps": [],
    "bg_events": [
      {
        "x": 9,
        "y": 51,
        "description": "TEXT_ROUTE17_NOTICE_SIGN1"
      },
      {
        "x": 9,
        "y": 63,
        "description": "TEXT_ROUTE17_TRAINER_TIPS1"
      },
      {
        "x": 9,
        "y": 75,
        "description": "TEXT_ROUTE17_TRAINER_TIPS2"
      },
      {
        "x": 9,
        "y": 87,
        "description": "TEXT_ROUTE17_SIGN"
      },
      {
        "x": 9,
        "y": 111,
        "description": "TEXT_ROUTE17_NOTICE_SIGN2"
      },
      {
        "x": 9,
        "y": 141,
        "description": "TEXT_ROUTE17_CYCLING_ROAD_ENDS_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 19,
        "name": "TEXT_ROUTE17_BIKER1"
      },
      {
        "x": 11,
        "y": 16,
        "name": "TEXT_ROUTE17_BIKER2"
      },
      {
        "x": 4,
        "y": 18,
        "name": "TEXT_ROUTE17_BIKER3"
      },
      {
        "x": 7,
        "y": 32,
        "name": "TEXT_ROUTE17_BIKER4"
      },
      {
        "x": 14,
        "y": 34,
        "name": "TEXT_ROUTE17_BIKER5"
      },
      {
        "x": 17,
        "y": 58,
        "name": "TEXT_ROUTE17_BIKER6"
      },
      {
        "x": 2,
        "y": 68,
        "name": "TEXT_ROUTE17_BIKER7"
      },
      {
        "x": 14,
        "y": 98,
        "name": "TEXT_ROUTE17_BIKER8"
      },
      {
        "x": 5,
        "y": 98,
        "name": "TEXT_ROUTE17_BIKER9"
      },
      {
        "x": 10,
        "y": 118,
        "name": "TEXT_ROUTE17_BIKER10"
      }
    ]
  },
  "29": {
    "mapIdHex": "0x1D",
    "mapIdDecimal": 29,
    "mapName": "ROUTE_18",
    "width": 25,
    "height": 9,
    "warps": [
      {
        "x": 33,
        "y": 8,
        "targetMap": "ROUTE_18_GATE_1F",
        "targetWarpId": 1
      },
      {
        "x": 33,
        "y": 9,
        "targetMap": "ROUTE_18_GATE_1F",
        "targetWarpId": 2
      },
      {
        "x": 40,
        "y": 8,
        "targetMap": "ROUTE_18_GATE_1F",
        "targetWarpId": 3
      },
      {
        "x": 40,
        "y": 9,
        "targetMap": "ROUTE_18_GATE_1F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 43,
        "y": 7,
        "description": "TEXT_ROUTE18_SIGN"
      },
      {
        "x": 33,
        "y": 5,
        "description": "TEXT_ROUTE18_CYCLING_ROAD_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 36,
        "y": 11,
        "name": "TEXT_ROUTE18_COOLTRAINER_M1"
      },
      {
        "x": 40,
        "y": 15,
        "name": "TEXT_ROUTE18_COOLTRAINER_M2"
      },
      {
        "x": 42,
        "y": 13,
        "name": "TEXT_ROUTE18_COOLTRAINER_M3"
      }
    ]
  },
  "30": {
    "mapIdHex": "0x1E",
    "mapIdDecimal": 30,
    "mapName": "ROUTE_19",
    "width": 10,
    "height": 27,
    "warps": [],
    "bg_events": [
      {
        "x": 11,
        "y": 9,
        "description": "TEXT_ROUTE19_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 7,
        "name": "TEXT_ROUTE19_COOLTRAINER_M1"
      },
      {
        "x": 13,
        "y": 7,
        "name": "TEXT_ROUTE19_COOLTRAINER_M2"
      },
      {
        "x": 13,
        "y": 25,
        "name": "TEXT_ROUTE19_SWIMMER1"
      },
      {
        "x": 4,
        "y": 27,
        "name": "TEXT_ROUTE19_SWIMMER2"
      },
      {
        "x": 16,
        "y": 31,
        "name": "TEXT_ROUTE19_SWIMMER3"
      },
      {
        "x": 9,
        "y": 11,
        "name": "TEXT_ROUTE19_SWIMMER4"
      },
      {
        "x": 8,
        "y": 43,
        "name": "TEXT_ROUTE19_SWIMMER5"
      },
      {
        "x": 11,
        "y": 43,
        "name": "TEXT_ROUTE19_SWIMMER6"
      },
      {
        "x": 9,
        "y": 42,
        "name": "TEXT_ROUTE19_SWIMMER7"
      },
      {
        "x": 10,
        "y": 44,
        "name": "TEXT_ROUTE19_SWIMMER8"
      }
    ]
  },
  "31": {
    "mapIdHex": "0x1F",
    "mapIdDecimal": 31,
    "mapName": "ROUTE_20",
    "width": 50,
    "height": 9,
    "warps": [
      {
        "x": 48,
        "y": 5,
        "targetMap": "SEAFOAM_ISLANDS_1F",
        "targetWarpId": 1
      },
      {
        "x": 58,
        "y": 9,
        "targetMap": "SEAFOAM_ISLANDS_1F",
        "targetWarpId": 3
      }
    ],
    "bg_events": [
      {
        "x": 51,
        "y": 7,
        "description": "TEXT_ROUTE20_SEAFOAM_ISLANDS_WEST_SIGN"
      },
      {
        "x": 57,
        "y": 11,
        "description": "TEXT_ROUTE20_SEAFOAM_ISLANDS_EAST_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 87,
        "y": 8,
        "name": "TEXT_ROUTE20_SWIMMER1"
      },
      {
        "x": 68,
        "y": 11,
        "name": "TEXT_ROUTE20_SWIMMER2"
      },
      {
        "x": 45,
        "y": 10,
        "name": "TEXT_ROUTE20_SWIMMER3"
      },
      {
        "x": 55,
        "y": 14,
        "name": "TEXT_ROUTE20_SWIMMER4"
      },
      {
        "x": 38,
        "y": 13,
        "name": "TEXT_ROUTE20_SWIMMER5"
      },
      {
        "x": 87,
        "y": 13,
        "name": "TEXT_ROUTE20_SWIMMER6"
      },
      {
        "x": 34,
        "y": 9,
        "name": "TEXT_ROUTE20_COOLTRAINER_M"
      },
      {
        "x": 25,
        "y": 7,
        "name": "TEXT_ROUTE20_SWIMMER7"
      },
      {
        "x": 24,
        "y": 12,
        "name": "TEXT_ROUTE20_SWIMMER8"
      },
      {
        "x": 15,
        "y": 8,
        "name": "TEXT_ROUTE20_SWIMMER9"
      }
    ]
  },
  "32": {
    "mapIdHex": "0x20",
    "mapIdDecimal": 32,
    "mapName": "ROUTE_21",
    "width": 10,
    "height": 45,
    "warps": [],
    "npc_events": [
      {
        "x": 4,
        "y": 24,
        "name": "TEXT_ROUTE21_FISHER1"
      },
      {
        "x": 6,
        "y": 25,
        "name": "TEXT_ROUTE21_FISHER2"
      },
      {
        "x": 10,
        "y": 31,
        "name": "TEXT_ROUTE21_SWIMMER1"
      },
      {
        "x": 12,
        "y": 30,
        "name": "TEXT_ROUTE21_SWIMMER2"
      },
      {
        "x": 16,
        "y": 63,
        "name": "TEXT_ROUTE21_SWIMMER3"
      },
      {
        "x": 5,
        "y": 71,
        "name": "TEXT_ROUTE21_SWIMMER4"
      },
      {
        "x": 15,
        "y": 71,
        "name": "TEXT_ROUTE21_SWIMMER5"
      },
      {
        "x": 14,
        "y": 56,
        "name": "TEXT_ROUTE21_FISHER3"
      },
      {
        "x": 17,
        "y": 57,
        "name": "TEXT_ROUTE21_FISHER4"
      }
    ]
  },
  "33": {
    "mapIdHex": "0x21",
    "mapIdDecimal": 33,
    "mapName": "ROUTE_22",
    "width": 20,
    "height": 9,
    "warps": [
      {
        "x": 8,
        "y": 5,
        "targetMap": "ROUTE_22_GATE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 7,
        "y": 11,
        "description": "TEXT_ROUTE22_POKEMON_LEAGUE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 25,
        "y": 5,
        "name": "TEXT_ROUTE22_RIVAL1"
      },
      {
        "x": 25,
        "y": 5,
        "name": "TEXT_ROUTE22_RIVAL2"
      }
    ]
  },
  "34": {
    "mapIdHex": "0x22",
    "mapIdDecimal": 34,
    "mapName": "ROUTE_23",
    "width": 10,
    "height": 72,
    "warps": [
      {
        "x": 7,
        "y": 139,
        "targetMap": "ROUTE_22_GATE",
        "targetWarpId": 3
      },
      {
        "x": 8,
        "y": 139,
        "targetMap": "ROUTE_22_GATE",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 31,
        "targetMap": "VICTORY_ROAD_1F",
        "targetWarpId": 1
      },
      {
        "x": 14,
        "y": 31,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 2
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 33,
        "description": "TEXT_ROUTE23_VICTORY_ROAD_GATE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 35,
        "name": "TEXT_ROUTE23_GUARD1"
      },
      {
        "x": 10,
        "y": 56,
        "name": "TEXT_ROUTE23_GUARD2"
      },
      {
        "x": 8,
        "y": 85,
        "name": "TEXT_ROUTE23_SWIMMER1"
      },
      {
        "x": 11,
        "y": 96,
        "name": "TEXT_ROUTE23_SWIMMER2"
      },
      {
        "x": 12,
        "y": 105,
        "name": "TEXT_ROUTE23_GUARD3"
      },
      {
        "x": 8,
        "y": 119,
        "name": "TEXT_ROUTE23_GUARD4"
      },
      {
        "x": 8,
        "y": 136,
        "name": "TEXT_ROUTE23_GUARD5"
      }
    ]
  },
  "35": {
    "mapIdHex": "0x23",
    "mapIdDecimal": 35,
    "mapName": "ROUTE_24",
    "width": 10,
    "height": 18,
    "warps": [],
    "npc_events": [
      {
        "x": 11,
        "y": 15,
        "name": "TEXT_ROUTE24_COOLTRAINER_M1"
      },
      {
        "x": 5,
        "y": 20,
        "name": "TEXT_ROUTE24_COOLTRAINER_M2"
      },
      {
        "x": 11,
        "y": 19,
        "name": "TEXT_ROUTE24_COOLTRAINER_M3"
      },
      {
        "x": 10,
        "y": 22,
        "name": "TEXT_ROUTE24_COOLTRAINER_F1"
      },
      {
        "x": 11,
        "y": 25,
        "name": "TEXT_ROUTE24_YOUNGSTER1"
      },
      {
        "x": 10,
        "y": 28,
        "name": "TEXT_ROUTE24_COOLTRAINER_F2"
      },
      {
        "x": 11,
        "y": 31,
        "name": "TEXT_ROUTE24_YOUNGSTER2"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_ROUTE24_TM_THUNDER_WAVE"
      }
    ]
  },
  "36": {
    "mapIdHex": "0x24",
    "mapIdDecimal": 36,
    "mapName": "ROUTE_25",
    "width": 30,
    "height": 9,
    "warps": [
      {
        "x": 45,
        "y": 3,
        "targetMap": "BILLS_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 43,
        "y": 3,
        "description": "TEXT_ROUTE25_BILL_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 14,
        "y": 2,
        "name": "TEXT_ROUTE25_YOUNGSTER1"
      },
      {
        "x": 18,
        "y": 5,
        "name": "TEXT_ROUTE25_YOUNGSTER2"
      },
      {
        "x": 24,
        "y": 4,
        "name": "TEXT_ROUTE25_COOLTRAINER_M"
      },
      {
        "x": 18,
        "y": 8,
        "name": "TEXT_ROUTE25_COOLTRAINER_F1"
      },
      {
        "x": 32,
        "y": 3,
        "name": "TEXT_ROUTE25_YOUNGSTER3"
      },
      {
        "x": 37,
        "y": 4,
        "name": "TEXT_ROUTE25_COOLTRAINER_F2"
      },
      {
        "x": 8,
        "y": 4,
        "name": "TEXT_ROUTE25_HIKER1"
      },
      {
        "x": 23,
        "y": 9,
        "name": "TEXT_ROUTE25_HIKER2"
      },
      {
        "x": 13,
        "y": 7,
        "name": "TEXT_ROUTE25_HIKER3"
      },
      {
        "x": 22,
        "y": 2,
        "name": "TEXT_ROUTE25_TM_SEISMIC_TOSS"
      }
    ]
  },
  "37": {
    "mapIdHex": "0x25",
    "mapIdDecimal": 37,
    "mapName": "REDS_HOUSE_1F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "REDS_HOUSE_2F",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 1,
        "description": "TEXT_REDSHOUSE1F_TV"
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_REDSHOUSE1F_MOM"
      }
    ]
  },
  "38": {
    "mapIdHex": "0x26",
    "mapIdDecimal": 38,
    "mapName": "REDS_HOUSE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 1,
        "targetMap": "REDS_HOUSE_1F",
        "targetWarpId": 3
      }
    ]
  },
  "39": {
    "mapIdHex": "0x27",
    "mapIdDecimal": 39,
    "mapName": "BLUES_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_BLUESHOUSE_DAISY_SITTING"
      },
      {
        "x": 6,
        "y": 4,
        "name": "TEXT_BLUESHOUSE_DAISY_WALKING"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_BLUESHOUSE_TOWN_MAP"
      }
    ]
  },
  "40": {
    "mapIdHex": "0x28",
    "mapIdDecimal": 40,
    "mapName": "OAKS_LAB",
    "width": 5,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_OAKSLAB_RIVAL"
      },
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_OAKSLAB_CHARMANDER_POKE_BALL"
      },
      {
        "x": 7,
        "y": 3,
        "name": "TEXT_OAKSLAB_SQUIRTLE_POKE_BALL"
      },
      {
        "x": 8,
        "y": 3,
        "name": "TEXT_OAKSLAB_BULBASAUR_POKE_BALL"
      },
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_OAKSLAB_OAK1"
      },
      {
        "x": 2,
        "y": 1,
        "name": "TEXT_OAKSLAB_POKEDEX1"
      },
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_OAKSLAB_POKEDEX2"
      },
      {
        "x": 5,
        "y": 10,
        "name": "TEXT_OAKSLAB_OAK2"
      },
      {
        "x": 1,
        "y": 9,
        "name": "TEXT_OAKSLAB_GIRL"
      },
      {
        "x": 2,
        "y": 10,
        "name": "TEXT_OAKSLAB_SCIENTIST1"
      },
      {
        "x": 8,
        "y": 10,
        "name": "TEXT_OAKSLAB_SCIENTIST2"
      }
    ]
  },
  "41": {
    "mapIdHex": "0x29",
    "mapIdDecimal": 41,
    "mapName": "VIRIDIAN_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_VIRIDIANPOKECENTER_NURSE"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_VIRIDIANPOKECENTER_GENTLEMAN"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_VIRIDIANPOKECENTER_COOLTRAINER_M"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_VIRIDIANPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "42": {
    "mapIdHex": "0x2A",
    "mapIdDecimal": 42,
    "mapName": "VIRIDIAN_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_VIRIDIANMART_CLERK"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_VIRIDIANMART_YOUNGSTER"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_VIRIDIANMART_COOLTRAINER_M"
      }
    ]
  },
  "43": {
    "mapIdHex": "0x2B",
    "mapIdDecimal": 43,
    "mapName": "VIRIDIAN_SCHOOL_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_VIRIDIANSCHOOLHOUSE_BRUNETTE_GIRL"
      },
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_VIRIDIANSCHOOLHOUSE_COOLTRAINER_F"
      }
    ]
  },
  "44": {
    "mapIdHex": "0x2C",
    "mapIdDecimal": 44,
    "mapName": "VIRIDIAN_NICKNAME_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_VIRIDIANNICKNAMEHOUSE_BALDING_GUY"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_VIRIDIANNICKNAMEHOUSE_LITTLE_GIRL"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_VIRIDIANNICKNAMEHOUSE_SPEAROW"
      },
      {
        "x": 4,
        "y": 0,
        "name": "TEXT_VIRIDIANNICKNAMEHOUSE_SPEARY_SIGN"
      }
    ]
  },
  "45": {
    "mapIdHex": "0x2D",
    "mapIdDecimal": 45,
    "mapName": "VIRIDIAN_GYM",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 16,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 17,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 1,
        "name": "TEXT_VIRIDIANGYM_GIOVANNI"
      },
      {
        "x": 12,
        "y": 7,
        "name": "TEXT_VIRIDIANGYM_COOLTRAINER_M1"
      },
      {
        "x": 11,
        "y": 11,
        "name": "TEXT_VIRIDIANGYM_HIKER1"
      },
      {
        "x": 10,
        "y": 7,
        "name": "TEXT_VIRIDIANGYM_ROCKER1"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_VIRIDIANGYM_HIKER2"
      },
      {
        "x": 13,
        "y": 5,
        "name": "TEXT_VIRIDIANGYM_COOLTRAINER_M2"
      },
      {
        "x": 10,
        "y": 1,
        "name": "TEXT_VIRIDIANGYM_HIKER3"
      },
      {
        "x": 2,
        "y": 16,
        "name": "TEXT_VIRIDIANGYM_ROCKER2"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_VIRIDIANGYM_COOLTRAINER_M3"
      },
      {
        "x": 16,
        "y": 15,
        "name": "TEXT_VIRIDIANGYM_GYM_GUIDE"
      },
      {
        "x": 16,
        "y": 9,
        "name": "TEXT_VIRIDIANGYM_REVIVE"
      }
    ]
  },
  "46": {
    "mapIdHex": "0x2E",
    "mapIdDecimal": 46,
    "mapName": "DIGLETTS_CAVE_ROUTE_2",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "DIGLETTS_CAVE",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_DIGLETTSCAVEROUTE2_FISHING_GURU"
      }
    ]
  },
  "47": {
    "mapIdHex": "0x2F",
    "mapIdDecimal": 47,
    "mapName": "VIRIDIAN_FOREST_NORTH_GATE",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "VIRIDIAN_FOREST",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "VIRIDIAN_FOREST",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 2,
        "name": "TEXT_VIRIDIANFORESTNORTHGATE_SUPER_NERD"
      },
      {
        "x": 2,
        "y": 5,
        "name": "TEXT_VIRIDIANFORESTNORTHGATE_GRAMPS"
      }
    ]
  },
  "48": {
    "mapIdHex": "0x30",
    "mapIdDecimal": 48,
    "mapName": "ROUTE_2_TRADE_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_ROUTE2TRADEHOUSE_SCIENTIST"
      },
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_ROUTE2TRADEHOUSE_GAMEBOY_KID"
      }
    ]
  },
  "49": {
    "mapIdHex": "0x31",
    "mapIdDecimal": 49,
    "mapName": "ROUTE_2_GATE",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_ROUTE2GATE_OAKS_AIDE"
      },
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_ROUTE2GATE_YOUNGSTER"
      }
    ]
  },
  "50": {
    "mapIdHex": "0x32",
    "mapIdDecimal": 50,
    "mapName": "VIRIDIAN_FOREST_SOUTH_GATE",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 0,
        "targetMap": "VIRIDIAN_FOREST",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "VIRIDIAN_FOREST",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 4,
        "name": "TEXT_VIRIDIANFORESTSOUTHGATE_GIRL"
      },
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_VIRIDIANFORESTSOUTHGATE_LITTLE_GIRL"
      }
    ]
  },
  "51": {
    "mapIdHex": "0x33",
    "mapIdDecimal": 51,
    "mapName": "VIRIDIAN_FOREST",
    "width": 17,
    "height": 24,
    "warps": [
      {
        "x": 1,
        "y": 0,
        "targetMap": "VIRIDIAN_FOREST_NORTH_GATE",
        "targetWarpId": 3
      },
      {
        "x": 2,
        "y": 0,
        "targetMap": "VIRIDIAN_FOREST_NORTH_GATE",
        "targetWarpId": 4
      },
      {
        "x": 15,
        "y": 47,
        "targetMap": "VIRIDIAN_FOREST_SOUTH_GATE",
        "targetWarpId": 2
      },
      {
        "x": 16,
        "y": 47,
        "targetMap": "VIRIDIAN_FOREST_SOUTH_GATE",
        "targetWarpId": 2
      },
      {
        "x": 17,
        "y": 47,
        "targetMap": "VIRIDIAN_FOREST_SOUTH_GATE",
        "targetWarpId": 2
      },
      {
        "x": 18,
        "y": 47,
        "targetMap": "VIRIDIAN_FOREST_SOUTH_GATE",
        "targetWarpId": 2
      }
    ],
    "bg_events": [
      {
        "x": 24,
        "y": 40,
        "description": "TEXT_VIRIDIANFOREST_TRAINER_TIPS1"
      },
      {
        "x": 16,
        "y": 32,
        "description": "TEXT_VIRIDIANFOREST_USE_ANTIDOTE_SIGN"
      },
      {
        "x": 26,
        "y": 17,
        "description": "TEXT_VIRIDIANFOREST_TRAINER_TIPS2"
      },
      {
        "x": 4,
        "y": 24,
        "description": "TEXT_VIRIDIANFOREST_TRAINER_TIPS3"
      },
      {
        "x": 18,
        "y": 45,
        "description": "TEXT_VIRIDIANFOREST_TRAINER_TIPS4"
      },
      {
        "x": 2,
        "y": 1,
        "description": "TEXT_VIRIDIANFOREST_LEAVING_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 16,
        "y": 43,
        "name": "TEXT_VIRIDIANFOREST_YOUNGSTER1"
      },
      {
        "x": 30,
        "y": 33,
        "name": "TEXT_VIRIDIANFOREST_YOUNGSTER2"
      },
      {
        "x": 30,
        "y": 19,
        "name": "TEXT_VIRIDIANFOREST_YOUNGSTER3"
      },
      {
        "x": 2,
        "y": 18,
        "name": "TEXT_VIRIDIANFOREST_YOUNGSTER4"
      },
      {
        "x": 25,
        "y": 11,
        "name": "TEXT_VIRIDIANFOREST_ANTIDOTE"
      },
      {
        "x": 12,
        "y": 29,
        "name": "TEXT_VIRIDIANFOREST_POTION"
      },
      {
        "x": 1,
        "y": 31,
        "name": "TEXT_VIRIDIANFOREST_POKE_BALL"
      },
      {
        "x": 27,
        "y": 40,
        "name": "TEXT_VIRIDIANFOREST_YOUNGSTER5"
      }
    ]
  },
  "52": {
    "mapIdHex": "0x34",
    "mapIdDecimal": 52,
    "mapName": "MUSEUM_1F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 10,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 17,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 7,
        "targetMap": "MUSEUM_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 4,
        "name": "TEXT_MUSEUM1F_SCIENTIST1"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_MUSEUM1F_GAMBLER"
      },
      {
        "x": 15,
        "y": 2,
        "name": "TEXT_MUSEUM1F_SCIENTIST2"
      },
      {
        "x": 17,
        "y": 4,
        "name": "TEXT_MUSEUM1F_SCIENTIST3"
      },
      {
        "x": 16,
        "y": 2,
        "name": "TEXT_MUSEUM1F_OLD_AMBER"
      }
    ]
  },
  "53": {
    "mapIdHex": "0x35",
    "mapIdDecimal": 53,
    "mapName": "MUSEUM_2F",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "MUSEUM_1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 11,
        "y": 2,
        "description": "TEXT_MUSEUM2F_SPACE_SHUTTLE_SIGN"
      },
      {
        "x": 2,
        "y": 5,
        "description": "TEXT_MUSEUM2F_MOON_STONE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 7,
        "name": "TEXT_MUSEUM2F_YOUNGSTER"
      },
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_MUSEUM2F_GRAMPS"
      },
      {
        "x": 7,
        "y": 5,
        "name": "TEXT_MUSEUM2F_SCIENTIST"
      },
      {
        "x": 11,
        "y": 5,
        "name": "TEXT_MUSEUM2F_BRUNETTE_GIRL"
      },
      {
        "x": 12,
        "y": 5,
        "name": "TEXT_MUSEUM2F_HIKER"
      }
    ]
  },
  "54": {
    "mapIdHex": "0x36",
    "mapIdDecimal": 54,
    "mapName": "PEWTER_GYM",
    "width": 5,
    "height": 7,
    "warps": [
      {
        "x": 4,
        "y": 13,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 13,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_PEWTERGYM_BROCK"
      },
      {
        "x": 3,
        "y": 6,
        "name": "TEXT_PEWTERGYM_COOLTRAINER_M"
      },
      {
        "x": 7,
        "y": 10,
        "name": "TEXT_PEWTERGYM_GYM_GUIDE"
      }
    ]
  },
  "55": {
    "mapIdHex": "0x37",
    "mapIdDecimal": 55,
    "mapName": "PEWTER_NIDORAN_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 5,
        "name": "TEXT_PEWTERNIDORANHOUSE_NIDORAN"
      },
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_PEWTERNIDORANHOUSE_LITTLE_BOY"
      },
      {
        "x": 1,
        "y": 2,
        "name": "TEXT_PEWTERNIDORANHOUSE_MIDDLE_AGED_MAN"
      }
    ]
  },
  "56": {
    "mapIdHex": "0x38",
    "mapIdDecimal": 56,
    "mapName": "PEWTER_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_PEWTERMART_CLERK"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_PEWTERMART_YOUNGSTER"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_PEWTERMART_SUPER_NERD"
      }
    ]
  },
  "57": {
    "mapIdHex": "0x39",
    "mapIdDecimal": 57,
    "mapName": "PEWTER_SPEECH_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_PEWTERSPEECHHOUSE_GAMBLER"
      },
      {
        "x": 4,
        "y": 5,
        "name": "TEXT_PEWTERSPEECHHOUSE_YOUNGSTER"
      }
    ]
  },
  "58": {
    "mapIdHex": "0x3A",
    "mapIdDecimal": 58,
    "mapName": "PEWTER_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_PEWTERPOKECENTER_NURSE"
      },
      {
        "x": 11,
        "y": 7,
        "name": "TEXT_PEWTERPOKECENTER_GENTLEMAN"
      },
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_PEWTERPOKECENTER_JIGGLYPUFF"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_PEWTERPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "59": {
    "mapIdHex": "0x3B",
    "mapIdDecimal": 59,
    "mapName": "MT_MOON_1F",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 14,
        "y": 35,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 15,
        "y": 35,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 5,
        "y": 5,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 1
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 3
      },
      {
        "x": 25,
        "y": 15,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 15,
        "y": 23,
        "description": "TEXT_MTMOON1F_BEWARE_ZUBAT_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_MTMOON1F_HIKER"
      },
      {
        "x": 12,
        "y": 16,
        "name": "TEXT_MTMOON1F_YOUNGSTER1"
      },
      {
        "x": 30,
        "y": 4,
        "name": "TEXT_MTMOON1F_COOLTRAINER_F1"
      },
      {
        "x": 24,
        "y": 31,
        "name": "TEXT_MTMOON1F_SUPER_NERD"
      },
      {
        "x": 16,
        "y": 23,
        "name": "TEXT_MTMOON1F_COOLTRAINER_F2"
      },
      {
        "x": 7,
        "y": 22,
        "name": "TEXT_MTMOON1F_YOUNGSTER2"
      },
      {
        "x": 30,
        "y": 27,
        "name": "TEXT_MTMOON1F_YOUNGSTER3"
      },
      {
        "x": 2,
        "y": 20,
        "name": "TEXT_MTMOON1F_POTION1"
      },
      {
        "x": 2,
        "y": 2,
        "name": "TEXT_MTMOON1F_MOON_STONE"
      },
      {
        "x": 35,
        "y": 31,
        "name": "TEXT_MTMOON1F_RARE_CANDY"
      },
      {
        "x": 36,
        "y": 23,
        "name": "TEXT_MTMOON1F_ESCAPE_ROPE"
      },
      {
        "x": 20,
        "y": 33,
        "name": "TEXT_MTMOON1F_POTION2"
      },
      {
        "x": 5,
        "y": 32,
        "name": "TEXT_MTMOON1F_TM_WATER_GUN"
      }
    ]
  },
  "60": {
    "mapIdHex": "0x3C",
    "mapIdDecimal": 60,
    "mapName": "MT_MOON_B1F",
    "width": 14,
    "height": 14,
    "warps": [
      {
        "x": 5,
        "y": 5,
        "targetMap": "MT_MOON_1F",
        "targetWarpId": 3
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "MT_MOON_B2F",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 9,
        "targetMap": "MT_MOON_1F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 15,
        "targetMap": "MT_MOON_1F",
        "targetWarpId": 5
      },
      {
        "x": 21,
        "y": 17,
        "targetMap": "MT_MOON_B2F",
        "targetWarpId": 2
      },
      {
        "x": 13,
        "y": 27,
        "targetMap": "MT_MOON_B2F",
        "targetWarpId": 3
      },
      {
        "x": 23,
        "y": 3,
        "targetMap": "MT_MOON_B2F",
        "targetWarpId": 4
      },
      {
        "x": 27,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ]
  },
  "61": {
    "mapIdHex": "0x3D",
    "mapIdDecimal": 61,
    "mapName": "MT_MOON_B2F",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 25,
        "y": 9,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 2
      },
      {
        "x": 21,
        "y": 17,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 5
      },
      {
        "x": 15,
        "y": 27,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 6
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "MT_MOON_B1F",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 8,
        "name": "TEXT_MTMOONB2F_SUPER_NERD"
      },
      {
        "x": 11,
        "y": 16,
        "name": "TEXT_MTMOONB2F_ROCKET1"
      },
      {
        "x": 15,
        "y": 22,
        "name": "TEXT_MTMOONB2F_ROCKET2"
      },
      {
        "x": 29,
        "y": 11,
        "name": "TEXT_MTMOONB2F_ROCKET3"
      },
      {
        "x": 29,
        "y": 17,
        "name": "TEXT_MTMOONB2F_ROCKET4"
      },
      {
        "x": 12,
        "y": 6,
        "name": "TEXT_MTMOONB2F_DOME_FOSSIL"
      },
      {
        "x": 13,
        "y": 6,
        "name": "TEXT_MTMOONB2F_HELIX_FOSSIL"
      },
      {
        "x": 25,
        "y": 21,
        "name": "TEXT_MTMOONB2F_HP_UP"
      },
      {
        "x": 29,
        "y": 5,
        "name": "TEXT_MTMOONB2F_TM_MEGA_PUNCH"
      }
    ]
  },
  "62": {
    "mapIdHex": "0x3E",
    "mapIdDecimal": 62,
    "mapName": "CERULEAN_TRASHED_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 0,
        "description": "TEXT_CERULEANTRASHEDHOUSE_WALL_HOLE"
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 1,
        "name": "TEXT_CERULEANTRASHEDHOUSE_FISHING_GURU"
      },
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_CERULEANTRASHEDHOUSE_GIRL"
      }
    ]
  },
  "63": {
    "mapIdHex": "0x3F",
    "mapIdDecimal": 63,
    "mapName": "CERULEAN_TRADE_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_CERULEANTRADEHOUSE_GRANNY"
      },
      {
        "x": 1,
        "y": 2,
        "name": "TEXT_CERULEANTRADEHOUSE_GAMBLER"
      }
    ]
  },
  "64": {
    "mapIdHex": "0x40",
    "mapIdDecimal": 64,
    "mapName": "CERULEAN_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_CERULEANPOKECENTER_NURSE"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_CERULEANPOKECENTER_SUPER_NERD"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_CERULEANPOKECENTER_GENTLEMAN"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_CERULEANPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "65": {
    "mapIdHex": "0x41",
    "mapIdDecimal": 65,
    "mapName": "CERULEAN_GYM",
    "width": 5,
    "height": 7,
    "warps": [
      {
        "x": 4,
        "y": 13,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 13,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_CERULEANGYM_MISTY"
      },
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_CERULEANGYM_COOLTRAINER_F"
      },
      {
        "x": 8,
        "y": 7,
        "name": "TEXT_CERULEANGYM_SWIMMER"
      },
      {
        "x": 7,
        "y": 10,
        "name": "TEXT_CERULEANGYM_GYM_GUIDE"
      }
    ]
  },
  "66": {
    "mapIdHex": "0x42",
    "mapIdDecimal": 66,
    "mapName": "BIKE_SHOP",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_BIKESHOP_CLERK"
      },
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_BIKESHOP_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_BIKESHOP_YOUNGSTER"
      }
    ]
  },
  "67": {
    "mapIdHex": "0x43",
    "mapIdDecimal": 67,
    "mapName": "CERULEAN_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_CERULEANMART_CLERK"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_CERULEANMART_COOLTRAINER_M"
      },
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_CERULEANMART_COOLTRAINER_F"
      }
    ]
  },
  "68": {
    "mapIdHex": "0x44",
    "mapIdDecimal": 68,
    "mapName": "MT_MOON_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_MTMOONPOKECENTER_NURSE"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_MTMOONPOKECENTER_YOUNGSTER"
      },
      {
        "x": 7,
        "y": 3,
        "name": "TEXT_MTMOONPOKECENTER_GENTLEMAN"
      },
      {
        "x": 10,
        "y": 6,
        "name": "TEXT_MTMOONPOKECENTER_MAGIKARP_SALESMAN"
      },
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_MTMOONPOKECENTER_CLIPBOARD"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_MTMOONPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "69": {
    "mapIdHex": "0x45",
    "mapIdDecimal": 69,
    "mapName": "CERULEAN_TRASHED_HOUSE_COPY",
    "width": 4,
    "height": 4
  },
  "70": {
    "mapIdHex": "0x46",
    "mapIdDecimal": 70,
    "mapName": "ROUTE_5_GATE",
    "width": 4,
    "height": 3,
    "warps": [
      {
        "x": 3,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_ROUTE5GATE_GUARD"
      }
    ]
  },
  "71": {
    "mapIdHex": "0x47",
    "mapIdDecimal": 71,
    "mapName": "UNDERGROUND_PATH_ROUTE_5",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_NORTH_SOUTH",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_UNDERGROUNDPATHROUTE5_LITTLE_GIRL"
      }
    ]
  },
  "72": {
    "mapIdHex": "0x48",
    "mapIdDecimal": 72,
    "mapName": "DAYCARE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_DAYCARE_GENTLEMAN"
      }
    ]
  },
  "73": {
    "mapIdHex": "0x49",
    "mapIdDecimal": 73,
    "mapName": "ROUTE_6_GATE",
    "width": 4,
    "height": 3,
    "warps": [
      {
        "x": 3,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_ROUTE6GATE_GUARD"
      }
    ]
  },
  "74": {
    "mapIdHex": "0x4A",
    "mapIdDecimal": 74,
    "mapName": "UNDERGROUND_PATH_ROUTE_6",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_NORTH_SOUTH",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_UNDERGROUNDPATHROUTE6_GIRL"
      }
    ]
  },
  "75": {
    "mapIdHex": "0x4B",
    "mapIdDecimal": 75,
    "mapName": "UNDERGROUND_PATH_ROUTE_6_COPY",
    "width": 4,
    "height": 4
  },
  "76": {
    "mapIdHex": "0x4C",
    "mapIdDecimal": 76,
    "mapName": "ROUTE_7_GATE",
    "width": 3,
    "height": 4,
    "warps": [
      {
        "x": 0,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 0,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_ROUTE7GATE_GUARD"
      }
    ]
  },
  "77": {
    "mapIdHex": "0x4D",
    "mapIdDecimal": 77,
    "mapName": "UNDERGROUND_PATH_ROUTE_7",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_WEST_EAST",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_UNDERGROUNDPATHROUTE7_MIDDLE_AGED_MAN"
      }
    ]
  },
  "78": {
    "mapIdHex": "0x4E",
    "mapIdDecimal": 78,
    "mapName": "UNDERGROUND_PATH_ROUTE_7_COPY",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_WEST_EAST",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 2,
        "name": "TEXT_UNDERGROUNDPATHROUTE7COPY_UNUSED_GIRL"
      },
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_UNDERGROUNDPATHROUTE7COPY_UNUSED_MIDDLE_AGED_MAN"
      }
    ]
  },
  "79": {
    "mapIdHex": "0x4F",
    "mapIdDecimal": 79,
    "mapName": "ROUTE_8_GATE",
    "width": 3,
    "height": 4,
    "warps": [
      {
        "x": 0,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 0,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 5,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 1,
        "name": "TEXT_ROUTE8GATE_GUARD"
      }
    ]
  },
  "80": {
    "mapIdHex": "0x50",
    "mapIdDecimal": 80,
    "mapName": "UNDERGROUND_PATH_ROUTE_8",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_WEST_EAST",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_UNDERGROUNDPATHROUTE8_GIRL"
      }
    ]
  },
  "81": {
    "mapIdHex": "0x51",
    "mapIdDecimal": 81,
    "mapName": "ROCK_TUNNEL_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_ROCKTUNNELPOKECENTER_NURSE"
      },
      {
        "x": 7,
        "y": 3,
        "name": "TEXT_ROCKTUNNELPOKECENTER_GENTLEMAN"
      },
      {
        "x": 2,
        "y": 5,
        "name": "TEXT_ROCKTUNNELPOKECENTER_FISHER"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_ROCKTUNNELPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "82": {
    "mapIdHex": "0x52",
    "mapIdDecimal": 82,
    "mapName": "ROCK_TUNNEL_1F",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 15,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 15,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 15,
        "y": 33,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 15,
        "y": 35,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 37,
        "y": 3,
        "targetMap": "ROCK_TUNNEL_B1F",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 3,
        "targetMap": "ROCK_TUNNEL_B1F",
        "targetWarpId": 2
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "ROCK_TUNNEL_B1F",
        "targetWarpId": 3
      },
      {
        "x": 37,
        "y": 17,
        "targetMap": "ROCK_TUNNEL_B1F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 11,
        "y": 29,
        "description": "TEXT_ROCKTUNNEL1F_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 5,
        "name": "TEXT_ROCKTUNNEL1F_HIKER1"
      },
      {
        "x": 5,
        "y": 16,
        "name": "TEXT_ROCKTUNNEL1F_HIKER2"
      },
      {
        "x": 17,
        "y": 15,
        "name": "TEXT_ROCKTUNNEL1F_HIKER3"
      },
      {
        "x": 23,
        "y": 8,
        "name": "TEXT_ROCKTUNNEL1F_SUPER_NERD"
      },
      {
        "x": 37,
        "y": 21,
        "name": "TEXT_ROCKTUNNEL1F_COOLTRAINER_F1"
      },
      {
        "x": 22,
        "y": 24,
        "name": "TEXT_ROCKTUNNEL1F_COOLTRAINER_F2"
      },
      {
        "x": 32,
        "y": 24,
        "name": "TEXT_ROCKTUNNEL1F_COOLTRAINER_F3"
      }
    ]
  },
  "83": {
    "mapIdHex": "0x53",
    "mapIdDecimal": 83,
    "mapName": "POWER_PLANT",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 4,
        "y": 35,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 35,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 0,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 9,
        "y": 20,
        "name": "TEXT_POWERPLANT_VOLTORB1"
      },
      {
        "x": 32,
        "y": 18,
        "name": "TEXT_POWERPLANT_VOLTORB2"
      },
      {
        "x": 21,
        "y": 25,
        "name": "TEXT_POWERPLANT_VOLTORB3"
      },
      {
        "x": 25,
        "y": 18,
        "name": "TEXT_POWERPLANT_ELECTRODE1"
      },
      {
        "x": 23,
        "y": 34,
        "name": "TEXT_POWERPLANT_VOLTORB4"
      },
      {
        "x": 26,
        "y": 28,
        "name": "TEXT_POWERPLANT_VOLTORB5"
      },
      {
        "x": 21,
        "y": 14,
        "name": "TEXT_POWERPLANT_ELECTRODE2"
      },
      {
        "x": 37,
        "y": 32,
        "name": "TEXT_POWERPLANT_VOLTORB6"
      },
      {
        "x": 4,
        "y": 9,
        "name": "TEXT_POWERPLANT_ZAPDOS"
      },
      {
        "x": 7,
        "y": 25,
        "name": "TEXT_POWERPLANT_CARBOS"
      },
      {
        "x": 28,
        "y": 3,
        "name": "TEXT_POWERPLANT_HP_UP"
      },
      {
        "x": 34,
        "y": 3,
        "name": "TEXT_POWERPLANT_RARE_CANDY"
      },
      {
        "x": 26,
        "y": 32,
        "name": "TEXT_POWERPLANT_TM_THUNDER"
      },
      {
        "x": 20,
        "y": 32,
        "name": "TEXT_POWERPLANT_TM_REFLECT"
      }
    ]
  },
  "84": {
    "mapIdHex": "0x54",
    "mapIdDecimal": 84,
    "mapName": "ROUTE_11_GATE_1F",
    "width": 4,
    "height": 5,
    "warps": [
      {
        "x": 0,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 0,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 6,
        "y": 8,
        "targetMap": "ROUTE_11_GATE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_ROUTE11GATE1F_GUARD"
      }
    ]
  },
  "85": {
    "mapIdHex": "0x55",
    "mapIdDecimal": 85,
    "mapName": "DIGLETTS_CAVE_ROUTE_11",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 4,
        "targetMap": "DIGLETTS_CAVE",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_DIGLETTSCAVEROUTE11_GAMBLER"
      }
    ]
  },
  "86": {
    "mapIdHex": "0x56",
    "mapIdDecimal": 86,
    "mapName": "ROUTE_11_GATE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "ROUTE_11_GATE_1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 2,
        "description": "TEXT_ROUTE11GATE2F_LEFT_BINOCULARS"
      },
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_ROUTE11GATE2F_RIGHT_BINOCULARS"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_ROUTE11GATE2F_YOUNGSTER"
      },
      {
        "x": 2,
        "y": 6,
        "name": "TEXT_ROUTE11GATE2F_OAKS_AIDE"
      }
    ]
  },
  "87": {
    "mapIdHex": "0x57",
    "mapIdDecimal": 87,
    "mapName": "ROUTE_12_GATE_1F",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 8,
        "y": 6,
        "targetMap": "ROUTE_12_GATE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_ROUTE12GATE1F_GUARD"
      }
    ]
  },
  "88": {
    "mapIdHex": "0x58",
    "mapIdDecimal": 88,
    "mapName": "BILLS_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_BILLSHOUSE_BILL_POKEMON"
      },
      {
        "x": 4,
        "y": 4,
        "name": "TEXT_BILLSHOUSE_BILL_SS_TICKET"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_BILLSHOUSE_BILL_CHECK_OUT_MY_RARE_POKEMON"
      }
    ]
  },
  "89": {
    "mapIdHex": "0x59",
    "mapIdDecimal": 89,
    "mapName": "VERMILION_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_VERMILIONPOKECENTER_NURSE"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_VERMILIONPOKECENTER_FISHING_GURU"
      },
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_VERMILIONPOKECENTER_SAILOR"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_VERMILIONPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "90": {
    "mapIdHex": "0x5A",
    "mapIdDecimal": 90,
    "mapName": "POKEMON_FAN_CLUB",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 0,
        "description": "TEXT_POKEMONFANCLUB_SIGN_1"
      },
      {
        "x": 6,
        "y": 0,
        "description": "TEXT_POKEMONFANCLUB_SIGN_2"
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_POKEMONFANCLUB_PIKACHU_FAN"
      },
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_POKEMONFANCLUB_SEEL_FAN"
      },
      {
        "x": 6,
        "y": 4,
        "name": "TEXT_POKEMONFANCLUB_PIKACHU"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_POKEMONFANCLUB_SEEL"
      },
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_POKEMONFANCLUB_CHAIRMAN"
      },
      {
        "x": 5,
        "y": 1,
        "name": "TEXT_POKEMONFANCLUB_RECEPTIONIST"
      }
    ]
  },
  "91": {
    "mapIdHex": "0x5B",
    "mapIdDecimal": 91,
    "mapName": "VERMILION_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_VERMILIONMART_CLERK"
      },
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_VERMILIONMART_COOLTRAINER_M"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_VERMILIONMART_COOLTRAINER_F"
      }
    ]
  },
  "92": {
    "mapIdHex": "0x5C",
    "mapIdDecimal": 92,
    "mapName": "VERMILION_GYM",
    "width": 5,
    "height": 9,
    "warps": [
      {
        "x": 4,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 1,
        "name": "TEXT_VERMILIONGYM_LT_SURGE"
      },
      {
        "x": 9,
        "y": 6,
        "name": "TEXT_VERMILIONGYM_GENTLEMAN"
      },
      {
        "x": 3,
        "y": 8,
        "name": "TEXT_VERMILIONGYM_SUPER_NERD"
      },
      {
        "x": 0,
        "y": 10,
        "name": "TEXT_VERMILIONGYM_SAILOR"
      },
      {
        "x": 4,
        "y": 14,
        "name": "TEXT_VERMILIONGYM_GYM_GUIDE"
      }
    ]
  },
  "93": {
    "mapIdHex": "0x5D",
    "mapIdDecimal": 93,
    "mapName": "VERMILION_PIDGEY_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_VERMILIONPIDGEYHOUSE_YOUNGSTER"
      },
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_VERMILIONPIDGEYHOUSE_PIDGEY"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_VERMILIONPIDGEYHOUSE_LETTER"
      }
    ]
  },
  "94": {
    "mapIdHex": "0x5E",
    "mapIdDecimal": 94,
    "mapName": "VERMILION_DOCK",
    "width": 14,
    "height": 6,
    "warps": [
      {
        "x": 14,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 14,
        "y": 2,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 2
      }
    ]
  },
  "95": {
    "mapIdHex": "0x5F",
    "mapIdDecimal": 95,
    "mapName": "SS_ANNE_1F",
    "width": 20,
    "height": 9,
    "warps": [
      {
        "x": 26,
        "y": 0,
        "targetMap": "VERMILION_DOCK",
        "targetWarpId": 2
      },
      {
        "x": 27,
        "y": 0,
        "targetMap": "VERMILION_DOCK",
        "targetWarpId": 2
      },
      {
        "x": 31,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 2
      },
      {
        "x": 19,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 3
      },
      {
        "x": 15,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 4
      },
      {
        "x": 11,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 5
      },
      {
        "x": 7,
        "y": 8,
        "targetMap": "SS_ANNE_1F_ROOMS",
        "targetWarpId": 6
      },
      {
        "x": 2,
        "y": 6,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 7
      },
      {
        "x": 37,
        "y": 15,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 6
      },
      {
        "x": 3,
        "y": 16,
        "targetMap": "SS_ANNE_KITCHEN",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 6,
        "name": "TEXT_SSANNE1F_WAITER"
      },
      {
        "x": 27,
        "y": 5,
        "name": "TEXT_SSANNE1F_SAILOR"
      }
    ]
  },
  "96": {
    "mapIdHex": "0x60",
    "mapIdDecimal": 96,
    "mapName": "SS_ANNE_2F",
    "width": 20,
    "height": 9,
    "warps": [
      {
        "x": 9,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 3
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 5
      },
      {
        "x": 21,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 7
      },
      {
        "x": 25,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 9
      },
      {
        "x": 29,
        "y": 11,
        "targetMap": "SS_ANNE_2F_ROOMS",
        "targetWarpId": 11
      },
      {
        "x": 2,
        "y": 4,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 9
      },
      {
        "x": 2,
        "y": 12,
        "targetMap": "SS_ANNE_3F",
        "targetWarpId": 2
      },
      {
        "x": 36,
        "y": 4,
        "targetMap": "SS_ANNE_CAPTAINS_ROOM",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_SSANNE2F_WAITER"
      },
      {
        "x": 36,
        "y": 4,
        "name": "TEXT_SSANNE2F_RIVAL"
      }
    ]
  },
  "97": {
    "mapIdHex": "0x61",
    "mapIdDecimal": 97,
    "mapName": "SS_ANNE_3F",
    "width": 10,
    "height": 3,
    "warps": [
      {
        "x": 0,
        "y": 3,
        "targetMap": "SS_ANNE_BOW",
        "targetWarpId": 1
      },
      {
        "x": 19,
        "y": 3,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 9,
        "y": 3,
        "name": "TEXT_SSANNE3F_SAILOR"
      }
    ]
  },
  "98": {
    "mapIdHex": "0x62",
    "mapIdDecimal": 98,
    "mapName": "SS_ANNE_B1F",
    "width": 15,
    "height": 4,
    "warps": [
      {
        "x": 23,
        "y": 3,
        "targetMap": "SS_ANNE_B1F_ROOMS",
        "targetWarpId": 9
      },
      {
        "x": 19,
        "y": 3,
        "targetMap": "SS_ANNE_B1F_ROOMS",
        "targetWarpId": 7
      },
      {
        "x": 15,
        "y": 3,
        "targetMap": "SS_ANNE_B1F_ROOMS",
        "targetWarpId": 5
      },
      {
        "x": 11,
        "y": 3,
        "targetMap": "SS_ANNE_B1F_ROOMS",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 3,
        "targetMap": "SS_ANNE_B1F_ROOMS",
        "targetWarpId": 1
      },
      {
        "x": 27,
        "y": 5,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 10
      }
    ]
  },
  "99": {
    "mapIdHex": "0x63",
    "mapIdDecimal": 99,
    "mapName": "SS_ANNE_BOW",
    "width": 10,
    "height": 7,
    "warps": [
      {
        "x": 13,
        "y": 6,
        "targetMap": "SS_ANNE_3F",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 7,
        "targetMap": "SS_ANNE_3F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_SSANNEBOW_SUPER_NERD"
      },
      {
        "x": 4,
        "y": 9,
        "name": "TEXT_SSANNEBOW_SAILOR1"
      },
      {
        "x": 7,
        "y": 11,
        "name": "TEXT_SSANNEBOW_COOLTRAINER_M"
      },
      {
        "x": 4,
        "y": 4,
        "name": "TEXT_SSANNEBOW_SAILOR2"
      },
      {
        "x": 10,
        "y": 8,
        "name": "TEXT_SSANNEBOW_SAILOR3"
      }
    ]
  },
  "100": {
    "mapIdHex": "0x64",
    "mapIdDecimal": 100,
    "mapName": "SS_ANNE_KITCHEN",
    "width": 7,
    "height": 8,
    "warps": [
      {
        "x": 6,
        "y": 0,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 11
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 8,
        "name": "TEXT_SSANNEKITCHEN_COOK1"
      },
      {
        "x": 5,
        "y": 8,
        "name": "TEXT_SSANNEKITCHEN_COOK2"
      },
      {
        "x": 9,
        "y": 7,
        "name": "TEXT_SSANNEKITCHEN_COOK3"
      },
      {
        "x": 13,
        "y": 6,
        "name": "TEXT_SSANNEKITCHEN_COOK4"
      },
      {
        "x": 13,
        "y": 8,
        "name": "TEXT_SSANNEKITCHEN_COOK5"
      },
      {
        "x": 13,
        "y": 10,
        "name": "TEXT_SSANNEKITCHEN_COOK6"
      },
      {
        "x": 11,
        "y": 13,
        "name": "TEXT_SSANNEKITCHEN_COOK7"
      }
    ]
  },
  "101": {
    "mapIdHex": "0x65",
    "mapIdDecimal": 101,
    "mapName": "SS_ANNE_CAPTAINS_ROOM",
    "width": 3,
    "height": 4,
    "warps": [
      {
        "x": 0,
        "y": 7,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 9
      }
    ],
    "bg_events": [
      {
        "x": 4,
        "y": 1,
        "description": "TEXT_SSANNECAPTAINSROOM_TRASH"
      },
      {
        "x": 1,
        "y": 2,
        "description": "TEXT_SSANNECAPTAINSROOM_SEASICK_BOOK"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_SSANNECAPTAINSROOM_CAPTAIN"
      }
    ]
  },
  "102": {
    "mapIdHex": "0x66",
    "mapIdDecimal": 102,
    "mapName": "SS_ANNE_1F_ROOMS",
    "width": 12,
    "height": 8,
    "warps": [
      {
        "x": 0,
        "y": 0,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 3
      },
      {
        "x": 10,
        "y": 0,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 4
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 5
      },
      {
        "x": 0,
        "y": 10,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 6
      },
      {
        "x": 10,
        "y": 10,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 7
      },
      {
        "x": 20,
        "y": 10,
        "targetMap": "SS_ANNE_1F",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_SSANNE1FROOMS_GENTLEMAN1"
      },
      {
        "x": 11,
        "y": 4,
        "name": "TEXT_SSANNE1FROOMS_GENTLEMAN2"
      },
      {
        "x": 11,
        "y": 14,
        "name": "TEXT_SSANNE1FROOMS_YOUNGSTER"
      },
      {
        "x": 13,
        "y": 11,
        "name": "TEXT_SSANNE1FROOMS_COOLTRAINER_F"
      },
      {
        "x": 22,
        "y": 3,
        "name": "TEXT_SSANNE1FROOMS_GIRL1"
      },
      {
        "x": 0,
        "y": 14,
        "name": "TEXT_SSANNE1FROOMS_MIDDLE_AGED_MAN"
      },
      {
        "x": 2,
        "y": 11,
        "name": "TEXT_SSANNE1FROOMS_LITTLE_GIRL"
      },
      {
        "x": 3,
        "y": 11,
        "name": "TEXT_SSANNE1FROOMS_WIGGLYTUFF"
      },
      {
        "x": 10,
        "y": 13,
        "name": "TEXT_SSANNE1FROOMS_GIRL2"
      },
      {
        "x": 12,
        "y": 15,
        "name": "TEXT_SSANNE1FROOMS_TM_BODY_SLAM"
      },
      {
        "x": 21,
        "y": 13,
        "name": "TEXT_SSANNE1FROOMS_GENTLEMAN3"
      }
    ]
  },
  "103": {
    "mapIdHex": "0x67",
    "mapIdDecimal": 103,
    "mapName": "SS_ANNE_2F_ROOMS",
    "width": 12,
    "height": 8,
    "warps": [
      {
        "x": 2,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 2
      },
      {
        "x": 13,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 2
      },
      {
        "x": 22,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 3
      },
      {
        "x": 23,
        "y": 5,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 3
      },
      {
        "x": 2,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 4
      },
      {
        "x": 12,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 5
      },
      {
        "x": 13,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 5
      },
      {
        "x": 22,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 6
      },
      {
        "x": 23,
        "y": 15,
        "targetMap": "SS_ANNE_2F",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_SSANNE2FROOMS_GENTLEMAN1"
      },
      {
        "x": 13,
        "y": 4,
        "name": "TEXT_SSANNE2FROOMS_FISHER"
      },
      {
        "x": 0,
        "y": 14,
        "name": "TEXT_SSANNE2FROOMS_GENTLEMAN2"
      },
      {
        "x": 2,
        "y": 11,
        "name": "TEXT_SSANNE2FROOMS_COOLTRAINER_F"
      },
      {
        "x": 1,
        "y": 2,
        "name": "TEXT_SSANNE2FROOMS_GENTLEMAN3"
      },
      {
        "x": 12,
        "y": 1,
        "name": "TEXT_SSANNE2FROOMS_MAX_ETHER"
      },
      {
        "x": 21,
        "y": 2,
        "name": "TEXT_SSANNE2FROOMS_GENTLEMAN4"
      },
      {
        "x": 22,
        "y": 1,
        "name": "TEXT_SSANNE2FROOMS_GRAMPS"
      },
      {
        "x": 0,
        "y": 12,
        "name": "TEXT_SSANNE2FROOMS_RARE_CANDY"
      },
      {
        "x": 12,
        "y": 12,
        "name": "TEXT_SSANNE2FROOMS_GENTLEMAN5"
      },
      {
        "x": 11,
        "y": 14,
        "name": "TEXT_SSANNE2FROOMS_LITTLE_BOY"
      },
      {
        "x": 22,
        "y": 12,
        "name": "TEXT_SSANNE2FROOMS_BRUNETTE_GIRL"
      },
      {
        "x": 20,
        "y": 12,
        "name": "TEXT_SSANNE2FROOMS_BEAUTY"
      }
    ]
  },
  "104": {
    "mapIdHex": "0x68",
    "mapIdDecimal": 104,
    "mapName": "SS_ANNE_B1F_ROOMS",
    "width": 12,
    "height": 8,
    "warps": [
      {
        "x": 2,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 5
      },
      {
        "x": 12,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 4
      },
      {
        "x": 13,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 4
      },
      {
        "x": 22,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 3
      },
      {
        "x": 23,
        "y": 5,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 3
      },
      {
        "x": 2,
        "y": 15,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 2
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 2
      },
      {
        "x": 12,
        "y": 15,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 15,
        "targetMap": "SS_ANNE_B1F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 13,
        "name": "TEXT_SSANNEB1FROOMS_SAILOR1"
      },
      {
        "x": 2,
        "y": 11,
        "name": "TEXT_SSANNEB1FROOMS_SAILOR2"
      },
      {
        "x": 12,
        "y": 3,
        "name": "TEXT_SSANNEB1FROOMS_SAILOR3"
      },
      {
        "x": 22,
        "y": 2,
        "name": "TEXT_SSANNEB1FROOMS_SAILOR4"
      },
      {
        "x": 0,
        "y": 2,
        "name": "TEXT_SSANNEB1FROOMS_SAILOR5"
      },
      {
        "x": 0,
        "y": 4,
        "name": "TEXT_SSANNEB1FROOMS_FISHER"
      },
      {
        "x": 10,
        "y": 13,
        "name": "TEXT_SSANNEB1FROOMS_SUPER_NERD"
      },
      {
        "x": 11,
        "y": 12,
        "name": "TEXT_SSANNEB1FROOMS_MACHOKE"
      },
      {
        "x": 20,
        "y": 2,
        "name": "TEXT_SSANNEB1FROOMS_ETHER"
      },
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_SSANNEB1FROOMS_TM_REST"
      },
      {
        "x": 12,
        "y": 11,
        "name": "TEXT_SSANNEB1FROOMS_MAX_POTION"
      }
    ]
  },
  "105": {
    "mapIdHex": "0x69",
    "mapIdDecimal": 105,
    "mapName": "UNUSED_MAP_69",
    "width": 0,
    "height": 0
  },
  "106": {
    "mapIdHex": "0x6A",
    "mapIdDecimal": 106,
    "mapName": "UNUSED_MAP_6A",
    "width": 0,
    "height": 0
  },
  "107": {
    "mapIdHex": "0x6B",
    "mapIdDecimal": 107,
    "mapName": "UNUSED_MAP_6B",
    "width": 0,
    "height": 0
  },
  "108": {
    "mapIdHex": "0x6C",
    "mapIdDecimal": 108,
    "mapName": "VICTORY_ROAD_1F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 8,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 9,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 5,
        "name": "TEXT_VICTORYROAD1F_COOLTRAINER_F"
      },
      {
        "x": 3,
        "y": 2,
        "name": "TEXT_VICTORYROAD1F_COOLTRAINER_M"
      },
      {
        "x": 11,
        "y": 0,
        "name": "TEXT_VICTORYROAD1F_TM_SKY_ATTACK"
      },
      {
        "x": 9,
        "y": 2,
        "name": "TEXT_VICTORYROAD1F_RARE_CANDY"
      },
      {
        "x": 5,
        "y": 15,
        "name": "TEXT_VICTORYROAD1F_BOULDER1"
      },
      {
        "x": 14,
        "y": 2,
        "name": "TEXT_VICTORYROAD1F_BOULDER2"
      },
      {
        "x": 2,
        "y": 10,
        "name": "TEXT_VICTORYROAD1F_BOULDER3"
      }
    ]
  },
  "109": {
    "mapIdHex": "0x6D",
    "mapIdDecimal": 109,
    "mapName": "UNUSED_MAP_6D",
    "width": 0,
    "height": 0
  },
  "110": {
    "mapIdHex": "0x6E",
    "mapIdDecimal": 110,
    "mapName": "UNUSED_MAP_6E",
    "width": 0,
    "height": 0
  },
  "111": {
    "mapIdHex": "0x6F",
    "mapIdDecimal": 111,
    "mapName": "UNUSED_MAP_6F",
    "width": 0,
    "height": 0
  },
  "112": {
    "mapIdHex": "0x70",
    "mapIdDecimal": 112,
    "mapName": "UNUSED_MAP_70",
    "width": 0,
    "height": 0
  },
  "113": {
    "mapIdHex": "0x71",
    "mapIdDecimal": 113,
    "mapName": "LANCES_ROOM",
    "width": 13,
    "height": 13,
    "warps": [
      {
        "x": 24,
        "y": 16,
        "targetMap": "AGATHAS_ROOM",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "CHAMPIONS_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 6,
        "y": 0,
        "targetMap": "CHAMPIONS_ROOM",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 1,
        "name": "TEXT_LANCESROOM_LANCE"
      }
    ]
  },
  "114": {
    "mapIdHex": "0x72",
    "mapIdDecimal": 114,
    "mapName": "UNUSED_MAP_72",
    "width": 0,
    "height": 0
  },
  "115": {
    "mapIdHex": "0x73",
    "mapIdDecimal": 115,
    "mapName": "UNUSED_MAP_73",
    "width": 0,
    "height": 0
  },
  "116": {
    "mapIdHex": "0x74",
    "mapIdDecimal": 116,
    "mapName": "UNUSED_MAP_74",
    "width": 0,
    "height": 0
  },
  "117": {
    "mapIdHex": "0x75",
    "mapIdDecimal": 117,
    "mapName": "UNUSED_MAP_75",
    "width": 0,
    "height": 0
  },
  "118": {
    "mapIdHex": "0x76",
    "mapIdDecimal": 118,
    "mapName": "HALL_OF_FAME",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 7,
        "targetMap": "CHAMPIONS_ROOM",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "CHAMPIONS_ROOM",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_HALLOFFAME_OAK"
      }
    ]
  },
  "119": {
    "mapIdHex": "0x77",
    "mapIdDecimal": 119,
    "mapName": "UNDERGROUND_PATH_NORTH_SOUTH",
    "width": 4,
    "height": 24,
    "warps": [
      {
        "x": 5,
        "y": 4,
        "targetMap": "UNDERGROUND_PATH_ROUTE_5",
        "targetWarpId": 3
      },
      {
        "x": 2,
        "y": 41,
        "targetMap": "UNDERGROUND_PATH_ROUTE_6",
        "targetWarpId": 3
      }
    ]
  },
  "120": {
    "mapIdHex": "0x78",
    "mapIdDecimal": 120,
    "mapName": "CHAMPIONS_ROOM",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LANCES_ROOM",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LANCES_ROOM",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 0,
        "targetMap": "HALL_OF_FAME",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "HALL_OF_FAME",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_CHAMPIONSROOM_RIVAL"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_CHAMPIONSROOM_OAK"
      }
    ]
  },
  "121": {
    "mapIdHex": "0x79",
    "mapIdDecimal": 121,
    "mapName": "UNDERGROUND_PATH_WEST_EAST",
    "width": 25,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 5,
        "targetMap": "UNDERGROUND_PATH_ROUTE_7",
        "targetWarpId": 3
      },
      {
        "x": 47,
        "y": 2,
        "targetMap": "UNDERGROUND_PATH_ROUTE_8",
        "targetWarpId": 3
      }
    ]
  },
  "122": {
    "mapIdHex": "0x7A",
    "mapIdDecimal": 122,
    "mapName": "CELADON_MART_1F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 17,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 12,
        "y": 1,
        "targetMap": "CELADON_MART_2F",
        "targetWarpId": 1
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "CELADON_MART_ELEVATOR",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 11,
        "y": 4,
        "description": "TEXT_CELADONMART1F_DIRECTORY_SIGN"
      },
      {
        "x": 14,
        "y": 1,
        "description": "TEXT_CELADONMART1F_CURRENT_FLOOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 3,
        "name": "TEXT_CELADONMART1F_RECEPTIONIST"
      }
    ]
  },
  "123": {
    "mapIdHex": "0x7B",
    "mapIdDecimal": 123,
    "mapName": "CELADON_MART_2F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 12,
        "y": 1,
        "targetMap": "CELADON_MART_1F",
        "targetWarpId": 5
      },
      {
        "x": 16,
        "y": 1,
        "targetMap": "CELADON_MART_3F",
        "targetWarpId": 2
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "CELADON_MART_ELEVATOR",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 14,
        "y": 1,
        "description": "TEXT_CELADONMART2F_CURRENT_FLOOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_CELADONMART2F_CLERK1"
      },
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_CELADONMART2F_CLERK2"
      },
      {
        "x": 19,
        "y": 5,
        "name": "TEXT_CELADONMART2F_MIDDLE_AGED_MAN"
      },
      {
        "x": 14,
        "y": 4,
        "name": "TEXT_CELADONMART2F_GIRL"
      }
    ]
  },
  "124": {
    "mapIdHex": "0x7C",
    "mapIdDecimal": 124,
    "mapName": "CELADON_MART_3F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 12,
        "y": 1,
        "targetMap": "CELADON_MART_4F",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 1,
        "targetMap": "CELADON_MART_2F",
        "targetWarpId": 2
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "CELADON_MART_ELEVATOR",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 2,
        "y": 4,
        "description": "TEXT_CELADONMART3F_SNES1"
      },
      {
        "x": 3,
        "y": 4,
        "description": "TEXT_CELADONMART3F_RPG"
      },
      {
        "x": 5,
        "y": 4,
        "description": "TEXT_CELADONMART3F_SNES2"
      },
      {
        "x": 6,
        "y": 4,
        "description": "TEXT_CELADONMART3F_SPORTS_GAME"
      },
      {
        "x": 2,
        "y": 6,
        "description": "TEXT_CELADONMART3F_SNES3"
      },
      {
        "x": 3,
        "y": 6,
        "description": "TEXT_CELADONMART3F_PUZZLE_GAME"
      },
      {
        "x": 5,
        "y": 6,
        "description": "TEXT_CELADONMART3F_SNES4"
      },
      {
        "x": 6,
        "y": 6,
        "description": "TEXT_CELADONMART3F_FIGHTING_GAME"
      },
      {
        "x": 14,
        "y": 1,
        "description": "TEXT_CELADONMART3F_CURRENT_FLOOR_SIGN"
      },
      {
        "x": 4,
        "y": 1,
        "description": "TEXT_CELADONMART3F_POKEMON_POSTER1"
      },
      {
        "x": 6,
        "y": 1,
        "description": "TEXT_CELADONMART3F_POKEMON_POSTER2"
      },
      {
        "x": 10,
        "y": 1,
        "description": "TEXT_CELADONMART3F_POKEMON_POSTER3"
      }
    ],
    "npc_events": [
      {
        "x": 16,
        "y": 5,
        "name": "TEXT_CELADONMART3F_CLERK"
      },
      {
        "x": 11,
        "y": 6,
        "name": "TEXT_CELADONMART3F_GAMEBOY_KID1"
      },
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_CELADONMART3F_GAMEBOY_KID2"
      },
      {
        "x": 8,
        "y": 2,
        "name": "TEXT_CELADONMART3F_GAMEBOY_KID3"
      },
      {
        "x": 2,
        "y": 5,
        "name": "TEXT_CELADONMART3F_LITTLE_BOY"
      }
    ]
  },
  "125": {
    "mapIdHex": "0x7D",
    "mapIdDecimal": 125,
    "mapName": "CELADON_MART_4F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 12,
        "y": 1,
        "targetMap": "CELADON_MART_3F",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 1,
        "targetMap": "CELADON_MART_5F",
        "targetWarpId": 2
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "CELADON_MART_ELEVATOR",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 14,
        "y": 1,
        "description": "TEXT_CELADONMART4F_CURRENT_FLOOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 7,
        "name": "TEXT_CELADONMART4F_CLERK"
      },
      {
        "x": 15,
        "y": 5,
        "name": "TEXT_CELADONMART4F_SUPER_NERD"
      },
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_CELADONMART4F_YOUNGSTER"
      }
    ]
  },
  "126": {
    "mapIdHex": "0x7E",
    "mapIdDecimal": 126,
    "mapName": "CELADON_MART_ROOF",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 15,
        "y": 2,
        "targetMap": "CELADON_MART_5F",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 10,
        "y": 1,
        "description": "TEXT_CELADONMARTROOF_VENDING_MACHINE1"
      },
      {
        "x": 11,
        "y": 1,
        "description": "TEXT_CELADONMARTROOF_VENDING_MACHINE2"
      },
      {
        "x": 12,
        "y": 2,
        "description": "TEXT_CELADONMARTROOF_VENDING_MACHINE3"
      },
      {
        "x": 13,
        "y": 2,
        "description": "TEXT_CELADONMARTROOF_CURRENT_FLOOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 4,
        "name": "TEXT_CELADONMARTROOF_SUPER_NERD"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_CELADONMARTROOF_LITTLE_GIRL"
      }
    ]
  },
  "127": {
    "mapIdHex": "0x7F",
    "mapIdDecimal": 127,
    "mapName": "CELADON_MART_ELEVATOR",
    "width": 2,
    "height": 2,
    "warps": [
      {
        "x": 1,
        "y": 3,
        "targetMap": "CELADON_MART_1F",
        "targetWarpId": 6
      },
      {
        "x": 2,
        "y": 3,
        "targetMap": "CELADON_MART_1F",
        "targetWarpId": 6
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 0,
        "description": "TEXT_CELADONMARTELEVATOR"
      }
    ]
  },
  "128": {
    "mapIdHex": "0x80",
    "mapIdDecimal": 128,
    "mapName": "CELADON_MANSION_1F",
    "width": 4,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "CELADON_MANSION_2F",
        "targetWarpId": 2
      },
      {
        "x": 2,
        "y": 1,
        "targetMap": "CELADON_MANSION_2F",
        "targetWarpId": 3
      }
    ],
    "bg_events": [
      {
        "x": 4,
        "y": 9,
        "description": "TEXT_CELADONMANSION1F_MANAGERS_SUITE_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_CELADONMANSION1F_MEOWTH"
      },
      {
        "x": 1,
        "y": 5,
        "name": "TEXT_CELADONMANSION1F_GRANNY"
      },
      {
        "x": 1,
        "y": 8,
        "name": "TEXT_CELADONMANSION1F_CLEFAIRY"
      },
      {
        "x": 4,
        "y": 4,
        "name": "TEXT_CELADONMANSION1F_NIDORANF"
      }
    ]
  },
  "129": {
    "mapIdHex": "0x81",
    "mapIdDecimal": 129,
    "mapName": "CELADON_MANSION_2F",
    "width": 4,
    "height": 6,
    "warps": [
      {
        "x": 6,
        "y": 1,
        "targetMap": "CELADON_MANSION_3F",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "CELADON_MANSION_1F",
        "targetWarpId": 4
      },
      {
        "x": 2,
        "y": 1,
        "targetMap": "CELADON_MANSION_1F",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 1,
        "targetMap": "CELADON_MANSION_3F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 4,
        "y": 9,
        "description": "TEXT_CELADONMANSION2F_MEETING_ROOM_SIGN"
      }
    ]
  },
  "130": {
    "mapIdHex": "0x82",
    "mapIdDecimal": 130,
    "mapName": "CELADON_MANSION_3F",
    "width": 4,
    "height": 6,
    "warps": [
      {
        "x": 6,
        "y": 1,
        "targetMap": "CELADON_MANSION_2F",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "CELADON_MANSION_ROOF",
        "targetWarpId": 1
      },
      {
        "x": 2,
        "y": 1,
        "targetMap": "CELADON_MANSION_ROOF",
        "targetWarpId": 2
      },
      {
        "x": 4,
        "y": 1,
        "targetMap": "CELADON_MANSION_2F",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 3,
        "description": "TEXT_CELADONMANSION3F_GAME_PROGRAM_PC"
      },
      {
        "x": 4,
        "y": 3,
        "description": "TEXT_CELADONMANSION3F_PLAYING_GAME_PC"
      },
      {
        "x": 1,
        "y": 6,
        "description": "TEXT_CELADONMANSION3F_GAME_SCRIPT_PC"
      },
      {
        "x": 4,
        "y": 9,
        "description": "TEXT_CELADONMANSION3F_DEV_ROOM_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 4,
        "name": "TEXT_CELADONMANSION3F_PROGRAMMER"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_CELADONMANSION3F_GRAPHIC_ARTIST"
      },
      {
        "x": 0,
        "y": 7,
        "name": "TEXT_CELADONMANSION3F_WRITER"
      },
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_CELADONMANSION3F_GAME_DESIGNER"
      }
    ]
  },
  "131": {
    "mapIdHex": "0x83",
    "mapIdDecimal": 131,
    "mapName": "CELADON_MANSION_ROOF",
    "width": 4,
    "height": 6,
    "warps": [
      {
        "x": 6,
        "y": 1,
        "targetMap": "CELADON_MANSION_3F",
        "targetWarpId": 2
      },
      {
        "x": 2,
        "y": 1,
        "targetMap": "CELADON_MANSION_3F",
        "targetWarpId": 3
      },
      {
        "x": 2,
        "y": 7,
        "targetMap": "CELADON_MANSION_ROOF_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 7,
        "description": "TEXT_CELADONMANSIONROOF_HOUSE_SIGN"
      }
    ]
  },
  "132": {
    "mapIdHex": "0x84",
    "mapIdDecimal": 132,
    "mapName": "CELADON_MANSION_ROOF_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "CELADON_MANSION_ROOF",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "CELADON_MANSION_ROOF",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 2,
        "name": "TEXT_CELADONMANSION_ROOF_HOUSE_HIKER"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_CELADONMANSION_ROOF_HOUSE_EEVEE_POKEBALL"
      }
    ]
  },
  "133": {
    "mapIdHex": "0x85",
    "mapIdDecimal": 133,
    "mapName": "CELADON_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_CELADONPOKECENTER_NURSE"
      },
      {
        "x": 7,
        "y": 3,
        "name": "TEXT_CELADONPOKECENTER_GENTLEMAN"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_CELADONPOKECENTER_BEAUTY"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_CELADONPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "134": {
    "mapIdHex": "0x86",
    "mapIdDecimal": 134,
    "mapName": "CELADON_GYM",
    "width": 5,
    "height": 9,
    "warps": [
      {
        "x": 4,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 5,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_CELADONGYM_ERIKA"
      },
      {
        "x": 2,
        "y": 11,
        "name": "TEXT_CELADONGYM_COOLTRAINER_F1"
      },
      {
        "x": 7,
        "y": 10,
        "name": "TEXT_CELADONGYM_BEAUTY1"
      },
      {
        "x": 9,
        "y": 5,
        "name": "TEXT_CELADONGYM_COOLTRAINER_F2"
      },
      {
        "x": 1,
        "y": 5,
        "name": "TEXT_CELADONGYM_BEAUTY2"
      },
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_CELADONGYM_COOLTRAINER_F3"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_CELADONGYM_BEAUTY3"
      },
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_CELADONGYM_COOLTRAINER_F4"
      }
    ]
  },
  "135": {
    "mapIdHex": "0x87",
    "mapIdDecimal": 135,
    "mapName": "GAME_CORNER",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 15,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 16,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 17,
        "y": 4,
        "targetMap": "ROCKET_HIDEOUT_B1F",
        "targetWarpId": 2
      }
    ],
    "bg_events": [
      {
        "x": 9,
        "y": 4,
        "description": "TEXT_GAMECORNER_POSTER"
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 6,
        "name": "TEXT_GAMECORNER_BEAUTY1"
      },
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_GAMECORNER_CLERK1"
      },
      {
        "x": 2,
        "y": 10,
        "name": "TEXT_GAMECORNER_MIDDLE_AGED_MAN1"
      },
      {
        "x": 2,
        "y": 13,
        "name": "TEXT_GAMECORNER_BEAUTY2"
      },
      {
        "x": 5,
        "y": 11,
        "name": "TEXT_GAMECORNER_FISHING_GURU"
      },
      {
        "x": 8,
        "y": 11,
        "name": "TEXT_GAMECORNER_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 8,
        "y": 14,
        "name": "TEXT_GAMECORNER_GYM_GUIDE"
      },
      {
        "x": 11,
        "y": 15,
        "name": "TEXT_GAMECORNER_GAMBLER"
      },
      {
        "x": 14,
        "y": 11,
        "name": "TEXT_GAMECORNER_CLERK2"
      },
      {
        "x": 17,
        "y": 13,
        "name": "TEXT_GAMECORNER_GENTLEMAN"
      },
      {
        "x": 9,
        "y": 5,
        "name": "TEXT_GAMECORNER_ROCKET"
      }
    ]
  },
  "136": {
    "mapIdHex": "0x88",
    "mapIdDecimal": 136,
    "mapName": "CELADON_MART_5F",
    "width": 10,
    "height": 4,
    "warps": [
      {
        "x": 12,
        "y": 1,
        "targetMap": "CELADON_MART_ROOF",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 1,
        "targetMap": "CELADON_MART_4F",
        "targetWarpId": 2
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "CELADON_MART_ELEVATOR",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 14,
        "y": 1,
        "description": "TEXT_CELADONMART5F_CURRENT_FLOOR_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 14,
        "y": 5,
        "name": "TEXT_CELADONMART5F_GENTLEMAN"
      },
      {
        "x": 2,
        "y": 6,
        "name": "TEXT_CELADONMART5F_SAILOR"
      },
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_CELADONMART5F_CLERK1"
      },
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_CELADONMART5F_CLERK2"
      }
    ]
  },
  "137": {
    "mapIdHex": "0x89",
    "mapIdDecimal": 137,
    "mapName": "GAME_CORNER_PRIZE_ROOM",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 10
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 10
      }
    ],
    "bg_events": [
      {
        "x": 2,
        "y": 2,
        "description": "TEXT_GAMECORNERPRIZEROOM_PRIZE_VENDOR_1"
      },
      {
        "x": 4,
        "y": 2,
        "description": "TEXT_GAMECORNERPRIZEROOM_PRIZE_VENDOR_2"
      },
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_GAMECORNERPRIZEROOM_PRIZE_VENDOR_3"
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_GAMECORNERPRIZEROOM_BALDING_GUY"
      },
      {
        "x": 7,
        "y": 3,
        "name": "TEXT_GAMECORNERPRIZEROOM_GAMBLER"
      }
    ]
  },
  "138": {
    "mapIdHex": "0x8A",
    "mapIdDecimal": 138,
    "mapName": "CELADON_DINER",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 11
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 11
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 5,
        "name": "TEXT_CELADONDINER_COOK"
      },
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_CELADONDINER_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_CELADONDINER_MIDDLE_AGED_MAN"
      },
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_CELADONDINER_FISHER"
      },
      {
        "x": 0,
        "y": 1,
        "name": "TEXT_CELADONDINER_GYM_GUIDE"
      }
    ]
  },
  "139": {
    "mapIdHex": "0x8B",
    "mapIdDecimal": 139,
    "mapName": "CELADON_CHIEF_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 12
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 12
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_CELADONCHIEFHOUSE_CHIEF"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_CELADONCHIEFHOUSE_ROCKET"
      },
      {
        "x": 5,
        "y": 6,
        "name": "TEXT_CELADONCHIEFHOUSE_SAILOR"
      }
    ]
  },
  "140": {
    "mapIdHex": "0x8C",
    "mapIdDecimal": 140,
    "mapName": "CELADON_HOTEL",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 13
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 13
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_CELADONHOTEL_GRANNY"
      },
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_CELADONHOTEL_BEAUTY"
      },
      {
        "x": 8,
        "y": 4,
        "name": "TEXT_CELADONHOTEL_SUPER_NERD"
      }
    ]
  },
  "141": {
    "mapIdHex": "0x8D",
    "mapIdDecimal": 141,
    "mapName": "LAVENDER_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_LAVENDERPOKECENTER_NURSE"
      },
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_LAVENDERPOKECENTER_GENTLEMAN"
      },
      {
        "x": 2,
        "y": 6,
        "name": "TEXT_LAVENDERPOKECENTER_LITTLE_GIRL"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_LAVENDERPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "142": {
    "mapIdHex": "0x8E",
    "mapIdDecimal": 142,
    "mapName": "POKEMON_TOWER_1F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 10,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 11,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_2F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 15,
        "y": 13,
        "name": "TEXT_POKEMONTOWER1F_RECEPTIONIST"
      },
      {
        "x": 6,
        "y": 8,
        "name": "TEXT_POKEMONTOWER1F_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 8,
        "y": 12,
        "name": "TEXT_POKEMONTOWER1F_BALDING_GUY"
      },
      {
        "x": 13,
        "y": 7,
        "name": "TEXT_POKEMONTOWER1F_GIRL"
      },
      {
        "x": 17,
        "y": 7,
        "name": "TEXT_POKEMONTOWER1F_CHANNELER"
      }
    ]
  },
  "143": {
    "mapIdHex": "0x8F",
    "mapIdDecimal": 143,
    "mapName": "POKEMON_TOWER_2F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 9,
        "targetMap": "POKEMON_TOWER_3F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_1F",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 14,
        "y": 5,
        "name": "TEXT_POKEMONTOWER2F_RIVAL"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_POKEMONTOWER2F_CHANNELER"
      }
    ]
  },
  "144": {
    "mapIdHex": "0x90",
    "mapIdDecimal": 144,
    "mapName": "POKEMON_TOWER_3F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 9,
        "targetMap": "POKEMON_TOWER_2F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_4F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 3,
        "name": "TEXT_POKEMONTOWER3F_CHANNELER1"
      },
      {
        "x": 9,
        "y": 8,
        "name": "TEXT_POKEMONTOWER3F_CHANNELER2"
      },
      {
        "x": 10,
        "y": 13,
        "name": "TEXT_POKEMONTOWER3F_CHANNELER3"
      },
      {
        "x": 12,
        "y": 1,
        "name": "TEXT_POKEMONTOWER3F_ESCAPE_ROPE"
      }
    ]
  },
  "145": {
    "mapIdHex": "0x91",
    "mapIdDecimal": 145,
    "mapName": "POKEMON_TOWER_4F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 9,
        "targetMap": "POKEMON_TOWER_5F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_3F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 10,
        "name": "TEXT_POKEMONTOWER4F_CHANNELER1"
      },
      {
        "x": 15,
        "y": 7,
        "name": "TEXT_POKEMONTOWER4F_CHANNELER2"
      },
      {
        "x": 14,
        "y": 12,
        "name": "TEXT_POKEMONTOWER4F_CHANNELER3"
      },
      {
        "x": 12,
        "y": 10,
        "name": "TEXT_POKEMONTOWER4F_ELIXER"
      },
      {
        "x": 9,
        "y": 10,
        "name": "TEXT_POKEMONTOWER4F_AWAKENING"
      },
      {
        "x": 12,
        "y": 16,
        "name": "TEXT_POKEMONTOWER4F_HP_UP"
      }
    ]
  },
  "146": {
    "mapIdHex": "0x92",
    "mapIdDecimal": 146,
    "mapName": "POKEMON_TOWER_5F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 9,
        "targetMap": "POKEMON_TOWER_4F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_6F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 8,
        "name": "TEXT_POKEMONTOWER5F_CHANNELER1"
      },
      {
        "x": 17,
        "y": 7,
        "name": "TEXT_POKEMONTOWER5F_CHANNELER2"
      },
      {
        "x": 14,
        "y": 3,
        "name": "TEXT_POKEMONTOWER5F_CHANNELER3"
      },
      {
        "x": 6,
        "y": 10,
        "name": "TEXT_POKEMONTOWER5F_CHANNELER4"
      },
      {
        "x": 9,
        "y": 16,
        "name": "TEXT_POKEMONTOWER5F_CHANNELER5"
      },
      {
        "x": 6,
        "y": 14,
        "name": "TEXT_POKEMONTOWER5F_NUGGET"
      }
    ]
  },
  "147": {
    "mapIdHex": "0x93",
    "mapIdDecimal": 147,
    "mapName": "POKEMON_TOWER_6F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 18,
        "y": 9,
        "targetMap": "POKEMON_TOWER_5F",
        "targetWarpId": 2
      },
      {
        "x": 9,
        "y": 16,
        "targetMap": "POKEMON_TOWER_7F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 10,
        "name": "TEXT_POKEMONTOWER6F_CHANNELER1"
      },
      {
        "x": 9,
        "y": 5,
        "name": "TEXT_POKEMONTOWER6F_CHANNELER2"
      },
      {
        "x": 16,
        "y": 5,
        "name": "TEXT_POKEMONTOWER6F_CHANNELER3"
      },
      {
        "x": 6,
        "y": 8,
        "name": "TEXT_POKEMONTOWER6F_RARE_CANDY"
      },
      {
        "x": 14,
        "y": 14,
        "name": "TEXT_POKEMONTOWER6F_X_ACCURACY"
      }
    ]
  },
  "148": {
    "mapIdHex": "0x94",
    "mapIdDecimal": 148,
    "mapName": "POKEMON_TOWER_7F",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 9,
        "y": 16,
        "targetMap": "POKEMON_TOWER_6F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 9,
        "y": 11,
        "name": "TEXT_POKEMONTOWER7F_ROCKET1"
      },
      {
        "x": 12,
        "y": 9,
        "name": "TEXT_POKEMONTOWER7F_ROCKET2"
      },
      {
        "x": 9,
        "y": 7,
        "name": "TEXT_POKEMONTOWER7F_ROCKET3"
      },
      {
        "x": 10,
        "y": 3,
        "name": "TEXT_POKEMONTOWER7F_MR_FUJI"
      }
    ]
  },
  "149": {
    "mapIdHex": "0x95",
    "mapIdDecimal": 149,
    "mapName": "MR_FUJIS_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_MRFUJISHOUSE_SUPER_NERD"
      },
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_MRFUJISHOUSE_LITTLE_GIRL"
      },
      {
        "x": 6,
        "y": 4,
        "name": "TEXT_MRFUJISHOUSE_PSYDUCK"
      },
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_MRFUJISHOUSE_NIDORINO"
      },
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_MRFUJISHOUSE_MR_FUJI"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_MRFUJISHOUSE_POKEDEX"
      }
    ]
  },
  "150": {
    "mapIdHex": "0x96",
    "mapIdDecimal": 150,
    "mapName": "LAVENDER_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_LAVENDERMART_CLERK"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_LAVENDERMART_BALDING_GUY"
      },
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_LAVENDERMART_COOLTRAINER_M"
      }
    ]
  },
  "151": {
    "mapIdHex": "0x97",
    "mapIdDecimal": 151,
    "mapName": "LAVENDER_CUBONE_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_LAVENDERCUBONEHOUSE_CUBONE"
      },
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_LAVENDERCUBONEHOUSE_BRUNETTE_GIRL"
      }
    ]
  },
  "152": {
    "mapIdHex": "0x98",
    "mapIdDecimal": 152,
    "mapName": "FUCHSIA_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_FUCHSIAMART_CLERK"
      },
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_FUCHSIAMART_MIDDLE_AGED_MAN"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_FUCHSIAMART_COOLTRAINER_F"
      }
    ]
  },
  "153": {
    "mapIdHex": "0x99",
    "mapIdDecimal": 153,
    "mapName": "FUCHSIA_BILLS_GRANDPAS_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_FUCHSIABILLSGRANDPASHOUSE_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_FUCHSIABILLSGRANDPASHOUSE_BILLS_GRANDPA"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_FUCHSIABILLSGRANDPASHOUSE_YOUNGSTER"
      }
    ]
  },
  "154": {
    "mapIdHex": "0x9A",
    "mapIdDecimal": 154,
    "mapName": "FUCHSIA_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_FUCHSIAPOKECENTER_NURSE"
      },
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_FUCHSIAPOKECENTER_ROCKER"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_FUCHSIAPOKECENTER_COOLTRAINER_F"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_FUCHSIAPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "155": {
    "mapIdHex": "0x9B",
    "mapIdDecimal": 155,
    "mapName": "WARDENS_HOUSE",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 4,
        "y": 3,
        "description": "TEXT_WARDENSHOUSE_DISPLAY_LEFT"
      },
      {
        "x": 5,
        "y": 3,
        "description": "TEXT_WARDENSHOUSE_DISPLAY_RIGHT"
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_WARDENSHOUSE_WARDEN"
      },
      {
        "x": 8,
        "y": 3,
        "name": "TEXT_WARDENSHOUSE_RARE_CANDY"
      },
      {
        "x": 8,
        "y": 4,
        "name": "TEXT_WARDENSHOUSE_BOULDER"
      }
    ]
  },
  "156": {
    "mapIdHex": "0x9C",
    "mapIdDecimal": 156,
    "mapName": "SAFARI_ZONE_GATE",
    "width": 4,
    "height": 3,
    "warps": [
      {
        "x": 3,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 0,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_SAFARIZONEGATE_SAFARI_ZONE_WORKER1"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_SAFARIZONEGATE_SAFARI_ZONE_WORKER2"
      }
    ]
  },
  "157": {
    "mapIdHex": "0x9D",
    "mapIdDecimal": 157,
    "mapName": "FUCHSIA_GYM",
    "width": 5,
    "height": 9,
    "warps": [
      {
        "x": 4,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 5,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 10,
        "name": "TEXT_FUCHSIAGYM_KOGA"
      },
      {
        "x": 8,
        "y": 13,
        "name": "TEXT_FUCHSIAGYM_ROCKER1"
      },
      {
        "x": 7,
        "y": 8,
        "name": "TEXT_FUCHSIAGYM_ROCKER2"
      },
      {
        "x": 1,
        "y": 12,
        "name": "TEXT_FUCHSIAGYM_ROCKER3"
      },
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_FUCHSIAGYM_ROCKER4"
      },
      {
        "x": 8,
        "y": 2,
        "name": "TEXT_FUCHSIAGYM_ROCKER5"
      },
      {
        "x": 2,
        "y": 7,
        "name": "TEXT_FUCHSIAGYM_ROCKER6"
      },
      {
        "x": 7,
        "y": 15,
        "name": "TEXT_FUCHSIAGYM_GYM_GUIDE"
      }
    ]
  },
  "158": {
    "mapIdHex": "0x9E",
    "mapIdDecimal": 158,
    "mapName": "FUCHSIA_MEETING_ROOM",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_FUCHSIAMEETINGROOM_SAFARI_ZONE_WORKER1"
      },
      {
        "x": 0,
        "y": 2,
        "name": "TEXT_FUCHSIAMEETINGROOM_SAFARI_ZONE_WORKER2"
      },
      {
        "x": 10,
        "y": 1,
        "name": "TEXT_FUCHSIAMEETINGROOM_SAFARI_ZONE_WORKER3"
      }
    ]
  },
  "159": {
    "mapIdHex": "0x9F",
    "mapIdDecimal": 159,
    "mapName": "SEAFOAM_ISLANDS_B1F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 4,
        "y": 2,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "SEAFOAM_ISLANDS_1F",
        "targetWarpId": 5
      },
      {
        "x": 13,
        "y": 7,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 3
      },
      {
        "x": 19,
        "y": 15,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 4
      },
      {
        "x": 23,
        "y": 15,
        "targetMap": "SEAFOAM_ISLANDS_1F",
        "targetWarpId": 7
      },
      {
        "x": 25,
        "y": 11,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 6
      },
      {
        "x": 25,
        "y": 3,
        "targetMap": "SEAFOAM_ISLANDS_1F",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 17,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB1F_BOULDER1"
      },
      {
        "x": 22,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB1F_BOULDER2"
      }
    ]
  },
  "160": {
    "mapIdHex": "0xA0",
    "mapIdDecimal": 160,
    "mapName": "SEAFOAM_ISLANDS_B2F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 5,
        "y": 3,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 13,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 1
      },
      {
        "x": 13,
        "y": 7,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 3
      },
      {
        "x": 19,
        "y": 15,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 3,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 11,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 6
      },
      {
        "x": 25,
        "y": 14,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 18,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB2F_BOULDER1"
      },
      {
        "x": 23,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB2F_BOULDER2"
      }
    ]
  },
  "161": {
    "mapIdHex": "0xA1",
    "mapIdDecimal": 161,
    "mapName": "SEAFOAM_ISLANDS_B3F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 5,
        "y": 12,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 2
      },
      {
        "x": 8,
        "y": 6,
        "targetMap": "SEAFOAM_ISLANDS_B4F",
        "targetWarpId": 3
      },
      {
        "x": 25,
        "y": 4,
        "targetMap": "SEAFOAM_ISLANDS_B4F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 3,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 5
      },
      {
        "x": 25,
        "y": 14,
        "targetMap": "SEAFOAM_ISLANDS_B2F",
        "targetWarpId": 7
      },
      {
        "x": 20,
        "y": 17,
        "targetMap": "SEAFOAM_ISLANDS_B4F",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 17,
        "targetMap": "SEAFOAM_ISLANDS_B4F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 14,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER1"
      },
      {
        "x": 3,
        "y": 15,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER2"
      },
      {
        "x": 8,
        "y": 14,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER3"
      },
      {
        "x": 9,
        "y": 14,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER4"
      },
      {
        "x": 18,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER5"
      },
      {
        "x": 19,
        "y": 6,
        "name": "TEXT_SEAFOAMISLANDSB3F_BOULDER6"
      }
    ]
  },
  "162": {
    "mapIdHex": "0xA2",
    "mapIdDecimal": 162,
    "mapName": "SEAFOAM_ISLANDS_B4F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 20,
        "y": 17,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 6
      },
      {
        "x": 21,
        "y": 17,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 7
      },
      {
        "x": 11,
        "y": 7,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 2
      },
      {
        "x": 25,
        "y": 4,
        "targetMap": "SEAFOAM_ISLANDS_B3F",
        "targetWarpId": 3
      }
    ],
    "bg_events": [
      {
        "x": 9,
        "y": 15,
        "description": "TEXT_SEAFOAMISLANDSB4F_BOULDERS_SIGN"
      },
      {
        "x": 23,
        "y": 1,
        "description": "TEXT_SEAFOAMISLANDSB4F_DANGER_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 15,
        "name": "TEXT_SEAFOAMISLANDSB4F_BOULDER1"
      },
      {
        "x": 5,
        "y": 15,
        "name": "TEXT_SEAFOAMISLANDSB4F_BOULDER2"
      },
      {
        "x": 6,
        "y": 1,
        "name": "TEXT_SEAFOAMISLANDSB4F_ARTICUNO"
      }
    ]
  },
  "163": {
    "mapIdHex": "0xA3",
    "mapIdDecimal": 163,
    "mapName": "VERMILION_OLD_ROD_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_VERMILIONOLDRODHOUSE_FISHING_GURU"
      }
    ]
  },
  "164": {
    "mapIdHex": "0xA4",
    "mapIdDecimal": 164,
    "mapName": "FUCHSIA_GOOD_ROD_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      },
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_FUCHSIAGOODRODHOUSE_FISHING_GURU"
      }
    ]
  },
  "165": {
    "mapIdHex": "0xA5",
    "mapIdDecimal": 165,
    "mapName": "POKEMON_MANSION_1F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 4,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 6,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 10,
        "targetMap": "POKEMON_MANSION_2F",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 23,
        "targetMap": "POKEMON_MANSION_B1F",
        "targetWarpId": 1
      },
      {
        "x": 26,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 27,
        "y": 27,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 17,
        "y": 17,
        "name": "TEXT_POKEMONMANSION1F_SCIENTIST"
      },
      {
        "x": 14,
        "y": 3,
        "name": "TEXT_POKEMONMANSION1F_ESCAPE_ROPE"
      },
      {
        "x": 18,
        "y": 21,
        "name": "TEXT_POKEMONMANSION1F_CARBOS"
      }
    ]
  },
  "166": {
    "mapIdHex": "0xA6",
    "mapIdDecimal": 166,
    "mapName": "CINNABAR_GYM",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 16,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 17,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_CINNABARGYM_BLAINE"
      },
      {
        "x": 17,
        "y": 2,
        "name": "TEXT_CINNABARGYM_SUPER_NERD1"
      },
      {
        "x": 17,
        "y": 8,
        "name": "TEXT_CINNABARGYM_SUPER_NERD2"
      },
      {
        "x": 11,
        "y": 4,
        "name": "TEXT_CINNABARGYM_SUPER_NERD3"
      },
      {
        "x": 11,
        "y": 8,
        "name": "TEXT_CINNABARGYM_SUPER_NERD4"
      },
      {
        "x": 11,
        "y": 14,
        "name": "TEXT_CINNABARGYM_SUPER_NERD5"
      },
      {
        "x": 3,
        "y": 14,
        "name": "TEXT_CINNABARGYM_SUPER_NERD6"
      },
      {
        "x": 3,
        "y": 8,
        "name": "TEXT_CINNABARGYM_SUPER_NERD7"
      },
      {
        "x": 16,
        "y": 13,
        "name": "TEXT_CINNABARGYM_GYM_GUIDE"
      }
    ]
  },
  "167": {
    "mapIdHex": "0xA7",
    "mapIdDecimal": 167,
    "mapName": "CINNABAR_LAB",
    "width": 9,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 8,
        "y": 4,
        "targetMap": "CINNABAR_LAB_TRADE_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 4,
        "targetMap": "CINNABAR_LAB_METRONOME_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 4,
        "targetMap": "CINNABAR_LAB_FOSSIL_ROOM",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 2,
        "description": "TEXT_CINNABARLAB_PHOTO"
      },
      {
        "x": 9,
        "y": 4,
        "description": "TEXT_CINNABARLAB_MEETING_ROOM_SIGN"
      },
      {
        "x": 13,
        "y": 4,
        "description": "TEXT_CINNABARLAB_R_AND_D_SIGN"
      },
      {
        "x": 17,
        "y": 4,
        "description": "TEXT_CINNABARLAB_TESTING_ROOM_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_CINNABARLAB_FISHING_GURU"
      }
    ]
  },
  "168": {
    "mapIdHex": "0xA8",
    "mapIdDecimal": 168,
    "mapName": "CINNABAR_LAB_TRADE_ROOM",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 2,
        "name": "TEXT_CINNABARLABTRADEROOM_SUPER_NERD"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_CINNABARLABTRADEROOM_GRAMPS"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_CINNABARLABTRADEROOM_BEAUTY"
      }
    ]
  },
  "169": {
    "mapIdHex": "0xA9",
    "mapIdDecimal": 169,
    "mapName": "CINNABAR_LAB_METRONOME_ROOM",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 4
      }
    ],
    "bg_events": [
      {
        "x": 0,
        "y": 4,
        "description": "TEXT_CINNABARLABMETRONOMEROOM_PC_KEYBOARD"
      },
      {
        "x": 1,
        "y": 4,
        "description": "TEXT_CINNABARLABMETRONOMEROOM_PC_MONITOR"
      },
      {
        "x": 2,
        "y": 1,
        "description": "TEXT_CINNABARLABMETRONOMEROOM_AMBER_PIPE"
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 2,
        "name": "TEXT_CINNABARLABMETRONOMEROOM_SCIENTIST1"
      },
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_CINNABARLABMETRONOMEROOM_SCIENTIST2"
      }
    ]
  },
  "170": {
    "mapIdHex": "0xAA",
    "mapIdDecimal": 170,
    "mapName": "CINNABAR_LAB_FOSSIL_ROOM",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "CINNABAR_LAB",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_CINNABARLABFOSSILROOM_SCIENTIST1"
      },
      {
        "x": 7,
        "y": 6,
        "name": "TEXT_CINNABARLABFOSSILROOM_SCIENTIST2"
      }
    ]
  },
  "171": {
    "mapIdHex": "0xAB",
    "mapIdDecimal": 171,
    "mapName": "CINNABAR_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_CINNABARPOKECENTER_NURSE"
      },
      {
        "x": 9,
        "y": 4,
        "name": "TEXT_CINNABARPOKECENTER_COOLTRAINER_F"
      },
      {
        "x": 2,
        "y": 6,
        "name": "TEXT_CINNABARPOKECENTER_GENTLEMAN"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_CINNABARPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "172": {
    "mapIdHex": "0xAC",
    "mapIdDecimal": 172,
    "mapName": "CINNABAR_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_CINNABARMART_CLERK"
      },
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_CINNABARMART_SILPH_WORKER_F"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_CINNABARMART_SCIENTIST"
      }
    ]
  },
  "173": {
    "mapIdHex": "0xAD",
    "mapIdDecimal": 173,
    "mapName": "CINNABAR_MART_COPY",
    "width": 4,
    "height": 4
  },
  "174": {
    "mapIdHex": "0xAE",
    "mapIdDecimal": 174,
    "mapName": "INDIGO_PLATEAU_LOBBY",
    "width": 8,
    "height": 6,
    "warps": [
      {
        "x": 7,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 8,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 8,
        "y": 0,
        "targetMap": "LORELEIS_ROOM",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 5,
        "name": "TEXT_INDIGOPLATEAULOBBY_NURSE"
      },
      {
        "x": 4,
        "y": 9,
        "name": "TEXT_INDIGOPLATEAULOBBY_GYM_GUIDE"
      },
      {
        "x": 5,
        "y": 1,
        "name": "TEXT_INDIGOPLATEAULOBBY_COOLTRAINER_F"
      },
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_INDIGOPLATEAULOBBY_CLERK"
      },
      {
        "x": 13,
        "y": 6,
        "name": "TEXT_INDIGOPLATEAULOBBY_LINK_RECEPTIONIST"
      }
    ]
  },
  "175": {
    "mapIdHex": "0xAF",
    "mapIdDecimal": 175,
    "mapName": "COPYCATS_HOUSE_1F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "COPYCATS_HOUSE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 2,
        "name": "TEXT_COPYCATSHOUSE1F_MIDDLE_AGED_WOMAN"
      },
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_COPYCATSHOUSE1F_MIDDLE_AGED_MAN"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_COPYCATSHOUSE1F_CHANSEY"
      }
    ]
  },
  "176": {
    "mapIdHex": "0xB0",
    "mapIdDecimal": 176,
    "mapName": "COPYCATS_HOUSE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 1,
        "targetMap": "COPYCATS_HOUSE_1F",
        "targetWarpId": 3
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 5,
        "description": "TEXT_COPYCATSHOUSE2F_SNES"
      },
      {
        "x": 0,
        "y": 1,
        "description": "TEXT_COPYCATSHOUSE2F_PC"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_COPYCATSHOUSE2F_COPYCAT"
      },
      {
        "x": 4,
        "y": 6,
        "name": "TEXT_COPYCATSHOUSE2F_DODUO"
      },
      {
        "x": 5,
        "y": 1,
        "name": "TEXT_COPYCATSHOUSE2F_MONSTER"
      },
      {
        "x": 2,
        "y": 0,
        "name": "TEXT_COPYCATSHOUSE2F_BIRD"
      },
      {
        "x": 1,
        "y": 6,
        "name": "TEXT_COPYCATSHOUSE2F_FAIRY"
      }
    ]
  },
  "177": {
    "mapIdHex": "0xB1",
    "mapIdDecimal": 177,
    "mapName": "FIGHTING_DOJO",
    "width": 5,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_FIGHTINGDOJO_KARATE_MASTER"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_FIGHTINGDOJO_BLACKBELT1"
      },
      {
        "x": 3,
        "y": 6,
        "name": "TEXT_FIGHTINGDOJO_BLACKBELT2"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_FIGHTINGDOJO_BLACKBELT3"
      },
      {
        "x": 5,
        "y": 7,
        "name": "TEXT_FIGHTINGDOJO_BLACKBELT4"
      },
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_FIGHTINGDOJO_HITMONLEE_POKE_BALL"
      },
      {
        "x": 5,
        "y": 1,
        "name": "TEXT_FIGHTINGDOJO_HITMONCHAN_POKE_BALL"
      }
    ]
  },
  "178": {
    "mapIdHex": "0xB2",
    "mapIdDecimal": 178,
    "mapName": "SAFFRON_GYM",
    "width": 10,
    "height": 9,
    "warps": [
      {
        "x": 8,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 9,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 1,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 23
      },
      {
        "x": 5,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 16
      },
      {
        "x": 1,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 19
      },
      {
        "x": 5,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 9
      },
      {
        "x": 1,
        "y": 9,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 28
      },
      {
        "x": 5,
        "y": 9,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 17
      },
      {
        "x": 1,
        "y": 11,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 6
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 14
      },
      {
        "x": 1,
        "y": 15,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 24
      },
      {
        "x": 5,
        "y": 15,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 31
      },
      {
        "x": 1,
        "y": 17,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 18
      },
      {
        "x": 5,
        "y": 17,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 10
      },
      {
        "x": 9,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 27
      },
      {
        "x": 11,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 4
      },
      {
        "x": 9,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 8
      },
      {
        "x": 11,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 13
      },
      {
        "x": 11,
        "y": 11,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 5
      },
      {
        "x": 11,
        "y": 15,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 32
      },
      {
        "x": 15,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 25
      },
      {
        "x": 19,
        "y": 3,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 29
      },
      {
        "x": 15,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 3
      },
      {
        "x": 19,
        "y": 5,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 11
      },
      {
        "x": 15,
        "y": 9,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 21
      },
      {
        "x": 19,
        "y": 9,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 30
      },
      {
        "x": 15,
        "y": 11,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 15
      },
      {
        "x": 19,
        "y": 11,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 7
      },
      {
        "x": 15,
        "y": 15,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 22
      },
      {
        "x": 19,
        "y": 15,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 26
      },
      {
        "x": 15,
        "y": 17,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 12
      },
      {
        "x": 19,
        "y": 17,
        "targetMap": "SAFFRON_GYM",
        "targetWarpId": 20
      }
    ],
    "npc_events": [
      {
        "x": 9,
        "y": 8,
        "name": "TEXT_SAFFRONGYM_SABRINA"
      },
      {
        "x": 10,
        "y": 1,
        "name": "TEXT_SAFFRONGYM_CHANNELER1"
      },
      {
        "x": 17,
        "y": 1,
        "name": "TEXT_SAFFRONGYM_YOUNGSTER1"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_SAFFRONGYM_CHANNELER2"
      },
      {
        "x": 17,
        "y": 7,
        "name": "TEXT_SAFFRONGYM_YOUNGSTER2"
      },
      {
        "x": 3,
        "y": 13,
        "name": "TEXT_SAFFRONGYM_CHANNELER3"
      },
      {
        "x": 17,
        "y": 13,
        "name": "TEXT_SAFFRONGYM_YOUNGSTER3"
      },
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_SAFFRONGYM_YOUNGSTER4"
      },
      {
        "x": 10,
        "y": 15,
        "name": "TEXT_SAFFRONGYM_GYM_GUIDE"
      }
    ]
  },
  "179": {
    "mapIdHex": "0xB3",
    "mapIdDecimal": 179,
    "mapName": "SAFFRON_PIDGEY_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_SAFFRONPIDGEYHOUSE_BRUNETTE_GIRL"
      },
      {
        "x": 0,
        "y": 4,
        "name": "TEXT_SAFFRONPIDGEYHOUSE_PIDGEY"
      },
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_SAFFRONPIDGEYHOUSE_YOUNGSTER"
      },
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_SAFFRONPIDGEYHOUSE_PAPER"
      }
    ]
  },
  "180": {
    "mapIdHex": "0xB4",
    "mapIdDecimal": 180,
    "mapName": "SAFFRON_MART",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 0,
        "y": 5,
        "name": "TEXT_SAFFRONMART_CLERK"
      },
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_SAFFRONMART_SUPER_NERD"
      },
      {
        "x": 6,
        "y": 5,
        "name": "TEXT_SAFFRONMART_COOLTRAINER_F"
      }
    ]
  },
  "181": {
    "mapIdHex": "0xB5",
    "mapIdDecimal": 181,
    "mapName": "SILPH_CO_1F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 10,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 11,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 26,
        "y": 0,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 1
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 10,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_SILPHCO1F_LINK_RECEPTIONIST"
      }
    ]
  },
  "182": {
    "mapIdHex": "0xB6",
    "mapIdDecimal": 182,
    "mapName": "SAFFRON_POKECENTER",
    "width": 7,
    "height": 4,
    "warps": [
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 1,
        "name": "TEXT_SAFFRONPOKECENTER_NURSE"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_SAFFRONPOKECENTER_BEAUTY"
      },
      {
        "x": 8,
        "y": 3,
        "name": "TEXT_SAFFRONPOKECENTER_GENTLEMAN"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_SAFFRONPOKECENTER_LINK_RECEPTIONIST"
      }
    ]
  },
  "183": {
    "mapIdHex": "0xB7",
    "mapIdDecimal": 183,
    "mapName": "MR_PSYCHICS_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_MRPSYCHICSHOUSE_MR_PSYCHIC"
      }
    ]
  },
  "184": {
    "mapIdHex": "0xB8",
    "mapIdDecimal": 184,
    "mapName": "ROUTE_15_GATE_1F",
    "width": 4,
    "height": 5,
    "warps": [
      {
        "x": 0,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 0,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 6,
        "y": 8,
        "targetMap": "ROUTE_15_GATE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_ROUTE15GATE1F_GUARD"
      }
    ]
  },
  "185": {
    "mapIdHex": "0xB9",
    "mapIdDecimal": 185,
    "mapName": "ROUTE_15_GATE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "ROUTE_15_GATE_1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_ROUTE15GATE2F_BINOCULARS"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_ROUTE15GATE2F_OAKS_AIDE"
      }
    ]
  },
  "186": {
    "mapIdHex": "0xBA",
    "mapIdDecimal": 186,
    "mapName": "ROUTE_16_GATE_1F",
    "width": 4,
    "height": 7,
    "warps": [
      {
        "x": 0,
        "y": 8,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 0,
        "y": 9,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 8,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 9,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 0,
        "y": 2,
        "targetMap": "LAST_MAP",
        "targetWarpId": 5
      },
      {
        "x": 0,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 7,
        "y": 2,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 7,
        "y": 3,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 6,
        "y": 12,
        "targetMap": "ROUTE_16_GATE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 5,
        "name": "TEXT_ROUTE16GATE1F_GUARD"
      },
      {
        "x": 4,
        "y": 3,
        "name": "TEXT_ROUTE16GATE1F_GAMBLER"
      }
    ]
  },
  "187": {
    "mapIdHex": "0xBB",
    "mapIdDecimal": 187,
    "mapName": "ROUTE_16_GATE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "ROUTE_16_GATE_1F",
        "targetWarpId": 9
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 2,
        "description": "TEXT_ROUTE16GATE2F_LEFT_BINOCULARS"
      },
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_ROUTE16GATE2F_RIGHT_BINOCULARS"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_ROUTE16GATE2F_LITTLE_BOY"
      },
      {
        "x": 2,
        "y": 5,
        "name": "TEXT_ROUTE16GATE2F_LITTLE_GIRL"
      }
    ]
  },
  "188": {
    "mapIdHex": "0xBC",
    "mapIdDecimal": 188,
    "mapName": "ROUTE_16_FLY_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 3,
        "name": "TEXT_ROUTE16FLYHOUSE_BRUNETTE_GIRL"
      },
      {
        "x": 6,
        "y": 4,
        "name": "TEXT_ROUTE16FLYHOUSE_FEAROW"
      }
    ]
  },
  "189": {
    "mapIdHex": "0xBD",
    "mapIdDecimal": 189,
    "mapName": "ROUTE_12_SUPER_ROD_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_ROUTE12SUPERRODHOUSE_FISHING_GURU"
      }
    ]
  },
  "190": {
    "mapIdHex": "0xBE",
    "mapIdDecimal": 190,
    "mapName": "ROUTE_18_GATE_1F",
    "width": 4,
    "height": 5,
    "warps": [
      {
        "x": 0,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 0,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 4,
        "targetMap": "LAST_MAP",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 6,
        "y": 8,
        "targetMap": "ROUTE_18_GATE_2F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 1,
        "name": "TEXT_ROUTE18GATE1F_GUARD"
      }
    ]
  },
  "191": {
    "mapIdHex": "0xBF",
    "mapIdDecimal": 191,
    "mapName": "ROUTE_18_GATE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "ROUTE_18_GATE_1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 2,
        "description": "TEXT_ROUTE18GATE2F_LEFT_BINOCULARS"
      },
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_ROUTE18GATE2F_RIGHT_BINOCULARS"
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_ROUTE18GATE2F_YOUNGSTER"
      }
    ]
  },
  "192": {
    "mapIdHex": "0xC0",
    "mapIdDecimal": 192,
    "mapName": "SEAFOAM_ISLANDS_1F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 4,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 26,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 27,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      },
      {
        "x": 7,
        "y": 5,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 2
      },
      {
        "x": 25,
        "y": 3,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 7
      },
      {
        "x": 23,
        "y": 15,
        "targetMap": "SEAFOAM_ISLANDS_B1F",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 18,
        "y": 10,
        "name": "TEXT_SEAFOAMISLANDS1F_BOULDER1"
      },
      {
        "x": 26,
        "y": 7,
        "name": "TEXT_SEAFOAMISLANDS1F_BOULDER2"
      }
    ]
  },
  "193": {
    "mapIdHex": "0xC1",
    "mapIdDecimal": 193,
    "mapName": "ROUTE_22_GATE",
    "width": 5,
    "height": 4,
    "warps": [
      {
        "x": 4,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_ROUTE22GATE_GUARD"
      }
    ]
  },
  "194": {
    "mapIdHex": "0xC2",
    "mapIdDecimal": 194,
    "mapName": "VICTORY_ROAD_2F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 0,
        "y": 8,
        "targetMap": "VICTORY_ROAD_1F",
        "targetWarpId": 3
      },
      {
        "x": 29,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 29,
        "y": 8,
        "targetMap": "LAST_MAP",
        "targetWarpId": 4
      },
      {
        "x": 23,
        "y": 7,
        "targetMap": "VICTORY_ROAD_3F",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 14,
        "targetMap": "VICTORY_ROAD_3F",
        "targetWarpId": 3
      },
      {
        "x": 27,
        "y": 7,
        "targetMap": "VICTORY_ROAD_3F",
        "targetWarpId": 2
      },
      {
        "x": 1,
        "y": 1,
        "targetMap": "VICTORY_ROAD_3F",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 12,
        "y": 9,
        "name": "TEXT_VICTORYROAD2F_HIKER"
      },
      {
        "x": 21,
        "y": 13,
        "name": "TEXT_VICTORYROAD2F_SUPER_NERD1"
      },
      {
        "x": 19,
        "y": 8,
        "name": "TEXT_VICTORYROAD2F_COOLTRAINER_M"
      },
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_VICTORYROAD2F_SUPER_NERD2"
      },
      {
        "x": 26,
        "y": 3,
        "name": "TEXT_VICTORYROAD2F_SUPER_NERD3"
      },
      {
        "x": 11,
        "y": 5,
        "name": "TEXT_VICTORYROAD2F_MOLTRES"
      },
      {
        "x": 27,
        "y": 5,
        "name": "TEXT_VICTORYROAD2F_TM_SUBMISSION"
      },
      {
        "x": 18,
        "y": 9,
        "name": "TEXT_VICTORYROAD2F_FULL_HEAL"
      },
      {
        "x": 9,
        "y": 11,
        "name": "TEXT_VICTORYROAD2F_TM_MEGA_KICK"
      },
      {
        "x": 11,
        "y": 0,
        "name": "TEXT_VICTORYROAD2F_GUARD_SPEC"
      },
      {
        "x": 4,
        "y": 14,
        "name": "TEXT_VICTORYROAD2F_BOULDER1"
      },
      {
        "x": 5,
        "y": 5,
        "name": "TEXT_VICTORYROAD2F_BOULDER2"
      },
      {
        "x": 23,
        "y": 16,
        "name": "TEXT_VICTORYROAD2F_BOULDER3"
      }
    ]
  },
  "195": {
    "mapIdHex": "0xC3",
    "mapIdDecimal": 195,
    "mapName": "ROUTE_12_GATE_2F",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 7,
        "y": 7,
        "targetMap": "ROUTE_12_GATE_1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 2,
        "description": "TEXT_ROUTE12GATE2F_LEFT_BINOCULARS"
      },
      {
        "x": 6,
        "y": 2,
        "description": "TEXT_ROUTE12GATE2F_RIGHT_BINOCULARS"
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_ROUTE12GATE2F_BRUNETTE_GIRL"
      }
    ]
  },
  "196": {
    "mapIdHex": "0xC4",
    "mapIdDecimal": 196,
    "mapName": "VERMILION_TRADE_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_VERMILIONTRADEHOUSE_LITTLE_GIRL"
      }
    ]
  },
  "197": {
    "mapIdHex": "0xC5",
    "mapIdDecimal": 197,
    "mapName": "DIGLETTS_CAVE",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 5,
        "y": 5,
        "targetMap": "DIGLETTS_CAVE_ROUTE_2",
        "targetWarpId": 3
      },
      {
        "x": 37,
        "y": 31,
        "targetMap": "DIGLETTS_CAVE_ROUTE_11",
        "targetWarpId": 3
      }
    ]
  },
  "198": {
    "mapIdHex": "0xC6",
    "mapIdDecimal": 198,
    "mapName": "VICTORY_ROAD_3F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 23,
        "y": 7,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 4
      },
      {
        "x": 26,
        "y": 8,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 6
      },
      {
        "x": 27,
        "y": 15,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 5
      },
      {
        "x": 2,
        "y": 0,
        "targetMap": "VICTORY_ROAD_2F",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 28,
        "y": 5,
        "name": "TEXT_VICTORYROAD3F_COOLTRAINER_M1"
      },
      {
        "x": 7,
        "y": 13,
        "name": "TEXT_VICTORYROAD3F_COOLTRAINER_F1"
      },
      {
        "x": 6,
        "y": 14,
        "name": "TEXT_VICTORYROAD3F_COOLTRAINER_M2"
      },
      {
        "x": 13,
        "y": 3,
        "name": "TEXT_VICTORYROAD3F_COOLTRAINER_F2"
      },
      {
        "x": 26,
        "y": 5,
        "name": "TEXT_VICTORYROAD3F_MAX_REVIVE"
      },
      {
        "x": 7,
        "y": 7,
        "name": "TEXT_VICTORYROAD3F_TM_EXPLOSION"
      },
      {
        "x": 22,
        "y": 3,
        "name": "TEXT_VICTORYROAD3F_BOULDER1"
      },
      {
        "x": 13,
        "y": 12,
        "name": "TEXT_VICTORYROAD3F_BOULDER2"
      },
      {
        "x": 24,
        "y": 10,
        "name": "TEXT_VICTORYROAD3F_BOULDER3"
      },
      {
        "x": 22,
        "y": 15,
        "name": "TEXT_VICTORYROAD3F_BOULDER4"
      }
    ]
  },
  "199": {
    "mapIdHex": "0xC7",
    "mapIdDecimal": 199,
    "mapName": "ROCKET_HIDEOUT_B1F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 23,
        "y": 2,
        "targetMap": "ROCKET_HIDEOUT_B2F",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 2,
        "targetMap": "GAME_CORNER",
        "targetWarpId": 3
      },
      {
        "x": 24,
        "y": 19,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 24,
        "targetMap": "ROCKET_HIDEOUT_B2F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 19,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 26,
        "y": 8,
        "name": "TEXT_ROCKETHIDEOUTB1F_ROCKET1"
      },
      {
        "x": 12,
        "y": 6,
        "name": "TEXT_ROCKETHIDEOUTB1F_ROCKET2"
      },
      {
        "x": 18,
        "y": 17,
        "name": "TEXT_ROCKETHIDEOUTB1F_ROCKET3"
      },
      {
        "x": 15,
        "y": 25,
        "name": "TEXT_ROCKETHIDEOUTB1F_ROCKET4"
      },
      {
        "x": 28,
        "y": 18,
        "name": "TEXT_ROCKETHIDEOUTB1F_ROCKET5"
      },
      {
        "x": 11,
        "y": 14,
        "name": "TEXT_ROCKETHIDEOUTB1F_ESCAPE_ROPE"
      },
      {
        "x": 9,
        "y": 17,
        "name": "TEXT_ROCKETHIDEOUTB1F_HYPER_POTION"
      }
    ]
  },
  "200": {
    "mapIdHex": "0xC8",
    "mapIdDecimal": 200,
    "mapName": "ROCKET_HIDEOUT_B2F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 27,
        "y": 8,
        "targetMap": "ROCKET_HIDEOUT_B1F",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 8,
        "targetMap": "ROCKET_HIDEOUT_B3F",
        "targetWarpId": 1
      },
      {
        "x": 24,
        "y": 19,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 22,
        "targetMap": "ROCKET_HIDEOUT_B1F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 19,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 20,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB2F_ROCKET"
      },
      {
        "x": 1,
        "y": 11,
        "name": "TEXT_ROCKETHIDEOUTB2F_MOON_STONE"
      },
      {
        "x": 16,
        "y": 8,
        "name": "TEXT_ROCKETHIDEOUTB2F_NUGGET"
      },
      {
        "x": 6,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB2F_TM_HORN_DRILL"
      },
      {
        "x": 3,
        "y": 21,
        "name": "TEXT_ROCKETHIDEOUTB2F_SUPER_POTION"
      }
    ]
  },
  "201": {
    "mapIdHex": "0xC9",
    "mapIdDecimal": 201,
    "mapName": "ROCKET_HIDEOUT_B3F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 25,
        "y": 6,
        "targetMap": "ROCKET_HIDEOUT_B2F",
        "targetWarpId": 2
      },
      {
        "x": 19,
        "y": 18,
        "targetMap": "ROCKET_HIDEOUT_B4F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 22,
        "name": "TEXT_ROCKETHIDEOUTB3F_ROCKET1"
      },
      {
        "x": 26,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB3F_ROCKET2"
      },
      {
        "x": 26,
        "y": 17,
        "name": "TEXT_ROCKETHIDEOUTB3F_TM_DOUBLE_EDGE"
      },
      {
        "x": 20,
        "y": 14,
        "name": "TEXT_ROCKETHIDEOUTB3F_RARE_CANDY"
      }
    ]
  },
  "202": {
    "mapIdHex": "0xCA",
    "mapIdDecimal": 202,
    "mapName": "ROCKET_HIDEOUT_B4F",
    "width": 15,
    "height": 12,
    "warps": [
      {
        "x": 19,
        "y": 10,
        "targetMap": "ROCKET_HIDEOUT_B3F",
        "targetWarpId": 2
      },
      {
        "x": 24,
        "y": 15,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 15,
        "targetMap": "ROCKET_HIDEOUT_ELEVATOR",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 25,
        "y": 3,
        "name": "TEXT_ROCKETHIDEOUTB4F_GIOVANNI"
      },
      {
        "x": 23,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB4F_ROCKET1"
      },
      {
        "x": 26,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB4F_ROCKET2"
      },
      {
        "x": 11,
        "y": 2,
        "name": "TEXT_ROCKETHIDEOUTB4F_ROCKET3"
      },
      {
        "x": 10,
        "y": 12,
        "name": "TEXT_ROCKETHIDEOUTB4F_HP_UP"
      },
      {
        "x": 9,
        "y": 4,
        "name": "TEXT_ROCKETHIDEOUTB4F_TM_RAZOR_WIND"
      },
      {
        "x": 12,
        "y": 20,
        "name": "TEXT_ROCKETHIDEOUTB4F_IRON"
      },
      {
        "x": 25,
        "y": 2,
        "name": "TEXT_ROCKETHIDEOUTB4F_SILPH_SCOPE"
      },
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_ROCKETHIDEOUTB4F_LIFT_KEY"
      }
    ]
  },
  "203": {
    "mapIdHex": "0xCB",
    "mapIdDecimal": 203,
    "mapName": "ROCKET_HIDEOUT_ELEVATOR",
    "width": 3,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 1,
        "targetMap": "ROCKET_HIDEOUT_B1F",
        "targetWarpId": 3
      },
      {
        "x": 3,
        "y": 1,
        "targetMap": "ROCKET_HIDEOUT_B1F",
        "targetWarpId": 5
      }
    ],
    "bg_events": [
      {
        "x": 1,
        "y": 1,
        "description": "TEXT_ROCKETHIDEOUTELEVATOR"
      }
    ]
  },
  "204": {
    "mapIdHex": "0xCC",
    "mapIdDecimal": 204,
    "mapName": "UNUSED_MAP_CC",
    "width": 0,
    "height": 0
  },
  "205": {
    "mapIdHex": "0xCD",
    "mapIdDecimal": 205,
    "mapName": "UNUSED_MAP_CD",
    "width": 0,
    "height": 0
  },
  "206": {
    "mapIdHex": "0xCE",
    "mapIdDecimal": 206,
    "mapName": "UNUSED_MAP_CE",
    "width": 0,
    "height": 0
  },
  "207": {
    "mapIdHex": "0xCF",
    "mapIdDecimal": 207,
    "mapName": "SILPH_CO_2F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 24,
        "y": 0,
        "targetMap": "SILPH_CO_1F",
        "targetWarpId": 3
      },
      {
        "x": 26,
        "y": 0,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 1
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 3,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 7
      },
      {
        "x": 13,
        "y": 3,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 5
      },
      {
        "x": 27,
        "y": 15,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 6
      },
      {
        "x": 9,
        "y": 15,
        "targetMap": "SILPH_CO_6F",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 1,
        "name": "TEXT_SILPHCO2F_SILPH_WORKER_F"
      },
      {
        "x": 5,
        "y": 12,
        "name": "TEXT_SILPHCO2F_SCIENTIST1"
      },
      {
        "x": 24,
        "y": 13,
        "name": "TEXT_SILPHCO2F_SCIENTIST2"
      },
      {
        "x": 16,
        "y": 11,
        "name": "TEXT_SILPHCO2F_ROCKET1"
      },
      {
        "x": 24,
        "y": 7,
        "name": "TEXT_SILPHCO2F_ROCKET2"
      }
    ]
  },
  "208": {
    "mapIdHex": "0xD0",
    "mapIdDecimal": 208,
    "mapName": "SILPH_CO_3F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 26,
        "y": 0,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 2
      },
      {
        "x": 24,
        "y": 0,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 1
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 11,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 10
      },
      {
        "x": 3,
        "y": 3,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 6
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 7
      },
      {
        "x": 27,
        "y": 3,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 11,
        "targetMap": "SILPH_CO_9F",
        "targetWarpId": 4
      },
      {
        "x": 11,
        "y": 11,
        "targetMap": "SILPH_CO_7F",
        "targetWarpId": 5
      },
      {
        "x": 27,
        "y": 15,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 24,
        "y": 8,
        "name": "TEXT_SILPHCO3F_SILPH_WORKER_M"
      },
      {
        "x": 20,
        "y": 7,
        "name": "TEXT_SILPHCO3F_ROCKET"
      },
      {
        "x": 7,
        "y": 9,
        "name": "TEXT_SILPHCO3F_SCIENTIST"
      },
      {
        "x": 8,
        "y": 5,
        "name": "TEXT_SILPHCO3F_HYPER_POTION"
      }
    ]
  },
  "209": {
    "mapIdHex": "0xD1",
    "mapIdDecimal": 209,
    "mapName": "SILPH_CO_4F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 24,
        "y": 0,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 2
      },
      {
        "x": 26,
        "y": 0,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 2
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 7,
        "targetMap": "SILPH_CO_10F",
        "targetWarpId": 4
      },
      {
        "x": 17,
        "y": 3,
        "targetMap": "SILPH_CO_6F",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SILPH_CO_10F",
        "targetWarpId": 5
      },
      {
        "x": 17,
        "y": 11,
        "targetMap": "SILPH_CO_10F",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_SILPHCO4F_SILPH_WORKER_M"
      },
      {
        "x": 9,
        "y": 14,
        "name": "TEXT_SILPHCO4F_ROCKET1"
      },
      {
        "x": 14,
        "y": 6,
        "name": "TEXT_SILPHCO4F_SCIENTIST"
      },
      {
        "x": 26,
        "y": 10,
        "name": "TEXT_SILPHCO4F_ROCKET2"
      },
      {
        "x": 3,
        "y": 9,
        "name": "TEXT_SILPHCO4F_FULL_HEAL"
      },
      {
        "x": 4,
        "y": 7,
        "name": "TEXT_SILPHCO4F_MAX_REVIVE"
      },
      {
        "x": 5,
        "y": 8,
        "name": "TEXT_SILPHCO4F_ESCAPE_ROPE"
      }
    ]
  },
  "210": {
    "mapIdHex": "0xD2",
    "mapIdDecimal": 210,
    "mapName": "SILPH_CO_5F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 24,
        "y": 0,
        "targetMap": "SILPH_CO_6F",
        "targetWarpId": 2
      },
      {
        "x": 26,
        "y": 0,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 2
      },
      {
        "x": 20,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 27,
        "y": 3,
        "targetMap": "SILPH_CO_7F",
        "targetWarpId": 6
      },
      {
        "x": 9,
        "y": 15,
        "targetMap": "SILPH_CO_9F",
        "targetWarpId": 5
      },
      {
        "x": 11,
        "y": 5,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 13,
        "y": 9,
        "name": "TEXT_SILPHCO5F_SILPH_WORKER_M"
      },
      {
        "x": 8,
        "y": 16,
        "name": "TEXT_SILPHCO5F_ROCKET1"
      },
      {
        "x": 8,
        "y": 3,
        "name": "TEXT_SILPHCO5F_SCIENTIST"
      },
      {
        "x": 18,
        "y": 10,
        "name": "TEXT_SILPHCO5F_ROCKER"
      },
      {
        "x": 28,
        "y": 4,
        "name": "TEXT_SILPHCO5F_ROCKET2"
      },
      {
        "x": 2,
        "y": 13,
        "name": "TEXT_SILPHCO5F_TM_TAKE_DOWN"
      },
      {
        "x": 4,
        "y": 6,
        "name": "TEXT_SILPHCO5F_PROTEIN"
      },
      {
        "x": 21,
        "y": 16,
        "name": "TEXT_SILPHCO5F_CARD_KEY"
      },
      {
        "x": 22,
        "y": 12,
        "name": "TEXT_SILPHCO5F_POKEMON_REPORT1"
      },
      {
        "x": 25,
        "y": 10,
        "name": "TEXT_SILPHCO5F_POKEMON_REPORT2"
      },
      {
        "x": 24,
        "y": 6,
        "name": "TEXT_SILPHCO5F_POKEMON_REPORT3"
      }
    ]
  },
  "211": {
    "mapIdHex": "0xD3",
    "mapIdDecimal": 211,
    "mapName": "SILPH_CO_6F",
    "width": 13,
    "height": 9,
    "warps": [
      {
        "x": 16,
        "y": 0,
        "targetMap": "SILPH_CO_7F",
        "targetWarpId": 2
      },
      {
        "x": 14,
        "y": 0,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 3,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 5
      },
      {
        "x": 23,
        "y": 3,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 10,
        "y": 6,
        "name": "TEXT_SILPHCO6F_SILPH_WORKER_M1"
      },
      {
        "x": 20,
        "y": 6,
        "name": "TEXT_SILPHCO6F_SILPH_WORKER_M2"
      },
      {
        "x": 21,
        "y": 6,
        "name": "TEXT_SILPHCO6F_SILPH_WORKER_F1"
      },
      {
        "x": 11,
        "y": 10,
        "name": "TEXT_SILPHCO6F_SILPH_WORKER_F2"
      },
      {
        "x": 18,
        "y": 13,
        "name": "TEXT_SILPHCO6F_SILPH_WORKER_M3"
      },
      {
        "x": 17,
        "y": 3,
        "name": "TEXT_SILPHCO6F_ROCKET1"
      },
      {
        "x": 7,
        "y": 8,
        "name": "TEXT_SILPHCO6F_SCIENTIST"
      },
      {
        "x": 14,
        "y": 15,
        "name": "TEXT_SILPHCO6F_ROCKET2"
      },
      {
        "x": 3,
        "y": 12,
        "name": "TEXT_SILPHCO6F_HP_UP"
      },
      {
        "x": 2,
        "y": 15,
        "name": "TEXT_SILPHCO6F_X_ACCURACY"
      }
    ]
  },
  "212": {
    "mapIdHex": "0xD4",
    "mapIdDecimal": 212,
    "mapName": "SILPH_CO_7F",
    "width": 13,
    "height": 9,
    "warps": [
      {
        "x": 16,
        "y": 0,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 2
      },
      {
        "x": 22,
        "y": 0,
        "targetMap": "SILPH_CO_6F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 7,
        "targetMap": "SILPH_CO_11F",
        "targetWarpId": 4
      },
      {
        "x": 5,
        "y": 3,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 9
      },
      {
        "x": 21,
        "y": 15,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 5,
        "name": "TEXT_SILPHCO7F_SILPH_WORKER_M1"
      },
      {
        "x": 13,
        "y": 13,
        "name": "TEXT_SILPHCO7F_SILPH_WORKER_M2"
      },
      {
        "x": 7,
        "y": 10,
        "name": "TEXT_SILPHCO7F_SILPH_WORKER_M3"
      },
      {
        "x": 10,
        "y": 8,
        "name": "TEXT_SILPHCO7F_SILPH_WORKER_M4"
      },
      {
        "x": 13,
        "y": 1,
        "name": "TEXT_SILPHCO7F_ROCKET1"
      },
      {
        "x": 2,
        "y": 13,
        "name": "TEXT_SILPHCO7F_SCIENTIST"
      },
      {
        "x": 20,
        "y": 2,
        "name": "TEXT_SILPHCO7F_ROCKET2"
      },
      {
        "x": 19,
        "y": 14,
        "name": "TEXT_SILPHCO7F_ROCKET3"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_SILPHCO7F_RIVAL"
      },
      {
        "x": 1,
        "y": 9,
        "name": "TEXT_SILPHCO7F_CALCIUM"
      },
      {
        "x": 24,
        "y": 11,
        "name": "TEXT_SILPHCO7F_TM_SWORDS_DANCE"
      }
    ]
  },
  "213": {
    "mapIdHex": "0xD5",
    "mapIdDecimal": 213,
    "mapName": "SILPH_CO_8F",
    "width": 13,
    "height": 9,
    "warps": [
      {
        "x": 16,
        "y": 0,
        "targetMap": "SILPH_CO_9F",
        "targetWarpId": 2
      },
      {
        "x": 14,
        "y": 0,
        "targetMap": "SILPH_CO_7F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 11,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 7
      },
      {
        "x": 3,
        "y": 15,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 5
      },
      {
        "x": 11,
        "y": 5,
        "targetMap": "SILPH_CO_2F",
        "targetWarpId": 6
      },
      {
        "x": 11,
        "y": 9,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_SILPHCO8F_SILPH_WORKER_M"
      },
      {
        "x": 19,
        "y": 2,
        "name": "TEXT_SILPHCO8F_ROCKET1"
      },
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_SILPHCO8F_SCIENTIST"
      },
      {
        "x": 12,
        "y": 15,
        "name": "TEXT_SILPHCO8F_ROCKET2"
      }
    ]
  },
  "214": {
    "mapIdHex": "0xD6",
    "mapIdDecimal": 214,
    "mapName": "POKEMON_MANSION_2F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 5,
        "y": 10,
        "targetMap": "POKEMON_MANSION_1F",
        "targetWarpId": 5
      },
      {
        "x": 7,
        "y": 10,
        "targetMap": "POKEMON_MANSION_3F",
        "targetWarpId": 1
      },
      {
        "x": 25,
        "y": 14,
        "targetMap": "POKEMON_MANSION_3F",
        "targetWarpId": 3
      },
      {
        "x": 6,
        "y": 1,
        "targetMap": "POKEMON_MANSION_3F",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 17,
        "name": "TEXT_POKEMONMANSION2F_SUPER_NERD"
      },
      {
        "x": 28,
        "y": 7,
        "name": "TEXT_POKEMONMANSION2F_CALCIUM"
      },
      {
        "x": 18,
        "y": 2,
        "name": "TEXT_POKEMONMANSION2F_DIARY1"
      },
      {
        "x": 3,
        "y": 22,
        "name": "TEXT_POKEMONMANSION2F_DIARY2"
      }
    ]
  },
  "215": {
    "mapIdHex": "0xD7",
    "mapIdDecimal": 215,
    "mapName": "POKEMON_MANSION_3F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 7,
        "y": 10,
        "targetMap": "POKEMON_MANSION_2F",
        "targetWarpId": 2
      },
      {
        "x": 6,
        "y": 1,
        "targetMap": "POKEMON_MANSION_2F",
        "targetWarpId": 4
      },
      {
        "x": 25,
        "y": 14,
        "targetMap": "POKEMON_MANSION_2F",
        "targetWarpId": 3
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 11,
        "name": "TEXT_POKEMONMANSION3F_SUPER_NERD"
      },
      {
        "x": 20,
        "y": 11,
        "name": "TEXT_POKEMONMANSION3F_SCIENTIST"
      },
      {
        "x": 1,
        "y": 16,
        "name": "TEXT_POKEMONMANSION3F_MAX_POTION"
      },
      {
        "x": 25,
        "y": 5,
        "name": "TEXT_POKEMONMANSION3F_IRON"
      },
      {
        "x": 6,
        "y": 12,
        "name": "TEXT_POKEMONMANSION3F_DIARY"
      }
    ]
  },
  "216": {
    "mapIdHex": "0xD8",
    "mapIdDecimal": 216,
    "mapName": "POKEMON_MANSION_B1F",
    "width": 15,
    "height": 14,
    "warps": [
      {
        "x": 23,
        "y": 22,
        "targetMap": "POKEMON_MANSION_1F",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 16,
        "y": 23,
        "name": "TEXT_POKEMONMANSIONB1F_BURGLAR"
      },
      {
        "x": 27,
        "y": 11,
        "name": "TEXT_POKEMONMANSIONB1F_SCIENTIST"
      },
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_POKEMONMANSIONB1F_RARE_CANDY"
      },
      {
        "x": 1,
        "y": 22,
        "name": "TEXT_POKEMONMANSIONB1F_FULL_RESTORE"
      },
      {
        "x": 19,
        "y": 25,
        "name": "TEXT_POKEMONMANSIONB1F_TM_BLIZZARD"
      },
      {
        "x": 5,
        "y": 4,
        "name": "TEXT_POKEMONMANSIONB1F_TM_SOLARBEAM"
      },
      {
        "x": 16,
        "y": 20,
        "name": "TEXT_POKEMONMANSIONB1F_DIARY"
      },
      {
        "x": 5,
        "y": 13,
        "name": "TEXT_POKEMONMANSIONB1F_SECRET_KEY"
      }
    ]
  },
  "217": {
    "mapIdHex": "0xD9",
    "mapIdDecimal": 217,
    "mapName": "SAFARI_ZONE_EAST",
    "width": 15,
    "height": 13,
    "warps": [
      {
        "x": 0,
        "y": 4,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 7
      },
      {
        "x": 0,
        "y": 5,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 8
      },
      {
        "x": 0,
        "y": 22,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 7
      },
      {
        "x": 0,
        "y": 23,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 7
      },
      {
        "x": 25,
        "y": 9,
        "targetMap": "SAFARI_ZONE_EAST_REST_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 26,
        "y": 10,
        "description": "TEXT_SAFARIZONEEAST_REST_HOUSE_SIGN"
      },
      {
        "x": 6,
        "y": 4,
        "description": "TEXT_SAFARIZONEEAST_TRAINER_TIPS"
      },
      {
        "x": 5,
        "y": 23,
        "description": "TEXT_SAFARIZONEEAST_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 21,
        "y": 10,
        "name": "TEXT_SAFARIZONEEAST_FULL_RESTORE"
      },
      {
        "x": 3,
        "y": 7,
        "name": "TEXT_SAFARIZONEEAST_MAX_RESTORE"
      },
      {
        "x": 20,
        "y": 13,
        "name": "TEXT_SAFARIZONEEAST_CARBOS"
      },
      {
        "x": 15,
        "y": 12,
        "name": "TEXT_SAFARIZONEEAST_TM_EGG_BOMB"
      }
    ]
  },
  "218": {
    "mapIdHex": "0xDA",
    "mapIdDecimal": 218,
    "mapName": "SAFARI_ZONE_NORTH",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 2,
        "y": 35,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 1
      },
      {
        "x": 3,
        "y": 35,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 2
      },
      {
        "x": 8,
        "y": 35,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 3
      },
      {
        "x": 9,
        "y": 35,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 4
      },
      {
        "x": 20,
        "y": 35,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 5
      },
      {
        "x": 21,
        "y": 35,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 6
      },
      {
        "x": 39,
        "y": 30,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 1
      },
      {
        "x": 39,
        "y": 31,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 2
      },
      {
        "x": 35,
        "y": 3,
        "targetMap": "SAFARI_ZONE_NORTH_REST_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 36,
        "y": 4,
        "description": "TEXT_SAFARIZONENORTH_REST_HOUSE_SIGN"
      },
      {
        "x": 4,
        "y": 25,
        "description": "TEXT_SAFARIZONENORTH_TRAINER_TIPS_1"
      },
      {
        "x": 13,
        "y": 31,
        "description": "TEXT_SAFARIZONENORTH_SIGN"
      },
      {
        "x": 19,
        "y": 33,
        "description": "TEXT_SAFARIZONENORTH_TRAINER_TIPS_2"
      },
      {
        "x": 26,
        "y": 28,
        "description": "TEXT_SAFARIZONENORTH_TRAINER_TIPS_3"
      }
    ],
    "npc_events": [
      {
        "x": 25,
        "y": 1,
        "name": "TEXT_SAFARIZONENORTH_PROTEIN"
      },
      {
        "x": 19,
        "y": 7,
        "name": "TEXT_SAFARIZONENORTH_TM_SKULL_BASH"
      }
    ]
  },
  "219": {
    "mapIdHex": "0xDB",
    "mapIdDecimal": 219,
    "mapName": "SAFARI_ZONE_WEST",
    "width": 15,
    "height": 13,
    "warps": [
      {
        "x": 20,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 1
      },
      {
        "x": 21,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 2
      },
      {
        "x": 26,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 3
      },
      {
        "x": 27,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 4
      },
      {
        "x": 29,
        "y": 22,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 3
      },
      {
        "x": 29,
        "y": 23,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 4
      },
      {
        "x": 3,
        "y": 3,
        "targetMap": "SAFARI_ZONE_SECRET_HOUSE",
        "targetWarpId": 1
      },
      {
        "x": 11,
        "y": 11,
        "targetMap": "SAFARI_ZONE_WEST_REST_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 12,
        "y": 12,
        "description": "TEXT_SAFARIZONEWEST_REST_HOUSE_SIGN"
      },
      {
        "x": 17,
        "y": 3,
        "description": "TEXT_SAFARIZONEWEST_FIND_WARDENS_TEETH_SIGN"
      },
      {
        "x": 26,
        "y": 4,
        "description": "TEXT_SAFARIZONEWEST_TRAINER_TIPS"
      },
      {
        "x": 24,
        "y": 22,
        "description": "TEXT_SAFARIZONEWEST_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 8,
        "y": 20,
        "name": "TEXT_SAFARIZONEWEST_MAX_POTION"
      },
      {
        "x": 9,
        "y": 7,
        "name": "TEXT_SAFARIZONEWEST_TM_DOUBLE_TEAM"
      },
      {
        "x": 18,
        "y": 18,
        "name": "TEXT_SAFARIZONEWEST_MAX_REVIVE"
      },
      {
        "x": 19,
        "y": 7,
        "name": "TEXT_SAFARIZONEWEST_GOLD_TEETH"
      }
    ]
  },
  "220": {
    "mapIdHex": "0xDC",
    "mapIdDecimal": 220,
    "mapName": "SAFARI_ZONE_CENTER",
    "width": 15,
    "height": 13,
    "warps": [
      {
        "x": 14,
        "y": 25,
        "targetMap": "SAFARI_ZONE_GATE",
        "targetWarpId": 3
      },
      {
        "x": 15,
        "y": 25,
        "targetMap": "SAFARI_ZONE_GATE",
        "targetWarpId": 4
      },
      {
        "x": 0,
        "y": 10,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 5
      },
      {
        "x": 0,
        "y": 11,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 6
      },
      {
        "x": 14,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 5
      },
      {
        "x": 15,
        "y": 0,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 6
      },
      {
        "x": 29,
        "y": 10,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 3
      },
      {
        "x": 29,
        "y": 11,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 4
      },
      {
        "x": 17,
        "y": 19,
        "targetMap": "SAFARI_ZONE_CENTER_REST_HOUSE",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 18,
        "y": 20,
        "description": "TEXT_SAFARIZONECENTER_REST_HOUSE_SIGN"
      },
      {
        "x": 14,
        "y": 22,
        "description": "TEXT_SAFARIZONECENTER_TRAINER_TIPS_SIGN"
      }
    ],
    "npc_events": [
      {
        "x": 14,
        "y": 10,
        "name": "TEXT_SAFARIZONECENTER_NUGGET"
      }
    ]
  },
  "221": {
    "mapIdHex": "0xDD",
    "mapIdDecimal": 221,
    "mapName": "SAFARI_ZONE_CENTER_REST_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 9
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "SAFARI_ZONE_CENTER",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 2,
        "name": "TEXT_SAFARIZONECENTERRESTHOUSE_GIRL"
      },
      {
        "x": 1,
        "y": 4,
        "name": "TEXT_SAFARIZONECENTERRESTHOUSE_SCIENTIST"
      }
    ]
  },
  "222": {
    "mapIdHex": "0xDE",
    "mapIdDecimal": 222,
    "mapName": "SAFARI_ZONE_SECRET_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 7
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 3,
        "name": "TEXT_SAFARIZONESECRETHOUSE_FISHING_GURU"
      }
    ]
  },
  "223": {
    "mapIdHex": "0xDF",
    "mapIdDecimal": 223,
    "mapName": "SAFARI_ZONE_WEST_REST_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 8
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "SAFARI_ZONE_WEST",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 4,
        "y": 4,
        "name": "TEXT_SAFARIZONEWESTRESTHOUSE_SCIENTIST"
      },
      {
        "x": 0,
        "y": 2,
        "name": "TEXT_SAFARIZONEWESTRESTHOUSE_COOLTRAINER_M"
      },
      {
        "x": 6,
        "y": 2,
        "name": "TEXT_SAFARIZONEWESTRESTHOUSE_SILPH_WORKER_F"
      }
    ]
  },
  "224": {
    "mapIdHex": "0xE0",
    "mapIdDecimal": 224,
    "mapName": "SAFARI_ZONE_EAST_REST_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "SAFARI_ZONE_EAST",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 3,
        "name": "TEXT_SAFARIZONEEASTRESTHOUSE_SCIENTIST"
      },
      {
        "x": 4,
        "y": 2,
        "name": "TEXT_SAFARIZONEEASTRESTHOUSE_ROCKER"
      },
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_SAFARIZONEEASTRESTHOUSE_SILPH_WORKER_M"
      }
    ]
  },
  "225": {
    "mapIdHex": "0xE1",
    "mapIdDecimal": 225,
    "mapName": "SAFARI_ZONE_NORTH_REST_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 9
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "SAFARI_ZONE_NORTH",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 6,
        "y": 3,
        "name": "TEXT_SAFARIZONENORTHRESTHOUSE_SCIENTIST"
      },
      {
        "x": 3,
        "y": 4,
        "name": "TEXT_SAFARIZONENORTHRESTHOUSE_SAFARI_ZONE_WORKER"
      },
      {
        "x": 1,
        "y": 5,
        "name": "TEXT_SAFARIZONENORTHRESTHOUSE_GENTLEMAN"
      }
    ]
  },
  "226": {
    "mapIdHex": "0xE2",
    "mapIdDecimal": 226,
    "mapName": "CERULEAN_CAVE_2F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 29,
        "y": 1,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 3
      },
      {
        "x": 22,
        "y": 6,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 4
      },
      {
        "x": 19,
        "y": 7,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 5
      },
      {
        "x": 9,
        "y": 1,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 6
      },
      {
        "x": 1,
        "y": 3,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 7
      },
      {
        "x": 3,
        "y": 11,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 29,
        "y": 9,
        "name": "TEXT_CERULEANCAVE2F_PP_UP"
      },
      {
        "x": 4,
        "y": 15,
        "name": "TEXT_CERULEANCAVE2F_ULTRA_BALL"
      },
      {
        "x": 13,
        "y": 6,
        "name": "TEXT_CERULEANCAVE2F_FULL_RESTORE"
      }
    ]
  },
  "227": {
    "mapIdHex": "0xE3",
    "mapIdDecimal": 227,
    "mapName": "CERULEAN_CAVE_B1F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 3,
        "y": 6,
        "targetMap": "CERULEAN_CAVE_1F",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 27,
        "y": 13,
        "name": "TEXT_CERULEANCAVEB1F_MEWTWO"
      },
      {
        "x": 16,
        "y": 9,
        "name": "TEXT_CERULEANCAVEB1F_ULTRA_BALL"
      },
      {
        "x": 18,
        "y": 1,
        "name": "TEXT_CERULEANCAVEB1F_MAX_REVIVE"
      }
    ]
  },
  "228": {
    "mapIdHex": "0xE4",
    "mapIdDecimal": 228,
    "mapName": "CERULEAN_CAVE_1F",
    "width": 15,
    "height": 9,
    "warps": [
      {
        "x": 24,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 25,
        "y": 17,
        "targetMap": "LAST_MAP",
        "targetWarpId": 7
      },
      {
        "x": 27,
        "y": 1,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 1
      },
      {
        "x": 23,
        "y": 7,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 2
      },
      {
        "x": 18,
        "y": 9,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 3
      },
      {
        "x": 7,
        "y": 1,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 4
      },
      {
        "x": 1,
        "y": 3,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 5
      },
      {
        "x": 3,
        "y": 11,
        "targetMap": "CERULEAN_CAVE_2F",
        "targetWarpId": 6
      },
      {
        "x": 0,
        "y": 6,
        "targetMap": "CERULEAN_CAVE_B1F",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 13,
        "name": "TEXT_CERULEANCAVE1F_FULL_RESTORE"
      },
      {
        "x": 19,
        "y": 3,
        "name": "TEXT_CERULEANCAVE1F_MAX_ELIXER"
      },
      {
        "x": 5,
        "y": 0,
        "name": "TEXT_CERULEANCAVE1F_NUGGET"
      }
    ]
  },
  "229": {
    "mapIdHex": "0xE5",
    "mapIdDecimal": 229,
    "mapName": "NAME_RATERS_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 6
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_NAMERATERSHOUSE_NAME_RATER"
      }
    ]
  },
  "230": {
    "mapIdHex": "0xE6",
    "mapIdDecimal": 230,
    "mapName": "CERULEAN_BADGE_HOUSE",
    "width": 4,
    "height": 4,
    "warps": [
      {
        "x": 2,
        "y": 0,
        "targetMap": "LAST_MAP",
        "targetWarpId": 10
      },
      {
        "x": 2,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      },
      {
        "x": 3,
        "y": 7,
        "targetMap": "LAST_MAP",
        "targetWarpId": 9
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 3,
        "name": "TEXT_CERULEANBADGEHOUSE_MIDDLE_AGED_MAN"
      }
    ]
  },
  "231": {
    "mapIdHex": "0xE7",
    "mapIdDecimal": 231,
    "mapName": "UNUSED_MAP_E7",
    "width": 0,
    "height": 0
  },
  "232": {
    "mapIdHex": "0xE8",
    "mapIdDecimal": 232,
    "mapName": "ROCK_TUNNEL_B1F",
    "width": 20,
    "height": 18,
    "warps": [
      {
        "x": 33,
        "y": 25,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 5
      },
      {
        "x": 27,
        "y": 3,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 6
      },
      {
        "x": 23,
        "y": 11,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 7
      },
      {
        "x": 3,
        "y": 3,
        "targetMap": "ROCK_TUNNEL_1F",
        "targetWarpId": 8
      }
    ],
    "npc_events": [
      {
        "x": 11,
        "y": 13,
        "name": "TEXT_ROCKTUNNELB1F_COOLTRAINER_F1"
      },
      {
        "x": 6,
        "y": 10,
        "name": "TEXT_ROCKTUNNELB1F_HIKER1"
      },
      {
        "x": 3,
        "y": 5,
        "name": "TEXT_ROCKTUNNELB1F_SUPER_NERD1"
      },
      {
        "x": 20,
        "y": 21,
        "name": "TEXT_ROCKTUNNELB1F_SUPER_NERD2"
      },
      {
        "x": 30,
        "y": 10,
        "name": "TEXT_ROCKTUNNELB1F_HIKER2"
      },
      {
        "x": 14,
        "y": 28,
        "name": "TEXT_ROCKTUNNELB1F_COOLTRAINER_F2"
      },
      {
        "x": 33,
        "y": 5,
        "name": "TEXT_ROCKTUNNELB1F_HIKER3"
      },
      {
        "x": 26,
        "y": 30,
        "name": "TEXT_ROCKTUNNELB1F_SUPER_NERD3"
      }
    ]
  },
  "233": {
    "mapIdHex": "0xE9",
    "mapIdDecimal": 233,
    "mapName": "SILPH_CO_9F",
    "width": 13,
    "height": 9,
    "warps": [
      {
        "x": 14,
        "y": 0,
        "targetMap": "SILPH_CO_10F",
        "targetWarpId": 1
      },
      {
        "x": 16,
        "y": 0,
        "targetMap": "SILPH_CO_8F",
        "targetWarpId": 1
      },
      {
        "x": 18,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 9,
        "y": 3,
        "targetMap": "SILPH_CO_3F",
        "targetWarpId": 8
      },
      {
        "x": 17,
        "y": 15,
        "targetMap": "SILPH_CO_5F",
        "targetWarpId": 5
      }
    ],
    "npc_events": [
      {
        "x": 3,
        "y": 14,
        "name": "TEXT_SILPHCO9F_NURSE"
      },
      {
        "x": 2,
        "y": 4,
        "name": "TEXT_SILPHCO9F_ROCKET1"
      },
      {
        "x": 21,
        "y": 13,
        "name": "TEXT_SILPHCO9F_SCIENTIST"
      },
      {
        "x": 13,
        "y": 16,
        "name": "TEXT_SILPHCO9F_ROCKET2"
      }
    ]
  },
  "234": {
    "mapIdHex": "0xEA",
    "mapIdDecimal": 234,
    "mapName": "SILPH_CO_10F",
    "width": 8,
    "height": 9,
    "warps": [
      {
        "x": 8,
        "y": 0,
        "targetMap": "SILPH_CO_9F",
        "targetWarpId": 1
      },
      {
        "x": 10,
        "y": 0,
        "targetMap": "SILPH_CO_11F",
        "targetWarpId": 1
      },
      {
        "x": 12,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 9,
        "y": 11,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 4
      },
      {
        "x": 13,
        "y": 15,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 6
      },
      {
        "x": 13,
        "y": 7,
        "targetMap": "SILPH_CO_4F",
        "targetWarpId": 7
      }
    ],
    "npc_events": [
      {
        "x": 1,
        "y": 9,
        "name": "TEXT_SILPHCO10F_ROCKET"
      },
      {
        "x": 10,
        "y": 2,
        "name": "TEXT_SILPHCO10F_SCIENTIST"
      },
      {
        "x": 9,
        "y": 15,
        "name": "TEXT_SILPHCO10F_SILPH_WORKER_F"
      },
      {
        "x": 2,
        "y": 12,
        "name": "TEXT_SILPHCO10F_TM_EARTHQUAKE"
      },
      {
        "x": 4,
        "y": 14,
        "name": "TEXT_SILPHCO10F_RARE_CANDY"
      },
      {
        "x": 5,
        "y": 11,
        "name": "TEXT_SILPHCO10F_CARBOS"
      }
    ]
  },
  "235": {
    "mapIdHex": "0xEB",
    "mapIdDecimal": 235,
    "mapName": "SILPH_CO_11F",
    "width": 9,
    "height": 9,
    "warps": [
      {
        "x": 9,
        "y": 0,
        "targetMap": "SILPH_CO_10F",
        "targetWarpId": 2
      },
      {
        "x": 13,
        "y": 0,
        "targetMap": "SILPH_CO_ELEVATOR",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 5,
        "targetMap": "LAST_MAP",
        "targetWarpId": 10
      },
      {
        "x": 3,
        "y": 2,
        "targetMap": "SILPH_CO_7F",
        "targetWarpId": 4
      }
    ],
    "npc_events": [
      {
        "x": 7,
        "y": 5,
        "name": "TEXT_SILPHCO11F_SILPH_PRESIDENT"
      },
      {
        "x": 10,
        "y": 5,
        "name": "TEXT_SILPHCO11F_BEAUTY"
      },
      {
        "x": 6,
        "y": 9,
        "name": "TEXT_SILPHCO11F_GIOVANNI"
      },
      {
        "x": 3,
        "y": 16,
        "name": "TEXT_SILPHCO11F_ROCKET1"
      },
      {
        "x": 15,
        "y": 9,
        "name": "TEXT_SILPHCO11F_ROCKET2"
      }
    ]
  },
  "236": {
    "mapIdHex": "0xEC",
    "mapIdDecimal": 236,
    "mapName": "SILPH_CO_ELEVATOR",
    "width": 2,
    "height": 2,
    "warps": [
      {
        "x": 1,
        "y": 3,
        "targetMap": "UNUSED_MAP_ED",
        "targetWarpId": 1
      },
      {
        "x": 2,
        "y": 3,
        "targetMap": "UNUSED_MAP_ED",
        "targetWarpId": 1
      }
    ],
    "bg_events": [
      {
        "x": 3,
        "y": 0,
        "description": "TEXT_SILPHCOELEVATOR_ELEVATOR"
      }
    ]
  },
  "237": {
    "mapIdHex": "0xED",
    "mapIdDecimal": 237,
    "mapName": "UNUSED_MAP_ED",
    "width": 0,
    "height": 0
  },
  "238": {
    "mapIdHex": "0xEE",
    "mapIdDecimal": 238,
    "mapName": "UNUSED_MAP_EE",
    "width": 0,
    "height": 0
  },
  "239": {
    "mapIdHex": "0xEF",
    "mapIdDecimal": 239,
    "mapName": "TRADE_CENTER",
    "width": 5,
    "height": 4,
    "warps": [],
    "npc_events": [
      {
        "x": 2,
        "y": 2,
        "name": "TEXT_TRADECENTER_OPPONENT"
      }
    ]
  },
  "240": {
    "mapIdHex": "0xF0",
    "mapIdDecimal": 240,
    "mapName": "COLOSSEUM",
    "width": 5,
    "height": 4,
    "warps": [],
    "npc_events": [
      {
        "x": 2,
        "y": 2,
        "name": "TEXT_COLOSSEUM_OPPONENT"
      }
    ]
  },
  "241": {
    "mapIdHex": "0xF1",
    "mapIdDecimal": 241,
    "mapName": "UNUSED_MAP_F1",
    "width": 0,
    "height": 0
  },
  "242": {
    "mapIdHex": "0xF2",
    "mapIdDecimal": 242,
    "mapName": "UNUSED_MAP_F2",
    "width": 0,
    "height": 0
  },
  "243": {
    "mapIdHex": "0xF3",
    "mapIdDecimal": 243,
    "mapName": "UNUSED_MAP_F3",
    "width": 0,
    "height": 0
  },
  "244": {
    "mapIdHex": "0xF4",
    "mapIdDecimal": 244,
    "mapName": "UNUSED_MAP_F4",
    "width": 0,
    "height": 0
  },
  "245": {
    "mapIdHex": "0xF5",
    "mapIdDecimal": 245,
    "mapName": "LORELEIS_ROOM",
    "width": 5,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "INDIGO_PLATEAU_LOBBY",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "INDIGO_PLATEAU_LOBBY",
        "targetWarpId": 3
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "BRUNOS_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "BRUNOS_ROOM",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_LORELEISROOM_LORELEI"
      }
    ]
  },
  "246": {
    "mapIdHex": "0xF6",
    "mapIdDecimal": 246,
    "mapName": "BRUNOS_ROOM",
    "width": 5,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "LORELEIS_ROOM",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "LORELEIS_ROOM",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "AGATHAS_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "AGATHAS_ROOM",
        "targetWarpId": 2
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_BRUNOSROOM_BRUNO"
      }
    ]
  },
  "247": {
    "mapIdHex": "0xF7",
    "mapIdDecimal": 247,
    "mapName": "AGATHAS_ROOM",
    "width": 5,
    "height": 6,
    "warps": [
      {
        "x": 4,
        "y": 11,
        "targetMap": "BRUNOS_ROOM",
        "targetWarpId": 3
      },
      {
        "x": 5,
        "y": 11,
        "targetMap": "BRUNOS_ROOM",
        "targetWarpId": 4
      },
      {
        "x": 4,
        "y": 0,
        "targetMap": "LANCES_ROOM",
        "targetWarpId": 1
      },
      {
        "x": 5,
        "y": 0,
        "targetMap": "LANCES_ROOM",
        "targetWarpId": 1
      }
    ],
    "npc_events": [
      {
        "x": 5,
        "y": 2,
        "name": "TEXT_AGATHASROOM_AGATHA"
      }
    ]
  }
}
