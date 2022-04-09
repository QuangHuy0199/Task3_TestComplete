def Test1():
  TestedApps.wmplayer.Run()
  libraryContainer = Aliases.wmplayer.wndWMPlayerApp.WMPAppHost.WMPSkinHost.LibraryContainer
  editSearchEditBox = libraryContainer.editSearchEditBox
  editSearchEditBox.Click(85, 8)
  editSearchEditBox.SetText("B")
  libraryContainer.tvLibraryNavigationPane.ClickItem("|Playlists|Play1")
  editSearchEditBox.Click(141, 9)
  editSearchEditBox.SetText("T")
