# KodiPlugins
Plugins for Kodi Media Player


repository.merlink.kodi-addons: My Repo to install and Update all Plugins


script.logviewer: A Simple Kodi Log Viewer


script.mvg.departures: Check Departures for a Station of MVG Munich


script.zfs.checker: A simple Plugin for checking ZFS Status in Kodi Media Player

(The Script must have Access to "zpool status", please have a look in Readme.txt)

## OceanKTV youtube-dl plugin upgrade

**更新步驟：**
1. new a branch
2. 更新 code，根據下面「修改那些 code」進行修改
3. push branch
4. NAS 重新安裝 OceanKTV qpkg (先不啟動 KTV)
5. 手動修改 NAS 上 OceanKTV 的 TVplayer youtube plugin xml，將內容指到 new branch，可參考([committed](https://github.com/qeek-dev/KodiPlugins/commit/28ef590d54bfc419021886f23d8ef8c965dbda2b))做更改
```
[/share/CACHEDEV1_DATA/.qpkg/KTVStation/player/script.oceanktv.youtube.dl] # vi addon.xml
[/share/CACHEDEV1_DATA/.qpkg/KTVStation/player/repository.merlink.kodi-addons] # vi addon.xml
```
6. 開啟 OceanKTV 稍等片刻後查看是否更新成功，更新成功可在下列路徑確定安裝的套件版本
```
/share/CACHEDEV1_DATA/.qpkg/KTVStation/root/.kodi/addons/script.module.youtube.dl/addon.xml
```
7. 上述步驟完成沒問題後，即可 merge 回 master :+1:


**修改那些 code：**
* 更新 youtube-dl library

   1. pull 最新的 [rg3 master branch](https://github.com/rg3/youtube-dl)
   2. 將 KodiPlugins [script.oceanktv.youtube.dl/lib/youtube_dl/](https://github.com/qeek-dev/KodiPlugins/tree/master/script.oceanktv.youtube.dl/lib/youtube_dl/) 底下的所有內容，替換成 rg3 的 [youtube-dl](https://github.com/rg3/youtube-dl/tree/master/youtube_dl) 內容

* 更改 script.oceanktv.youtube.dl [addon.xml](https://github.com/qeek-dev/KodiPlugins/blob/master/script.oceanktv.youtube.dl/addon.xml) 的版本號碼

   * 版本號碼更新方式為 年.月日.當天第幾版
   * 如 2017.9.18 第一版： 17.918.0
   ```xml
   <addon id="script.oceanktv.youtube.dl" name="oceanktv youtube-dl" version="17.918.0" provider-name="qnap">
   ```

* 更改 KodiPlugins [addons.xml](https://github.com/qeek-dev/KodiPlugins/blob/master/addons.xml) 裡描述的 script.oceanktv.youtube.dl 版本號碼
   ```xml
   <addon id="script.oceanktv.youtube.dl" name="oceanktv youtube-dl" version="17.918.0" provider-name="qnap">
   ```

* 製作 plugin zip 檔

   1. 將 script.oceanktv.youtube.dl 整個目錄，右鍵壓成 zip 檔
   2. 檔案名稱加上版號 script.oceanktv.youtube.dl-17.918.0.zip，並置於 [releases/script.oceanktv.youtube.dl/](https://github.com/qeek-dev/KodiPlugins/tree/master/releases/script.oceanktv.youtube.dl)

* Done
