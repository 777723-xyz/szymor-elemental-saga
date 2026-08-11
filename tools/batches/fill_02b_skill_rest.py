#!/usr/bin/env python3
"""Fill the remaining skill descriptions (batch 02b)."""
import csv
import os

D = {
"DB_Skills_151_description": "A combo spell that soaks the enemy with a tsunami, then drops a colossal bolt of\nlightning. Deals about 5000 damage to all enemies and stuns. Costs 50 EP.",
"DB_Skills_158_description": "For enemies.",
"DB_Skills_159_description": "Water magic. Summons a tsunami to crash down on the enemy group... a mighty spell.\nDeals about 1200 damage to all enemies. Costs 30 EP.",
"DB_Skills_15_description": "Attacks with the equipped weapon.",
"DB_Skills_160_description": "Wind magic. A gale wraps around the body, doubling agility and allowing movement\nat superhuman speed. Costs 9 EP.",
"DB_Skills_161_description": "Wind magic. Sharp blades of vacuum tear at the enemy's feet.\nDeals about 800 damage to one enemy and lowers agility. Costs 18 EP.",
"DB_Skills_162_description": "Wind magic. Calls a massive bolt of lightning down on the enemy... a mighty power.\nDeals about 2000 damage to one enemy and stuns. Costs 40 EP.",
"DB_Skills_163_description": "Attacks with the equipped weapon.",
"DB_Skills_164_description": "A thrust that confuses the enemy with deft spearplay and strikes the opening it\ncreates. Ignores defense and lowers the enemy's defense. Costs 20 SP.",
"DB_Skills_165_description": "Runs into the enemy group while swinging the weapon around. Costs 9 SP.",
"DB_Skills_166_description": "Dances the berserker dance while swinging a flame-wreathed sword.\nApplies the Warrior effect to the whole party. Costs 50 SP.",
"DB_Skills_168_description": "The defense-focused shape of the main gauche can even destroy enemy weapons.\nIgnores defense and lowers attack power. Costs 20 EP.",
"DB_Skills_169_description": "Attacks with the equipped weapon.",
"DB_Skills_16_description": "Charges into the enemy group, swinging a large weapon around.\nWeaker than a normal attack. A straight sword and curved sword skill.",
"DB_Skills_170_description": "Charges one's spirit and brings a great sword down in a huge swing. Sometimes\nmisses, but deals about double damage. Costs 18 SP.",
"DB_Skills_171_description": "Attacks with the equipped weapon.",
"DB_Skills_172_description": "Hides, circles behind the enemy group, and suddenly strikes.\nIgnores defense against all enemies and inflicts confusion. Costs 30 SP.",
"DB_Skills_173_description": "Wind magic. A gale wraps around the body, doubling agility and allowing movement\nat superhuman speed. Costs 9 EP.",
"DB_Skills_174_description": "Water magic. Uses the power of the crest to create healing water.\nRestores about 800 HP to one ally. Costs 10 EP.",
"DB_Skills_175_description": "For enemies.",
"DB_Skills_17_description": "Charges into the enemy group, swinging a large weapon around.\nWeaker than a normal attack. A straight sword and curved sword skill.",
"DB_Skills_18_description": "Attacks with the equipped weapon.",
"DB_Skills_1_description": "Attacks with the equipped weapon.",
"DB_Skills_20_description": "A skill that sweeps the enemy group's feet. If it works, the enemy falls.\nA fallen enemy's defense drops greatly. A spear skill. Costs 12 SP.",
"DB_Skills_21_description": "Breaks the enemy's defense with the first stroke and slashes with the second.\nAn attack ignoring half the enemy's defense. A katana skill. Costs 12 SP.",
"DB_Skills_22_description": "Charges one's spirit and brings a great sword down in a huge swing. Sometimes\nmisses, but deals about double damage. Costs 18 SP.",
"DB_Skills_23_description": "Attacks with the equipped weapon.",
"DB_Skills_25_description": "For enemies.",
"DB_Skills_26_description": "For enemies.",
"DB_Skills_27_description": "Charges into the enemy group, swinging a large weapon around.\nWeaker than a normal attack. A straight sword and curved sword skill.",
"DB_Skills_28_description": "A thrust from near ground level that strikes at the enemy's vitals in an instant.\nThe enemy can't react in time; ignores defense. Costs 18 SP.",
"DB_Skills_29_description": "A thrust that confuses the enemy with deft swordplay and strikes the opening it\ncreates. Ignores defense and lowers the enemy's defense. Costs 20 SP.",
"DB_Skills_30_description": "Wind magic. A gale wraps around the body, doubling agility and allowing movement\nat superhuman speed. Cannot be stacked. Costs 9 EP.",
"DB_Skills_31_description": "Wind magic. Sharp blades of vacuum tear at the enemy's feet.\nDeals about 800 damage to one enemy and lowers agility. Costs 18 EP.",
}

PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "docs", "text", "batches", "description.tsv"))


def main():
    with open(PATH, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    filled = 0
    for r in rows:
        if not (r.get("translation") or "").strip() and r["id"] in D:
            r["translation"] = D[r["id"]]
            filled += 1
    with open(PATH, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    remaining = [r["id"] for r in rows if not (r.get("translation") or "").strip()]
    print("filled", filled, "remaining", len(remaining), remaining)


if __name__ == "__main__":
    main()
