#!/usr/bin/env python3
"""Fill batch 01: System.json UI terms and plugin parameter strings."""
import csv
import os

SYS = {
    "SYS_armorTypes_1": "General Armor", "SYS_armorTypes_2": "Magic Armor",
    "SYS_armorTypes_3": "Light Armor", "SYS_armorTypes_4": "Heavy Armor",
    "SYS_armorTypes_5": "Small Shield", "SYS_armorTypes_6": "Large Shield",
    "SYS_armorTypes_7": "Knight Armor", "SYS_armorTypes_8": "Royal Gear",
    "SYS_armorTypes_9": "Samurai Armor",
    "SYS_elements_1": "Physical", "SYS_elements_2": "Fire",
    "SYS_elements_3": "Water", "SYS_elements_4": "Wind", "SYS_elements_5": "Dark",
    "SYS_equipTypes_1": "Weapon", "SYS_equipTypes_2": "Shield",
    "SYS_equipTypes_3": "Accessory", "SYS_equipTypes_4": "Body",
    "SYS_gameTitle": "Crest Story", "SYS_skillTypes_1": "Magic",
    "SYS_skillTypes_2": "Skill",
    "SYS_terms_basic_0": "Level", "SYS_terms_basic_8": "EXP",
    "SYS_terms_commands_0": "Battle Start", "SYS_terms_commands_1": "Flee",
    "SYS_terms_commands_10": "Quit Game", "SYS_terms_commands_11": "Options",
    "SYS_terms_commands_12": "Weapons", "SYS_terms_commands_13": "Armor",
    "SYS_terms_commands_14": "Key Items", "SYS_terms_commands_15": "Equip",
    "SYS_terms_commands_16": "Optimize", "SYS_terms_commands_17": "Remove All",
    "SYS_terms_commands_18": "New Game", "SYS_terms_commands_19": "Continue",
    "SYS_terms_commands_21": "To Title", "SYS_terms_commands_22": "Quit",
    "SYS_terms_commands_24": "Buy", "SYS_terms_commands_25": "Sell",
    "SYS_terms_commands_3": "Guard", "SYS_terms_commands_4": "Item",
    "SYS_terms_commands_5": "Skill", "SYS_terms_commands_6": "Equip",
    "SYS_terms_commands_7": "Status", "SYS_terms_commands_8": "Order",
    "SYS_terms_commands_9": "Save",
    "SYS_terms_messages_actionFailure": "%1 was ineffective!",
    "SYS_terms_messages_actorDamage": "%1 took %2 damage!",
    "SYS_terms_messages_actorDrain": "%1's %2 was drained by %3!",
    "SYS_terms_messages_actorGain": "%1's %2 rose by %3!",
    "SYS_terms_messages_actorLoss": "%1's %2 fell by %3!",
    "SYS_terms_messages_actorNoDamage": "%1 took no damage!",
    "SYS_terms_messages_actorNoHit": "Miss! %1 took no damage!",
    "SYS_terms_messages_actorRecovery": "%1's %2 recovered by %3!",
    "SYS_terms_messages_alwaysDash": "Always Dash",
    "SYS_terms_messages_bgmVolume": "BGM Volume",
    "SYS_terms_messages_bgsVolume": "BGS Volume",
    "SYS_terms_messages_buffAdd": "%1's %2 rose!",
    "SYS_terms_messages_buffRemove": "%1's %2 returned to normal!",
    "SYS_terms_messages_commandRemember": "Remember Commands",
    "SYS_terms_messages_counterAttack": "%1 counterattacks!",
    "SYS_terms_messages_criticalToActor": "Critical blow!!",
    "SYS_terms_messages_criticalToEnemy": "A mighty critical!!",
    "SYS_terms_messages_debuffAdd": "%1's %2 fell!",
    "SYS_terms_messages_defeat": "%1 was defeated...!!",
    "SYS_terms_messages_emerge": "%1 appears!",
    "SYS_terms_messages_enemyDamage": "%1 took %2 damage!",
    "SYS_terms_messages_enemyDrain": "%1's %2 was drained by %3!",
    "SYS_terms_messages_enemyGain": "%1's %2 rose by %3!",
    "SYS_terms_messages_enemyLoss": "%1's %2 fell by %3!",
    "SYS_terms_messages_enemyNoDamage": "No damage to %1!",
    "SYS_terms_messages_enemyNoHit": "Miss! No damage to %1!",
    "SYS_terms_messages_enemyRecovery": "%1's %2 recovered by %3!",
    "SYS_terms_messages_escapeFailure": "But you couldn't escape!",
    "SYS_terms_messages_escapeStart": "%1 fled the battle!",
    "SYS_terms_messages_evasion": "%1 evaded the attack!",
    "SYS_terms_messages_expNext": "Next %1:",
    "SYS_terms_messages_expTotal": "Current %1:",
    "SYS_terms_messages_file": "File",
    "SYS_terms_messages_levelUp": "%1 reached %2 %3!",
    "SYS_terms_messages_loadMessage": "Which file would you like to load?",
    "SYS_terms_messages_magicEvasion": "%1 nullified the magic!",
    "SYS_terms_messages_magicReflection": "%1 reflected the magic!",
    "SYS_terms_messages_meVolume": "ME Volume",
    "SYS_terms_messages_obtainExp": "Gained %1 %2!",
    "SYS_terms_messages_obtainGold": "Gained %1\\G!",
    "SYS_terms_messages_obtainItem": "Obtained %1!",
    "SYS_terms_messages_obtainSkill": "Learned %1!",
    "SYS_terms_messages_partyName": "%1's Party",
    "SYS_terms_messages_possession": "Number in possession",
    "SYS_terms_messages_preemptive": "%1 got the upper hand!",
    "SYS_terms_messages_saveMessage": "Which file would you like to save to?",
    "SYS_terms_messages_seVolume": "SE Volume",
    "SYS_terms_messages_substitute": "%1 protected %2!",
    "SYS_terms_messages_surprise": "%1 was caught off guard!",
    "SYS_terms_messages_useItem": "%1 used %2!",
    "SYS_terms_messages_victory": "%1 won the battle!",
    "SYS_terms_params_0": "Max HP", "SYS_terms_params_1": "Max EP",
    "SYS_terms_params_2": "Attack", "SYS_terms_params_3": "Defense",
    "SYS_terms_params_4": "Magic Attack", "SYS_terms_params_5": "Magic Defense",
    "SYS_terms_params_6": "Agility", "SYS_terms_params_7": "Luck",
    "SYS_terms_params_8": "Hit Rate", "SYS_terms_params_9": "Evasion Rate",
    "SYS_weaponTypes_1": "Dagger", "SYS_weaponTypes_12": "Spear",
    "SYS_weaponTypes_2": "Rapier", "SYS_weaponTypes_3": "Straight Sword",
    "SYS_weaponTypes_4": "Curved Sword", "SYS_weaponTypes_5": "Great Sword",
    "SYS_weaponTypes_6": "Katana", "SYS_weaponTypes_7": "Short Sword",
}

