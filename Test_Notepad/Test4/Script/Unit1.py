def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.MainMenu.Click("File|[1]")
  dlgOpen = notepad.dlgOpen
  dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.Test1.Name.Click(30, 15)
  dlgOpen.btnOpen.ClickButton()
  wndNotepad.MainMenu.Click("File|[5]")
  notepad.dlgNotepad.btnYes.ClickButton()
