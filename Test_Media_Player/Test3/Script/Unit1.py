def Test1():
  TestedApps.wmplayer.Run()
  wmplayer = Aliases.wmplayer
  lvDetailsPane = wmplayer.wndWMPlayerApp.WMPAppHost.WMPSkinHost.LibraryContainer.lvDetailsPane
  lvDetailsPane.ClickItemR("T3", 0)
  lvDetailsPane.PopupMenu.Click("Open file location")
  Aliases.explorer.wndPictures.Close()
  lvDetailsPane.ClickItemR("T3", 0)
  lvDetailsPane.PopupMenu.Click("Properties")
  dlgProperties = wmplayer.dlgProperties
  tbcProperties = dlgProperties.tbcProperties
  tbcProperties.ClickTab("Content")
  tbcProperties.ClickTab("Media Usage Rights")
  dlgProperties.btnOK.ClickButton()
  lvDetailsPane.DblClickItem("T3", 0)
  EVRVideoHandler = wmplayer.wndWMPSkinHost2.WMPPluginUIHost.CWmpControlCntr.WMPPluginUIHost.CWmpControlCntr.EVRVideoHandler
  EVRVideoHandler.ClickR(260, 80)
  EVRVideoHandler.PopupMenu.Click("Full screen")
  wmplayer.wndFullScreenTopLayout.Click(1340, 15)
