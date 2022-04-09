def Test1():
  TestedApps.wmplayer.Run()
  wmplayer = Aliases.wmplayer
  lvDetailsPane = wmplayer.wndWMPlayerApp.WMPAppHost.WMPSkinHost.LibraryContainer.lvDetailsPane
  lvDetailsPane.ClickItemR("Video", 0)
  lvDetailsPane.PopupMenu.Click("Open file location")
  explorer = Aliases.explorer
  explorer.wndVideos.Close()
  lvDetailsPane.ClickItemR("Video", 0)
  lvDetailsPane.PopupMenu.Click("Properties")
  dlgProperties = wmplayer.dlgProperties
  tbcProperties = dlgProperties.tbcProperties
  tbcProperties.ClickTab("Content")
  tbcProperties.ClickTab("Media Usage Rights")
  dlgProperties.btnOK.ClickButton()
  lvDetailsPane.ClickItemR("Video", 0)
  lvDetailsPane.PopupMenu.Click("Play")
  EVRVideoHandler = wmplayer.wndWMPSkinHost2.WMPPluginUIHost.CWmpControlCntr.WMPPluginUIHost.CWmpControlCntr.EVRVideoHandler
  EVRVideoHandler.ClickR(453, 263)
  EVRVideoHandler.PopupMenu.Click("Full screen")
  wmplayer.wndFullScreenBottomLayout.Click(1322, 33)
  explorer.wndShell_TrayWnd.TrayNotifyWnd.TrayButton.Click(2, 4)
  EVRVideoHandler.Click(287, 243)
  EVRVideoHandler.ClickR(217, 134)
  EVRVideoHandler.PopupMenu.Click("More options...")
  wmplayer.dlgOptions.btnOK.ClickButton()
