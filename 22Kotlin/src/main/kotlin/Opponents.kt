data class Player(val hp: Int, val mana: Int, val armor: Int) {

  val isDead = hp <= 0

  fun addHp(hp: Int) = copy(hp = this.hp + hp)
  fun subHp(hp: Int) = copy(hp = this.hp - hp)
  fun addMana(mana: Int) = copy(mana = this.mana + mana)
  fun subMana(mana: Int) = copy(mana = this.mana - mana)
  fun setArmor(armor: Int) = copy(armor = armor)

}

data class Boss(val hp: Int, val damage: Int) {

  val isDead = hp <= 0

  fun subHp(hp: Int) = copy(hp = this.hp - hp)

}
