def Test1():
  TestedApps.wmplayer.Run()
  wmplayer = Aliases.wmplayer
  WMPAppHost = wmplayer.wndWMPlayerApp.WMPAppHost
  libraryContainer = WMPAppHost.WMPSkinHost.LibraryContainer
  tvLibraryNavigationPane = libraryContainer.tvLibraryNavigationPane
  tvLibraryNavigationPane.ClickItemR("|Playlists|Play1")
  tvLibraryNavigationPane.PopupMenu.Click("Delete")
  dlgWindowsMediaPlayer = wmplayer.dlgWindowsMediaPlayer
  btnOK = dlgWindowsMediaPlayer.btnOK
  btnOK.ClickButton()
  tvLibraryNavigationPane.ClickItemR("|Playlists|Play2")
  tvLibraryNavigationPane.PopupMenu.Click("Delete")
  btnOK.ClickButton()
  toolbarCommandToolbar = libraryContainer.toolbarCommandToolbar
  toolbarCommandToolbar.ClickItemXY("&Create playlist", 57, 16, False)
  edit = tvLibraryNavigationPane.Edit
  edit.SetText("Play1")
  edit.Keys("[Enter]")
  btnYes = dlgWindowsMediaPlayer.btnYes
  btnYes.ClickButton()
  toolbarCommandToolbar.ClickItemXY("&Create playlist", 55, 15, False)
  edit.SetText("Play2")
  edit.Keys("[Enter]")
  btnYes.ClickButton()
  tvLibraryNavigationPane.ClickItem("|Videos")
  tvLibraryNavigationPane.ClickItem("|Music")
  lvDetailsPane = libraryContainer.lvDetailsPane
  lvDetailsPane.ClickItemR(0, "Bensound-Energy")
  lvDetailsPane.PopupMenu.Click("Add to|Play2")
  lvDetailsPane.ClickItemR(0, "Bensound-Energy")
  lvDetailsPane.PopupMenu.Click("Add to|Play1")
  tvLibraryNavigationPane.ClickItem("|Pictures")
  lvDetailsPane.ClickItemR("T3", 0)
  lvDetailsPane.PopupMenu.Click("Add to|Play1")
  tvLibraryNavigationPane.ClickItem("|Videos")
  lvDetailsPane.ClickItemR("Video", 0)
  lvDetailsPane.PopupMenu.Click("Add to|Play2")
  tvLibraryNavigationPane.ClickItem("|Playlists|Play2")
  lvDetailsPane.DblClickItem("2", "Bensound-Energy")
  tvLibraryNavigationPane.DblClickItem("|Playlists|Play1")
