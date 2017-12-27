interface Spell {
  val cost: Int
  fun updatePlayer(p: Player): Player
  fun updateBoss(b: Boss): Boss
}

interface InstantSpell : Spell

interface EffectSpell : Spell {
  val duration: Int
}

interface TempEffectSpell : EffectSpell {
  fun resetPlayer(p: Player): Player
  fun resetBoss(b: Boss): Boss
}

object MagicMissile : InstantSpell {
  override val cost = 53
  override fun updatePlayer(p: Player) = p
  override fun updateBoss(b: Boss) = b.subHp(4)
}

object Drain : InstantSpell {
  override val cost = 73
  override fun updatePlayer(p: Player) = p.addHp(2)
  override fun updateBoss(b: Boss) = b.subHp(2)
}

object Shield : TempEffectSpell {
  override val cost = 113
  override val duration = 6
  override fun updatePlayer(p: Player) = p.setArmor(7)
  override fun updateBoss(b: Boss) = b
  override fun resetPlayer(p: Player) = p.setArmor(0)
  override fun resetBoss(b: Boss) = b
}

object Poison : EffectSpell {
  override val cost = 173
  override val duration = 6
  override fun updatePlayer(p: Player) = p
  override fun updateBoss(b: Boss) = b.subHp(3)
}

object Recharge : EffectSpell {
  override val cost = 229
  override val duration = 5
  override fun updatePlayer(p: Player) = p.addMana(101)
  override fun updateBoss(b: Boss) = b
}
