def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  tkChild = wndNotepad.TkChild
  tkChild.TkChild.TkChild.Click(167, 34)
  tkChild.Keys("Nguyen Van C[Enter]HI")
  wndNotepad.MainMenu.Click("File|[0]")
  notepad.dlgNotepad.btnNo.ClickButton()
