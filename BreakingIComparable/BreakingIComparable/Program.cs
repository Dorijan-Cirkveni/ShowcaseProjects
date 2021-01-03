using System;
using System.Collections.Generic;

namespace BreakingIComparable
{
    class Program
    {
        static void Main(string[] args)
        {
            List<RockPaperScissorsComparable> X = new List<RockPaperScissorsComparable>();
            for (int i = 0; i < 20; i++) X.Add(new RockPaperScissorsComparable(i));
            for (int i = 0; i < 20; i++) Console.Out.Write(X[i].value.ToString() + ";");
            Console.Out.Write("\n");
            X.Sort();
            for (int i = 0; i < 20; i++) Console.Out.Write(X[i].value.ToString()+";");
        }
    }
}
