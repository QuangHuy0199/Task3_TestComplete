def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.MainMenu.Click("Edit|[6]")
  btnOK = notepad.dlgTimeDate.btnOK
  btnOK.ClickButton()
  wndNotepad.MainMenu.Click("Edit|[6]")
  btnOK.ClickButton()
