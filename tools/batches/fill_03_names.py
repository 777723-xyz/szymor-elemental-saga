#!/usr/bin/env python3
"""Fill batch 03: troop formation names (mostly dev-facing, but translated)."""
import csv
import os

D = {
"DB_Troops_1_name": "Man-eating Bat x3",
"DB_Troops_2_name": "Man-eating Rat x2",
"DB_Troops_3_name": "Man-eating Spider x2",
"DB_Troops_4_name": "Man-eating Bat x2, Man-eating Rat",
"DB_Troops_5_name": "Man-eating Bat x2, Man-eating Spider x2",
"DB_Troops_6_name": "Man-eating Rat x2, Man-eating Spider x2",
"DB_Troops_8_name": "Man-eating Spider x3",
"DB_Troops_11_name": "Man-eating Bee x2",
"DB_Troops_12_name": "Man-eating Grass x2",
"DB_Troops_14_name": "Nau, Final Battle",
"DB_Troops_16_name": "Nau, Auto Battle",
"DB_Troops_18_name": "Desert Wolf x2",
"DB_Troops_22_name": "Aodaisho, Mamushi",
"DB_Troops_23_name": "Habu, Aodaisho",
"DB_Troops_24_name": "Mamushi x2",
"DB_Troops_25_name": "Habu, Mamushi, Aodaisho",
"DB_Troops_26_name": "Moving Doll x3",
"DB_Troops_31_name": "Moving Doll x2",
"DB_Troops_34_name": "Flame Fiend, Wind Fiend, Ice Fiend",
"DB_Troops_35_name": "Mycenae, Seiryu",
"DB_Troops_37_name": "Fire-Eating Bird x4, Flame Bull",
"DB_Troops_38_name": "Sachiko x3",
"DB_Troops_39_name": "Sachiko x2, Flame Bull",
"DB_Troops_41_name": "Nau, Second Fight",
"DB_Troops_47_name": "Sachiko, Flame Bull",
"DB_Troops_49_name": "Thunder Bull, Sachiko",
"DB_Troops_50_name": "Fire-Eating Bird x2, Flame Bull",
"DB_Troops_51_name": "Fire-Breathing Dog x2",
"DB_Troops_52_name": "Fire-Eating Bird x2, Fire-Breathing Dog",
"DB_Troops_53_name": "Sachiko x3",
"DB_Troops_54_name": "Flame Bull, Thunder Bull",
"DB_Troops_55_name": "test",
"DB_Troops_56_name": "Charred Doll x2, Frozen Doll x2",
"DB_Troops_57_name": "Growing Eyeball x2",
"DB_Troops_58_name": "Growing Eyeball x3",
"DB_Troops_61_name": "Thunder Fairy x2",
"DB_Troops_63_name": "Charred Doll, Siren, Frozen Doll",
"DB_Troops_64_name": "Growing Eyeball x2, Dancing Fiend",
"DB_Troops_65_name": "Frozen Doll, Fire-Breathing Dog, Charred Doll",
"DB_Troops_66_name": "Thunder Fairy x2, Dancing Fiend",
"DB_Troops_67_name": "Thunder Fairy x2, Siren",
"DB_Troops_68_name": "Thunder Fairy x2, Thunder Bull",
"DB_Troops_69_name": "Frozen Doll, Siren, Growing Eyeball, Charred Doll",
"DB_Troops_70_name": "Charred Doll, Dancing Fiend, Siren, Frozen Doll",
"DB_Troops_71_name": "Dancing Fiend x3",
"DB_Troops_72_name": "Growing Eyeball x4",
"DB_Troops_76_name": "Yabamination, Trash Mob",
"DB_Troops_77_name": "Darkly Shining Dragon, Trash Mob",
"DB_Troops_81_name": "Demon King Dafill, First Fight",
"DB_Troops_82_name": "Demon King Dafill, The Real Thing",
"DB_Troops_85_name": "Man-eating Bat x3",
"DB_Troops_86_name": "Man-eating Rat x2",
"DB_Troops_87_name": "Man-eating Spider x2",
"DB_Troops_88_name": "Man-eating Bat x2, Man-eating Rat",
"DB_Troops_89_name": "Man-eating Bat x2, Man-eating Spider x2",
"DB_Troops_90_name": "Man-eating Rat x2, Man-eating Spider x2",
"DB_Troops_92_name": "Man-eating Spider x3",
"DB_Troops_95_name": "Nau, Final Battle (Rear)",
"DB_Troops_99_name": "Hair-Growing Doll x2",
"DB_Troops_102_name": "Samurai Boss",
"DB_Troops_103_name": "Fire Samurai, Ice Samurai",
"DB_Troops_104_name": "Ice Samurai, Wind Samurai",
"DB_Troops_105_name": "Hair-Growing Doll x3",
"DB_Troops_106_name": "Mycenae (Rear)",
"DB_Troops_107_name": "Nau, Mycenae",
"DB_Troops_109_name": "Brainwashed Pipin (Rear)",
"DB_Troops_110_name": "Cloud Turtle, Boss",
"DB_Troops_111_name": "Thunder Dog, Boss",
"DB_Troops_116_name": "Venomous Snake x3",
"DB_Troops_117_name": "Venomous Snake x2",
"DB_Troops_122_name": "Sayoko, Dark Fairy, Venomous Snake",
"DB_Troops_123_name": "Burning Hinotama, Dark Fairy, Frozen Hinotama",
"DB_Troops_124_name": "Burning Hinotama, Venomous Snake, Frozen Hinotama",
"DB_Troops_125_name": "Dark Fairy, Burning Hinotama, Venomous Snake",
"DB_Troops_126_name": "Dark Fairy, Blue Giant",
"DB_Troops_127_name": "Burning Hinotama, Blue Giant",
"DB_Troops_128_name": "Blue Giant, Frozen Hinotama",
"DB_Troops_130_name": "Skilled Bandit, Frozen Hinotama",
"DB_Troops_131_name": "Skilled Bandit, Burning Hinotama",
"DB_Troops_132_name": "Sayoko, Skilled Bandit, Venomous Snake",
"DB_Troops_133_name": "Skilled Bandit, Blue Giant",
"DB_Troops_135_name": "Grand Mage Pikepike (Rear)",
"DB_Troops_136_name": "Mycenae (Rear)",
"DB_Troops_137_name": "Nau (Rear)",
"DB_Troops_138_name": "Demon King Dafill, First Fight (Rear)",
"DB_Troops_139_name": "Demon King Dafill, The Real Thing (Rear)",
"DB_Troops_140_name": "Great Demon King Dafill (Rear)",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "name.tsv"))


def main():
    with open(PATH, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    filled = 0
    for r in rows:
        if r["id"] in D:
            r["translation"] = D[r["id"]]
            filled += 1
    with open(PATH, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print("name.tsv filled", filled, "/", len(rows))


if __name__ == "__main__":
    main()
