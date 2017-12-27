import GameState.*
import java.util.*
import kotlin.math.max

class Game(val player: Player, val boss: Boss) {

  private val spells = listOf(
      MagicMissile,
      Drain,
      Shield,
      Poison,
      Recharge
  )

  fun computeCheapestWin(hardMode: Boolean): Int? {
    val cache = mutableMapOf<Strategy, InProgress>().apply {
      put(Strategy(emptyList()), InProgress(player = player, boss = boss, effects = emptyMap()))
    }

    val queue = PriorityQueue<Strategy>(compareBy { it.cost })
    spells.forEach { queue.add(Strategy(listOf(it))) }

    loop@ while (queue.isNotEmpty()) {
      val strategy = queue.poll()
      val gameState = computeGameState(
          oldGameState = cache[strategy.previous]!!,
          newSpell = strategy.spells.last(),
          hardMode = hardMode)

      when (gameState) {
        is Won -> { return strategy.cost }

        is InProgress -> {
          cache.put(strategy, gameState)
          spells.mapTo(queue) { Strategy(strategy.spells + it) }
        }
      }
    }

    return null
  }

  private fun computeGameState(oldGameState: InProgress, newSpell: Spell, hardMode: Boolean): GameState {
    var player  = oldGameState.player
    var boss    = oldGameState.boss
    var effects = oldGameState.effects

    val expiredTempEffects = mutableListOf<TempEffectSpell>()

    // Player turn -------------------------------------------------------------------------------------------------- //

    if (hardMode) {
      // If in hard mode, reduce player health by 1 at the start of every player turn.
      player = player.subHp(1)

      // Check if the player died as a result of the automatic health deduction.
      if (player.isDead) return Lost()
    }

    // Apply all active effects.
    effects.forEach { (spell, _) ->
      player = spell.updatePlayer(player)
      boss = spell.updateBoss(boss)
    }

    // Check if an effect killed the boss.
    if (boss.isDead) return Won()

    // Update remaining effect durations.
    effects = effects.mapValues { it.value - 1 }

    // Store any temporary effects that have expired so we can deactivate them later.
    expiredTempEffects.addAll(effects.filter { it.value == 0 }.mapNotNull { it.key as? TempEffectSpell })

    // Remove all expired effects.
    effects = effects.filter { it.value > 0 }

    // We can't cast a spell if its effect is still lingering.
    if (effects.keys.contains(newSpell)) return Invalid()

    // We can't cast a spell that we can't afford.
    if (newSpell.cost > player.mana) return Invalid()

    // Deduct the cost of the spell.
    player = player.subMana(newSpell.cost)

    // Perform player spell.
    when (newSpell) {
      is InstantSpell -> {
        player = newSpell.updatePlayer(player)
        boss = newSpell.updateBoss(boss)
      }

      is EffectSpell -> {
        effects = effects.toMutableMap().apply { put(newSpell, newSpell.duration) }
      }
    }

    if (boss.isDead) return Won()

    // Deactivate expired temporary effects.
    expiredTempEffects.forEach { spell ->
      player = spell.resetPlayer(player)
      boss = spell.resetBoss(boss)
    }

    expiredTempEffects.clear()

    // Boss turn ---------------------------------------------------------------------------------------------------- //

    // Apply all active effects.
    effects.forEach { (spell, _) ->
      player = spell.updatePlayer(player)
      boss = spell.updateBoss(boss)
    }

    // Check if an effect killed the boss.
    if (boss.isDead) return Won()

    // Update remaining effect durations.
    effects = effects.mapValues { it.value - 1 }

    // Store any temporary effects that have expired so we can deactivate them later.
    expiredTempEffects.addAll(effects.filter { it.value == 0 }.mapNotNull { it.key as? TempEffectSpell })

    // Remove all expired effects.
    effects = effects.filter { it.value > 0 }

    // Perform boss attack.
    val bossDamage = max(1, boss.damage - player.armor)
    player = player.subHp(bossDamage)

    // Check if boss killed player.
    if (player.isDead) return Lost()

    // Deactivate expired temporary effects.
    expiredTempEffects.forEach { spell ->
      player = spell.resetPlayer(player)
      boss = spell.resetBoss(boss)
    }

    expiredTempEffects.clear()

    // If we performed both turns without the game ending, it's still in progress!
    return InProgress(player, boss, effects)
  }

}
