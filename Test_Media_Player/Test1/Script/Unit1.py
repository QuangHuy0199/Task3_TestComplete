def Test1():
  TestedApps.wmplayer.Run()
  wmplayer = Aliases.wmplayer
  WMPAppHost = wmplayer.wndWMPlayerApp.WMPAppHost
  lvDetailsPane = WMPAppHost.WMPSkinHost.LibraryContainer.lvNg_nChiTi_t
  lvDetailsPane.DblClickItem(0, "Bensound-Energy")
  WMPAppHost.Drag(710, 544, -18, -4)
  WMPAppHost.Click(470, 538)
  WMPAppHost.Click(560, 541)
  OCR.Recognize(WMPAppHost).BlockByText("II").Click()
  lvDetailsPane.ClickItemR(0, "Bensound-Energy")
  lvDetailsPane.PopupMenu.Click("Open file location")
  Aliases.explorer.wndTest.Close()
  lvDetailsPane.ClickItemR(0, "Bensound-Energy")
  lvDetailsPane.PopupMenu.Click("Properties")
  dlgProperties = wmplayer.dlgProperties
  tbcProperties = dlgProperties.tbcProperties
  tbcProperties.ClickTab("Content")
  tbcProperties.ClickTab("Media Usage Rights")
  tbcProperties.Click(155, 12)
  dlgProperties.btnOK.ClickButton()

