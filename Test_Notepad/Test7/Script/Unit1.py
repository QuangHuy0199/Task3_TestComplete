def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.MainMenu.Click("File|[1]")
  dlgOpen = notepad.dlgOpen
  OCR.Recognize(dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.Test1.Name).BlockByText("Test1").Click()
  dlgOpen.btnOpen.ClickButton()
  wndNotepad.MainMenu.Click("Edit|[5]")
  wndNotepad.MainMenu.Click("Edit|[3]")
