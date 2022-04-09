def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  for i in range(5):
    wndNotepad.MainMenu.Click("Help|[0]")
    dlgAboutNotepad = notepad.dlgAboutNotepad
    dlgAboutNotepad.Close()
