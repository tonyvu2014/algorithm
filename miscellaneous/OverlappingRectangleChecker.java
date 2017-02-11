/***
Read data from stdin.

Each line contains 8 integers separated by spaces. The first 4 numbers represent the lower left co-ordinate, width and height of the first rectangle. The next 4 numbers are lower left co-ordinate, width and height of the second rectangle.

Check if the 2 rectangles are overlapping and print out true if they are and false otherwise.
**/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class OverlappingRectangleChecker {
    
  private static final String DELIMITER = "\\s+";
    
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder output = new StringBuilder();
    String s;
    while (!(s = in.readLine()).equals("")) {
      String[] inputs = getInputs(s);
      
      Rectangle firstRectangle = getRectangleFromInput(Arrays.copyOfRange(inputs, 0 , 4));
      Rectangle secondRectangle = getRectangleFromInput(Arrays.copyOfRange(inputs, 4 , 8));
      
      boolean result = checkOverlap(firstRectangle, secondRectangle);
      output.append(result);
      output.append("\n");
    }
    
    System.out.println(output);
  }
  
  private static String[] getInputs(String line) {
    if (line == null) {
      throw new IllegalArgumentException("Input must not be null");
    }
      
    String[] inputs = line.split(DELIMITER);
    if (inputs.length < 8) {
        throw new IllegalArgumentException("At least 8 values are required. " + inputs.length + " is provided.");
    }
    
    return inputs;
  }
  
  private static boolean checkOverlap(Rectangle firstRectangle, Rectangle secondRectangle) {
      return firstRectangle.hasVerticesInside(secondRectangle) || secondRectangle.hasVerticesInside(firstRectangle);
  }
  
  private static Rectangle getRectangleFromInput(String[] inputs) {
     int x = Integer.parseInt(inputs[0]); 
     int y = Integer.parseInt(inputs[1]);
     int w = Integer.parseInt(inputs[2]);
     if (w <= 0) {
    	 throw new IllegalArgumentException(w + ": Width must be a positive integer."); 
     }
     int h = Integer.parseInt(inputs[3]);
     if (h <= 0) {
    	 throw new IllegalArgumentException(h + ": Height must be a positive integer."); 
     }
     
     Point lowerLeft = new Point(x, y);
     
     return new Rectangle(lowerLeft, w ,h);
  }
}
  
class Rectangle {
      private Point lowerLeft;
      private int width;
      private int height;
      private Point upperLeft;
      private Point upperRight;
      private Point lowerRight;
      
      public Rectangle(Point loweLeft, int width, int height) {
        this.lowerLeft = loweLeft;
        this.width = width;
        this.height = height;
        this.upperLeft = new Point(lowerLeft.getX(), lowerLeft.getY() + height);
        this.upperRight = new Point(lowerLeft.getX() + width, lowerLeft.getY() + height);
        this.lowerRight = new Point(lowerLeft.getX() + width, lowerLeft.getY());
      }
      
      public Point getLowerLeft() {
        return this.lowerLeft;
      }
      
      public int getWidth() {
        return this.width;
      }

      public int getHeight() {
        return this.height;
      }
      
      public Point getUpperLeft() {
        return this.upperLeft;
      }
      
      public Point getUpperRight() {
        return this.upperRight;
      }
      
      public Point getLowerRight() {
        return this.lowerRight;
      }
      
      //Check if a point is inside this rectangle
      public boolean isPointInside(Point p) {
        int px = p.getX();
        int py = p.getY();
        
        return (px >= lowerLeft.getX() && px <= getLowerRight().getX()) && 
        		(py >= lowerLeft.getY() && py <= getUpperLeft().getY());
      }
      
      //Check if this rectangle has one of the 4 vertices inside another rectangle
      public boolean hasVerticesInside(Rectangle anotherRectangle) {
          return anotherRectangle.isPointInside(getLowerLeft()) || anotherRectangle.isPointInside(getLowerRight())              || anotherRectangle.isPointInside(getUpperLeft()) || anotherRectangle.isPointInside(getUpperRight());
      }
  }
 
class Point {
    private int x;
    private int y;
    
    public Point(int x,  int y) {
      this.x = x;
      this.y = y;
    }
      
    public int getX() {
      return x;
    }

    public int getY() {
      return y;
    }
}
  
