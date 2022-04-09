def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  tkChild = wndNotepad.TkChild
  tkChild.TkChild.TkChild.Click(180, 35)
  tkChild.Keys("Nguyen Van B[Enter]MSSV: 4567[Enter]Lop: 7890[Enter]SDT: 99990000")
  wndNotepad.MainMenu.Click("File|[3]")
  HWNDView = notepad.dlgSaveAs.DUIViewWndClassName.Explorer_Pane
  HWNDView.FloatNotifySink.ComboBox.ClickItem("All files")
  comboBox = HWNDView.FloatNotifySink2.ComboBox
  edit = comboBox.Edit
  edit.Click(292, 9)
  comboBox.SetText("Test2.py")
  edit.Keys("[Enter]")
