def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.MainMenu.Click("File|[1]")
  dlgOpen = notepad.dlgOpen
  dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.Test1.Name.Click(28, 15)
  dlgOpen.btnOpen.ClickButton()
  tkChild = wndNotepad.TkChild
  tkChild2 = tkChild.TkChild.TkChild
  tkChild2.Drag(114, 69, -116, 0)
  wndNotepad.MainMenu.Click("Edit|[1]")
  tkChild2.Click(60, 109)
  wndNotepad.MainMenu.Click("Edit|[2]")
  tkChild2.Drag(95, 56, -97, -46)
  wndNotepad.MainMenu.Click("Edit|[1]")
  tkChild2.Click(114, 94)
  tkChild.Keys("[Enter]")
  wndNotepad.MainMenu.Click("Edit|[2]")
