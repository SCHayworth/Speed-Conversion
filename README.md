# Speed-Conversion
 Creates a table of speeds in Kph and their Mph equivalents

## Scope
Write a program that displays a table of speeds in kilometers per hour with their values converted to miles per hour. The table should display the speeds from 40 KPH through 120 KPH, in increments of 10 KPH. (See sample below). Your program must contain a loop to display this information.

MPH = KPH * 0.6214

### Sample Run
    KPH   MPH
    --------------------
      40    24
      50    31
      60    37
      70    43
      80    49
      90    55
     100    62
     110    68
     120    74

## Pseudocode
### Main function
    START
      SET kph to 40
      PRINT table header
      FOR 9 times
        PRINT kph
        CALL kph_to_mph(kph)
        INCREMENT kph by 10
      ENDFOR
    END

### kph_to_mph function
    START
      PASS IN: kph
      CALCULATE the mph equivalent
        mph = kph * 0.6214
      RETURN mph
    END
