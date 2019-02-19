
abstract class Day(dayNumber: Int) extends App {
    val fileName = dayNumber.toString
    val lines = readFile("../input/" + fileName + ".txt")
    println(solveA(lines))
    println(solveB(lines))

    def readFile(filename: String): Seq[String] = {
        val bufferedSource = io.Source.fromFile(filename)
        val lines = (for (line <- bufferedSource.getLines()) yield line).toList
        bufferedSource.close
        lines
    }

    def solveA(lines: Seq[String]): String
    def solveB(lines: Seq[String]): String
}
