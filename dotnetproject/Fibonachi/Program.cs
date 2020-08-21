using System;

namespace Fibonachi
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number for Fibonacci sequence: ");
            long v = long.Parse(Console.ReadLine());
            long a = 0, b = 1, c = 0;
            Console.Write(" {0} {1}", a + System.Environment.NewLine,b + System.Environment.NewLine);
            for (long i = 2; i < v; i++)
            {
                c= a + b;
                Console.Write(" {0}", c + System.Environment.NewLine);
                a= b;
                b= c;
                
            }
            Console.WriteLine("");


        }
    }
}
