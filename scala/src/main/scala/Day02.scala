import scala.collection.immutable.HashMap

object Day02 extends Day(2) {
  def f(x: Boolean): Int = if (x) 1 else 0

  override def solveA(lines: Seq[String]): String = {
    lines.map{ line => 
      line.foldLeft(new HashMap[Char, Int]()) { case (m, c) =>
        if (m contains c) (m + (c -> (m(c) + 1))) else m + (c -> 1)
      }
    }
      .map { m => (m.exists({ case (_, v) => v == 2}), m.exists({case (_, v) => v == 3})) }
      .map { case (a, b) => (f(a), f(b)) }
      .foldLeft((0,0)) { case ((acc1, acc2), (x, y)) => (acc1 + x, acc2 + y) }
      .productIterator.foldLeft(1) { case (x: Int, y: Int) => x * y }
      .toString
  }

  override def solveB(lines: Seq[String]): String = {
    def testBoxIdsWithoutSingleLetter(boxIds: Seq[String], i: Int): Option[String] = {
      (boxIds map {id: String => id.slice(0, i) + id.substring(i + 1)})
            .foldLeft(new HashMap[String, Int]()) { case (m, id) => {
              if (m contains id) m + (id -> (m(id) + 1)) else m + (id -> 1) 
            }}
            .find { case (key, value) => value > 1 }.map { _._1}
    }

    val s = ((for ( i <- 0 until lines(0).length ) yield testBoxIdsWithoutSingleLetter(lines, i)).flatten)
    s(0)

  }
}
