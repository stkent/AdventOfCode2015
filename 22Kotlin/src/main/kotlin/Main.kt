class Main {

  companion object {
    @JvmStatic
    fun main(args: Array<String>) {
      val game = Game(
          player  = Player(hp = 50, mana = 500, armor = 0),
          boss    = Boss(hp = 58, damage = 9))

      println("Part 1 solution: ${game.computeCheapestWin(hardMode = false)}")
      println("Part 2 solution: ${game.computeCheapestWin(hardMode = true)}")
    }
  }

}
