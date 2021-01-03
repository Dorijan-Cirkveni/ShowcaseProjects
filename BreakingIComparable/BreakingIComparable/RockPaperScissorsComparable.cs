using System;
using System.Collections.Generic;
using System.Text;

namespace BreakingIComparable
{
    class RockPaperScissorsComparable:IComparable
    {
        public readonly int value;
        public RockPaperScissorsComparable(int value)
        {
            this.value = value;
        }

        public int CompareTo(object obj)
        {
            RockPaperScissorsComparable other = (RockPaperScissorsComparable)obj;
            int diffmod = (other.value - this.value + 1) % 3 - 1;
            return diffmod;
        }
    }
}
