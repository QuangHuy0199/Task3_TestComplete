def Test1():
  TestedApps.Notepad.Run()
  notepad = Aliases.Notepad
  wndNotepad = notepad.wndNotepad
  tkChild = wndNotepad.TkChild
  tkChild.TkChild.TkChild.Click(338, 43)
  tkChild.Keys("Nguyen Van A[Enter]MSSV: 123[Enter]Lop: 456[Enter]GPA: 3.2[Enter]SDT: 00008888")
  wndNotepad.MainMenu.Click("File|[2]")
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("Test1.txt")
  dlgSaveAs.btnSave.ClickButton()
