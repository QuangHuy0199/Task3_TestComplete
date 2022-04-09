def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.MainMenu.Click("File|[1]")
  dlgOpen = notepad.dlgOpen
  dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.adhoc_2.UIImage.Click(16, 12)
  dlgOpen.btnOpen.ClickButton()
  wndNotepad.TkChild.TkChild.TkChild.Drag(179, 267, -180, -125)
  wndNotepad.MainMenu.Click("Edit|[0]")
