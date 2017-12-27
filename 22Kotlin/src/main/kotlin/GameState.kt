sealed class GameState {
  class Won : GameState()
  class Lost : GameState()
  class Invalid : GameState()

  class InProgress(
      val player: Player,
      val boss: Boss,
      val effects: Map<EffectSpell, Int>) : GameState()
}
