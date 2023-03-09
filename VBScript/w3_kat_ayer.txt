'************************************************************
'Script Name: Folder Info
'Author: Kat Ayer
'Class: ENTD261
'Unversity: American Public University
'Due Date: Feb 26, 2023

'This script does not require passing any command line arguments.
'Instead, it prompts the user for a folder location via InputBox.
'Code checks if file path exists, then lists contents.

'Results will not show file size for restricted system subfolders at C:\ level

'Script Examples:
'cscript .\w3_kat_ayer.vbs "C:\"
'cscript .\w3_kat_ayer.vbs "C:\Program Files"
'cscript .\w3_kat_ayer.vbs "C:\USERS\user\Documents"
'************************************************************

Dim NameInput, FolderName, FoundFolder
On Error Resume Next

NameInput = WScript.Arguments(0)


'Verifies user has input a folder
If NameInput = "" or Null Then
    WScript.Echo("Please enter a folder name to continue. Try again.")
    WScript.Quit
End IF

'Creates actionable object
Set FolderName = CreateObject("Scripting.FileSystemObject")

'No matches error handling
If FolderName.FolderExists(NameInput) = False Then
    WScript.Echo("Folder doesn't exist.")
    WScript.Quit
End If

'Joins created objext and user input
Set FoundFolder = FolderName.GetFolder(NameInput)

'List all file names inside, types, sizes, and date created
'Maybe subfolders have Dir type
For Each folder in FoundFolder.SubFolders
    WScript.Echo(folder.Name)
    WScript.Echo(folder.Type)
    WScript.Echo(folder.Size/1024 & " KB")
    WScript.Echo(folder.DateCreated) & vbCrLf
    vbCrLf
Next

For Each file in FoundFolder.Files
    WScript.Echo(file.Name)
    WScript.Echo(file.Type)
    WScript.Echo(file.Size/1024 & " KB")
    WScript.Echo(file.DateCreated) & vbCrLf
Next
WScript.Quit