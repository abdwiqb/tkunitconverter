# tkunitconverter
a basic unit converter made with tkinter

I dont suspect this to be useful to anybody since there are better/more convenient converters

but it was fun to make

# how to use

there is a measurment dropdown list, choose which measurment to convert from there

measurments are LENGTH, WIDTH, and TEMPERATURE

from them you can choose which system to take, and which system to convert to

and from those you can choose which unit you want to go from, and convert to

press swap to swap the input text box and the output label

press convert to convert the input

the options frame contains the options, although there is only one option...

# Chart

1. Length

    1. Metric
       
        1. Millimeter
           
        2. Centimeter
           
        3. Decimeter
           
        4. Meter
           
        5. Decameter
            
        6. Hectometer
            
        7. Kilometer
            
    2. Imperial
       
        1. Inch
           
        2. Foot
           
        3. Yard
            
        4. Mile
             
2. Mass
   
    1. Metric
       
        1. Milligram
        
        2. Cenigram
        
        3. Decigram
        
        4. Gram
        
        5. Decagram
        
        6. Hectogram
        
        7. Kilogram
        
        8. Metric Ton 
    
    2. Imperial
    
        1. Ounce
        
        2. Pound
        
        3. Stone
        
        4. Imperial Ton 

3. Temperature

    1. Celsius
    
    2. Fahrenheit
    
    3. Kelvin 

# Modifying the data

the first layer is the measurment

give it a name and make it  a dictionary 

after is the diffrent "systems" inside

for example metric and imperial are diffrent systems

and so are celsius, fahrenheit and kelvin

inside each system, is the pattern

the pattern bassically, is how many of the prev value makes the next

for metric its easy, its just *10 each time

imperial... its more complex

if there is no more pattern left, it takes the last value

the values are the units

for something like temperature, there is only one, degree

after is the conversions

the conversions are for the first value in both systems

the conversion is multiplied and divided to the index of the type chosen

in the conversions add the name of the other systems, and make it a dictionary

in each conversion is the operations and the steps

the operations are,

+ "a" for add
+ "s" for subtract
+ "m" for multiply
+ "d" for division
+ "e" for exponent

the steps are what number you do each operation by

you can put "s" for the input

and capital "s" for what the conversion is at that point
