data class Strategy(val spells: List<Spell>) {

  val cost = spells.sumBy { it.cost }

  val previous by lazy { Strategy(spells.dropLast(1)) }

}
