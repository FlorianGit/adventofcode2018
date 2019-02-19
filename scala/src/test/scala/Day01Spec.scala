import org.scalatest._
import Day01.solveB

class Day01Spec extends FlatSpec with Matchers {
    "Solution for problem B" should "be correct" in {
      solveB(Array("+1","-1")) should be ("0")
      solveB(Array("+3","3","4", "-2", "-4")) should be ("10")

    }
}
