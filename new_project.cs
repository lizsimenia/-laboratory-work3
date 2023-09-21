using System;

namespace ConsoleApp1 {
 class Program {
  delegate double Function (double x);
  static void Table (double x1, double dx, double x2, Function f) {
   double y;
   string OutputFormat = "{0:F4}	{1:F4}";
   Console.WriteLine (OutputFormat, "x", "y");
   for (double x = x1; x <= x2; x += dx) {
    y = f (x);
    Console.WriteLine (OutputFormat,x,y);
   }
  }
