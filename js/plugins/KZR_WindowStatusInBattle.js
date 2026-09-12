//=============================================================================
// KZR_WindowStatusInBattle.js
// Version : 1.00
// -----------------------------------------------------------------------------
// [Homepage]: かざり - ホームページ名なんて飾りです。偉い人にはそれがわからんのですよ。 -
//             http://nyannyannyan.bake-neko.net/
// -----------------------------------------------------------------------------
// [Version]
// 1.00 2016/12/01 公開
//=============================================================================

/*:
 * @plugindesc 戦闘中にステータス画面を表示することができます。
 * @author ぶちょー
 *
 * @param CommandName
 * @desc コマンドの名前です。
 * @default ステータス
 *
 * @param CommandPosition
 * @desc ステータスのコマンドを挿入する位置です。
 * 詳しくはヘルプを参照してください。
 * @default bottom
 *
 * @help
 * ステータスのコマンドをどの位置に挿入するか選択できます。
 * top    : 一番上
 * attack : 攻撃コマンドの下
 * skill  : スキルコマンドの下
 * guard  : 防御コマンドの下
 * item   : アイテムコマンドの下
 * bottom : 一番下
 *
 */

(function() {
  var parameters = PluginManager.parameters('KZR_WindowStatusInBattle');
  var WSIB_CommandName = (parameters['CommandName'] || 'ステータス');
  var WSIB_CommandPosition = (parameters['CommandPosition'] || 'bottom');

//-----------------------------------------------------------------------------
// Scene_Battle
//

var _kzr_WSIB_Scene_Battle_isAnyInputWindowActive = Scene_Battle.prototype.isAnyInputWindowActive;
Scene_Battle.prototype.isAnyInputWindowActive = function() {
    return (_kzr_WSIB_Scene_Battle_isAnyInputWindowActive.call(this) ||
            this._statusWindowInBattle.active);
};

var _kzr_WSIB_Scene_Battle_createAllWindows = Scene_Battle.prototype.createAllWindows;
Scene_Battle.prototype.createAllWindows = function() {
    _kzr_WSIB_Scene_Battle_createAllWindows.call(this);
    this.createStatusWindowInBattle();
};

var _kzr_WSIB_Scene_Battle_createActorCommandWindow = Scene_Battle.prototype.createActorCommandWindow;
Scene_Battle.prototype.createActorCommandWindow = function() {
    _kzr_WSIB_Scene_Battle_createActorCommandWindow.call(this);
    this._actorCommandWindow.setHandler('wsib', this.commandStatusWindow.bind(this));
    this.addWindow(this._actorCommandWindow);
};

Scene_Battle.prototype.createStatusWindowInBattle = function() {
    this._statusWindowInBattle = new Window_Status();
    this._statusWindowInBattle.setHandler('ok',     this.onStatusWindowClose.bind(this));
    this._statusWindowInBattle.setHandler('cancel', this.onStatusWindowClose.bind(this));
    this._statusWindowInBattle.hide();
    this._statusWindowInBattle.deactivate();
    this.addWindow(this._statusWindowInBattle);
};

Scene_Battle.prototype.commandStatusWindow = function() {
    this._statusWindowInBattle.setActor(BattleManager.actor());
    this._statusWindowInBattle.show();
    this._statusWindowInBattle.activate();
};

Scene_Battle.prototype.onStatusWindowClose = function() {
    this._statusWindowInBattle.hide();
    this._statusWindowInBattle.deactivate();
    this._actorCommandWindow.activate();
};

//-----------------------------------------------------------------------------
// Window_ActorCommand
//

var _kzr_WSIB_Window_ActorCommand_makeCommandList = Window_ActorCommand.prototype.makeCommandList;
Window_ActorCommand.prototype.makeCommandList = function() {
    if (this._actor) {
        if (WSIB_CommandPosition === 'top') { this.addWindowStatusCommand() };
        _kzr_WSIB_Window_ActorCommand_makeCommandList.call(this);
        if (WSIB_CommandPosition === 'bottom') { this.addWindowStatusCommand() };
    }
};

var _kzr_WSIB_Window_ActorCommand_addAttackCommand = Window_ActorCommand.prototype.addAttackCommand;
Window_ActorCommand.prototype.addAttackCommand = function() {
    _kzr_WSIB_Window_ActorCommand_addAttackCommand.call(this);
    if (WSIB_CommandPosition === 'attack') { this.addWindowStatusCommand() };
};

var _kzr_WSIB_Window_ActorCommand_addSkillCommands = Window_ActorCommand.prototype.addSkillCommands;
Window_ActorCommand.prototype.addSkillCommands = function() {
    _kzr_WSIB_Window_ActorCommand_addSkillCommands.call(this);
    if (WSIB_CommandPosition === 'skill') { this.addWindowStatusCommand() };
};

var _kzr_WSIB_Window_ActorCommand_addGuardCommand = Window_ActorCommand.prototype.addGuardCommand;
Window_ActorCommand.prototype.addGuardCommand = function() {
    _kzr_WSIB_Window_ActorCommand_addGuardCommand.call(this);
    if (WSIB_CommandPosition === 'guard') { this.addWindowStatusCommand() };
};

var _kzr_WSIB_Window_ActorCommand_addItemCommand = Window_ActorCommand.prototype.addItemCommand;
Window_ActorCommand.prototype.addItemCommand = function() {
    _kzr_WSIB_Window_ActorCommand_addItemCommand.call(this);
    if (WSIB_CommandPosition === 'item') { this.addWindowStatusCommand() };
};

Window_ActorCommand.prototype.addWindowStatusCommand = function() {
    this.addCommand(WSIB_CommandName, 'wsib');
};

})();
