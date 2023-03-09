'************************************************************
'Script Name: 3 Number Calculations
'Author: Kat Ayer
'Class: ENTD261
'Unversity: American Public University
'Due Date: Feb 19, 2023
'************************************************************
'Create variables for the three numbers
Dim items 
Dim Num1
Dim Num2
Dim Num3

'Tells script to continue past its error point to display the error message
On Error Resume Next

'Verify there are exactly 3 items in input
Set items = WScript.Arguments
If items.Count <> 3 Then
    WScript.Echo("Error: You need exactly 3 numbers. Please double check your arguments.")
    WScript.Quit
End If

'Define variables
Num1 = items.Item(0)
Num2 = items.Item(1)
Num3 = items.Item(2)

'Add them together with allowances for floats that also take 
'the length of the inputs into account
Sum = Round(Num1, len(Num1)) + Round(Num2, len(Num2)) + Round(Num3, len(Num3))

'I couldn't get it to specifically check for non-roundable characters so I just 
'rigged it for the same effect lol
If Err > 0 Then
    WScript.Echo("Error: Use numbers only. Try again")
    WScript.Quit
End If

WScript.Echo("The sum of your numbers is: ")
WScript.Echo(Sum)

'Find the average
Average = Sum / 3
WScript.Echo("The average of your numbers is: ")
WScript.Echo (Average)