PLUG = {
    "PLUGIN_AutoBattle_Auto Battle Message": "Press _key to start auto-battle.",
    "PLUGIN_AutoBattle_Auto Battle Usable Message":
        "Auto-battle in progress. Press _key to cancel.",
    "PLUGIN_EndGme_endName": "Close Game",
    "PLUGIN_GamepadConfig_Cancel Help": "Button used to cancel menu actions.",
    "PLUGIN_GamepadConfig_Command Name": "Gamepad Settings",
    "PLUGIN_GamepadConfig_Finish Help": "Finish configuring the gamepad?",
    "PLUGIN_GamepadConfig_Menu Help": "Open the main menu from the field.",
    "PLUGIN_GamepadConfig_OK Help":
        "Button used to confirm menu selections or talk to people.",
    "PLUGIN_GamepadConfig_PageDown Help": "Quickly scroll down in menus.",
    "PLUGIN_GamepadConfig_PageUp Help": "Quickly scroll up in menus.",
    "PLUGIN_GamepadConfig_Reset Help": "Reset the controller config to default.",
    "PLUGIN_GamepadConfig_Shift Button": "Dash",
    "PLUGIN_GamepadConfig_Shift Help": "Hold to dash on the field.",
    "PLUGIN_KZR_WindowStatusInBattle_CommandName": "Status",
    "PLUGIN_KeyboardConfig_Cancel Text": "Cancel",
    "PLUGIN_KeyboardConfig_Command Name": "Keyboard Settings",
    "PLUGIN_KeyboardConfig_Default Help": "Reset the keyboard settings to default.",
    "PLUGIN_KeyboardConfig_Default Layout": "Default Layout",
    "PLUGIN_KeyboardConfig_Down Text": "Down ▼",
    "PLUGIN_KeyboardConfig_Finish Help": "Finish configuring the keyboard?",
    "PLUGIN_KeyboardConfig_Key Help": "Change the config for this key?",
    "PLUGIN_KeyboardConfig_Left Text": "Left ◄",
    "PLUGIN_KeyboardConfig_OK Text": "OK / Talk",
    "PLUGIN_KeyboardConfig_PageDown Text": "Page Down",
    "PLUGIN_KeyboardConfig_PageUp Text": "Page Up",
    "PLUGIN_KeyboardConfig_Right Text": "Right ►",
    "PLUGIN_KeyboardConfig_Shift Text": "Dash",
    "PLUGIN_KeyboardConfig_Up Text": "Up ▲",
    "PLUGIN_KeyboardConfig_WASD Help": "Switch the keyboard to WASD layout.",
    "PLUGIN_KeyboardConfig_WASD Layout": "WASD Layout",
    "PLUGIN_MakeScreenCapture_署名": "©WGT Hamkatsu 2019  Crest Story Elesaga",
    "PLUGIN_RetryBattle_コマンドタイトル": "To Title",
    "PLUGIN_RetryBattle_コマンドリトライ": "Retry Battle!",
    "PLUGIN_RetryBattle_コマンドロード": "Load Game",
    "PLUGIN_RetryBattle_メッセージ":
        "\\i[1]\\c[2]You lost the battle...\\c[0]\\i[1]",
    "PLUGIN_TMVplugin_sparamText":
        "Aggro Rate,Guard Effect,Recovery Effect,Medicine Knowledge,"
        "MP Cost,TP Charge,,,Floor Damage,EXP Gain",
    "PLUGIN_TMVplugin_xparamText":
        "Hit,Evasion,Critical,Critical Evasion,Magic Evasion,Magic Reflect,"
        "Counter,HP Regen,MP Regen,TP Regen",
    "PLUGIN_YEP_VictoryAftermath_Battle Drops Text": "Spoils",
    "PLUGIN_YEP_VictoryAftermath_Battle Results Text": "Battle Results",
    "PLUGIN_YEP_VictoryAftermath_Gained EXP Text": "EXP Gained",
}

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "text", "batches")
BATCHES = (("system.tsv", SYS), ("plugins.tsv", PLUG))


def main():
    for fname, table in BATCHES:
        path = os.path.normpath(os.path.join(BASE, fname))
        with open(path, encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        filled = 0
        for r in rows:
            if r["id"] in table:
                r["translation"] = table[r["id"]]
                filled += 1
        with open(path, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["id", "japanese", "translation"],
                               delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(fname, "filled", filled, "/", len(rows))


if __name__ == "__main__":
    main()
