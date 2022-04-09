def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  tkChild = wndNotepad.TkChild
  tkChild.TkChild.TkChild.Click(34, 14)
  tkChild.Keys("Nguyen Van D")
  wndNotepad.MainMenu.Click("File|[2]")
  dlgSaveAs = notepad.dlgSaveAs
  HWNDView = dlgSaveAs.DUIViewWndClassName.Explorer_Pane
  comboBox = HWNDView.FloatNotifySink.ComboBox
  comboBox.SetText("test10.txt")
  btnSave = dlgSaveAs.btnSave
  btnSave.ClickButton()
  wndNotepad.MainMenu.Click("File|[0]")
  dlgNotepad = notepad.dlgNotepad
  dlgNotepad.btnNo.ClickButton()
  wndNotepad.MainMenu.Click("File|[1]")
  dlgOpen = notepad.dlgOpen
  dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.Test1.Name.Click(34, 7)
  dlgOpen.btnOpen.ClickButton()
  wndNotepad.MainMenu.Click("Edit|[5]")
  wndNotepad.MainMenu.Click("Edit|[1]")
  wndNotepad.MainMenu.Click("Edit|[2]")
  wndNotepad.MainMenu.Click("Edit|[2]")
  wndNotepad.MainMenu.Click("Edit|[5]")
  wndNotepad.MainMenu.Click("Edit|[3]")
  wndNotepad.MainMenu.Click("Edit|[2]")
  wndNotepad.MainMenu.Click("Edit|[6]")
  notepad.dlgTimeDate.btnOK.ClickButton()
  wndNotepad.MainMenu.Click("File|[3]")
  HWNDView.FloatNotifySink2.ComboBox.ClickItem("All files")
  comboBox.Edit.Click(295, 11)
  comboBox.SetText("Test10.cpp")
  btnSave.ClickButton()
  wndNotepad.MainMenu.Click("File|[5]")
  dlgNotepad.btnYes.ClickButton()
