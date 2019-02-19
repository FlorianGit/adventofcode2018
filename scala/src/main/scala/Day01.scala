import scala.collection.immutable.HashSet

object Day01 extends Day(1) {
    override def solveA(lines: Seq[String]): String = {
        lines.map {_.toInt}
             .foldLeft(0) {_ + _}
             .toString
    }

    override def solveB(lines: Seq[String]): String = {
          Stream.continually(lines.map{_.toInt}.toStream).flatten
               .scanLeft(0) {_ + _}
               .scanLeft((new HashSet[Int](), new HashSet[Int]())) {
                    case ((doubles, singles), x: Int) => {
                      if (singles contains x) (doubles + x, singles)
                      else (doubles, singles + x)
                    }
               }
               .dropWhile { case (doubles, singles) => doubles isEmpty }(0)
               ._1
               .head
               .toString
    }

}
